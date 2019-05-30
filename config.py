class MariaDBConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:decider@@localhost/test?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
