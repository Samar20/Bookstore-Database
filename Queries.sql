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
