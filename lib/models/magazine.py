from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        mag_id = cursor.lastrowid
        conn.close()
        return cls(mag_id, name, category)

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        return cursor.fetchall()

    def authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT au.* FROM authors au
            JOIN articles a ON a.author_id = au.id
            WHERE a.magazine_id = ?
        """, (self.id,))
        return cursor.fetchall()
