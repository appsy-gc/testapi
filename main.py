from flask import Flask

app = Flask(__name__)

# DATABASE_URL=

# FLASK_APP=main
# FLASK_ENV=development
# FLASK_DEBUG=True

@app.route("/")
def hello_world():
    return "Hello world!"