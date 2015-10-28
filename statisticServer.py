#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import bottle

app = bottle.Bottle()



@app.route('/statistic/<server>/<port>')
def show(server, port):

   rows = retrive_data(server, port)
   text = '''<!DOCTYPE html>
             <html>
             <head>
             <style>
             table, th, td {
                 border: 1px solid black;
                 border-collapse: collapse;
             }
             th, td {
                 padding: 5px;
             }
             </style>
             </head>
             <body>
             <h1> ESTADISTICAS DE USO </h1> 
             <table style="width:100%">
               <tr>
                 <th>Id</th>
                 <th>Servername</th>		
                 <th>Port</th>
                 <th>Timerange</th>
                 <th>Source IP</th>
                 <th>Source Path</th>
                 <th>Count</th>
               </tr>
             '''
   temp_text = ""
   for row in rows:
      rowString = ""
      for n in xrange(0,7):
         rowString = "<td>" + str(row[n]) + "</td>" + rowString
   
      temp_text="<tr>" + rowString + "</tr>" + temp_text

   text = text + temp_text  
   text = text + "</table> </body> </html>"
   

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