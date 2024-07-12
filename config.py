class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'dev'

class TestingConfig:
    TESTING = True
    SECRET_KEY = 'test'

class ProductionConfig:
    SECRET_KEY = 'prod'
