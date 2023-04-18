import sqlite3
import re
from flask import Flask, request, jsonify, redirect, url_for
from database import *
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
# ,get_raw_jwt,revoked_tokens

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Set your own secret key

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    # Get the user credentials from the request
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Verify the user credentials
    if not username or not password or username != 'myuser' or password != 'mypassword':
        return jsonify({"msg": "Bad username or password"}), 401

    # Generate an access token and return it to the user
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# @app.route('/logout', methods=['DELETE'])
# @jwt_required
# def logout():
#     # Revoke the user's access token
#     jti = get_raw_jwt()['jti']
#     revoked_tokens.add(jti)
#     return jsonify({"msg": "Successfully logged out"}), 200


# Define the root URL
@app.route('/')
def index():
  return ("Welcome to my PhoneBook API")

# Define the /PhoneBook/list endpoint
@app.route('/PhoneBook/list', methods=['GET'])
@jwt_required
def list_contacts():
  contacts = get_contacts()
  return jsonify(contacts)


# Define the /PhoneBook/add endpoint
@app.route('/PhoneBook/add', methods=['POST'])
def add_contact():
  data = request.form
  name = request.json['name']
  phone_number = request.json['phone_number']
  name_regex = r'^[a-zA-Z ,.\'-]+(?:[a-zA-Z\'’]+)?(?:-[a-zA-Z\'’]+)?(?:,[a-zA-Z ,.\'-]+(?:[a-zA-Z\'’]+)?(?:-[a-zA-Z\'’]+)?)?$'
  phone_regex = r'^(?!\+01\s\(\d{3}\)\s\d{3}-\d{4}$)(?!(\+1234\s\(201\)\s\d{3}-\d{4})$)(?!7031111234)(\(\d{3}\)\d{3}-\d{4}|\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9})$'

  if not re.match(name_regex, name):
      return jsonify({'error': 'Invalid name'}), 400

  if not re.match(phone_regex, phone_number):
      return jsonify({'error': 'Invalid phone number'}), 400

  add_contact_to_database(name, phone_number)
  return redirect(url_for('list_contacts'))

# Define the /PhoneBook/deleteByName endpoint
@app.route('/PhoneBook/deleteByName', methods=['PUT'])
def delete_contact_by_name():
    name = request.json['name']
    success = delete_contact_by_name_from_database(name)
    if success:
        return jsonify({'message': 'Contact deleted successfully'}), 200
    else:
        return jsonify({'error': 'Contact not found'}), 404

@app.route('/PhoneBook/deleteByNumber', methods=['PUT'])
def delete_contact_by_number():
    phone_number = request.json['phone_number']
    success = delete_contact_by_number_from_database(phone_number)
    if success:
        return jsonify({'message': 'number deleted successfully'}), 200
    else:
        return jsonify({'error': 'Number not found'}), 404

@app.route('/PhoneBook/logs', methods=['GET'])
def view_logs():
  page = int(request.args.get('page', 1))
  limit = 10
  offset = (page - 1) * limit
  conn = sqlite3.connect('phonebook.db')
  c = conn.cursor()
  c.execute('SELECT * FROM log ORDER BY timestamp DESC LIMIT ? OFFSET ?', (limit, offset))
  rows = c.fetchall()
  log_data = [{'timestamp': row[0], 'action': row[1], 'name': row[2], 'phone_number': row[3]} for row in rows]
  conn.close()

  return jsonify(log_data)

if __name__ == '__main__':
  app.run(debug=True)