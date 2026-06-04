import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="student_score",
        cursorclass=pymysql.cursors.DictCursor
    )


def add_student(student_code, full_name):
    conn = get_connection()

    with conn.cursor() as cursor:
        sql = """
        INSERT INTO students (student_code, full_name)
        VALUES (%s,%s)
        """
        cursor.execute(sql, (student_code, full_name))
        conn.commit()
        return cursor.lastrowid


def add_score(student_id, subject, semester, score, score_hash):
    conn = get_connection()

    with conn.cursor() as cursor:
        sql = """
        INSERT INTO scores
        (student_id, subject, semester, score, score_hash)
        VALUES (%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (student_id, subject, semester, score, score_hash))
        conn.commit()

    conn.close()


# =========================
# FIX: lấy nhiều record (KHÔNG xóa hàm cũ)
# =========================
def get_score_by_student_code(student_code):

    conn = get_connection()

    with conn.cursor() as cursor:

        sql = """
        SELECT
            st.student_code,
            st.full_name,
            sc.subject,
            sc.semester,
            sc.score,
            sc.score_hash
        FROM students st
        JOIN scores sc ON st.id = sc.student_id
        WHERE st.student_code = %s
        ORDER BY sc.id DESC
        LIMIT 1
        """

        cursor.execute(sql, (student_code,))
        result = cursor.fetchone()

    conn.close()
    return result


# =========================
# 🔥 NEW: lấy theo subject + semester (BỔ SUNG)
# =========================
def get_score_detail(student_code, subject, semester):

    conn = get_connection()

    with conn.cursor() as cursor:

        sql = """
        SELECT
            st.student_code,
            st.full_name,
            sc.subject,
            sc.semester,
            sc.score,
            sc.score_hash
        FROM students st
        JOIN scores sc ON st.id = sc.student_id
        WHERE st.student_code=%s
        AND sc.subject=%s
        AND sc.semester=%s
        """

        cursor.execute(sql, (student_code, subject, semester))
        result = cursor.fetchone()

    conn.close()
    return result