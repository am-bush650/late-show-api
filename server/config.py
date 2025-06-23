import os


SQLALCHEMY_DATABASE_URI = "postgresql://late_show_user:1234@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY", "secret")
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KET", "jwt-secret")