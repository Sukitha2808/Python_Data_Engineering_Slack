create table  bt1(id int primary key ,
                  name varchar(15) not null);
 
insert into bt1 values(10, 'Aswin');
insert into bt1 values(11,'Aswin');
insert into bt1 values(12,'Doss');
insert into bt1 values(13,'Doss');
ALTER TABLE bt1 add email varchar(20) null;
select * from bt1;
update bt1 set email='boosch_abcdefgh@yahoo.com' where name ='Aswin';
update bt1 set email='murugadoss@yahoo.com'  where name='Doss';
UPDATE bt1 SET email='boosch_abcdefgh@yahoo.com' WHERE name ='Aswin';
select * from bt1;

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(20)
);
 
select email , count(*) from bt1 group by email having count(*) > 1 ;
 
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(25),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE
);
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
SELECT * FROM Authors;
SELECT * FROM Books;
commit;
DELETE FROM Authors where AuthorID=2;

drop table Authors;
drop table Books;
show tables;

CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(20)
);

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(25),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE SET NULL
);
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
######
CREATE TABLE Authors (

    AuthorID INT PRIMARY KEY,

    AuthorName VARCHAR(20)

);
 

 
CREATE TABLE Books (

    BookID INT PRIMARY KEY,

    Title VARCHAR(25),

    AuthorID INT,

    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE CASCADE

);
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
 
 
SELECT * FROM Authors;

SELECT * FROM Books;
 
 
CREATE TABLE Authors (AuthorID INT PRIMARY KEY,AuthorName VARCHAR(20));
 
CREATE TABLE Books (BookID INT PRIMARY KEY,Title VARCHAR(25),AuthorID INT,

                    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID));
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
 
commit;

 


CREATE TABLE Authors (

    AuthorID INT PRIMARY KEY,

    AuthorName VARCHAR(20)

);
 

 
CREATE TABLE Books (

    BookID INT PRIMARY KEY,

    Title VARCHAR(25),

    AuthorID INT,

    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON DELETE SET NULL

);
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');

INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);

INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
 ######
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    AuthorName VARCHAR(20)
);
 
CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(25),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID) ON  UPDATE CASCADE
);
 
INSERT INTO Authors (AuthorID, AuthorName) VALUES (1, 'John Doe');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (2, 'Minal Pandey');
INSERT INTO Authors (AuthorID, AuthorName) VALUES (3, 'Mahi Pandey');
 
INSERT INTO Books (BookID, Title, AuthorID) VALUES (101, 'Introduction to SQL', 1);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (102, 'Database Fundamentals', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (103, 'Advanced SQL', 2);
INSERT INTO Books (BookID, Title, AuthorID) VALUES (104, 'Web Development', 3);
select * from Authors;
select * from Books;
UPDATE Authors SET AuthorID = 1 WHERE AuthorID = 4;
select * from Books;


