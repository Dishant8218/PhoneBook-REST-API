import sqlite3
import datetime


def create_table():
   conn = sqlite3.connect('phonebook.db')
   c = conn.cursor()
   c.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone_number TEXT)')
   c.execute('CREATE TABLE IF NOT EXISTS log (timestamp TEXT, action TEXT, name TEXT, phone_number TEXT)')
   conn.commit()
   conn.close()


def get_contacts():
   create_table()
   conn = sqlite3.connect('phonebook.db')
   c = conn.cursor()
   c.execute('SELECT name, phone_number FROM contacts')
   rows = c.fetchall()
   contacts = [{'name': row[0], 'phone_number': row[1]} for row in rows]
   conn.close()
   return contacts


def add_contact_to_database(name, phone_number):
   conn = sqlite3.connect('phonebook.db')
   c = conn.cursor()
   c.execute('INSERT INTO contacts VALUES (?, ?)', (name, phone_number))
   conn.commit()
   timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   action = "Added contact"
   c.execute('INSERT INTO log VALUES (?, ?, ?, ?)', (timestamp, action, name, phone_number))
   conn.commit()
   conn.close()


def delete_contact_by_name_from_database(name):
   conn = sqlite3.connect('phonebook.db')
   c = conn.cursor()
   c.execute('DELETE FROM contacts WHERE name=?', (name,))
   num_deleted = c.rowcount
   if num_deleted > 0:
       conn.commit()
       timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       action = "Deleted contact by name"
       c.execute('INSERT INTO log VALUES (?, ?, ?, ?)', (timestamp, action, name, ""))
       conn.commit()
   conn.close()
   return num_deleted > 0


def delete_contact_by_number_from_database(phone_number):
   conn = sqlite3.connect('phonebook.db')
   c = conn.cursor()
   c.execute('DELETE FROM contacts WHERE phone_number=?', (phone_number,))
   num_deleted = c.rowcount
   if num_deleted > 0:
       conn.commit()
       timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       action = "Deleted contact by phone number"
       c.execute('INSERT INTO log VALUES (?, ?, ?, ?)', (timestamp, action, "", phone_number))
       conn.commit()
   conn.close()
   return num_deleted > 0



