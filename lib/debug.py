from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

# Create entries
author = Author.create("Howard")
magazine = Magazine.create("AI Weekly", "Tech")
article = Article.create("Understanding AGI", author.id, magazine.id)

# Fetching
print(author.articles())
print(author.magazines())
print(magazine.authors())
