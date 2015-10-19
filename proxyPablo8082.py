from paste import httpserver 
from webob import Request
from wsgiproxy.app import WSGIProxyApp
from pprint import pprint



proxyDestination = "https://api.mercadolibre.com"


def wrapped_proxy_app(environ, start_response):
   req = Request(environ)
   #para sacar estadisticas esto se podria guardar en un db
   #pprint(req)
   proxy_app = WSGIProxyApp(proxyDestination)
   return proxy_app(environ, start_response)




httpserver.serve(wrapped_proxy_app, host='127.0.0.1', port=8082)