import os
import json
from flask import Flask

app = Flask(__name__)

app.secret_key = 'some_secret'

username = "default"

def set_username():
    """
    sets the user's username
    """
    username = input("Please enter your desired username: ")
    if len(username) > 0:
        print("Hello "+ username)
        return(username)
    else:
        print("Please enter a username")
        print("")
        set_username()
    




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)