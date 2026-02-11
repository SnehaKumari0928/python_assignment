show databases;

use ecommerce;

CREATE TABLE customer(
         customer_id INT PRIMARY KEY,
         name VARCHAR(50),
         city VARCHAR(50)
         );
         
create table orders(
        order_id INT PRIMARY KEY,
        customer_id INT,
        order_date date,
        total_amount INT,
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
        ON delete cascade
        ON update cascade
        );
        
CREATE TABLE order_items(
        order_item_id INT PRIMARY KEY,
        order_id INT,
        product VARCHAR(200),
        quantity INT,
        price INT,
		FOREIGN KEY (order_id) REFERENCES orders(order_id)
        ON delete cascade
        ON update cascade
        );
        
INSERT  INTO customer 
VALUES
(1,"Amit","Delhi"),
(2,"Neha","Mumbai"),
(3,"Rahul","Delhi");

INSERT INTO orders values
(101,1,"2024-01-05",4500),
(102,2,"2024-01-10",7000),
(103,1,"2024-02-01",3000),
(104,1,"2024-02-05",9000);

INSERT INTO order_items values
(1,101,"Laptop Bag",1,4500),
(2,102,"Headphones",2,3500),
(3,103,"Mouse",2,1500),
(4,104,"Laptop",1,9000);







        
SELECT c1.customer_id, c1.name, SUM(o2.price*o2.quantity)  as total_spent
from customer c1 JOIN orders o1 ON c1.customer_id = o1.customer_id JOIN order_items o2 ON o1.order_id = o2.order_id
group by c1.customer_id;

select c1.customer_id,c1.name,COUNT(o1.order_id) as total_orders,
SUM(o2.price*o2.quantity)  as total_spent
from customer c1 JOIN orders o1 ON c1.customer_id = o1.customer_id JOIN order_items o2 ON o1.order_id = o2.order_id
group by c1.customer_id Having (count(total_orders) > 1 AND total_spent > 5000);


select c1.city,c1.name, o1.order_id,MAX(o1.total_amount) as total_amount
from customer c1 JOIN orders o1 
ON c1.customer_id = o1.customer_id 
group by c1.city;


        
        
        
       
        