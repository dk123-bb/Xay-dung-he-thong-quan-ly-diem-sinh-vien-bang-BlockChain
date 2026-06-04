from flask import Flask, render_template, request, redirect, session
import mysql.connector
import hashlib

# ================= BLOCKCHAIN IMPORT (NEW) =================
from blockchain_utils import build_key, add_score_hash

app = Flask(__name__)
app.secret_key = "secret_key"


# ================= DB =================
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_score"
    )


# ================= HASH =================
def create_hash(student_id, subject, semester, score, prev_hash="0"):
    data = f"{student_id}{subject}{semester}{score}{prev_hash}"
    return hashlib.sha256(data.encode()).hexdigest()


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        role = request.form.get("role")

        db = get_db()
        cursor = db.cursor(dictionary=True)

        # ========== TEACHER ==========
        if role == "teacher":

            username = request.form.get("username")
            password = request.form.get("password")

            if username == "admin" and password == "123":
                session["user_id"] = 0
                session["name"] = "Admin"
                session["role"] = "teacher"
                return redirect("/teacher_dashboard")

            return "Sai thông tin teacher"

        # ========== STUDENT ==========
        elif role == "student":

            student_code = request.form.get("student_code")
            password = request.form.get("password")  # ignore

            cursor.execute("""
                SELECT * FROM students WHERE student_code=%s
            """, (student_code,))

            user = cursor.fetchone()

            if user:
                session["user_id"] = user["id"]
                session["name"] = user["full_name"]
                session["role"] = "student"
                return redirect("/student_dashboard")

            return "Sai student_code"

    return render_template("login.html")


# ================= TEACHER DASHBOARD =================
@app.route("/teacher_dashboard")
def teacher_dashboard():
    if session.get("role") != "teacher":
        return redirect("/")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT s.*, st.full_name, st.student_code
        FROM scores s
        JOIN students st ON s.student_id = st.id
        ORDER BY s.id DESC
    """)
    data = cursor.fetchall()

    cursor.execute("""
        SELECT id, student_code, full_name FROM students
    """)
    students = cursor.fetchall()

    db.close()

    return render_template(
        "teacher_dashboard.html",
        user=session["name"],
        data=data,
        students=students
    )


# ================= ADD STUDENT =================
@app.route("/add_student", methods=["POST"])
def add_student():
    if session.get("role") != "teacher":
        return "No permission"

    student_code = request.form["student_code"]
    full_name = request.form["full_name"]

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT * FROM students WHERE student_code=%s
    """, (student_code,))
    exist = cursor.fetchone()

    if exist:
        return "Student already exists"

    cursor.execute("""
        INSERT INTO students(student_code, full_name)
        VALUES (%s, %s)
    """, (student_code, full_name))

    db.commit()
    db.close()

    return redirect("/teacher_dashboard")


# ================= ADD SCORE (🔥 FIXED BLOCKCHAIN) =================
@app.route("/add_score", methods=["POST"])
def add_score():
    if session.get("role") != "teacher":
        return "No permission"

    student_code = request.form["student_code"]
    subject = request.form["subject"]
    semester = request.form["semester"]
    score = request.form["score"]

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT id FROM students WHERE student_code=%s
    """, (student_code,))
    student = cursor.fetchone()

    if not student:
        return "Student not found"

    student_id = student["id"]

    cursor.execute("""
        SELECT score_hash FROM scores ORDER BY id DESC LIMIT 1
    """)
    last = cursor.fetchone()

    prev_hash = last["score_hash"] if last else "0"

    new_hash = create_hash(student_id, subject, semester, score, prev_hash)

    # ================= SAVE MYSQL =================
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO scores(student_id, subject, semester, score, score_hash)
        VALUES (%s,%s,%s,%s,%s)
    """, (student_id, subject, semester, score, new_hash))

    db.commit()
    db.close()

    # ================= 🔥 SEND TO GANACHE (NEW) =================
    try:
        key = build_key(student_code, subject, semester)
        add_score_hash(key, new_hash)
        print("BLOCKCHAIN UPDATED SUCCESSFULLY")
    except Exception as e:
        print("BLOCKCHAIN ERROR:", e)

    return redirect("/teacher_dashboard")


# ================= STUDENT DASHBOARD =================
@app.route("/student_dashboard")
def student_dashboard():
    if session.get("role") != "student":
        return redirect("/")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM scores WHERE student_id=%s
    """, (session["user_id"],))

    data = cursor.fetchall()
    db.close()

    return render_template(
        "student_dashboard.html",
        user=session["name"],
        data=data
    )


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)