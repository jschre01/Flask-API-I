from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import string
import random
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return 'Hello, World!'

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name') 
      search_job = request.args.get('job')
      if search_username :
         subdict = {'users_list': []}
         if search_job :
            for user in users['users_list']:
               if user['name'] == search_username and user['job'] == search_job:                  subdict['users_list'].append(user)
              
         else :
            for user in users['users_list']:
               if user['name'] == search_username:
                  subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      if not request.args.get('id'):
         newID = generateID()
         userToAdd['id'] = newID
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201
      return resp

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
            if user['id'] == id:
               return user
         return ({})
      return users
   elif request.method == 'DELETE':
      if id:
         for user in users['users_list']:
            if user['id'] == id:
               users['users_list'].remove(user)
               resp = jsonify(success=True)
               return resp
         return users

def generateID():
   id = ''
   for i in range(3):
      id = id + random.choice(string.ascii_lowercase)
   for i in range(3):
      id = id + str(random.randint(0,9))
   for user in users['users_list']:
      if user['id'] == id:
         return generateID()
   return id

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}
