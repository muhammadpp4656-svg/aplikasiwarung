import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="finances.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Tabel untuk pemasukan dan pengeluaran
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT, -- 'pemasukan' atau 'pengeluaran'
                amount REAL,
                description TEXT,
                date TEXT
            )
        ''')
        # Tabel untuk utang
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS debts (
                id INTEGER PRIMARY KEY,
                person TEXT,
                amount REAL,
                is_paid INTEGER, -- 0: belum bayar, 1: sudah bayar
                date TEXT
            )
        ''')
        self.conn.commit()

    def add_transaction(self, type, amount, description, date):
        self.cursor.execute("INSERT INTO transactions (type, amount, description, date) VALUES (?, ?, ?, ?)",
                            (type, amount, description, date))
        self.conn.commit()

    def get_all_transactions(self):
        self.cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        return self.cursor.fetchall()

    def add_debt(self, person, amount, date):
        self.cursor.execute("INSERT INTO debts (person, amount, is_paid, date) VALUES (?, ?, 0, ?)",
                            (person, amount, date))
        self.conn.commit()

    def get_all_debts(self):
        self.cursor.execute("SELECT * FROM debts WHERE is_paid = 0 ORDER BY date DESC")
        return self.cursor.fetchall()

    def mark_debt_as_paid(self, debt_id):
        self.cursor.execute("UPDATE debts SET is_paid = 1 WHERE id = ?", (debt_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()