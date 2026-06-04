from database import get_score_by_student_code
from blockchain_utils import get_score_hash
from hash_utils import generate_hash, verify_hash


student_code = "SV004"

print("=" * 60)
print("VERIFY DATA INTEGRITY")
print("=" * 60)

data = get_score_by_student_code(student_code)

if not data:
    print("Khong tim thay sinh vien")
    exit()

mysql_hash = data["score_hash"]

mysql_valid = verify_hash(
    data["student_code"],
    data["subject"],
    data["semester"],
    data["score"],
    mysql_hash
)

# =========================
# FIX KEY BLOCKCHAIN
# =========================
from blockchain_utils import build_key

key = build_key(
    data["student_code"],
    data["subject"],
    data["semester"]
)

blockchain_hash = get_score_hash(key)

current_hash = generate_hash(
    data["student_code"],
    data["subject"],
    data["semester"],
    data["score"]
)

print("\nTHONG TIN SINH VIEN")
print("-" * 60)

print("Student Code :", data["student_code"])
print("Full Name    :", data["full_name"])
print("Subject      :", data["subject"])
print("Semester     :", data["semester"])
print("Score        :", data["score"])

print("\nVERIFY RESULT")
print("-" * 60)

if mysql_valid and current_hash == blockchain_hash:

    print("DATA VERIFIED")
else:
    print("DATA TAMPERED")

print("=" * 60)