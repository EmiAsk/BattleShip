import sqlite3
con = sqlite3.connect('battleship.bd')
cur = con.cursor()
cur.execute("UPDATE games SET result = ? WHERE name = ?", (config.RESULT, config.NAME))

cur.execute("UPDATE games SET score = ? WHERE name = ?", (config.SCORE, config.NAME))

wins = cur.execute("SELECT wins FROM users WHERE duration = ''").fetchall()
for elem in wins:
    wins = elem[0]
cur.execute("UPDATE users SET wins = ? WHERE name = ?", (wins + 1, config.NAME))

lose = cur.execute("SELECT lose FROM users WHERE duration = ''").fetchall()
for elem in lose:
    lose = elem[0]
cur.execute("UPDATE users SET lose = ? WHERE name = ?", (lose + 1, config.NAME))

score = cur.execute("SELECT score FROM users WHERE duration = ''").fetchall()
for elem in score:
    score = elem[0]
if config.SCORE > score:
    cur.execute("UPDATE users SET best_result (score) = ? WHERE name = ?", (config.SCORE, config.NAME))

con.commit()
con.close()