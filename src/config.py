import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

load_dotenv(os.path.join(BASE_DIR, '.env'))

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# SMTP_USER = os.getenv("SMTP_USER")
# SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# DB_TEST_HOST = os.getenv("DB_TEST_HOST")
# DB_TEST_PORT = os.getenv("DB_TEST_PORT")
# DB_TEST_NAME = os.getenv("DB_TEST_NAME")
# DB_TEST_USER = os.getenv("DB_TEST_USER")
# DB_TEST_PASSWORD = os.getenv("DB_TEST_PASSWORD")
