# Given a database with (at least) two tables: customers and orders as shown below, 
# write an SQL query that returns the customer name, city and amount for all orders between $100 and $3500 inclusive, 
# grouped by name and ordered by city.
# result for example
# name                  city                  totalSum
# --------------------  --------------------  ---------------
# Graham Zusi           California            261
# Jozy Altidore         Kyiv                  2000.0
# Brad Guzan            London                270.65
# Julian Green          London                250.45
# Nick Rimando          New York              3210.86
# FIRST 5 ROWS OF "CUSTOMERS" TABLE, ORDERED BY ID
# id      name             city          grade   salesperson_id
# ------  ---------------  ------------  ------  --------------
# 3001    Brad Guzan       London        100     5005
# 3002    Nick Rimando     New York      100     5001
# 3003    Jozy Altidore    Kyiv          200     5007
# 3004    Fabian Johns     Paris         300     5006
# 3005    Graham Zusi      California    200     5002 
# FIRST 5 ROWS OF "ORDERS" TABLE ORDERED BY ORDER_NUM
# order_num   amount     date        customer_id  saleperson_id
# ----------  ---------  ----------  -----------  -------------
# 70001       150.5      2022-10-05  3005         5002
# 70002       65.26      2022-10-05  3002         5001
# 70003       2480.4     2022-10-10  3009         5003
# 70004       110.5      2022-08-17  3005         5003
# 70005       2400.6     2022-07-27  3007         5001

# ------- MY CODE -----------

# SELECT
#     customers.name AS name,
#     customers.city AS city,
#     SUM(orders.amount) AS totalSum
# FROM
#     customers
# JOIN
#     orders ON customers.id = orders.customer_id
# WHERE
#     orders.amount BETWEEN 100 AND 3500
# GROUP BY
#     customers.name, customers.city
# ORDER BY
#     customers.city;
