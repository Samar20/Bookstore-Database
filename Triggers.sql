--DROP TRIGGER stock_reducer on inOrder;
--DROP TRIGGER stockCheck on inOrder;
--DROP FUNCTION stock_check_func();
--DROP FUNCTION stock_reducer_func();





/* Trigger that checks if stock of book is above threshold */
create TRIGGER stockCheck after insert on inOrder
FOR EACH ROW
EXECUTE PROCEDURE stock_check_func();



CREATE OR REPLACE FUNCTION stock_check_func()
  RETURNS trigger AS 
$$
BEGIN
    REFRESH MATERIALIZED VIEW  booksSold;
	IF NEW.ISBN in (SELECT isbn from book where stock < 10) then
		UPDATE book
		SET stock = stock + booksSold.count
		FROM booksSold, orders
		WHERE book.ISBN = NEW.ISBN and new.order_id = orders.order_id and booksSold.month =  EXTRACT(month  FROM orders.order_date - INTERVAL  '1 months') and booksSold.year = EXTRACT(year  FROM orders.order_date);
	END IF;
RETURN NEW;
END;
$$

LANGUAGE 'plpgsql';



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





