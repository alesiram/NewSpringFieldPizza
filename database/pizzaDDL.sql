-- Marisela Vasquez, Htet Hutton
-- CS340 Group 60 
-- Springfield Pizza Data Definition Language 
-- Citation for data organization is on course document bsg_world in module 5 and 6. 

SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;

-- Create entity tables
-- Customers table
CREATE TABLE Customers (
	customer_id INT(10) NOT NULL AUTO_INCREMENT,
	cfirst_name VARCHAR(45) NOT NULL,
	clast_name VARCHAR(45) NOT NULL,
	phone VARCHAR(20),
	PRIMARY KEY (customer_id)
);

-- Employees table
CREATE TABLE Employees (
	employee_id INT(10) NOT NULL AUTO_INCREMENT,
	efirst_name VARCHAR(45) NOT NULL,
	elast_name VARCHAR(45) NOT NULL,
	hourly_wage DECIMAL(5,2),
	PRIMARY KEY (employee_id)
);

-- Pizzas table
CREATE OR REPLACE TABLE Pizzas (
	pizza_id INT(10) NOT NULL AUTO_INCREMENT,
	pizza_type VARCHAR(45) NOT NULL UNIQUE,
	pizza_price DECIMAL(10,2) NOT NULL,
	PRIMARY KEY (pizza_id)
);
-- Orders table
-- Updated employee_id to default Null from project step 3 feedback
-- CASCADE tested and woring. 
--Deleting Customer also deletes Order with matching customer_id. 
CREATE OR REPLACE TABLE Orders (
	order_id INT(10) NOT NULL AUTO_INCREMENT,
	customer_id INT(10),
	employee_id INT(10) DEFAULT NULL,
	pizza_id INT(10) DEFAULT NULL,
	order_date DATE DEFAULT NULL,
    quantity INT(10) DEFAULT 0,
	order_total DECIMAL(10,2) DEFAULT 0,
	PRIMARY KEY (order_id),
	FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE
    ON UPDATE CASCADE,
	FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE
    ON UPDATE CASCADE,
    FOREIGN KEY (pizza_id) REFERENCES Pizzas(pizza_id) ON DELETE CASCADE
    ON UPDATE CASCADE
);


-- Insert sample data into tables
-- Insert data to Customers table
INSERT INTO Customers (cfirst_name, clast_name, phone)
VALUES 
('Miguel','Davis','555-555-5555'),
('Sam','Smith','555-555-5556'),
('Ana','Rodriguez','555-555-5557');

-- Insert data to Employees table
INSERT INTO Employees (efirst_name, elast_name, hourly_wage)
VALUES 
('Dan','Anderson',23.50),
('Mila','Gantes',16.20),
('Val','Obeso',24.00);


-- Insert data to Pizzas table
INSERT INTO Pizzas (pizza_type, pizza_price)
VALUES 
('Meat Lovers',26.12),
('Cheese',20.00),
('Pepperoni',23.22),
('Vegetarian',25.22); 
 
-- Insert data to Orders table
-- Used subquery for customer_id and employee_id like in Intermediate SQL Assignment
INSERT INTO Orders (customer_id, employee_id, pizza_id, order_date, order_total, quantity)
VALUES ((SELECT customer_id FROM Customers WHERE cfirst_name='Ana' AND clast_name='Rodriguez'), 
(SELECT employee_id FROM Employees WHERE efirst_name='Dan' AND elast_name='Anderson'),
(SELECT pizza_id FROM Pizzas WHERE pizza_type = 'Meat Lovers'), '2022-04-27', 52.24, 2),


((SELECT customer_id FROM Customers WHERE cfirst_name='Sam' AND clast_name='Smith'), 
(SELECT employee_id FROM Employees WHERE efirst_name='Val' AND elast_name='Obeso'), 
(SELECT pizza_id FROM Pizzas WHERE pizza_type = 'Vegetarian'), '2022-04-28', 25.22, 1),


(SELECT customer_id FROM Customers WHERE cfirst_name='Miguel' AND clast_name='Davis'), 
(SELECT employee_id FROM Employees WHERE efirst_name='Mila' AND elast_name='Gantes'),
(SELECT pizza_id FROM Pizzas WHERE pizza_type = 'Cheese'), '2022-04-29', 23.22, 1;

SET FOREIGN_KEY_CHECKS=1;
COMMIT;

