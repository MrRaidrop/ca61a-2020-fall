.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) AS average_price
  FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) 
  FROM inventory GROUP BY item ;
  
CREATE TABLE backups AS
  SELECT name, min(MSRP/rating) AS backup
  FROM products GROUP BY category;
  
CREATE TABLE shopping_list AS
  SELECT a.name,b.store 
  FROM backups AS a, lowest_prices AS b 
  WHERE a.name=b.item;


CREATE TABLE total_bandwidth AS
  SELECT sum(MBs) 
  FROM stores AS a, shopping_list AS b
  WHERE a.store=b.store;

