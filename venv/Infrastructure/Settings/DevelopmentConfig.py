import os

class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:kr140701@localhost/sr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False