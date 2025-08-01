from flask import Flask
from app.routes import routes

app = Flask(__name__)
app.secret_key = "super-secret-key"
routes(app)

if __name__ == "__main__":
    app.run(debug=True)