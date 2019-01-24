from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from myapp.models import User
from myapp import views

class LatestEntriesFeed(Feed):
    title = " Updates"
    link ="/news-sites/"
    description = "Updates on Users"

    def items(self):
        return User.objects.order_by('password')[:1]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.choice

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse(views.homepage)
