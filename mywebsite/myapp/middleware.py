import time

class log_middleware_class(object):
   

    def process_request(self, request):

        with open("log_data.txt", "a") as f:
            f.write(request.path + ' ' + str(time.ctime()) + '\n')
