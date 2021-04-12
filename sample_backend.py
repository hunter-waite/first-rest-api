import string
import random
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      search_job = request.args.get('job')
      if search_username and search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username and user['job'] == search_job:
               subdict['users_list'].append(user)
         return subdict
      return users
      if search_username :
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username:
               subdict['users_list'].append(user)
         return subdict
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = gen_unique_id()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True, updatedUser=userToAdd)
      resp.status_code = 201 #optionally, you can always set a response code. 
      return resp


@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
   print(id)
   if request.method == 'DELETE':
      for user in users['users_list']:
         if user['id'] == id:
            print("here")
            users['users_list'].remove(user)
            resp = jsonify(success=True)
            resp.status_code = 204
            return resp
      resp = jsonify(success=True)
      resp.status_code = 404
      return resp
   

def gen_unique_id():
   id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
   i = 0
   while i < len(users['users_list']):
      if users['users_list'][i]['id'] == id:
         id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
         i = 0
      i += 1
   return id
