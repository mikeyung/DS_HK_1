-- What customers are from the UK

SELECT * FROM Customers where Country = ‘UK'

-- What is the name of the customer who has the most orders?

SELECT Customers.CustomerName, count(Customers.CustomerID) AS CountOrder
FROM Customers 
JOIN Orders on (Orders.CustomerID = Customers.CustomerID) 
GROUP BY Customers.CustomerID
ORDER BY CountOrder DESC
Limit 1

-- What supplier has the highest average product price?

SELECT Suppliers.SupplierName, AVG(Products.Price) AS AveragePrice 
FROM Suppliers
JOIN Products on (Suppliers.SupplierID = Products.SupplierID)
GROUP by Suppliers.SupplierID
ORDER by AveragePrice DESC
LIMIT 1

-- What category has the most orders?

SELECT Categories.CategoryID, Categories.CategoryName, Sum(OrderDetails.Quantity) AS TotalQuantity
FROM OrderDetails
JOIN Orders on (Orders.OrderID = OrderDetails.OrderID)
JOIN Products on (OrderDetails.ProductID = Products.ProductID)
JOIN Categories on (Products.CategoryID = Categories.CategoryID)
GROUP BY Categories.CategoryID
ORDER BY TotalQuantity DESC
LIMIT 1

-- What employee made the most sales (by number of sales)?

SELECT Employees.FirstName, Employees.LastName, count(OrderID) AS NumSales
FROM Orders
JOIN Employees on (Employees.EmployeeID = Orders.EmployeeID)
GROUP BY Employees.EmployeeID
ORDER BY NumSales DESC
LIMIT 1

-- What employee made the most sales (by value of sales)?

SELECT Employees.FirstName, Employees.LastName, sum(OrderDetails.Quantity * Products.Price) AS ValueSales
FROM OrderDetails
JOIN Orders on (OrderDetails.OrderID = Orders.OrderID)
JOIN Products on (OrderDetails.ProductID = Products.ProductID)
JOIN Employees on (Employees.EmployeeID = Orders.EmployeeID)
GROUP BY Employees.EmployeeID
ORDER BY ValueSales DESC
LIMIT 1

-- What employees have BS degrees? (Hint: Look at LIKE operator)

SELECT FirstName, LastName, Notes
FROM Employees
WHERE Notes like '%BS %'

-- What supplier has the highest average product price assuming they have at least 2 products 
-- (Hint: Look at the HAVING operator)

SELECT Suppliers.SupplierName, AVG(Products.Price) AS AveragePrice, Count(Products.ProductID) As NumProducts
FROM Products
JOIN Suppliers on (Suppliers.SupplierID = Products.SupplierID)
GROUP by Products.SupplierID
HAVING NumProducts > 1
ORDER BY AveragePrice DESC
LIMIT 1
