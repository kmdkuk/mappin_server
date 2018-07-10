# coding: utf-8
import MySQLdb

connector = MySQLdb.connect(host="mysql", port=3306,
    db="db", user="root", passwd="pass", charset="utf8")
cursor = connector.cursor()

sql = "create table shop_info(" + \
          "shop_name varchar(255)," + \
          "company_name varchar(255)," + \
          "shop_image varchar(255)," + \
          "shop_location varchar(255)," + \
          "shop_businesshours varchar(255)," + \
          "shop_phonenumber varchar(255));"

cursor.execute(sql)

sql = "create table category(" + \
          "company_name varchar(255)," + \
          "category varchar(255));"
cursor.execute(sql)

sql = "create table file(" + \
          "shop_name varchar(255)," + \
          "file_name varchar(255)," + \
          "file_url varchar(255));"
cursor.execute(sql)

cursor.close()
connector.close()
