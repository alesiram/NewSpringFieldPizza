-- Marisela Vasquez, Htet Hutton
-- CS340 Group 60 
-- Springfield Pizza Data Manipulation Language Queries 
-- Citation for data organization is on course document bsg_world in module 5 and 6. 

---------------- Customers page CRUD----------------
-- CREATE
INSERT INTO Customers (cfirst_name, clast_name, phone)
VALUES (:cfirst_name, :clast_name, :phone);

-- RETRIEVE

SELECT * FROM Customers;

SELECT Customers.customer_id, Cusotmers.cfirst_name, Cusotmers.clast_name FROM Customers;

-- UPDATE
SELECT customer_id, cfname, clast_name, phone 
FROM Customers
WHERE customer_id = :customer_id_from_browser;


UPDATE Customers
SET  
cfirst__name = :cfirst_nameInput,
clast_name = :clast_nameInput,
phone = :phoneInput
WHERE customer_id = :customer_id_from_dropdown;

-- DELETE 

DELETE FROM Customers WHERE customer_id = :customer_id;
-- Customers page ends -------------


--------------------Employees page ------------------
-- CREATE
INSERT INTO Employees (efirst_name, elast_name, hourly_wage)
VALUES (:efirst_name, :elast_name, :hourly_wage);

-- Get all employees for Employees table
-- RETRIEVE 
SELECT * FROM Employees;

-- UPDATE 
UPDATE Employees 
SET 
efirst_name = (:efirst_name), 
elast_name = (:elast_name),
hourly_wage = (:hourly_wage)
WHERE employee_id=:employee_id;

-- DELETE dont add id - auto increment 
DELETE FROM Employees WHERE employee_id = :employee_id;

-- Employees page ends -------------


--------------------Pizzas page CRUD ------------------
-- CREATE
INSERT INTO Pizzas (pizza_type, pizza_price)
VALUES(:pizza_type, :pizza_price);

-- RETRIEVE 
SELECT * FROM Pizzas;

-- UPDATE
UPDATE Pizzas 
SET 
pizza_type = (:pizza_type), 
pizza_price = (:pizza_price)
WHERE pizza_id=:pizza_id;

-- DELETE - auto-incrementing.
DELETE FROM Pizzas WHERE pizza_id=:pizza_id;
-- Pizzas page ends ----------------


-----------------Orders page CRUD ----------------
-- CREATE 
INSERT INTO Orders (customer_id, employee_id, pizza_id, order_date, order_total, quantity)

VALUES 
(:customer_id,
:employee_id, 
:pizza_id, 
:order_date, 
:order_total, 
:quantity);


-- RETRIEVE 
-- pizza_id diskplays as pizza_type
-- customer_id displays as first name and last name.
-- LEFT JOIN is used here so that rows with NULL values will show up. 
SELECT 
order_id 
CONCAT(Customers.cfirst_name, ' ', Customers.clast_name) AS 'customer_name', 
employee_id,  
Pizzas.pizza_type, 
order_date,
order_total,
quantity, 
quantity*Pizzas.pizza_price FROM Orders
LEFT JOIN Pizzas ON Orders.pizza_id = Pizzas.pizza_id
LEFT JOIN Customers ON Customers.customer_id = Orders.customer_id
ORDER BY Order_id ASC;

-- UPDATE 
UPDATE Orders
SET
customer_id=:customer_id,
employee_id=:employee_id, 
pizza_id=:pizza_id, 
order_date=:order_date, 
order_total=:order_total, 
quantity=:quantity;


-- DELETE 
-- ONLY THOSE WHICH ARE SELECTED 
DELETE FROM Orders WHERE order_id=:order_id,
-- Orders page ends ----------------
