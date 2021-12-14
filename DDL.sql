create table users
    (
        user_ID			SERIAL UNIQUE, 
        user_name			varchar(20) not null, 
        user_email			varchar(40) not null,
        user_phonenumber			varchar(15),
        user_password			varchar(20) not null,
        street_number       varchar(35) not null, 
        street_name       varchar(35) not null, 
        city       varchar(35) not null, 
        prov       varchar(2) not null, 
        postal_code       varchar(7) not null, 
        country       varchar(50) not null, 
        member_years       numeric(2,0),
        primary key (user_ID)
    );
ALTER SEQUENCE users_user_ID_seq RESTART WITH 10000 INCREMENT BY 1;


create table publisher
    (
        publisher_id          varchar(5) not null,
        publisher_name        varchar(50) not null,
        publisher_email       varchar(40) not null,
        street_number         varchar(35) not null, 
        street_name           varchar(35) not null, 
        city                  varchar(35) not null, 
        prov                  varchar(35) not null, 
        postal_code           varchar(7) not null, 
        country               varchar(50) not null, 
        publisher_phone       varchar(15) not null, 
        publisher_bankAccount numeric(10,0) not null, 

        primary key (publisher_id)
    );

create table book 
	(
        ISBN       varchar(18), 
	    name	    varchar(50) not null, 
	    author_firstname       varchar(20) not null,
        author_lastname        varchar(20) ,
	    genre       varchar(15) check (genre in ('Childrens', 'Fiction', 'Memoir', 'Mystery', 'Nonfiction', 'Romance', 'SciFi/Fantasy', 'Young Adult')),
        num_pages       numeric(4,2) check(num_pages > 1),
        rating       integer check (rating > -1 and rating < 6),
        price       numeric(4,2) check (price >= 0),
        stock       integer,
        publisher_id       varchar(5) not null,
        publisher_percent       numeric(4,2),
        format       varchar(30),
	    primary key (ISBN),
	    foreign key (publisher_id) references publisher
		    on delete cascade
	);

create table orders
    (
        order_id       SERIAL UNIQUE,
        user_ID        integer, 
        order_date       DATE,
        total_price       numeric(4,2) check (total_price > 0), 
        no_of_items       numeric(5,2) check (no_of_items > 0),
        status_order       varchar(50),
        primary key (order_id),
        foreign key (user_ID) references users
    );

ALTER SEQUENCE orders_order_id_seq RESTART WITH 107021 INCREMENT BY 1;


create table inOrder
    (
        order_id       integer not null,
        ISBN       varchar(18), 
        primary key (order_id, ISBN),
        foreign key (order_id) references orders
            on delete cascade,
        foreign key(ISBN) references book
            on delete cascade



    );

create table buys
    (
        order_id       integer not null,
        user_ID        integer not null,
        primary key (order_ID),
        foreign key (order_id) references orders
            on delete cascade,
        foreign key (user_ID) references users
            on delete cascade

    );

create table owners
    (
        owner_ID			  varchar(5), 
        owner_name			  varchar(20) not null, 
        owner_email		   	  varchar(40) not null,
        owner_phonenumber	  varchar(15) not null,
        owner_password		  varchar(20) not null,
        street_number         varchar(35) not null, 
        street_name           varchar(35) not null, 
        city                  varchar(35) not null, 
        prov                  varchar(2) not null, 
        postal_code           varchar(7) not null, 
        country               varchar(50) not null,
        salary                numeric(8,2),

        primary key (owner_ID)
    );



create table publishes
    (
        ISBN                    varchar(18),
        publisher_id            varchar(5),

        primary key (ISBN),
        foreign key (ISBN) references book
            on delete cascade,
        foreign key (publisher_id) references publisher
            on delete cascade
    );

create table handles
    (
        order_id                integer,
        owner_ID                varchar(5),

        primary key (order_id), 
        foreign key (order_id) references orders   
            on delete cascade,
        foreign key (owner_ID) references owners
    );

create table addresses
    (
        order_id                integer,
        address_id              SERIAL UNIQUE,
        street_number           varchar(35) not null, 
        street_name             varchar(35) not null, 
        city                    varchar(35) not null, 
        prov                    varchar(35) not null, 
        postal_code             varchar(7) not null, 
        country                 varchar(50) not null, 

        primary key (address_id)
    );
    ALTER SEQUENCE addresses_address_id_seq RESTART WITH 9999 INCREMENT BY 1;