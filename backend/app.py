from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import mysql.connector
from mysql.connector import Error
import os

# Project folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend", "templates"),
    static_folder=os.path.join(BASE_DIR, "frontend", "static")
)

app.secret_key = "studenthub_secret_key"


# MySQL database details
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "student_management"
}


def connect_db():
    return mysql.connector.connect(**DB_CONFIG)


# ---------------- DASHBOARD ----------------

@app.route("/")
def dashboard():

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        # Total students
        cursor.execute("SELECT COUNT(*) AS total FROM students")
        total_students = cursor.fetchone()["total"]

        # Average marks
        cursor.execute(
            "SELECT COALESCE(AVG(marks), 0) AS avg_marks FROM students"
        )
        average_marks = round(
            float(cursor.fetchone()["avg_marks"] or 0), 2
        )

        # Average attendance
        cursor.execute(
            "SELECT COALESCE(AVG(attendance), 0) AS avg_attendance FROM students"
        )
        average_attendance = round(
            float(cursor.fetchone()["avg_attendance"] or 0), 2
        )

        # Top student
        cursor.execute(
            """
            SELECT name, marks
            FROM students
            ORDER BY marks DESC
            LIMIT 1
            """
        )

        top_student = cursor.fetchone()

        if top_student:
            top_student_name = top_student["name"]
            top_student_marks = float(top_student["marks"] or 0)
        else:
            top_student_name = "No Students"
            top_student_marks = 0

        # Students by department
        cursor.execute(
            """
            SELECT department, COUNT(*) AS total
            FROM students
            GROUP BY department
            ORDER BY total DESC
            """
        )

        department_data = cursor.fetchall()

        department_names = [
            row["department"] for row in department_data
        ]

        department_counts = [
            int(row["total"]) for row in department_data
        ]

        # Average marks by department
        cursor.execute(
            """
            SELECT department, ROUND(AVG(marks), 2) AS average_marks
            FROM students
            GROUP BY department
            ORDER BY average_marks DESC
            """
        )

        marks_data = cursor.fetchall()

        department_marks_names = [
            row["department"] for row in marks_data
        ]

        department_average_marks = [
            float(row["average_marks"] or 0)
            for row in marks_data
        ]

        # Average attendance by department
        cursor.execute(
            """
            SELECT department, ROUND(AVG(attendance), 2) AS average_attendance
            FROM students
            GROUP BY department
            ORDER BY average_attendance DESC
            """
        )

        attendance_data = cursor.fetchall()

        department_attendance_names = [
            row["department"] for row in attendance_data
        ]

        department_average_attendance = [
            float(row["average_attendance"] or 0)
            for row in attendance_data
        ]

        # Pass and fail
        cursor.execute(
            """
            SELECT
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END) AS passed,
                SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) AS failed
            FROM students
            """
        )

        result = cursor.fetchone()

        passed_students = int(result["passed"] or 0)
        failed_students = int(result["failed"] or 0)

        # Students by semester
        cursor.execute(
            """
            SELECT semester, COUNT(*) AS total
            FROM students
            GROUP BY semester
            ORDER BY semester
            """
        )

        semester_data = cursor.fetchall()

        semester_names = [
            str(row["semester"]) for row in semester_data
        ]

        semester_counts = [
            int(row["total"]) for row in semester_data
        ]

        # Department performance table
        cursor.execute(
            """
            SELECT
                department,
                COUNT(*) AS total_students,
                ROUND(AVG(marks), 2) AS average_marks,
                ROUND(AVG(attendance), 2) AS average_attendance,
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END) AS passed,
                SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) AS failed
            FROM students
            GROUP BY department
            ORDER BY average_marks DESC
            """
        )

        department_performance = cursor.fetchall()

        return render_template(
            "index.html",
            total_students=total_students,
            average_marks=average_marks,
            average_attendance=average_attendance,
            top_student_name=top_student_name,
            top_student_marks=top_student_marks,
            department_names=department_names,
            department_counts=department_counts,
            department_marks_names=department_marks_names,
            department_average_marks=department_average_marks,
            department_attendance_names=department_attendance_names,
            department_average_attendance=department_average_attendance,
            passed_students=passed_students,
            failed_students=failed_students,
            semester_names=semester_names,
            semester_counts=semester_counts,
            department_performance=department_performance
        )

    except Error as e:
        return render_template(
            "error.html",
            error=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


# ---------------- DASHBOARD API ----------------

@app.route("/api/dashboard")
def dashboard_api():

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT COUNT(*) AS total FROM students")
        total_students = cursor.fetchone()["total"]

        cursor.execute(
            "SELECT COALESCE(AVG(marks), 0) AS average FROM students"
        )
        average_marks = round(
            float(cursor.fetchone()["average"] or 0), 2
        )

        cursor.execute(
            "SELECT COALESCE(AVG(attendance), 0) AS average FROM students"
        )
        average_attendance = round(
            float(cursor.fetchone()["average"] or 0), 2
        )

        cursor.execute(
            """
            SELECT name, marks
            FROM students
            ORDER BY marks DESC
            LIMIT 1
            """
        )

        top_student = cursor.fetchone()

        if top_student:
            top_student_name = top_student["name"]
            top_student_marks = float(top_student["marks"] or 0)
        else:
            top_student_name = "No Students"
            top_student_marks = 0

        cursor.execute(
            """
            SELECT department, COUNT(*) AS total
            FROM students
            GROUP BY department
            ORDER BY total DESC
            """
        )

        department_data = cursor.fetchall()

        cursor.execute(
            """
            SELECT department, ROUND(AVG(marks), 2) AS average_marks
            FROM students
            GROUP BY department
            ORDER BY department
            """
        )

        marks_data = cursor.fetchall()

        cursor.execute(
            """
            SELECT department, ROUND(AVG(attendance), 2) AS average_attendance
            FROM students
            GROUP BY department
            ORDER BY department
            """
        )

        attendance_data = cursor.fetchall()

        cursor.execute(
            """
            SELECT
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END) AS passed,
                SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) AS failed
            FROM students
            """
        )

        pass_fail = cursor.fetchone()

        cursor.execute(
            """
            SELECT semester, COUNT(*) AS total
            FROM students
            GROUP BY semester
            ORDER BY semester
            """
        )

        semester_data = cursor.fetchall()

        cursor.execute(
            """
            SELECT
                department,
                COUNT(*) AS total_students,
                ROUND(AVG(marks), 2) AS average_marks,
                ROUND(AVG(attendance), 2) AS average_attendance,
                SUM(CASE WHEN marks >= 40 THEN 1 ELSE 0 END) AS passed,
                SUM(CASE WHEN marks < 40 THEN 1 ELSE 0 END) AS failed
            FROM students
            GROUP BY department
            ORDER BY average_marks DESC
            """
        )

        department_performance = cursor.fetchall()

        return jsonify({
            "total_students": total_students,
            "average_marks": average_marks,
            "average_attendance": average_attendance,
            "top_student_name": top_student_name,
            "top_student_marks": top_student_marks,

            "department_names": [
                row["department"] for row in department_data
            ],

            "department_counts": [
                int(row["total"]) for row in department_data
            ],

            "department_marks_names": [
                row["department"] for row in marks_data
            ],

            "department_average_marks": [
                float(row["average_marks"] or 0)
                for row in marks_data
            ],

            "department_attendance_names": [
                row["department"] for row in attendance_data
            ],

            "department_average_attendance": [
                float(row["average_attendance"] or 0)
                for row in attendance_data
            ],

            "passed_students": int(pass_fail["passed"] or 0),
            "failed_students": int(pass_fail["failed"] or 0),

            "semester_names": [
                str(row["semester"]) for row in semester_data
            ],

            "semester_counts": [
                int(row["total"]) for row in semester_data
            ],

            "department_performance": department_performance
        })

    except Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


# ---------------- VIEW STUDENTS ----------------

@app.route("/students")
def students():

    db = None
    cursor = None

    try:
        search = request.args.get("search", "").strip()

        db = connect_db()
        cursor = db.cursor(dictionary=True)

        if search:
            search_value = "%" + search + "%"

            cursor.execute(
                """
                SELECT *
                FROM students
                WHERE roll_no LIKE %s
                   OR name LIKE %s
                   OR department LIKE %s
                   OR email LIKE %s
                   OR phone LIKE %s
                ORDER BY id DESC
                """,
                (
                    search_value,
                    search_value,
                    search_value,
                    search_value,
                    search_value
                )
            )
        else:
            cursor.execute(
                """
                SELECT *
                FROM students
                ORDER BY id DESC
                """
            )

        student_list = cursor.fetchall()

        return render_template(
            "students.html",
            students=student_list,
            search=search
        )

    except Error as e:
        return render_template(
            "error.html",
            error=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


# ---------------- ADD STUDENT ----------------

@app.route("/add_student", methods=["GET", "POST"])
def add_student():

    if request.method == "POST":

        roll_no = request.form.get("roll_no", "").strip()
        name = request.form.get("name", "").strip()
        department = request.form.get("department", "").strip()
        semester = request.form.get("semester", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        marks = request.form.get("marks", "0").strip()
        attendance = request.form.get("attendance", "0").strip()

        if not roll_no or not name or not department or not semester:
            flash("Please fill all required fields.", "error")
            return redirect(url_for("add_student"))

        try:
            semester = int(semester)
            marks = float(marks or 0)
            attendance = float(attendance or 0)

            if semester < 1 or semester > 8:
                raise ValueError("Semester must be between 1 and 8.")

            if marks < 0 or marks > 100:
                raise ValueError("Marks must be between 0 and 100.")

            if attendance < 0 or attendance > 100:
                raise ValueError(
                    "Attendance must be between 0 and 100."
                )

        except ValueError as e:
            flash(str(e), "error")
            return redirect(url_for("add_student"))

        db = None
        cursor = None

        try:
            db = connect_db()
            cursor = db.cursor()

            # Check if roll number already exists
            cursor.execute(
                "SELECT id FROM students WHERE roll_no = %s",
                (roll_no,)
            )

            if cursor.fetchone():
                flash("Roll number already exists.", "error")
                return redirect(url_for("add_student"))

            cursor.execute(
                """
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
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    roll_no,
                    name,
                    department,
                    semester,
                    email or None,
                    phone or None,
                    marks,
                    attendance
                )
            )

            db.commit()

            flash("Student added successfully.", "success")
            return redirect(url_for("students"))

        except Error as e:
            if db:
                db.rollback()

            flash("Database error: " + str(e), "error")
            return redirect(url_for("add_student"))

        finally:
            if cursor:
                cursor.close()

            if db:
                db.close()

    return render_template("add_student.html")


# ---------------- EDIT STUDENT ----------------

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM students WHERE id = %s",
            (id,)
        )

        student = cursor.fetchone()

        if not student:
            flash("Student not found.", "error")
            return redirect(url_for("students"))

        if request.method == "POST":

            roll_no = request.form.get("roll_no", "").strip()
            name = request.form.get("name", "").strip()
            department = request.form.get("department", "").strip()
            semester = request.form.get("semester", "").strip()
            email = request.form.get("email", "").strip()
            phone = request.form.get("phone", "").strip()
            marks = request.form.get("marks", "0").strip()
            attendance = request.form.get("attendance", "0").strip()

            if not roll_no or not name or not department or not semester:
                flash("Please fill all required fields.", "error")
                return redirect(
                    url_for("edit_student", id=id)
                )

            try:
                semester = int(semester)
                marks = float(marks or 0)
                attendance = float(attendance or 0)

                if semester < 1 or semester > 8:
                    raise ValueError(
                        "Semester must be between 1 and 8."
                    )

                if marks < 0 or marks > 100:
                    raise ValueError(
                        "Marks must be between 0 and 100."
                    )

                if attendance < 0 or attendance > 100:
                    raise ValueError(
                        "Attendance must be between 0 and 100."
                    )

            except ValueError as e:
                flash(str(e), "error")
                return redirect(
                    url_for("edit_student", id=id)
                )

            # Check duplicate roll number
            cursor.execute(
                """
                SELECT id
                FROM students
                WHERE roll_no = %s AND id != %s
                """,
                (roll_no, id)
            )

            if cursor.fetchone():
                flash(
                    "Another student has this roll number.",
                    "error"
                )
                return redirect(
                    url_for("edit_student", id=id)
                )

            cursor.execute(
                """
                UPDATE students
                SET
                    roll_no = %s,
                    name = %s,
                    department = %s,
                    semester = %s,
                    email = %s,
                    phone = %s,
                    marks = %s,
                    attendance = %s
                WHERE id = %s
                """,
                (
                    roll_no,
                    name,
                    department,
                    semester,
                    email or None,
                    phone or None,
                    marks,
                    attendance,
                    id
                )
            )

            db.commit()

            flash("Student updated successfully.", "success")
            return redirect(url_for("students"))

        return render_template(
            "edit_student.html",
            student=student
        )

    except Error as e:
        if db:
            db.rollback()

        return render_template(
            "error.html",
            error=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


# ---------------- DELETE STUDENT ----------------

@app.route("/delete/<int:id>", methods=["POST"])
def delete_student(id):

    db = None
    cursor = None

    try:
        db = connect_db()
        cursor = db.cursor()

        cursor.execute(
            "DELETE FROM students WHERE id = %s",
            (id,)
        )

        if cursor.rowcount == 0:
            flash("Student not found.", "error")
        else:
            db.commit()
            flash("Student deleted successfully.", "success")

        return redirect(url_for("students"))

    except Error as e:
        if db:
            db.rollback()

        flash("Database error: " + str(e), "error")
        return redirect(url_for("students"))

    finally:
        if cursor:
            cursor.close()

        if db:
            db.close()


# ---------------- ERROR PAGE ----------------

@app.errorhandler(404)
def not_found(error):
    return render_template(
        "error.html",
        error="The page you are looking for does not exist."
    ), 404


if __name__ == "__main__":
    app.run(debug=True)