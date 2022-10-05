import os
from datetime import timedelta

import jwt


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'changeme'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'changeme'
    JWT_ALGORITHM = 'EdDSA'
    JWT_DECODE_ALGORITHMS = jwt.algorithms.get_default_algorithms()
    JWT_PRIVATE_KEY = os.environ.get('JWT_PRIVATE_KEY')
    JWT_PUBLIC_KEY = os.environ.get('JWT_PUBLIC_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    WTF_CSRF_ENABLED = False
