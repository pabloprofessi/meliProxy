#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2
import sys
import bottle

app = bottle.Bottle()


def printTable(prows):
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
                 text-align: left;
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
                 <th>Time Delta(sec)</th>
               </tr>
             '''
   temp_text = ""
   for row in prows:
      rowString = ""
      for n in xrange(0,len(row)):
         rowString = rowString + "<td>" + str(row[n]) + "</td>"
         


      temp_text="<tr>" + rowString + "</tr>" + temp_text

   text = text + temp_text  
   text = text + "</table> </body> </html>"

   return text

@app.route('/statistic/<server>/<port>/')
@app.route('/statistic/<server>/<port>')
def show(server, port):

   rows = retrive_data_port_server(server, port)
   htmltable = printTable(rows)
   return htmltable

@app.route('/statistic/<server>/')
@app.route('/statistic/<server>')
def show(server):

   rows = retrive_data_server(server)
   htmltable = printTable(rows)
   return htmltable

@app.route('/statistic/')
@app.route('/statistic')
def show():

   rows = retrive_data_all()
   htmltable = printTable(rows)
   return htmltable


@app.route('/')
def show():
   return '''<!DOCTYPE html>
             <html>
             <head> </head>
             <h1> Bienvenido al servidor de estadisticas!! </h1> 
             <h3> Para ver la carga del servidor vaya a /statistic/(server)/(puerto)  </h3> 

   '''

def retrive_data_port_server(pserver, pport):
	con = None

	try:
	     
	    con = psycopg2.connect("dbname='proxydb' user='pablo'") 
	    
	    cur = con.cursor()   
	    cur.execute("SELECT * FROM requests WHERE  servername=%(serv)s AND port=%(port)s", {'serv' : pserver , 'port' : pport})

	    rows = cur.fetchall()

	    
	    

	except psycopg2.DatabaseError, e:
	    print 'Error %s' % e    
	    sys.exit(1)
	    
	    
	finally:
	    
	    if con:
	        con.close()
   
	return rows


def retrive_data_server(pserver):
  con = None

  try:
       
      con = psycopg2.connect("dbname='proxydb' user='pablo'") 
      
      cur = con.cursor()   
      cur.execute("SELECT * FROM requests WHERE  servername=%(serv)s", {'serv' : pserver })

      rows = cur.fetchall()

      
      

  except psycopg2.DatabaseError, e:
      print 'Error %s' % e    
      sys.exit(1)
      
      
  finally:
      
      if con:
          con.close()
   
  return rows


def retrive_data_all():
  con = None

  try:
       
      con = psycopg2.connect("dbname='proxydb' user='pablo'") 
      
      cur = con.cursor()   
      cur.execute("SELECT * FROM requests ")

      rows = cur.fetchall()

      
      

  except psycopg2.DatabaseError, e:
      print 'Error %s' % e    
      sys.exit(1)
      
      
  finally:
      
      if con:
          con.close()
   
  return rows


app.run(host='localhost', port=9000, server='paste')