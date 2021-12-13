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



/* Trigger for when a new order is placed and stock goes down */

create trigger stock_reducer after insert on inOrder
referencing new row as nrow
when (nrow.order_id in ( -- Makes sure that order_id is in orders table first
            select order_id
            from orders))
begin
    update book
    set stock = stock - 1
    where book.ISBN = nrow.ISBN


end;


