import hashlib


def generate_hash(student_code, subject, semester, score):

    raw_data = (
        f"{student_code}|"
        f"{subject}|"
        f"{semester}|"
        f"{score}"
    )

    return hashlib.sha256(raw_data.encode("utf-8")).hexdigest()


def verify_hash(student_code, subject, semester, score, old_hash):

    new_hash = generate_hash(student_code, subject, semester, score)
    return new_hash == old_hash