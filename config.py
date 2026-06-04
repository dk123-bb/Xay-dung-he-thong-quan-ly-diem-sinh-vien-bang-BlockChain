# config.py

MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB = "student_score"

GANACHE_URL = "http://127.0.0.1:7545"

SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{MYSQL_USER}:"
    f"{MYSQL_PASSWORD}@"
    f"{MYSQL_HOST}:{MYSQL_PORT}/"
    f"{MYSQL_DB}"
)

SQLALCHEMY_TRACK_MODIFICATIONS = False