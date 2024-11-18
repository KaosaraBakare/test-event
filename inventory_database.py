import mysql.connector
import pymysql
class InventorySystemDatabase():
    def __init__(self):
        self.mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="password1"
        )
        self.my_cursor = self.mydb.cursor()


        # selecting the contacts database as your default database.....................
        self.my_cursor.execute("USE test1")
        # self.my_cursor.close()

    def addProducts(self,id,name,product_id,category,category_id,purchased_price,
                    sales_price,description,reorder_level,quantity):
        sql = "INSERT INTO products(id,name,product_id,category,category_id,purchased_price,\
         sales_price,description,reorder_level,quantity) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (id,name,product_id,category,category_id,purchased_price,sales_price,description,reorder_level,quantity)
        self.my_cursor.execute(sql, val)
        self.mydb.commit()

    def getProducts(self):
        sql = "SELECT * FROM products ORDER BY name"
        self.my_cursor.execute(sql)
        my_result = self.my_cursor.fetchall()
        for x in my_result:
            return x
    def restockLimit(self):
        sql = "SELECT reorder_level, IF(reorder_level <= 10,'You need to reorder more products','successful') FROM my products"
        self.my_cursor.execute(sql)
    def addCategories(self,category_id,name):
        sql = "INSERT INTO categories(category_id,name) VALUES (%s, %s)"
        val = (category_id, name)
        self.my_cursor.execute(sql, val)
        self.mydb.commit()
    def deleteCategories(self, name):
        sql = "DELETE FROM categories where name =%s,"
        self.my_cursor.execute((sql,name))
        self.mydb.commit()
    def getCategories(self):
        sql = 'SELECT name,category_id FROM categories ORDER BY name'
        self.my_cursor.execute(sql)
        myresult = self.my_cursor.fetchall()
        for x in myresult:
            return x

