#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('pos_empresa.db')
with con:    
 
    print "-----------cantidad total de ventas en 2013---------" 
    cur = con.cursor()    
    cur.execute("SELECT COUNT(gross_total) FROM sale WHERE [date] BETWEEN '2013-01-01' AND '2013-12-31'")
    rows = cur.fetchall()
    for row in rows:
      print row
#------------------------------------------------------------------------------------------------------
    print "--------Precio promedio de venta por producto------"

    cur.execute("SELECT avg(net_unit_price) AS promedio,  product.name FROM sale_product JOIN product WHERE product_id=product.id GROUP BY product.name ORDER BY name LIMIT 10")
    rows = cur.fetchall()
    for row in rows:
      print row
#-----------------------------------------------------------------------------------------------------
    print "----------Total de ventas por cliente----------"
    cur.execute("SELECT COUNT(sale.gross_total), entity.names, FROM sale JOIN entity WHERE sale.entity_id = entity.id GROUP BY entity.name LIMIT 10")
    rows = cur.fetchall()
    for row in rows:
      print row
#------------------------------------------------------------------------------------------------------
    print "------Total de ventas por cliente en año 2014-----"
    cur.execute("SELECT COUNT(sale.gross_total), entity.names, FROM sale JOIN entity WHERE sale.entity_id = entity.id AND [date] BETWEEN '2014-01-01' AND '2014-12-31'  GROUP BY entity.names LIMIT 10")
    rows = cur.fetchall()
    for row in rows:
      print row
#------------------------------------------------------------------------------------------------------
    print "-----Cantidad y monto total de ventas por dias en noviembre 2013------"
    cur.execute("SELECT date, COUNT(gross_total), SUM(gross_total) FROM sale WHERE date BETWEEN '2013-11-01' AND '2013-11-30' GROUP BY date ORDER BY date;")
    rows = cur.fetchall()
    for row in rows:
      print row
#------------------------------------------------------------------------------------------------------
    print"----Cantidad y montos totales agrupados por producto en orden descendente segun cantidad------"
    cur.execute("SELECT product.name, SUM(sale_product.quantity), SUM(sale_product.gross_total),  FROM sale_product JOIN product WHERE sale.product_id=product.id GROUP BY product.name ORDER BY SUM(sale_product.quantity) DESC LIMIT 10 ")
    rows = cur.fetchall()
    for row in rows:
      print row

