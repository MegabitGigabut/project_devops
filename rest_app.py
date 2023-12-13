from flask import Flask, request, render_template
from utility_methods import *


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
#Commit Dev 2
#Commit Dev 3
@app.route("/users/<user_id>", methods=["POST", "GET", "PUT", "DELETE"])
def interact_with_use(user_id):
    if request.method == 'POST':
        user_creation_request = {
            "user_id" : 2,
            "user_name" : "Jason"
        }
        created_user = create_user(user_creation_request)
        return render_template('create.html', created_user=created_user[0][0])
    elif request.method == 'GET':
        username = get_user(user_id)
        return render_template('get.html', username=username)
    elif request.method == 'PUT':
        updated_user = update_user(user_id)
        return render_template('update.html', updated_user=updated_user)
    elif request.method == 'DELETE':
        delete_user(user_id)
        return render_template('delete.html', delete_user=delete_user)
    
if __name__ == '__main__':
   app.run(debug = True)