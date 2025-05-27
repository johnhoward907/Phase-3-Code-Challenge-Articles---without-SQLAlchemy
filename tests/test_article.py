import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection
from scripts.setup_db import setup_database

def setup_module(module):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM authors;
        DELETE FROM magazines;
        INSERT INTO authors (id, name) VALUES (1, 'Author A');
        INSERT INTO magazines (id, name, category) VALUES (1, 'Science Weekly', 'Science');
    """)
    conn.commit()
    conn.close()

def test_create_article():
    article = Article(title="Amazing Science", author_id=1, magazine_id=1)
    article.save()
    assert article.id is not None

def test_find_article_by_title():
    article = Article.find_by_title("Amazing Science")
    assert article is not None
    assert article.title == "Amazing Science"