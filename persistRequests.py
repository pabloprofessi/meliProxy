#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
from pprint import pprint

def persist(pdict):
   print "----------------------------"
   pprint(pdict)
   print "guardando en base de datos"
  
   #cur.execute("CREATE TABLE requests(id BIGSERIAL PRIMARY KEY, servername VARCHAR(40), port INT, timerange VARCHAR(20), src_ip VARCHAR(20), src_path VARCHAR(100), count BIGINT)")
   con = None

   query = """INSERT INTO requests (servername, port, timerange, src_ip, 
              src_path,count ) VALUES ("""

   query = query + "'" + pdict['proxyServer']          + "'"  + ","
   query = query + "'" + pdict['port']                 + "'"  + ","
   query = query + "'" + str(pdict['timeRange'])       + "'"  + ","
   query = query + "'" + pdict.keys()[3][0]            + "'"  + ","
   query = query + "'" + pdict.keys()[3][1]            + "'"  + ","
   query = query +       str(pdict[pdict.keys()[3]])          + ")"
   
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
   print "----------------------------"
   pass



