import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLAlchemy의 이벤트를 처리하는 옵션 (현재 프로젝트에서 필요하지 않음)
