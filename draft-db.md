 create table jamroom_details (
    jamroom_id number(4) primary key,
    name varchar2(20),
   price_per_hour number(4),
    location varchar2(200),
    owner_id number(4) );


create table owner_details (
owner_id number(4) primary key,
owner_name varchar2(20),
owner_contact number(10)
);

create table working_hours (
day number(2),
hours varchar(10)
);



create table customer_details (
customer_id number(4) primary key,
customer_name varchar(20),
booking_id varchar(4)
);    

create table bookings (
customer_id references customer_details(customer_id) on delete cascade,
jamroom_id references jamroom(jamroom_id) on delete cascade,
timings references  
);



Headers:
blog_jamroom.csv :
               id,name,location,price_per_hour,owner_id_id

blog_owner.csv:
id,owner_name,owner_ph_no

blog_customer.csv:
"id","booking_istrue","customer_name"

blog_booking.csv:
"id","booked_time_slot","customer_id_id","jamroom_id_id"

blog_operatinghours.csv:
"id","start_hour","end_hour","jamroom_id_id","weekday"
