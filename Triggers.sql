DROP TRIGGER stock_reducer IF EXISTS on inOrder;
DROP FUNCTION stock_reducer_func();





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



/* Function that calls stock reducing trigger */
CREATE OR REPLACE FUNCTION stock_reducer_func()
  RETURNS trigger AS 
$$
BEGIN
    UPDATE book
    SET stock = stock - 1
    WHERE book.ISBN = NEW.ISBN;	
RETURN NEW;
END;

$$

LANGUAGE 'plpgsql';


/* Trigger for when a new order is placed and stock goes down */

create TRIGGER stock_reducer after insert on inOrder
FOR EACH ROW
EXECUTE PROCEDURE stock_reducer_func();





