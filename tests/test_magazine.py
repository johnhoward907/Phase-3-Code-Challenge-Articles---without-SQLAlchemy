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
        INSERT INTO authors (id, name) VALUES (1, 'Jane'), (2, 'John');
        INSERT INTO magazines (id, name, category) VALUES (1, 'World News', 'News');
        INSERT INTO articles (title, author_id, magazine_id) VALUES 
        ('News 1', 1, 1), 
        ('News 2', 2, 1);
    """)
    conn.commit()
    conn.close()

def test_find_magazine_by_name():
    mag = Magazine.find_by_name("World News")
    assert mag is not None
    assert mag.category == "News"

def test_magazine_authors():
    mag = Magazine.find_by_id(1)
    authors = mag.authors()
    assert len(authors) == 2
    assert any(author['name'] == 'Jane' for author in authors)