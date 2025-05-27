import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection
from scripts.setup_db import setup_database

@pytest.fixture(autouse=True)
def setup():
    setup_database()
    yield

def test_author_creation_and_fetching_articles():
    author = Author.create("Jane")
    mag = Magazine.create("Nature", "Science")
    Article.create("On Evolution", author.id, mag.id)
    
    articles = author.articles()
    assert len(articles) == 1
