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
## ----------------HOME PAG-----------------------
@app.route('/')
def root():
    return render_template('index.j2')

@app.route('/index')
def index():
    return render_template('index.j2')

# # ----------------PIZZA INFO-----------------------
# retrieve all data 
@app.route('/Pizzas', methods = ["POST", "GET"])
def Pizzas():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM Pizzas;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Pizzas.j2", data=data)

# Create FORM 
    if request.method =="POST":
        if request.form.get("Add_Pizzas"):
            pizza_type=request.form["pizza_type"]
            pizza_price=request.form["pizza_price"]

            query = "INSERT INTO Pizzas (pizza_type, pizza_price) VALUES (%s,%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (pizza_type, pizza_price))
            mysql.connection.commit()

        return redirect("/Pizzas")

# DELETE FORM Employees.j2
@app.route("/Pizzas_delete/<int:pizza_id>")
def Pizzas_delete(pizza_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Pizzas WHERE pizza_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (pizza_id,))
    mysql.connection.commit()

    # redirect back to Customers.j2
    return redirect("/Pizzas")



# EDIT PIZZA
@app.route("/Pizzas_edit/<int:pizza_id>", methods=["POST", "GET"])
def Pizzas_edit(pizza_id):
    if request.method == "GET":
        query = "SELECT * FROM Pizzas WHERE pizza_id = %s" % (pizza_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Pizzas_edit.j2", data=data)

    if request.method == "POST":
        if request.form.get("Pizzas_edit"):
            pizza_type=request.form["pizza_type"]
            pizza_price=request.form["pizza_price"]
            

        query = "UPDATE Pizzas SET Pizzas.pizza_type = %s, Pizzas.pizza_price = %s  WHERE Pizzas.pizza_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (pizza_type, pizza_price, pizza_id))
        mysql.connection.commit()

        return redirect("/Pizzas")


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

# retrieve all data 
@app.route('/Employees', methods = ["POST", "GET"])
def Employees():
    if request.method == "GET":
        # mySQL query to grab all
        query = "SELECT * FROM Employees;"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Employees.j2", data=data)

# Create FORM 
    if request.method =="POST":
        if request.form.get("Add_Employees"):
            efirst_name=request.form["efirst_name"]
            elast_name=request.form["elast_name"]
            hourly_wage=request.form["hourly_wage"]

            query = "INSERT INTO Employees (efirst_name, elast_name, hourly_wage) VALUES (%s,%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (efirst_name, elast_name, hourly_wage))
            mysql.connection.commit()

        return redirect("/Employees")

# DELETE FORM Employees.j2
@app.route("/Employee_delete/<int:employee_id>")
def Employee_delete(employee_id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Employees WHERE employee_id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (employee_id,))
    mysql.connection.commit()

    # redirect back to Customers.j2
    return redirect("/Employees")



# EDIT EMPLOYEES
@app.route("/Employees_edit/<int:employee_id>", methods=["POST", "GET"])
def Employees_edit(employee_id):
    if request.method == "GET":
        query = "SELECT * FROM Employees WHERE employee_id = %s" % (employee_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("Employees_edit.j2", data=data)

    if request.method == "POST":
        if request.form.get("Employees_edit"):
            efirst_name=request.form["efirst_name"]
            elast_name=request.form["elast_name"]
            hourly_wage=request.form["hourly_wage"]

        query = "UPDATE Employees SET Employees.efirst_name = %s, Employees.elast_name = %s, Employees.hourly_wage = %s WHERE Employees.employee_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (efirst_name, elast_name, hourly_wage, employee_id))
        mysql.connection.commit()

        return redirect("/Employees")




# # ----------------Order INFO------------------
# @app.route('/Orders')
# def Orders():
#     return render_template('Orders.html')






























# Listener
if __name__ == "__main__":

    #Start the app on port 3000, it will be different once hosted
    app.run(port=6767, debug=True) 