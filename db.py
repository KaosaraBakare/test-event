import mysql.connector
import pymysql


mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="password1",
database="test1",
)

mycursor = mydb.cursor()
# # creating a database............................
# mycursor.execute("CREATE DATABASE test1")


#
# deleting a database................................................................
# delete_database_query = """DROP DATABASE contact"""
# mycursor.execute(delete_database_query)
# mydb.commit()
# print("Table and Database Deleted successfully ")




# showing a database.................................
# mycursor.execute("SHOW databases")
# for x in mycursor:
#   print(x)



# creating a table.......................................................................
# mycursor.execute("CREATE TABLE form(id INT NOT NULL AUTO_INCREMENT, first_name varchar(255) NOT NULL,last_name varchar(255) NOT NULL ,other_name varchar(255) NOT NULL,gender varchar(255),date_of_birth DATE NOT NULL,jamb_registrationno varchar(255) NOT NULL,college varchar(255),address varchar(255),email varchar(255) UNIQUE,phone_number INT,nationality varchar(255),state_of_origin varchar(255),local_government varchar(255),guardian_name varchar(255) NOT NULL,guardian_address varchar(255),guardian_number INT,postal_address varchar (255),PRIMARY KEY (id))")
# mycursor.execute("CREATE TABLE categories(category_id INT PRIMARY KEY, name varchar(255) NOT NULL)")
# mycursor.execute("CREATE TABLE expenses(id INT PRIMARY KEY,"
#                  " type varchar(255) NOT NULL,category varchar(255) NOT NULL, date DATE NOT NULL,amount INT )")
# #
mycursor.execute("CREATE TABLE products(id INT PRIMARY KEY, name varchar(255) NOT NULL,product_id INT,category  varchar(255),category_id INT,purchased_price INT, sales_price INT, description varchar(255),reorder_level INT,quantity INT)")


# show a table.........................................................................................................
# mycursor.execute("SHOW tables")
# for x in mycursor:
#   print(x)



# Alter the table..........................................................................................................
# mycursor.execute("ALTER TABLE contacts ADD COLUMN user_id INT")
# mycursor.execute("ALTER TABLE expenses MODIFY date DATE")
# sql = mycursor.execute("ALTER TABLE products ADD CONSTRAINT categories_ibfk_1 FOREIGN KEY (category_id) \
# REFERENCES categories (category_id);")
# mycursor.execute(sql)

# mydb.commit()

# Inserting into a table..................................................................................
# sql = "INSERT INTO products(name, address) VALUES(%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql,val)
# # use mycursor.executemany(sql,val) when inserting multiple records
# mydb.commit()
# print("I record inserted ID:",mycursor.lastrowid)


#selecting from a table........................................................
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# selecting from the table..............................................................
# mycursor.execute("SELECT name, address FROM products ORDER BY name LIMIT 6")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# using fetchone method......................................................................
# mycursor.execute("SELECT * FROM customers")
#
# myresult = mycursor.fetchone()
#
# print(myresult)
# returns the first row



# selecting with filters...................................................................................
# mycursor.execute("SELECT * FROM customers WHERE address = 'Park Lane 38'")
# myresult = mycursor.fetchall()
# print(myresult)


# wildcards (choose words)....................................................................
# mycursor.execute("SELECT * FROM customers WHERE address Like '%way%'")
#
# myresult = mycursor.fetchall()
# #
# print(myresult)



# prevent in sql injection..............................................................

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#
# mycursor.execute(sql, adr)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


# sort the result...............................................................................
# sql = "SELECT * FROM customers ORDER BY name"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# ordering by desc....................(descending order)
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


# deleting a record.........................

# sql = "DELETE FROM customers WHERE address = 'Mountain 21' "
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# preventing sql injection..................................

# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
#
# mycursor.execute(sql, adr)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) deleted")


# deleting table.................................................................

# sql = "DROP TABLE categories"
# # sql = "DROP TABLE IF EXISTS customers"........ "if table exists"
# mycursor.execute(sql)


# updating  a table...................................................
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# print(mycursor.rowcount, "record(s) affected")



# putting a limit to query being returned #.....................................
# mycursor.execute("SELECT * FROM customers LIMIT 5")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)

# starting from a postion....................................
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 4")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)



# joining 2 tables together............................................
# sql = "SELECT \
#   customers.name AS customer, \
#   products.name AS product \
#   FROM customers \
#   INNER JOIN products ON customers.address = products.id"
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
