# Citations: app.py 
# Date 5/11/22
# Source URL: https://github.com/osu-cs340-ecampus/flask-starter-app

from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_vasquem2'
app.config['MYSQL_PASSWORD'] = '9610' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_vasquem2'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# OSU database connection 
# db_connection = db.connect_to_database()

# Routes
# @app.route('/')
# def root():
#     return render_template('index.html')

# # ----------------HOME PAG-----------------------
# @app.route('/index')
# def index():
#     return render_template('index.html')


# @app.route('/Pizzas')
# def Pizzas():
#     return render_template('Pizzas.html')

# # ----------------PIZZA INFO-----------------------
# @app.route('/Pizzas', methods = ['POST', 'GET'])
# def Pizzas():
#  # Separate out the request methods, in this case this is for a POST
#     # insert a pizza into the pizzas entity
#     if request.method == "POST":
#             # fire off if user presses the Add_Pizza button
#         if request.form.get("Add_Pizza"):
#          # grab user form inputs
#             pizza_type = request.form["pizza_type"]
#             # pizza_price = request.form["pizza_price"]
#             pizza_price = request.form["pizza_price"]
#     # mySQL query to insert a new pizza into pizza with our form inputs
#         else:
#             query = "INSERT INTO Pizzas (pizza_type, pizza_price) VALUES (%s, %s)"
#             cur = mysql.connection.cursor()
#             cur.execute(query, (pizza_type, pizza_price))
#             mysql.connection.commit()

#         # redirect back to index [pizza] page
#         return redirect("/Pizzas")
    
# # Grab pizzas data so we sent it to our template to display 
#     if request.method == 'GET':
#         # mySQL query to grab pizza id, name, type and price for our drop down menu 
#         query = 'SELECT pizza_id, pizza_type, pizza_price FROM Pizzas'
#         cur = mysql.connection.cursor()
#         cur.execute(query)
#         data = cur.fetchall()
#         # mySQL query to grab planet id/type for drop down menu
#         query2 = 'SELECT pizza_id, pizza_type FROM Pizzas'
#         cur = mysql.connection.cursor()
#         cur.execute(query2)
#         pizza_data = cur.fetchall()

#         #render edit_pizza page passing our query data and 
#         return render_template('Pizzas.j2', data=data, pizzas=pizza_data)

# #DELETE
# # route for delete functionality, deleting a pizza from pizzas,
# # we want to pass the 'id' value of that pizza on button click (see HTML) via the route

# @app.route("/Pizzas/<int:pizza_id>")
# def delete_pizza(pizzza_id):
#     # mySQL query to delete the person with our passed id
#     query = "DELETE FROM Pizzas WHERE id = '%s';"
#     cur = mysql.connection.cursor()
#     cur.execute(query, (id,))
#     mysql.connection.commit()

#     # redirect back to people page
#     return redirect("/Pizzas.j2")



# #EDIT 
# # route for edit functionality, updating the attributes of a pizza in pizzas
# # similar to our delete route, we want to the pass the 'pizza_id' value of that   pizza on button click (see HTML) via the route
# @app.route("/edit_pizza/<int:pizza_id>", methods=["POST", "GET"])
# def edit_pizza(pizza_id):
#     if request.method == "GET":
#         # mySQL query to grab the info of the person with our passed id
#         query = "SELECT * FROM Pizzas WHERE pizza_id = %s" % (pizza_id)
#         cur = mysql.connection.cursor()
#         cur.execute(query)
#         data = cur.fetchall()

#  # mySQL query to grab pizza id data for our dropdown
#         query2 = 'SELECT pizza_id, pizza_type FROM Pizzas'
#         cur = mysql.connection.cursor()
#         cur.execute(query2)
#         pizza_data = cur.fetchall()

#         # render edit_people page passing our query data and homeworld data to the edit_people template
#         return render_template('Pizzas.j2', data=data, pizzas=pizza_data)


# # meat and potatoes of our update functionality
#     if request.method == "POST":
#         # fire off if user clicks the 'Edit Pizza' button
#         if request.form.get("Edit_Pizza"):
#             # grab user form inputs
#             id = request.form["pizza_id"]
#             pizza_type = request.form["pizza_type"]
#             pizza_price = request.form["pizza_price"]


#     # no null inputs
#         else:
#             query = "UPDATE Pizzas SET Pizzas.pizza_type = %s, Pizzas.pizza_price = %s WHERE Pizzas.id = %s"
#             cur = mysql.connection.cursor()
#             cur.execute(query, (pizza_type, pizza_price, id))
#             mysql.connection.commit()

#                 # redirect back to people page after we execute the update query
#         return redirect("/Pizzas")



# ----------------Customer INFO-------------------
# retrieve all data 
@app.route('/Customers', methods = ["POST", "GET"])
def Customers():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM Customers;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Customers.j2", data=data)

# Create FORM 
    if request.method =="POST":
        if request.form.get("Add_Customer"):
            cfirst_name=request.form["cfirst_name"]
            clast_name=request.form["clast_name"]
            phone=request.form["phone"]

            query = "INSERT INTO Customers (cfirst_name, clast_name, phone) VALUES (%s,%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (cfirst_name, clast_name, phone))
            mysql.connection.commit()

        return redirect("/Customers")

# DELETE FORM Customers.j2
@app.route("/Customer_delete/<int:customer_id>")
def Customer_delete(customer_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Customers WHERE customer_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customer_id,))
    mysql.connection.commit()

    # redirect back to Customers.j2
    return redirect("/Customers")



# EDIT CUSTOMERS 
@app.route("/Customer_edit/<int:customer_id>", methods=["POST", "GET"])
def Customer_edit(customer_id):
    if request.method == "GET":
        query = "SELECT * FROM Customers WHERE customer_id = %s" % (customer_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Customer_edit.j2", data=data)

    if request.method == "POST":
        if request.form.get("Customer_edit"):
            cfirst_name=request.form["cfirst_name"]
            clast_name=request.form["clast_name"]
            phone=request.form["phone"]

        query = "UPDATE Customers SET Customers.cfirst_name = %s, Customers.clast_name = %s, Customers.phone = %s WHERE Customers.customer_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (cfirst_name, clast_name, phone, customer_id))
        mysql.connection.commit()

        return redirect("/Customers")







# ----------------Employees INFO-------------------
# @app.route('/Employees')
# def Employees():
#     return render_template('Employees.html')



# # ----------------Order INFO------------------
# @app.route('/Orders')
# def Orders():
#     return render_template('Orders.html')

# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=6767, debug=True) 