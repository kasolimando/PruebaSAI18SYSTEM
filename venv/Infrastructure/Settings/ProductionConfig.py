import os

class ProductionConfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:kr140701@localhost/sr"
    SQLALCHEMY_TRACK_MODIFICATIONS = False