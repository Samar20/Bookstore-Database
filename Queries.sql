-- Query

-- User - SearchByBook Title- 
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where name = '_'

-- User - SearchByAuthor (specific)
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where author_firstname = '_' AND author_lasrname = '_'
group by isbn, author_firstname

-- User - SearchByAuthor (specific)
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format 
from book
where author_firstname = '_' or author_lasrname = '_'
group by isbn, author_lasrname

-- User - SearchByISBN
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where ISBN = '_' 

-- User - SearchByGenre
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where genre = 'Mystery' 
group by isbn, genre

-- User - SearchByRating (firm)
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where rating = '_'
group by isbn, rating

-- User - SearchByRating (range - inclusive)
select isbn, name, author_firstname, author_lasrname, genre, num_pages, rating, price, stock, format
from book
where rating >= '_'
group by isbn, rating

-- User - Logging in (with email)
select user_id, user_name, user_email
from users
where user_email = 'indumini@me.com' AND user_password = 'password123'
group by user_id, user_email

-- User - Creating a new account
-- USER ID SHOULD BE SERIAL
insert into user (user_ID, user_name, user_email, user_phonenumber, user_password, street_number, street_name, city, prov, postal_code, country, 0)

-- Trigger
-- Running low on book
create trigger orderMoreBooks after update of book on stock
referencing new row as nrow
referencing old row as orow
for each row
when nrow >= 4
begin atomic
	update book
	set

-- Materialized View
-- Report: Inventory return one value on how many different types of books

-- Report: Inventory return one value on total stock

-- Report: Inventory return one value on number of distinct authors




/* Owner adding books query */

insert into book values (ISBN, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, publisher_id, publisher_percent, format);

/* Owner removing books query with ISBN */

DELETE FROM book WHERE ISBN = '';


/* Materialized View for Sales vs Expenditure Report */

CREATE MATERIALIZED VIEW salesVsExpen AS
SELECT EXTRACT(YEAR  FROM order_date) as Year, EXTRACT(MONTH  FROM order_date) as Month, SUM(total_price) AS Sales, 500 as expenditure
    FROM Orders
GROUP BY month, year
ORDER BY month;


/* Materialized View for Sales per Author Report */
CREATE MATERIALIZED VIEW salesPerAuthor AS
Select author_firstname, author_lasrname, SUM(price) as sales
From book LEFT JOIN inOrder on book.ISBN = inOrder.ISBN
Group by author_firstname, author_lasrname


/* Materialized View for Sales per Genre Report */
CREATE MATERIALIZED VIEW salesPerGenre AS
Select genre, SUM(price) as sales
From book LEFT JOIN inOrder on book.ISBN = inOrder.ISBN
Group by genre


/* Materialized View for Sales per Publisher Report */
CREATE MATERIALIZED VIEW salesPerPublisher AS
Select publisher_name, SUM((publisher_percent/100) * price) as percentage_sale
From book LEFT JOIN inOrder on book.ISBN = inOrder.ISBN
		  RIGHT JOIN publisher on publisher.publisher_id = book.publisher_id
		  
Group By publisher_name