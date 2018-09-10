from werkzeug.serving import run_simple
from werkzeug.wrappers import Response
from sylfk.wsgi_adapter import wsgi_app


class SYLFk:
    #init
    def __init__(self):
        #pass
        self.host='127.0.0.1'
        self.port=8086

    #route
    def dispatch_request(self,request):
        #pass
        status=200
        headers={
                'Server':'shiyanlou Framework'
        }
        return Response('<h1>hello,framework</h1>',content_type='text/html',headers=headers,status=status)

    #run entry
    def run(self,host=None,port=None,**options):
        #pass
        for key,value in options.items():
            if value is not None:
                self.__setattr__(key,value)
        if host:
            self.host=host
        if port:
            self.port=port
        run_simple(hostname=self.host,port=self.port,application=self,**options)

    #function thati framework interface is called by WSGI
    def __call__(self,environ,start_response):
        return wsgi_app(self,environ,start_response)

