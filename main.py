from flask import jsonify, request
import mysql
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
from flask import Flask
import pymysql
from inventory_database import InventorySystemDatabase



# initializing my sql and flask
app = Flask(__name__)
mysql = MySQL()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "password1"
app.config["MYSQL_DATABASE_DB"] = "test1"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
mysql.init_app(app)
ivd = InventorySystemDatabase()

# FOR CATEGORIES////////////////////////////////////////////////
@app.route('/add/category', methods=['GET', 'POST'])
def addCategories():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    category_id = request.json['category_id']
    name = request.json['name']
    ivd.addCategories(category_id=category_id,name=name)
    # connection.commit()
    cursor.close()
    output = {"category_id":category_id,"name":name,'Message': 'Success'}
    return jsonify(output)
@app.route('/delete/category', methods=['GET','DELETE'])
def deleteCategories():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    name = request.json["name"]
    sql = ivd.deleteCategories(name=name)
    # sql = "DELETE FROM categories where name = %s"
    # name = request.json['name']
    cursor.execute(sql)
    connection.commit()
    connection.rollback()
    output = {'Message': 'Success'}
    return jsonify(output)
@app.route('/getall', methods=['GET'])
def getCategories():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    query = 'SELECT name,category_id FROM categories ORDER BY name'
    cursor.execute(query)
    myresult = cursor.fetchall()
    return jsonify(myresult)



# FOR PRODUCTS..//////////////////////////////////////////////////
@app.route('/add/products', methods=['GET', 'POST'])
def addProducts():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    id = request.json['id']
    name = request.json['name']
    product_id = request.json['product_id']
    category = request.json['category']
    category_id = request.json['category_id']
    purchased_price = request.json['purchased_price']
    sales_price = request.json['sales_price']
    description = request.json['description']
    reorder_level = request.json['reorder_level']
    quantity = request.json['quantity']
    ivd.addProducts(id=id, name=name, product_id=product_id, category=category, category_id=category_id,
                    purchased_price=purchased_price, sales_price=sales_price, description=description,
                    reorder_level=reorder_level, quantity=quantity)
    # connection.commit()
    cursor.close()
    output = {"id": id, "name": name, "product_id": product_id, "category": category,
              "category_id": category_id, "purchased_price": purchased_price,
              "sales_price": sales_price, "description": description, "reorder_level": reorder_level, "quantity":quantity,'Message': 'Success'}
    return jsonify(output)

@app.route("/get/products", methods=["GET"])
def getProducts():
    connection = mysql.connect()
    _cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor = request.args.get("cursor")
    navigation = request.args.get("navigation")
    limit = request.args.get("limit")
    if limit is None:
       limit = 3
    else:
       limit = request.args.get("limit")
    print(navigation)
    if cursor is None:
        query = "SELECT * FROM products ORDER BY id,name limit 3"
    else:
        symbol = ">"
        if navigation != "NEXT":
            symbol = "<"
        query = "SELECT * FROM products WHERE id "+symbol+" %s ORDER BY id,name LIMIT " + str(limit)
    _cursor.execute(query, cursor)
    myresult = _cursor.fetchall()
    return jsonify(myresult)
@app.route("/get/reorder_level", methods=["GET"])
def displayrestockProducts():
    connection = mysql.connect()
    _cursor = connection.cursor(pymysql.cursors.DictCursor)
    navigation = request.args.get("navigation")
    limit = request.args.get("limit")
    cursor = request.args.get("cursor")
    if limit is None:
        limit = 3
    else:
        limit = limit = request.args.get("limit")
    if cursor is None:
        query = "SELECT id,reorder_level,name, \
        IF(quantity <= reorder_level,'You need to reorder more products','successful') AS message\
         FROM products WHERE quantity <= reorder_level"
    else:
        symbol = ">"
        if navigation != "NEXT":
            symbol = "<"
        query = "SELECT id,reorder_level,name, IF(quantity <= reorder_level,'You need to reorder more products','successful')\
     AS message FROM products WHERE quantity <= reorder_level AND id "+symbol+"%s ORDER BY id LIMIT " + str(limit)
    _cursor.execute(query,cursor)
    myresult = _cursor.fetchall()
    return jsonify(myresult)
@app.route("/get/reorder_level", methods=["GET"])
def displayrestockProduct():
    connection = mysql.connect()
    _cursor = connection.cursor(pymysql.cursors.DictCursor)
    navigation = request.args.get("navigation")
    limit = request.args.get("limit")
    cursor = request.args.get("cursor")
    if limit is None:
        limit = 1
    else:
       limit = request.args.get("limit")
    if cursor is None:
        query = "SELECT id,reorder_level,name,IF(quantity <= reorder_level,'You need to reorder more products','successful') \
            AS message FROM products WHERE quantity <= reorder_level OR name = %s"
    else:
        symbol = ">"
        if navigation != "NEXT":
            symbol = "<"
        query = "SELECT id,reorder_level,name,IF(quantity <= reorder_level,'You need to reorder more products','successful') \
            AS message FROM products WHERE quantity <= reorder_level and id" + symbol + "%s ORDER BY id LIMIT" + str(limit)
    _cursor.execute(query,cursor)
    myresult = _cursor.fetchall()
    return jsonify(myresult)
@app.route('/add/quantity', methods=['GET', 'POST'])
def restockProducts():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    quantity = request.json['quantity']
    query = "UPDATE products SET quantity = %s WHERE quantity <= reorder_level"
    cursor.execute(query,quantity)
    connection.commit()
    cursor.close()
    output = {'quantity': quantity, 'Message': 'Success'}
    # print(output)
    return jsonify(output)
if __name__ == "__main__":
    app.run(debug=True)
