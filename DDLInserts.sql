create table user
    (
        user_ID			varchar(5), 
        user_name			varchar(20) not null, 
        user_email			varchar(40) not null,
        user_phonenumber			varchar(15),
        user_password			varchar(20) not null,
        primary key (user_ID)
    )

create table user_addresses
    (
        address_id			varchar(1),
        user_ID			varchar(5),
        street_number       varchar(35) not null, 
        street_name       varchar(35) not null, 
        city       varchar(35) not null, 
        prov       varchar(2) not null, 
        postal_code       varchar(7) not null, 
        country       varchar(50) not null,
        primary key (address_id, user_ID, street_number, street_name) 

    )



create table book 
	(ISBN       varchar(13), 
	 name	    varchar(50) not null, 
	 author_firstname       varchar(20) not null,
     author_lasrname        varchar(20) ,
	 genre       varchar(15) check (genre in ('Childrens', 'Fiction', 'Memoir', 'Mystery', 'Nonfiction', 'Romance', 'SciFi/Fantasy', 'Young Adult')),
     num_pages       numeric(5,0) check(num_pages > 1),
     rating       numeric(1,0) check (rating > -1 and rating < 6),
     price       numeric(4,2) check (price >= 0),
     stock       numeric(5,2),
     publisher_id       varchar(5) not null,
     publisher_percent       numeric(4,2),
     bank_acc       varchar(10),
	 primary key (ISBN),
	 foreign key (publisher_id) references publisher
		on delete cascade,
	);

create table order
    (
        order_id       varchar(15) not null,
        user_ID       varchar(15) not null, 
        street_number       varchar(35) not null, 
        street_name       varchar(35) not null, 
        city       varchar(35) not null, 
        prov       varchar(2) not null, 
        postal_code       varchar(7) not null, 
        country       varchar(50) not null, 
        total_price       numeric(4,2) check (total_price > 0), 
        no_of_items       numeric(5,2) check (no_of_items > 0),
        primary key (order_id)
    )

*ask prof 
create table inorder
    (
        order_id       varchar(15) not null,
        ISBN       varchar(13), 
        primary key (order_id),
        foreign key (order_id) references order
            on delete cascade,
        foreign key(ISBN) references book



    )

create table buys
    (
        user_ID       varchar(15) not null,
        order_id       varchar(15) not null,
        primary key (user_ID),
        foreign key (user_ID) references user
            on delete cascade,
        foreign key (order_id) references order

    )