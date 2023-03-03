
CREATE TABLE students (
    id integer PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    marks INTEGER,
    subject VARCHAR(25)
);

INSERT INTO students VALUES(1,'Ryan',98,'Physics');
INSERT INTO students VALUES(2,'Smith',85,'Physics');
INSERT INTO students VALUES(3,'Rahul',99,'Physics');
INSERT INTO students VALUES(1,'Ryan',99,'Chemistry');
INSERT INTO students VALUES(2,'Smith',74,'Chemistry');
INSERT INTO students VALUES(3,'Rahul',78,'Chemistry');
INSERT INTO students VALUES(1,'Ryan',87,'Biology');
INSERT INTO students VALUES(2,'Smith',90,'Biology');
INSERT INTO students VALUES(3,'Rahul',76,'Biology');

select * from students;