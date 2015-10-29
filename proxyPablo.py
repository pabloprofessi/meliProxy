
#!/usr/bin/python
from persistRequests import persist, timeDelta
import sys
from paste import httpserver 
from webob import Request
from wsgiproxy.app import WSGIProxyApp
from pprint import pprint
import time


port = sys.argv[1]
host = "localhost" 

proxyDestination = "https://api.mercadolibre.com"

db_data_dict = {}
db_data_dict['port'] = port
db_data_dict['proxyServer'] = host
db_data_dict['timeRange'] = None 


def timeRangeSet():
	
   if db_data_dict['timeRange'] == None: 
      db_data_dict['timeRange'] = time.time()
   else:
      if (db_data_dict['timeRange'] + timeDelta ) < time.time():

      	persist(db_data_dict)
      	for keys in db_data_dict.keys():
      		if keys not in ['proxyServer','timeRange','port']:
      			db_data_dict.pop(keys, None)
      	db_data_dict['timeRange'] = time.time()
      else:
      	print "new request"
   return True

def requestMaganer(request):
   src_ip = request.client_addr
   src_path = request.path_qs
   
   if timeRangeSet(): 
      temp_tuple = (src_ip, src_path)
      if temp_tuple not in db_data_dict: 
         db_data_dict[temp_tuple] = 1
      else:
         db_data_dict[temp_tuple] = db_data_dict[temp_tuple] + 1

     
   pass
   	
 

def wrapped_proxy_app(environ, start_response):
   requestMaganer(Request(environ))
   proxy_app = WSGIProxyApp(proxyDestination)
   return proxy_app(environ, start_response)



httpserver.serve(wrapped_proxy_app, host=host, port=port)

