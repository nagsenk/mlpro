from django.contrib.syndication.views import Feed
import datetime

class LatestEntriesFeed(Feed):
    title = "Election Polls news feed"
    link = "/sitenews/"
    description = "Updates on changes and additions to polls central."
    pub_date = datetime.datetime(2018, 11, 2)

    def items(self):

        # One method would pickup the feeds from another source (like a database, then wrap them into objects, and return a list of these objects
        
        # HACK
        item1 = LatestEntriesFeed()
        item1.title = "One"
        item1.link = "/polls/main/"
        item1.description = '''On the World Wide Web, a web feed (or news feed) is a data format used for providing users with frequently updated content. Content distributors syndicate a web feed, thereby allowing users to subscribe a channel to it. Making a collection of web feeds accessible in one spot is known as aggregation, which is performed by a news aggregator. A web feed is also sometimes referred to as a syndicated feed.'''      

        item2 = LatestEntriesFeed()
        item2.title = "Two"
        item2.link = "/polls/main/"
        item2.description = '''A typical scenario of web-feed use might involve the following: a content provider publishes a feed link on its site which end users can register with an aggregator program (also called a feed reader or a news reader) running on their own machines; doing this is usually as simple as dragging the link from the web browser to the aggregator. When instructed, the aggregator asks all the servers in its feed list if they have new content; if so, the aggregator either makes a note of the new content or downloads it. One can schedule aggregators to check for new content periodically.'''

        return [item1, item2]

    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.description
    
    def item_link(self, item):
        return item.link

    def item_pubdate(self, item):
        return item.pub_date
