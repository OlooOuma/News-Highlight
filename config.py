import os

class Config:
    '''
    General configuration parent class
    '''
    TOP_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={}'
    EVERYTHING_URL = 'https://newsapi.org/v2/everything?sources={}&apikey={}'
    SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_API_KEY='e8e06f03414c437cae76e0f3cb40b3d1'
    SECRET_KEY = '1234567890'
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development': DevConfig,
'production': ProdConfig
}
