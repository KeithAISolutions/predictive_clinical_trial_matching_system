
class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = 'postgresql://devuser:devpassword@https://keithaisolutions-special-fortnight-4xgpxj967x535rwg-5432.preview.app.github.dev/:5432/devdb' 

class ProductionConfig:
    DEBUG = False
