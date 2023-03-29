#---------------------------------------------------------------
# Data Exploration
#---------------------------------------------------------------
# There are 5 tables in the sales database of AtliQ Hardware.
# customers table
# date table
# markets table
# products table
# transactions table

# Exploring the attributes in each table.
SELECT * FROM sales.customers;      # 3 attributes - customer_code, customer_name, customer_type.
SELECT * FROM sales.date;			# 5 attributes - date, cy_date, year, month_name, date_yy_mmm.
SELECT * FROM sales.markets;		# 3 attributes - markets_code, markets_name, zone.
SELECT * FROM sales.products;		# 2 attributes - product_code product_type.
SELECT * FROM sales.transactions;	
# 10 attributes - product_code, customer_code, market_code, order_date, sales_qry, 
# sales_amount, currency, profit_margin_percentage, profit_margin, cost_price.

# Exploring the number of observations in each table
SELECT COUNT(*) AS number_of_rows
FROM sales.customers;				# 38 observations
SELECT COUNT(*) AS number_of_rows
FROM sales.date;					# 1126 observations
SELECT COUNT(*) AS number_of_rows
FROM sales.markets;					# 17 observations
SELECT COUNT(*) AS number_of_rows
FROM sales.products;				# 279 observations
SELECT COUNT(*) AS number_of_rows
FROM sales.transactions;			# 148395 observations

# The transactions table can be considered as a fact table and the rest of the tables can be considered as dimension tables.
# The primary keys and the data types are correct.

#---------------------------------------------------------------
# Identifying data cleaning steps in transactions table
#---------------------------------------------------------------
# Checking the sales amount and sales qty attributes
SELECT sales_amount, sales_qty
FROM sales.transactions
WHERE sales_amount <= 0 OR sales_qty <= 0
GROUP BY sales_amount, sales_qty;

# Checking whether all the sales amount is in one format (INR)
SELECT order_date, sales_amount, sales_qty, currency 
FROM sales.transactions
WHERE currency != "INR"
GROUP BY order_date, sales_amount, sales_qty, currency; 
# There are 2 observations with USD currency.
# On 2017-11-20 the USD to INR conversion rate was 65.0372 INR
# On 2017-11-22 the USD to INR conversion rate was 64.7843 INR

#---------------------------------------------------------------
# Identifying data cleaning steps in markets table
#---------------------------------------------------------------
# The markets name or the cities consists of Paris and New york.
SELECT t.order_date, sales_amount, currency, m.markets_name
FROM sales.transactions t
LEFT JOIN sales.markets AS m ON t.market_code = m.markets_code
WHERE markets_name = "Paris" OR "New York"
GROUP BY t.order_date, sales_amount, currency, m.markets_name;
# There are no transactions recorded for Paris and New York markets.

#---------------------------------------------------------------
# Identifying data cleaning steps in date table
#---------------------------------------------------------------
# Checking month atrribute.
SELECT DISTINCT month_name
FROM sales.date; 
# The months are recorded correct.
# Checking year atrribute.
SELECT DISTINCT year 
FROM sales.date; 
# The years are recorded correct.

#---------------------------------------------------------------
# Identifying data cleaning steps in customers table
#---------------------------------------------------------------
SELECT DISTINCT custmer_name 
FROM sales.customers; 
# The customer names are recorded correct but need to rename the custmer_name attribute.

#---------------------------------------------------------------
# Identifying data cleaning steps in products table
#---------------------------------------------------------------
SELECT DISTINCT product_type 
FROM sales.products; 
# The product types are recorded correct.

#---------------------------------------------------------------
# Retrieving necessary data from the sales database based on the objectives.
#---------------------------------------------------------------
DROP VIEW IF EXISTS sales.atliq_retrieved_sales_data;

CREATE VIEW sales.atliq_retrieved_sales_data
AS
SELECT t.sales_amount, sales_qty, currency, 
	   IF(currency = "USD", sales_amount*65, sales_amount) AS cleaned_sales_amount,
       IF(currency = "USD", "INR", currency) AS cleaned_currency,
	   c.custmer_name AS customer_name,
       m.markets_name,
       d.date AS order_date, month_name AS month, year,
       p.product_type
FROM sales.transactions AS t
LEFT JOIN sales.customers AS c ON t.customer_code = c.customer_code
LEFT JOIN sales.markets AS m ON t.market_code = m.markets_code
LEFT JOIN sales.date AS d ON t.order_date = d.date
LEFT JOIN sales.products AS p ON t.product_code = p.product_code;

#---------------------------------------------------------------
# atliq retrieved sales data
#---------------------------------------------------------------
SELECT * 
FROM sales.atliq_retrieved_sales_data; # 11 attributes

SELECT COUNT(*) AS number_of_rows
FROM sales.atliq_retrieved_sales_data; # 148395 observations