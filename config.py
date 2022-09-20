##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
