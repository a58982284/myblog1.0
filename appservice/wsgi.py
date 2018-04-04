# coding: utf-8
import sys
sys.path.append ("..")
from app import create_app, db



application = create_app('production')



if __name__ == '__main__':
    application.run()