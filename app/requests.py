import urllib.request,json
from .models import Source, Article


#Getting api Key
api_key = None

#Getting the urls
sources_url = None
everything_url = None
category=None
language=None
country = None

def configure_request(app):
    global api_key, sources_url, everything_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_URL']
    everything_url = app.config['EVERYTHING_URL']
  

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)

        all_news_sources = None

        if sources_response['sources']:
            news_sources_list = sources_response['sources']
            all_news_sources = process_sources(news_sources_list)

            return all_news_sources

def process_sources(sources_list):
    '''
    Function  that processes the news sources and transform them to a list of Objects

    Args:
        sources_list: A list of dictionaries that contain sources details

    Returns :
        all_news_sources: A list of source objects
    '''
    all_news_sources = []
    for news_source in sources_list:
        id = news_source.get('id')
        name = news_source.get('name')
        description = news_source.get('description')
        url = news_source.get('url')
    
        source_object = Source(id, name, description, url, category, language, country)
        all_news_sources.append(source_object)

    return all_news_sources

def view_source(source_id):
    '''
    Function that processes a news source and transforms it to a list of Objects

    Args:
        source_id: An id of a specific news source

    Returns :
        source_news: A list of source objects
    '''
    get_source_news_url = everything_url.format(source_id, api_key)

    with urllib.request.urlopen(get_source_news_url) as url:
        source_news_data = url.read()
        source_news_response = json.loads(source_news_data)

        source_articles = None

        if source_news_response['articles']:
            source_news_list = source_news_response['articles']
            source_articles = process_news(source_news_list)

            return source_articles

def process_news(articles_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain articles details

    Returns :
        movie_results: A list of an source's articles objects
    '''

    source_articles = []
    for article in articles_list:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        if urlToImage:
            article_object = Article(author, title, description, url, urlToImage, publishedAt, content)
            source_articles.append(article_object)

    return source_articles
