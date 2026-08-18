STUDENT MANAGEMENT SYSTEM
PROJECT REPORT

Project Made By:
Manpreet Singh

Course:
Bachelor of Computer Applications (BCA)

University:
GNA University

Year:
2026


------------------------------------------------------------
1. INTRODUCTION
------------------------------------------------------------

Student Management System is a simple web based project made for
managing student records. The main purpose of this project is to
make it easier to add, view, update, delete and search student
information.

In colleges, student information is usually stored in different
files or registers. Managing this information manually can take
time and there can also be chances of mistakes. I made this project
to understand how a database and a web application can work
together.

The project contains a dashboard where basic student information
and performance can be seen. It also has separate pages for adding
and managing students.


------------------------------------------------------------
2. PROBLEM STATEMENT
------------------------------------------------------------

Managing student records manually is time consuming and makes it
difficult to search, update and maintain student information.

This project provides a simple system where student records can be
stored in a database and managed from one website.


------------------------------------------------------------
3. OBJECTIVE OF THE PROJECT
------------------------------------------------------------

The main objectives of this project are:

1. To store student information in a database.
2. To add new students easily.
3. To view all student records.
4. To search for a particular student.
5. To edit existing student information.
6. To delete unwanted student records.
7. To calculate average marks and attendance.
8. To display student data using charts.
9. To understand the connection between Flask and MySQL.
10. To improve my practical programming skills.


------------------------------------------------------------
4. TECHNOLOGIES USED
------------------------------------------------------------

The following technologies were used in this project:

Frontend:
- HTML5
- CSS3
- JavaScript

Backend:
- Python
- Flask

Database:
- MySQL

Other Tools:
- Visual Studio Code
- MySQL
- Chart.js
- Git

Python Library:
- mysql-connector-python


------------------------------------------------------------
5. WHY I USED THESE TECHNOLOGIES
------------------------------------------------------------

I used HTML5 for creating the structure of the web pages.

I used CSS3 to design the website and make the pages look clean
and modern.

JavaScript is used mainly for loading dashboard data and showing
charts.

Python was selected for the backend because I already had some
basic knowledge of Python and wanted to understand how it can be
used to create a web application.

I used Flask because it is simple and suitable for a small college
project. It handles the different pages and connects the frontend
with the database.

MySQL is used to store student records. I selected MySQL because
it is a commonly used relational database and I wanted to get
practical experience with SQL.

Chart.js is used to display student statistics in graphical form.


------------------------------------------------------------
6. MAIN FEATURES
------------------------------------------------------------

The project has the following main features:

1. Dashboard
   The dashboard shows total students, average marks, average
   attendance and the top performing student.

2. Add Student
   A new student can be added by entering roll number, name,
   department, semester, email, phone, marks and attendance.

3. View Students
   All students stored in the database can be viewed on one page.

4. Search Student
   Students can be searched using their name, roll number,
   department, email or phone number.

5. Edit Student
   Existing student information can be changed whenever required.

6. Delete Student
   A student record can be deleted from the database.

7. Department Statistics
   The dashboard shows the number of students in different
   departments.

8. Performance Charts
   Charts are used to show marks, attendance, pass/fail results
   and semester-wise student information.

9. Validation
   The system checks marks and attendance so that values cannot
   normally be entered outside the range of 0 to 100.

10. Duplicate Roll Number Check
    The system checks whether the roll number already exists before
    adding or updating a student.


------------------------------------------------------------
7. DATABASE DESIGN
------------------------------------------------------------

The project uses a MySQL database named:

student_management

The main table is:

students

The table contains the following fields:

id
roll_no
name
department
semester
email
phone
marks
attendance


The id field is the primary key and is automatically increased
when a new student is added.

The database is used to save the student information permanently
so that the records are available even after restarting the
application.


------------------------------------------------------------
8. WORKING OF THE PROJECT
------------------------------------------------------------

When the application is started, Flask runs the web server.

The user can open the dashboard in the browser.

From the sidebar, the user can move between:

Dashboard
View Students
Add Student

When a student is added, the form sends the information to the
Flask backend.

Flask checks the information and then sends an SQL query to MySQL.

If everything is correct, the record is inserted into the students
table.

The View Students page reads the records from MySQL and displays
them in a table.

If the user searches for a student, Flask uses a SQL LIKE query to
find matching records.

For editing, the selected student record is loaded into the edit
form. After changing the information, the database record is
updated.

For deleting, the selected student's record is removed from the
database.


------------------------------------------------------------
9. DASHBOARD
------------------------------------------------------------

The dashboard is one of the main parts of the project.

It displays:

- Total number of students
- Average marks
- Average attendance
- Top student
- Students by department
- Pass and fail students
- Average marks by department
- Average attendance by department
- Semester-wise student count
- Department performance table

The dashboard data is taken directly from MySQL.

I used SQL queries such as COUNT(), AVG(), SUM() and GROUP BY to
calculate the required information.


------------------------------------------------------------
10. PROJECT STRUCTURE
------------------------------------------------------------

The project is divided into frontend and backend parts.

Student Management System

    backend/
        app.py

    frontend/
        templates/
            index.html
            students.html
            add_student.html
            edit_student.html
            error.html

        static/
            dashboard.css


The backend contains the Flask application.

The templates folder contains the HTML pages.

The static folder contains the CSS file used for designing the
website.


------------------------------------------------------------
11. VALIDATION
------------------------------------------------------------

Some basic validation has been added to avoid incorrect data.

Roll number and student name cannot be empty.

Department and semester are required.

Marks must be between 0 and 100.

Attendance must also be between 0 and 100.

The project also checks duplicate roll numbers.

This helps to avoid storing incorrect or duplicate student
records.


------------------------------------------------------------
12. WHAT I LEARNED FROM THIS PROJECT
------------------------------------------------------------

While making this project, I learned how different parts of a
web application work together.

I learned how to create Flask routes and how to connect Python
with MySQL.

I also learned how SQL queries can be used to insert, update,
delete and retrieve records.

Another thing I learned was how HTML forms send information to the
backend.

I also got some practical experience with JavaScript and Chart.js
while creating the dashboard charts.

Before making this project, I mostly worked with individual
programming concepts. This project helped me understand how
frontend, backend and database can be combined into one complete
application.


------------------------------------------------------------
13. PROBLEMS FACED DURING DEVELOPMENT
------------------------------------------------------------

I faced a few problems while developing the project.

One problem was connecting Flask with MySQL. Initially the database
connection was not working properly because of configuration
issues.

I also faced problems with Flask packages and Python setup.

Another issue was displaying database information correctly on the
dashboard. I had to check the SQL queries and the data returned
from Flask.

I also had some problems with HTML template paths and CSS files.

After checking the code and testing different parts of the
application, I was able to solve these problems.


------------------------------------------------------------
14. TESTING
------------------------------------------------------------

I tested the main functions of the project manually.

Test 1:
Added a new student and checked whether the record appeared on the
View Students page.

Test 2:
Searched for a student using the name and roll number.

Test 3:
Edited the information of an existing student.

Test 4:
Deleted a student and checked whether the record was removed.

Test 5:
Added different students from different departments and checked
the dashboard statistics.

Test 6:
Entered marks and attendance above 100 and checked the validation.

Test 7:
Tried adding the same roll number again and checked the duplicate
roll number message.

These tests helped me make sure that the main functions were
working properly.


------------------------------------------------------------
15. ADVANTAGES
------------------------------------------------------------

- Easy to use.
- Student records can be stored in one place.
- Searching students is faster.
- Records can be edited easily.
- Unwanted records can be deleted.
- Dashboard gives a quick overview of student performance.
- Uses a proper relational database.
- Can be improved and expanded in the future.


------------------------------------------------------------
16. LIMITATIONS
------------------------------------------------------------

This project is mainly designed as a college-level project.

It currently does not have a separate login system for different
users.

It also does not have advanced features such as online attendance
marking, student fee management or automatic report generation.

The system is currently designed to run locally.


------------------------------------------------------------
17. FUTURE SCOPE
------------------------------------------------------------

There are many things that can be added to this project in the
future.

Some possible improvements are:

- Student login system.
- Admin login.
- Teacher login.
- Attendance management.
- Fee management.
- Subject-wise marks.
- Automatic report card generation.
- Export student records to Excel or PDF.
- Email notifications.
- More detailed analytics.
- Cloud database.
- Online deployment.


------------------------------------------------------------
18. CONCLUSION
------------------------------------------------------------

The Student Management System helped me understand how a complete
web application works.

The project successfully provides basic functions such as adding,
viewing, searching, editing and deleting student records.

It also displays useful academic statistics through the dashboard.

The most useful part of this project for me was learning how Flask,
Python, MySQL, HTML, CSS and JavaScript can be connected together.

Overall, this project gave me practical experience in web
development and database management. I can also use this project as
a base for adding more features in the future.


------------------------------------------------------------
19. PROJECT MADE BY
------------------------------------------------------------

Name: Manpreet Singh

Course: BCA

University: GNA University

Project: Student Management System

Year: 2026


------------------------------------------------------------
20. DECLARATION
------------------------------------------------------------

I hereby declare that this project titled "Student Management
System" was developed by me as part of my academic project work.

I have tried to understand and implement the different parts of
the project including the frontend, backend and database.

Name: Manpreet Singh
