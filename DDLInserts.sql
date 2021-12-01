delete from user;
delete from book;
delete from order;
delete from inOrder;
delete from buys;
delete from owner;
delete from publisher;
delete from publishes;
delete from handles;

insert into book values ('989-28-3705-987-7', 'Alanna Saves the Day', 'Bernard', 'Hopf', 'Childrens', '188', '5', '8.99', '20', 'CHP', '8', 'Paperback')
insert into book values ('989-28-3705-592-3', 'Banana Slug and the Glass Half Full', 'Gloria', 'Green', 'Childrens', '12', '4.5', '6.99', '18', 'CHP', '7', 'Paperback')
insert into book values ('989-28-3705-583-1', 'Banana Slug and the Lost Cow', 'Hillary', 'Barnhardt', 'Childrens', '13', '4', '6.99', '23', 'CHP', '10', 'Board book')
insert into book values ('989-28-3705-966-2', 'Heliotrope Pajamas', 'Malin', 'Wolff', 'Childrens', '31', '4.9', '10.99', '35', 'CHP', '5', 'Paperback')

insert into book values ('989-28-79-27078-0', 'No More Lightning', 'Charles', 'Fenimore', 'Fiction', '192', '4.6', '23.99', '14', 'ESP', '15', 'Graphic')
insert into book values ('989-28-79-30536-9', 'Not to Gossip, But', 'Gloria', 'Green', 'Fiction', '311', '3.9', '8.99', '32', 'ESP', '3', 'Mass market paperback')
insert into book values ('989-28-79-52883-6', 'Post Alley', 'Burton', 'Malamud', 'Fiction', '384', '4', '27.99', '20', 'ESP', '10', 'Hardcover')


insert into book values ('989-28-654-2017-5', 'Inconvenient Confessions: a memoir', 'Oliver', 'Lowry', 'Memoir', '337', '4', '29.99', '26', 'PP', '11', 'Paperback')
insert into book values ('989-28-654-7965-4', "We're Sisters and We Kinda Like Each Other", 'Patricia', 'Hazzard', 'Memoir', '288', '3', '29.99', '30', 'PP', '10.5', 'Hardcover')
insert into book values ('989-28-654-3899-6', 'Who Did You Think You Were Kidding?', 'Philip', 'Antrimn', 'Memoir', '207', '5', '29.99', '20', 'PP', '15.0', 'Hardcover')

insert into book values ('989-28-79-82749-6', '9803 North Millworks Road', 'Carolyn', 'Segal', 'Mystery', '384', '2', '22.99', '50', 'ESP', '16', 'Hardcover')
insert into book values ('989-28-79-82125-8', 'The Winchcombe Railway Museum Heist', 'Carolyn', 'Segal', 'Mystery', '293', '4', '22.99', '20', 'ESP', '12', 'Hardcover')
insert into book values ('989-28-79-22562-9', 'Zero over Twelve', 'Burton', 'Malamud', 'Mystery', '356', '3.5', '20.99', '28', 'ESP', '13.45', 'Hardcover')

insert into book values ('989-28-654-2620-7', 'Nothing But Capers', 'Abraham', 'Stackhouse', 'Nonfiction', '390', '4', '32.99', '40', 'PP', '17.30', 'Hardcover')
insert into book values ('989-28-654-6507-7', 'Say it with Snap!', 'John W.', 'Spanogle', 'Nonfiction', '387', '2', '15.99', '20', 'PP', '4.5', 'Paperback')
insert into book values ('989-28-654-8573-0', 'The Elephant House', 'John W.', 'Spanogle', 'Nonfiction', '598', '3', '23.99', '30', 'PP', '8.9', 'Paperback')

insert into book values ('989-28-229-0197-6', 'The Scent of Oranges', 'Lynne', 'Danticat', 'Romance', '255', '5', '9.5', '20', 'SSC', '5.6', 'Mass market paperback')
insert into book values ('989-28-229-1404-4', 'The Seawitch Sings', 'Lynne', 'Danticat', 'Romance', '381', '1', '9.5', '21', 'SSC', '7.4', 'Mass market paperback')
insert into book values ('989-28-229-6632-6', 'Whither Thou Goest', 'Lynne', 'Danticat', 'Romance', '423', '3', '9.5', '36', 'SSC', '8', 'Mass market paperback')

insert into book values ('989-28-79-69359-6', 'Concerning Prophecy', 'Grace', 'Harrison', 'SciFi/Fantasy', '706', '3', '21.5', '32', 'ESP', '3.0', 'Hardcover')
insert into book values ('989-28-79-44730-', 'Dust on the Rim', 'Kathy', 'Yglesias', 'SciFi/Fantasy', '575', '1', '8.99', '40', 'ESP', '15.0', 'Mass market paperback')
insert into book values ('989-28-79-40897-8', 'Portmeirion', 'Bianca', 'Thompson', 'SciFi/Fantasy', '656', '4', '21.50', '32', 'ESP', '6.5', 'Hardcover')


insert into book values ('989-28-3705-633-3', "It's Never Just a Glass", 'Leonard', 'Nabokov', 'Young Adult', '222', '1', '19.99', '30', 'CHP', '3.5', 'Hardcover')
insert into book values ('989-28-79-14379-4', 'Quiddity and Quoddity', 'Jill', 'Hergesheimer', 'Young Adult', '373', '2', '11.99', '42', 'ESP', '2.0', 'Trade paperback')
insert into book values ('989-28-79-03683-6', 'The Spark and The Ashe', 'Ursula', 'Karénine', 'Young Adult', '340', '4', '18.50', '35', 'ESP', '4.5', 'Hardcover')

insert into publisher values ('CHP', 'Cedar House Publishers', 'contact@cedarhousepub.com', '407', 'Eastview Drive', 'Friday Harbor', 'Washington', '24572', 'USA', '434-929-8002', 0321000021)
insert into publisher values ('SSC', 'Sound & Seas Co.,', 'contact@sound&seas.com', '123', 'Publisher Ave', 'Ottawa', 'Ontario', 'K19J7X', 'Canada', '613-123-5431', 2092944675)
insert into publisher values ('PP', 'Palimpsest Printing', 'contact@palimpsetprint.com', '432', 'welovesql street', 'Fremont', 'California', '93244', 'USA', '669-432-4325', 9432843295)
insert into publisher values ('ESP', 'Etaoin Shrdlu Press', 'contact@etaoinshrdlu.com', '321', 'book street', 'Toronto', 'Ontario', 'M3C0C3', 'Canada', '416-234-7645', 6543644098)