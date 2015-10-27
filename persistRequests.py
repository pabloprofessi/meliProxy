#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
from pprint import pprint

def persist(pdict):
   store_dict = {}
   store_dict['port']  = pdict['port'] 
   store_dict['proxyServer']  = pdict['proxyServer'] 
   store_dict['timeRange']  = pdict['timeRange'] 
   store_dict["src_ip_src_path_tuple"] = []

   for keys in pdict.keys():
      if keys not in ['proxyServer','timeRange','port']:
         store_dict["src_ip_src_path_tuple"].append((keys[0],keys[1],pdict[keys])) 


   
   #cur.execute("CREATE TABLE requests(id BIGSERIAL PRIMARY KEY, servername VARCHAR(40), port INT, timerange VARCHAR(20), src_ip VARCHAR(20), src_path VARCHAR(100), count BIGINT)")
   con = None
   query = ""

   for n in xrange(0, len(store_dict["src_ip_src_path_tuple"]) ):
      tmpquery = """INSERT INTO requests (servername, port, timerange, src_ip, 
   		           src_path,count ) VALUES ("""
      tmpquery = tmpquery + "'" + store_dict['proxyServer']          		      + "'"  + ","
      tmpquery = tmpquery + "'" + store_dict['port']                 		      + "'"  + ","
      tmpquery = tmpquery + "'" + str(store_dict['timeRange'])       		      + "'"  + ","
      tmpquery = tmpquery + "'" + store_dict["src_ip_src_path_tuple"][n][0]       + "'"  + ","
      tmpquery = tmpquery + "'" + store_dict["src_ip_src_path_tuple"][n][1]  	  + "'"  + ","
      tmpquery = tmpquery +       str(store_dict["src_ip_src_path_tuple"][n][2])  + ")"
      
      if query == "":
      	query = tmpquery
      else:
      	query = query + ";" + tmpquery  

   print "----------------------------"
   #pprint(query)
   print "guardando en base de datos"
   print "----------------------------"
  

   try:
      con = psycopg2.connect(database='proxydb', user='pablo') 
      cur = con.cursor()
      cur.execute(query)
      con.commit()
   except psycopg2.DatabaseError, e:
      print 'Error %s' % e    
      sys.exit(1)
      
      
   finally:
       
       if con:
           con.close()
   pass



