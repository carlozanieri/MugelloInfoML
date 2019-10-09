#!/usr/bin/env python
import os
import time
import logging
#import MySQLdb
#import torndb
#import tornado.escape
#import smtplib
from smtplib import SMTP, SMTPException
# *******
#<<<<<<< working copy
#import bcrypt
#=======
##import bcrypt
#>>>>>>> destination
#import concurrent.futures
#import MySQLdb
#import markdown
import pymysql
import os.path
#import re
#import subprocess
#import torndb
#import tornado.escape
from pygments.lexer import include
#from urllib import parse
#from tornado import gen
#import tornado.httpserver
#import tornado.ioloop
#import tornado.options
#import tornado.web
#import unicodedata
import os.path, random, string
#from tornado.options import define, options
# *******
from tornado import gen
import pymysql.cursors
#from tornado.ioloop import IOLoop
#from tornado.web import Application, RequestHandler
#from tornado.websocket import WebSocketHandler
from tornado.options import define, options

#from feed import Feed
from django.core.validators import slug_re
from IPython.terminal.shortcuts import cursor_in_leading_ws
class Connect:
    if not define:
            define("mysql_host", default="carlozanieri.net", help="ufficionline database host")
            define("mysql_database", default="ufficionline", help="ufficionline database name")
            define("mysql_user", default="root", help="ufficionline database user")
            define("mysql_password", default="trex39", help="ufficionline database password")
   # define("mysql_host", default="linuxmugello.net", help="ufficionline database host")
   # define("mysql_database", default="ufficionline", help="ufficionline database name")
    #define("mysql_user", default="root", help="ufficionline database user")
    #define("mysql_password", default="trex39", help="ufficionline database password")

    def get(sbarcode):
        if not define:
            define("mysql_host", default="carlozanieri.net", help="ufficionline database host")
            define("mysql_database", default="ufficionline", help="ufficionline database name")
            define("mysql_user", default="root", help="ufficionline database user")
            define("mysql_password", default="trex39", help="ufficionline database password")
        ###db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        db = pymysql.connect("carlozanieri.net", "root", "trex39", "ufficionline", cursorclass=pymysql.cursors.DictCursor)
        # db = pymysql.connect(options.mysql_host, options.mysql_database, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        barcodes = str(sbarcode)
        print(b"abcde".decode("utf-8"))
        print(bytes(barcodes, "utf-8").decode("utf-8"))

        #db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)
        b = bytes(barcodes, "utf-8").decode("utf-8")
        #b = "pppp"
        print(b"ppp".decode("utf-8"))
        cursor = db.cursor()
        cursor.execute("SELECT *  from barcode where barcode = %s", b)

        barcode = cursor.fetchone()
        if not barcode:
            cursor.execute("SELECT *  from barcode where barcode = %s", "0000000000000")

            barcode = cursor.fetchone()
            
        return barcode
    
    def menu(self):
        db = pymysql.connect("carlozanieri.net", "root", "trex39", "mugello",
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  FROM menu WHERE attivo = 1")

        menu = cursor.fetchall()
        return menu

    def submenu(self):
        db = pymysql.connect("carlozanieri.net", "root", "trex39", "mugello",
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM submenu")
        submenu = cursor.fetchall()
        return submenu

    def centralino(self):
        db = pymysql.connect("carlozanieri.net", "root", "trex39", "mugello",
                             cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT *  FROM centralino WHERE attivo = 1 order by titolo")

        centralino = cursor.fetchall()

        return centralino

    def entry(self):

        db = pymysql.connect("carlozanieri.net", "root", "trex39", "mugello",
        cursorclass=pymysql.cursors.DictCursor)
        cursor = db.cursor()
        cursor.execute("SELECT * ,concat(dir,img) as immagine FROM entries ORDER BY published ")
        entry = cursor.fetchall()
        title = "A Kajiki Template"
        # fruits = ["apple", "orange", "kiwi"]

        return entry

    def pdf(self):
        if not define:
            define("mysql_host", default="carlozanieri.net", help="ufficionline database host")
            define("mysql_database", default="ufficionline", help="ufficionline database name")
            define("mysql_user", default="root", help="ufficionline database user")
            define("mysql_password", default="trex39", help="ufficionline database password")
        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from feed WHERE attivo = 1 order by id asc")

        pdf = cursor.fetchall()

        return pdf

    def qrcode(self,scelta):
        if not define:
            define("mysql_host", default="carlozanieri.net", help="ufficionline database host")
            define("mysql_database", default="ufficionline", help="ufficionline database name")
            define("mysql_user", default="root", help="ufficionline database user")
            define("mysql_password", default="trex39", help="ufficionline database password")
        db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        cursor.execute("SELECT *  from barcode  WHERE attivo = 1  and barcode = %s", scelta)

        qr = cursor.fetchall()
        return qr

 #   def qrcodeuno(self):
 #       if not define:
 #           define("mysql_host", default="carlozanieri.net", help="ufficionline database host")
 #           define("mysql_database", default="ufficionline", help="ufficionline database name")
 #           define("mysql_user", default="root", help="ufficionline database user")
 #           define("mysql_password", default="trex39", help="ufficionline database password")
 #       db = pymysql.connect(options.mysql_host, options.mysql_user, options.mysql_password, options.mysql_database, cursorclass=pymysql.cursors.DictCursor)#

#        cursor = db.cursor()
#        cursor.execute("SELECT *  from barcode WHERE attivo = 1 and barcode = %s", self)
#
#        qr = cursor.fetchone()
#        return qr
