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
insert into user (user_ID, user_name, user_email, user_phonenumber, user_password, street_number, street_name, city, prov, postal_code, country, 0)

-- INDU - FINISH

-- Report: Inventory return one value on how many different types of books

-- Report: Inventory return one value on total stock

-- Report: Inventory return one value on number of distinct authors




/* Owner adding books query */

insert into book values (ISBN, name, author_firstname, author_lastname, genre, num_pages, rating, price, stock, publisher_id, publisher_percent, format);

/* Owner removing books query with ISBN */

DELETE FROM book WHERE ISBN = '';





/* A new Order is placed by user */

insert into orders values (user_id, curdate(), total_price, no_of_items, 'Succefully Placed Order');
insert into inOrder values (order_id, ISBN); -- Dependant on how many books
insert into buys values (order_id, user_id);