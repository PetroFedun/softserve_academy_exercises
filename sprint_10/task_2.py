# Given a database with (at least) a table customers as shown below, 
# write an SQL query that returns the name, city and grade of all customers who live in London or Paris, in ascending order of name.

# FIRST 5 ROWS OF CUSTOMERS TABLE, ORDERED BY ID
# id      name             city          grade   salesperson_id
# ------  ---------------  ------------  ------  --------------
# 3001    Brad Guzan       London        100     5005
# 3002    Nick Rimando     New York      100     5001
# 3003    Jozy Altidore    Kyiv          200     5007
# 3004    Fabian Johns     Paris         300     5006
# 3005    Graham Zusi      California    200     5002 

# ------ MY CODE -------

# SELECT name, city, grade
# FROM customers
# WHERE city = 'London' OR city = 'Paris'
# ORDER BY name
