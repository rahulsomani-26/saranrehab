import sqlite3 as sq
from tkinter import Tk, messagebox
import bcrypt

class Database:

    def __init__(self):
        self.connect_db()
    
    def connect_db(self):
        try:
            self.con = sq.connect('sarandb.sqlite3')
            self.cur = self.con.cursor()
            self.cur.execute("""
                CREATE TABLE IF NOT EXISTS USER (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL, 
                    password TEXT NOT NULL
                )
            """)
            self.cur.execute('''
                CREATE TABLE IF NOT EXISTS patients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    registration_number TEXT,
                    name TEXT,
                    address TEXT,
                    date_of_joining TEXT,
                    addiction_type TEXT,
                    gender TEXT,
                    duration TEXT,
                    room_type TEXT,
                    monthly_charge TEXT,
                    photo_path TEXT
                )
            ''')
            self.con.commit()
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))
    
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed
    
    def store_user(self, username, password):
        hashed_password = self.hash_password(password)
        try:
            self.cur.execute('INSERT INTO USER (username, password) VALUES (?, ?)', (username, hashed_password))
            self.con.commit()
            messagebox.showinfo(title="Success", message=f"User {username} added successfully.")
        except sq.IntegrityError:
            messagebox.showerror(title="Error", message=f"Username {username} already exists.")
        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    def verify_user(self, username, password):
        try:
            self.cur.execute('SELECT password FROM USER WHERE username = ?', (username,))
            result = self.cur.fetchone()
            if result:
                stored_password = result[0]
                if bcrypt.checkpw(password.encode('utf-8'), stored_password):
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            raise Exception(f"Error verifying user: {str(e)}")
        
    def insert_patient_data(self, data):
        self.cur.execute('''
            INSERT INTO patients (
                registration_number, name, address, date_of_joining,
                addiction_type, gender, duration, room_type,
                monthly_charge, photo_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        self.con.commit()

    def search_patient_by_name(self, name):
        self.cur.execute('SELECT * FROM patients WHERE name = ? COLLATE NOCASE', (name,))
        result = self.cur.fetchall()
        return result

