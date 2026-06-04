from database import add_student, add_score
from blockchain_utils import add_score_hash
from hash_utils import generate_hash

student_code = "SV003"
full_name = "Trương Văn Hậu"

subject = "Toán cao cấp"
semester = "HK1"
score = 7.5

# Tạo hash
score_hash = generate_hash(
    student_code,
    subject,
    semester,
    score
)

print("=" * 50)
print("HASH:")
print(score_hash)

# Thêm sinh viên
student_id = add_student(
    student_code,
    full_name
)

print(f"Student ID: {student_id}")

# Lưu điểm vào MySQL
add_score(
    student_id,
    subject,
    semester,
    score,
    score_hash
)

print("Đã lưu MySQL")

# Gửi hash lên Blockchain
receipt = add_score_hash(
    student_code,
    score_hash
)

print("Đã lưu Blockchain")
print("Transaction Hash:")
print(receipt["transactionHash"].hex())

print("=" * 50)
print("HOÀN THÀNH")