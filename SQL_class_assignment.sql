use bosch;
DESCRIBE Salesman;
DESCRIBE Customer;
DESCRIBE Orders;
select * from Salesman;
select * from Customer;
select * from Orders;
select o.salesman_id,o.ord_no,c1.customer_id, c1.cust_name from Orders as o join Customer as c1 where o.salesman_id= c1.salesman_id;
