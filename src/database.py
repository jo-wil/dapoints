import hashlib
import logging
import sqlite3

logger = logging.getLogger("uvicorn.error")

DEFAULT_PASSWORD = "cec747f10204682e9519c4522f2289574f72560eb47a380c0edced6d93e37012"

def run_migrations():
    logger.info("Running migrations.")
    con = sqlite3.connect("app.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Draft (Id INTEGER PRIMARY KEY, UserId INTEGER, TournamentId INTEGER, PlayerId INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS Player (Id INTEGER PRIMARY KEY, Name TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS Round (Id INTEGER PRIMARY KEY, TournamentId INTEGER, PlayerId INTEGER, Score INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS TournamentId (Id INTEGER PRIMARY KEY, Name TEXT, StartTimestamp INTEGER, StopTimestamp INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS User (Id INTEGER PRIMARY KEY, Name TEXT, Email TEXT, Password TEXT)")
    cur.executemany("INSERT OR IGNORE INTO User(Id, Name, Email, Password) VALUES (?, ?, ?, ?)", [
        (1, "Andrew Dala", "andrew@gmail.com", DEFAULT_PASSWORD),
        (2, "Connor Griffin", "connor@gmail.com", DEFAULT_PASSWORD),
        (3, "Daniel Araujo", "daniel@gmail.com", DEFAULT_PASSWORD),
        (4, "Eric Wagner", "eric@gmail.com", DEFAULT_PASSWORD),
        (5, "Joey Wilson", "joey.wilson.a@gmail.com", DEFAULT_PASSWORD),
        (6, "Perry McBeth", "perry@gmail.com", DEFAULT_PASSWORD),
    ])
    con.commit()
    con.close()
