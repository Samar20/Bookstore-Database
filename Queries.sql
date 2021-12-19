t-- Query

-- User - SearchByBook Title- 
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where name LIKE '%_%'

-- User - SearchByAuthor (specific)
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where author_firstname = '_' AND author_lastname = '_'
group by isbn, author_firstname

-- User - SearchByAuthor (first or last)
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format 
from book
where author_firstname = '%_%' or author_lastname = '%_%'
group by isbn, author_lastname

-- User - SearchByISBN
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where ISBN = '_' 

-- User - SearchByGenre
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where genre = '_' 
group by isbn, genre

-- User - SearchByRating (firm)
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where rating = '_'
group by isbn, rating

-- User - SearchByRating (range - inclusive)
select isbn, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, format
from book
where rating >= '_'
group by isbn, rating

-- User - Logging in (with email)
select user_id, user_name, user_email
from users
where user_email = 'indumini@me.com' AND user_password = 'password123'
group by user_id, user_email

-- User - Creating a new account
insert into users (user_ID, user_name, user_email, user_phonenumber, user_password, street_number, street_name, city, prov, postal_code, country, 0)

-- User - Get user's address
select street_number, street_name, city, prov, postal_code, country from users where user_id = {userID};

-- User - Add order
insert into orders (user_id, order_date, total_price, no_of_items, status_order) values ({userID},curdate(),'{total}','1','Succefully Placed Order');

-- User - Add address to Addresses
insert into addresses (order_id, street_number, street_name, city, prov, postal_code, country) values ('{orderID}','{strNum}','{strName}','{city}','{prov}','{postal}','{country}');

-- User - Add order to inOrder
insert into inOrder values('{orderID}','{book}');

-- Report: Inventory return one value on how many different types of books
select count(DISTINCT genre) as genre
from book

-- Report: Inventory return one value on total stock
select sum(stock) as total
from book

-- Report: Inventory return one value on number of distinct authors
select count(DISTINCT auth_name)
from (SELECT CONCAT(author_firstname, ' ', author_lastname) AS auth_name FROM book) as authorCount


/* Owner adding books query */

insert into book values (ISBN, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, publisher_id, publisher_percent, format);

/* Owner removing books query with ISBN */

DELETE FROM book WHERE ISBN = '';

-- Owner updating shipping status
UPDATE orders
SET status_order = '_' 
WHERE order_id = _;


