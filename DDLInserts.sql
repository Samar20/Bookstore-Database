delete from handles;
delete from publishes;
delete from owners;
delete from buys;
delete from inOrder;
delete from orders;
delete from book;
delete from publisher;
delete from users;


insert into users values (DEFAULT, 'Indumini', 'indumini@me.com', '123-543-2345', 'password123', '123', 'Sesame Street', 'Ottawa', 'ON', 'K2H8A7', 'Canada', 5);
insert into users values (DEFAULT, 'Samar', 'samar@me.com', '098-765-2343', 'password1234', '321', 'Sesame Street', 'Ottawa', 'ON', 'K2H8A8', 'Canada', 5);
insert into users values (DEFAULT, 'John', 'john@gmail.com', '643-234-9088', 'john123', '33', 'King Street', 'Toronto', 'ON', 'M4T2T1', 'Canada', 1);
insert into users values (DEFAULT, 'Samantha', 'samantha12@hotmail.com', '999-888-7777', 'samAntha12', '98', 'Jason Drive', 'Hamilton', 'ON', 'L0J9G7', 'Canada', 1);
insert into users values (DEFAULT, 'Jackson', 'jackson323@gmail.com', '111-222-3333', 'jjokasd123s', '9128', 'Queen Street', 'Ottawa', 'ON', 'K1Y9F7', 'Canada', 4);
insert into users values (DEFAULT, 'Jessica', 'jessjess@hotmail.com', '321-123-0000', 'jess1ca11', '777', 'Lucky Drive', 'Mississauga', 'ON', 'M4T7D6', 'Canada', 3);


insert into publisher values ('CHP', 'Cedar House Publishers', 'contact@cedarhousepub.com', '407', 'Eastview Drive', 'Friday Harbor', 'Washington', '24572', 'USA', '434-929-8002', 0321000021);
insert into publisher values ('SSC', 'Sound & Seas Co.', 'contact@sound&seas.com', '123', 'Publisher Ave', 'Ottawa', 'Ontario', 'K19J7X', 'Canada', '613-123-5431', 2092944675);
insert into publisher values ('PP', 'Palimpsest Printing', 'contact@palimpsetprint.com', '432', 'welovesql street', 'Fremont', 'California', '93244', 'USA', '669-432-4325', 9432843295);
insert into publisher values ('ESP', 'Etaoin Shrdlu Press', 'contact@etaoinshrdlu.com', '321', 'book street', 'Toronto', 'Ontario', 'M3C0C3', 'Canada', '416-234-7645', 6543644098);

insert into book values ('989-28-3705-987-7', 'Alanna Saves the Day', 'Bernard', 'Hopf', 'Childrens', '188', '5', '8.99', '20', 'CHP', '8', 'Paperback');
insert into book values ('989-28-3705-592-3', 'Banana Slug and the Glass Half Full', 'Gloria', 'Green', 'Childrens', '12', '4.5', '6.99', '18', 'CHP', '7', 'Paperback');
insert into book values ('989-28-3705-583-1', 'Banana Slug and the Lost Cow', 'Hillary', 'Barnhardt', 'Childrens', '13', '4', '6.99', '23', 'CHP', '10', 'Board book');
insert into book values ('989-28-3705-966-2', 'Heliotrope Pajamas', 'Malin', 'Wolff', 'Childrens', '31', '4.9', '10.99', '35', 'CHP', '5', 'Paperback');

insert into book values ('989-28-79-27078-0', 'No More Lightning', 'Charles', 'Fenimore', 'Fiction', '192', '4.6', '23.99', '14', 'ESP', '15', 'Graphic');
insert into book values ('989-28-79-30536-9', 'Not to Gossip, But', 'Gloria', 'Green', 'Fiction', '311', '3.9', '8.99', '32', 'ESP', '3', 'Mass market paperback');
insert into book values ('989-28-79-52883-6', 'Post Alley', 'Burton', 'Malamud', 'Fiction', '384', '4', '27.99', '20', 'ESP', '10', 'Hardcover');


insert into book values ('989-28-654-2017-5', 'Inconvenient Confessions: a memoir', 'Oliver', 'Lowry', 'Memoir', '337', '4', '29.99', '26', 'PP', '11', 'Paperback');
insert into book values ('989-28-654-7965-4', 'We''re Sisters and We Kinda Like Each Other', 'Patricia', 'Hazzard', 'Memoir', '288', '3', '29.99', '30', 'PP', '10.5', 'Hardcover');
insert into book values ('989-28-654-3899-6', 'Who Did You Think You Were Kidding?', 'Philip', 'Antrimn', 'Memoir', '207', '5', '29.99', '20', 'PP', '15.0', 'Hardcover');

insert into book values ('989-28-79-82749-6', '9803 North Millworks Road', 'Carolyn', 'Segal', 'Mystery', '384', '2', '22.99', '50', 'ESP', '16', 'Hardcover');
insert into book values ('989-28-79-82125-8', 'The Winchcombe Railway Museum Heist', 'Carolyn', 'Segal', 'Mystery', '293', '4', '22.99', '20', 'ESP', '12', 'Hardcover');
insert into book values ('989-28-79-22562-9', 'Zero over Twelve', 'Burton', 'Malamud', 'Mystery', '356', '3.5', '20.99', '28', 'ESP', '13.45', 'Hardcover');

insert into book values ('989-28-654-2620-7', 'Nothing But Capers', 'Abraham', 'Stackhouse', 'Nonfiction', '390', '4', '32.99', '40', 'PP', '17.30', 'Hardcover');
insert into book values ('989-28-654-6507-7', 'Say it with Snap!', 'John W.', 'Spanogle', 'Nonfiction', '387', '2', '15.99', '20', 'PP', '4.5', 'Paperback');
insert into book values ('989-28-654-8573-0', 'The Elephant House', 'John W.', 'Spanogle', 'Nonfiction', '598', '3', '23.99', '30', 'PP', '8.9', 'Paperback');

insert into book values ('989-28-229-0197-6', 'The Scent of Oranges', 'Lynne', 'Danticat', 'Romance', '255', '5', '9.5', '20', 'SSC', '5.6', 'Mass market paperback');
insert into book values ('989-28-229-1404-4', 'The Seawitch Sings', 'Lynne', 'Danticat', 'Romance', '381', '1', '9.5', '21', 'SSC', '7.4', 'Mass market paperback');
insert into book values ('989-28-229-6632-6', 'Whither Thou Goest', 'Lynne', 'Danticat', 'Romance', '423', '3', '9.5', '36', 'SSC', '8', 'Mass market paperback');

insert into book values ('989-28-79-69359-6', 'Concerning Prophecy', 'Grace', 'Harrison', 'SciFi/Fantasy', '706', '3', '21.5', '32', 'ESP', '3.0', 'Hardcover');
insert into book values ('989-28-79-44730-', 'Dust on the Rim', 'Kathy', 'Yglesias', 'SciFi/Fantasy', '575', '1', '8.99', '40', 'ESP', '15.0', 'Mass market paperback');
insert into book values ('989-28-79-40897-8', 'Portmeirion', 'Bianca', 'Thompson', 'SciFi/Fantasy', '656', '4', '21.50', '32', 'ESP', '6.5', 'Hardcover');


insert into book values ('989-28-3705-633-3', 'It''s Never Just a Glass', 'Leonard', 'Nabokov', 'Young Adult', '222', '1', '19.99', '30', 'CHP', '3.5', 'Hardcover');
insert into book values ('989-28-79-14379-4', 'Quiddity and Quoddity', 'Jill', 'Hergesheimer', 'Young Adult', '373', '2', '11.99', '42', 'ESP', '2.0', 'Trade paperback');
insert into book values ('989-28-79-03683-6', 'The Spark and The Ashe', 'Ursula', 'Karénine', 'Young Adult', '340', '4', '18.50', '35', 'ESP', '4.5', 'Hardcover');

insert into orders values (DEFAULT,'10000','2021-10-02','11.00','1','Shipped');
insert into orders values (DEFAULT,'10001','2021-10-02','26.00','1','Shipped');
insert into orders values (DEFAULT,'10002','2021-10-02','32.00','1','Shipped');
insert into orders values (DEFAULT,'10003','2021-10-02','25.00','1','Shipped');
insert into orders values (DEFAULT,'10004','2021-10-02','35.00','1','Shipped');
insert into orders values (DEFAULT,'10005','2021-10-02','11.50','1','Shipped');
insert into orders values (DEFAULT,'10000','2021-10-02','23.50','1','Shipped');
insert into orders values (DEFAULT,'10001','2021-10-02','22.00','1','Shipped');
insert into orders values (DEFAULT,'10002','2021-10-02','14.00','1','Shipped');
insert into orders values (DEFAULT,'10003','2021-10-02','20.50','1','Shipped');
insert into orders values (DEFAULT,'10004','2021-11-01','23.50','1','Shipped');
insert into orders values (DEFAULT,'10005','2021-11-01','26.00','1','Shipped');
insert into orders values (DEFAULT,'10000','2021-11-01','18.00','1','Shipped');
insert into orders values (DEFAULT,'10001','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10002','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10003','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10004','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10005','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10000','2021-11-01','25.00','1','Shipped');
insert into orders values (DEFAULT,'10001','2021-11-01','11.50','1','Shipped');
insert into orders values (DEFAULT,'10002','2021-12-01','32.00','1','Pending Shipment');
insert into orders values (DEFAULT,'10003','2021-12-01','9.00','1','Pending Shipment');
insert into orders values (DEFAULT,'10004','2021-12-01','9.00','1','Pending Shipment');
insert into orders values (DEFAULT,'10005','2021-12-01','13.00','1','Pending Shipment');
insert into orders values (DEFAULT,'10002','2021-12-01','32.00','1','Pending Shipment');
insert into orders values (DEFAULT,'10004','2021-12-01','11.00','1','Pending Shipment');


insert into inOrder values('107021','989-28-3705-987-7');
insert into inOrder values('107022','989-28-79-27078-0');
insert into inOrder values('107023','989-28-654-2017-5');
insert into inOrder values('107024','989-28-79-82749-6');
insert into inOrder values('107025','989-28-654-2620-7');
insert into inOrder values('107026','989-28-229-0197-6');
insert into inOrder values('107027','989-28-79-69359-6');
insert into inOrder values('107028','989-28-3705-633-3');
insert into inOrder values('107029','989-28-79-14379-4');
insert into inOrder values('107030','989-28-79-03683-6');
insert into inOrder values('107031','989-28-79-40897-8');
insert into inOrder values('107032','989-28-654-8573-0');
insert into inOrder values('107033','989-28-654-6507-7');
insert into inOrder values('107034','989-28-229-1404-4');
insert into inOrder values('107035','989-28-229-1404-4');
insert into inOrder values('107036','989-28-229-6632-6');
insert into inOrder values('107037','989-28-79-22562-9');
insert into inOrder values('107038','989-28-229-1404-4');
insert into inOrder values('107039','989-28-79-82125-8');
insert into inOrder values('107040','989-28-229-6632-6');
insert into inOrder values('107041','989-28-654-3899-6');
insert into inOrder values('107042','989-28-3705-592-3');
insert into inOrder values('107043','989-28-3705-583-1');
insert into inOrder values('107044','989-28-3705-966-2');
insert into inOrder values('107045','989-28-654-7965-4');
insert into inOrder values('107046','989-28-79-30536-9');




insert into buys values('107021','10000');
insert into buys values('107022','10001');
insert into buys values('107023','10002');
insert into buys values('107024','10003');
insert into buys values('107025','10004');
insert into buys values('107026','10005');
insert into buys values('107027','10000');
insert into buys values('107028','10001');
insert into buys values('107029','10002');
insert into buys values('107030','10003');

insert into buys values('107031','10004');
insert into buys values('107032','10005');
insert into buys values('107033','10000');
insert into buys values('107034','10001');
insert into buys values('107035','10002');
insert into buys values('107036','10003');
insert into buys values('107037','10004');
insert into buys values('107038','10005');
insert into buys values('107039','10000');
insert into buys values('107040','10001');

insert into buys values('107041','10002');
insert into buys values('107042','10003');
insert into buys values('107043','10004');
insert into buys values('107044','10005');
insert into buys values('107045','10002');
insert into buys values('107046','10004');

insert into publishes values ('989-28-3705-987-7', 'CHP');
insert into publishes values ('989-28-3705-592-3', 'CHP');
insert into publishes values ('989-28-3705-583-1', 'CHP');
insert into publishes values ('989-28-3705-966-2', 'CHP');
insert into publishes values ('989-28-79-27078-0', 'ESP');
insert into publishes values ('989-28-79-30536-9', 'ESP');
insert into publishes values ('989-28-79-52883-6', 'ESP');
insert into publishes values ('989-28-654-2017-5', 'PP');
insert into publishes values ('989-28-654-7965-4', 'PP');
insert into publishes values ('989-28-654-3899-6', 'PP');
insert into publishes values ('989-28-79-82749-6', 'ESP');
insert into publishes values ('989-28-79-82125-8', 'ESP');
insert into publishes values ('989-28-79-22562-9', 'ESP');
insert into publishes values ('989-28-654-2620-7', 'PP');
insert into publishes values ('989-28-654-6507-7', 'PP');
insert into publishes values ('989-28-654-8573-0', 'PP');
insert into publishes values ('989-28-229-0197-6', 'SSC');
insert into publishes values ('989-28-229-1404-4', 'SSC');
insert into publishes values ('989-28-229-6632-6', 'SSC');
insert into publishes values ('989-28-79-69359-6', 'ESP');
insert into publishes values ('989-28-79-44730-', 'ESP');
insert into publishes values ('989-28-79-40897-8', 'ESP');
insert into publishes values ('989-28-3705-633-3', 'CHP');
insert into publishes values ('989-28-79-14379-4', 'ESP');
insert into publishes values ('989-28-79-03683-6', 'ESP');


insert into owners values ('00000', 'LookInnaAdmin', 'admin@lookinna.com', '123-456-7890', 'password', '222', 'Bookstore Street', 'Ottawa', 'ON', 'K3T0V8', 'Canada', 50000.00);


insert into handles values ('107021','00000');
insert into handles values ('107022','00000');
insert into handles values ('107023','00000');
insert into handles values ('107024','00000');
insert into handles values ('107025','00000');
insert into handles values ('107026','00000');
insert into handles values ('107027','00000');
insert into handles values ('107028','00000');
insert into handles values ('107029','00000');
insert into handles values ('107030','00000');
insert into handles values ('107031','00000');
insert into handles values ('107032','00000');
insert into handles values ('107033','00000');
insert into handles values ('107034','00000');
insert into handles values ('107035','00000');
insert into handles values ('107036','00000');
insert into handles values ('107037','00000');
insert into handles values ('107038','00000');
insert into handles values ('107039','00000');
insert into handles values ('107040','00000');
insert into handles values ('107041','00000');
insert into handles values ('107042','00000');
insert into handles values ('107043','00000');
insert into handles values ('107044','00000');
insert into handles values ('107045','00000');
insert into handles values ('107046','00000');


insert into addresses values ('107021',DEFAULT,'123','Sesame St','Ottawa','Ontario','K1T5F3','Canada');
insert into addresses values ('107022',DEFAULT,'231','Owl Lane','Kingston','Ontario','K1T5FS3','Canada');
insert into addresses values ('107023',DEFAULT,'12','Joke St','Hamilton','Ontario','K125F3','Canada');
insert into addresses values ('107024',DEFAULT,'3','DMS Ave','Toronto','Ontario','K4T5F3','Canada');
insert into addresses values ('107025',DEFAULT,'65','Comp Dr','Los Angeles','California','97263','USA');
insert into addresses values ('107026',DEFAULT,'346','Art St','New York','New York','78990','USA');
insert into addresses values ('107027',DEFAULT,'654','Arch St',' Chicago','Illinois','67893','USA');
insert into addresses values ('107028',DEFAULT,'876','Carleton Dr','Vancouver','British Columbia','K2HJ3J','Canada');
insert into addresses values ('107029',DEFAULT,'6543','OttawaU St','Stratford','Ontario','K2B8D7','Canada');
insert into addresses values ('107030',DEFAULT,'765', 'King St','Ajax','Ontario','H8G7F6','Canada');
insert into addresses values ('107031',DEFAULT,'54','Queen St','Pickering','Ontario','HD8B87','Canada');
insert into addresses values ('107032',DEFAULT,'5','Prince St','Metcalfe','Ontario','J8B78S','Canada');
insert into addresses values ('107033',DEFAULT,'876','Princess Way','Greely','Ontario','J3N5H6','Canada');
insert into addresses values ('107034',DEFAULT,'976','Elizabeth Dr','Cornwall','Ontario','D3F3G4','Canada');
insert into addresses values ('107035',DEFAULT,'204','House Rd','Smith Falls','Ontario','Q1W2E3','Canada');
insert into addresses values ('107036',DEFAULT,'1755','Main St','Perth','Ontario','W2E3R4','Canada');
insert into addresses values ('107037',DEFAULT,'235','Road St','Winchester','Ontario','E3R4T5','Canada');
insert into addresses values ('107038',DEFAULT,'6543','Meghan Way','Kenora','Ontario','R4T5Y6','Canada');
insert into addresses values ('107039',DEFAULT,'2365','Bank St','London','Ontario','T5Y6U7','Canada');
insert into addresses values ('107040',DEFAULT,'743','Young St','Mississauga','Ontario','Y6U7I8','Canada');
insert into addresses values ('107041',DEFAULT,'624','Dawn Crt','Oshawa','Ontario','E3R4Y6','Canada');
insert into addresses values ('107042',DEFAULT,'999','Spongebob Way','Ottawa','Ontario','T5I8O9','Canada');
insert into addresses values ('107043',DEFAULT,'113','Patrick Pvt','Ottawa','Ontario','W2R4T5','Canada');
insert into addresses values ('107044',DEFAULT,'174','Squidward Ave','Montreal','Quebec','O9I8U7','Canada');
insert into addresses values ('107045',DEFAULT,'3','Holly Ave','Montreal','Quebec','U7Y6T5','Canada');
insert into addresses values ('107046',DEFAULT,'5','Science St','Montreal','Quebec','T5R4R3','Canada');



/* Materialized View for Sales vs Expenditure Report */

CREATE MATERIALIZED VIEW salesVsExpen AS
SELECT EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, SUM(total_price) AS Sales, 500 as expenditure, (SUM(total_price) - 500) As Net_Profits
    FROM Orders
GROUP BY month, year
ORDER BY month;


/* Materialized View for Sales per Author Report */
CREATE MATERIALIZED VIEW salesPerAuthor AS
Select EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, author_firstname, author_lastname, SUM(price) as sales
From book JOIN inOrder on book.ISBN = inOrder.ISBN
		  JOIN Orders on Orders.order_id = inOrder.order_id
Group by month, year, author_firstname, author_lastname
ORDER BY month;


/* Materialized View for Sales per Genre Report */
CREATE MATERIALIZED VIEW salesPerGenre AS
Select EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, genre, SUM(price) as sales
From book RIGHT JOIN inOrder on book.ISBN = inOrder.ISBN
          JOIN Orders on Orders.order_id = inOrder.order_id
Group by month, year, genre
ORDER BY month;


/* Materialized View for Sales per Publisher Report */
CREATE MATERIALIZED VIEW salesPerPublisher AS
Select EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, publisher_name as Publisher_Name, Round(SUM((publisher_percent/100) * price), 3) as Total_Profits
From book JOIN inOrder on book.ISBN = inOrder.ISBN
		  JOIN Orders on Orders.order_id = inOrder.order_id
		  RIGHT JOIN publisher on publisher.publisher_id = book.publisher_id
		  
Group By month, year, publisher_name
ORDER BY month;

/* Materialized View that keeps track of the count of books sold per month and year */
CREATE MATERIALIZED VIEW booksSold AS
Select EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, book.isbn, count(book.isbn) 
From book LEFT JOIN inOrder on book.ISBN = inOrder.ISBN
		  JOIN Orders on Orders.order_id = inOrder.order_id
Group by month, year, book.isbn
ORDER BY month;









