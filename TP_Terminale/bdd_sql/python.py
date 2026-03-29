import sqlite3
connexion = sqlite3.connect('db_livres_auteurs_python.db')

c = connexion.cursor()
c.execute("""
SELECT titre FROM LIVRES WHERE id>=16
""")
print("Nouveaux livres", c.fetchall())
c.execute("""
SELECT nom FROM AUTEURS WHERE id>=11
""")
print("Nouveaux auteurs", c.fetchall())
connexion.close()
