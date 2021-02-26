# import libraries necessary for the app to work
from flask import Flask, jsonify

# configure flask
app = Flask(__name__)

# TODO add / route to print JSONified hello world

# only run the app if it is being called directly
# this prevents it running e.g. if being erroneously imported
if __name__ == "__main__":
    app.run(debug=True)
