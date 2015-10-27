#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import bottle

app = bottle.Bottle()



@app.route('/statistic/<server>/<port>')
def show(server, port):

   rows = retrive_data(server, port)
   text = ""
   for row in rows:
      temp_text = " | ".join(map(str,row))
      text = text + temp_text  + "\n"


   return text





def retrive_data(pserver, pport):
	con = None

	try:
	     
	    con = psycopg2.connect("dbname='proxydb' user='pablo'") 
	    
	    cur = con.cursor()   
	    cur.execute("SELECT * FROM requests WHERE  servername=%s AND port=%s", (pserver, pport))

	    rows = cur.fetchall()

	    
	    

	except psycopg2.DatabaseError, e:
	    print 'Error %s' % e    
	    sys.exit(1)
	    
	    
	finally:
	    
	    if con:
	        con.close()
   
	return rows


app.run(host='localhost', port=9000, server='paste')