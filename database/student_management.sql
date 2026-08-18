DROP DATABASE IF EXISTS student_management;

CREATE DATABASE student_management;

USE student_management;


CREATE TABLE students (

    id INT AUTO_INCREMENT PRIMARY KEY,

    roll_no VARCHAR(20) NOT NULL UNIQUE,

    name VARCHAR(100) NOT NULL,

    department VARCHAR(50) NOT NULL,

    semester INT NOT NULL,

    email VARCHAR(100),

    phone VARCHAR(15),

    marks DECIMAL(5,2) DEFAULT 0,

    attendance DECIMAL(5,2) DEFAULT 0

);


-- Sample student

INSERT INTO students
(
    roll_no,
    name,
    department,
    semester,
    email,
    phone,
    marks,
    attendance
)
VALUES
(
    'BCA001',
    'Manpreet Singh',
    'BCA',
    5,
    'manpreet@gmail.com',
    '9876543210',
    89.50,
    95.00
);


-- Some sample records for testing

INSERT INTO students
(
    roll_no,
    name,
    department,
    semester,
    email,
    phone,
    marks,
    attendance
)
VALUES
(
    'BCA002',
    'Aman Kumar',
    'BCA',
    5,
    'aman@gmail.com',
    '9876543211',
    76.50,
    88.00
),

(
    'BCA003',
    'Simran Kaur',
    'BCA',
    5,
    'simran@gmail.com',
    '9876543212',
    92.00,
    94.00
),

(
    'BBA001',
    'Harpreet Kaur',
    'BBA',
    4,
    'harpreet@gmail.com',
    '9876543213',
    68.00,
    81.00
),

(
    'BTECH001',
    'Rahul Sharma',
    'B.Tech',
    6,
    'rahul@gmail.com',
    '9876543214',
    55.50,
    72.00
);


SELECT * FROM students;