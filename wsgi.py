# coding: utf-8
from app import create_app, db

application = create_app('production')

@application.before_first_request
def create_database():
     db.create_all()

if __name__ == '__main__':
    application.run()