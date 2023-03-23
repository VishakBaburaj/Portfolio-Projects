# Data Exploration

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
SELECT * FROM sales.transactions;	# 10 attributes - product_code, customer_code, market_code, order_date, sales_qry, 
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

# Retrieve necessary data from the sales database based on the objectives.
SELECT c.custmer_name,
	   t.sales_amount, sales_qty,
       m.markets_name,
       d.date AS order_date, month_name AS month, year,
       p.product_type
FROM sales.customers AS c
JOIN sales.transactions AS t ON c.customer_code = t.customer_code
JOIN sales.markets AS m ON m.markets_code = t.market_code
JOIN sales.date AS d ON d.date = t.order_date
JOIN sales.products AS p ON p.product_code = t.product_code;













