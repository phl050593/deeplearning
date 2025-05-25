import sqlite3
import pandas as pd

# 1. 連線到 SQLite 資料庫（會自動建立 .db 檔）
conn = sqlite3.connect('f1_analysis.db')
cursor = conn.cursor()

# 2. 建立四張表
cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Pos INTEGER,
    Driver TEXT,
    Nationality TEXT,
    Car TEXT,
    PTS REAL,
    year INTEGER,
    Code TEXT
);""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Pos INTEGER,
    Team TEXT,
    PTS REAL,
    year INTEGER
);""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS winners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Grand_Prix TEXT,
    Driver TEXT,
    Car TEXT,
    Time TEXT,
    year INTEGER,
    Code TEXT
);""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS fastest_laps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Grand_Prix TEXT,
    Driver TEXT,
    Car TEXT,
    Fastest_Lap TEXT,
    Fastest_Lap_Time TEXT,
    Avg_Speed REAL,
    year INTEGER
);""")
conn.commit()

# 3. 匯入你的 csv 檔案到資料庫
drivers = pd.read_csv('./data/drivers_updated.csv')
teams = pd.read_csv('./data/teams_updated.csv')
winners = pd.read_csv('./data/winners.csv')
fastest_laps = pd.read_csv('./data/fastest_laps_updated.csv')

drivers.to_sql('drivers', conn, if_exists='replace', index=False)
teams.to_sql('teams', conn, if_exists='replace', index=False)
winners.to_sql('winners', conn, if_exists='replace', index=False)
fastest_laps.to_sql('fastest_laps', conn, if_exists='replace', index=False)

conn.commit()
conn.close()
print("✅ 資料庫建立完成！")
