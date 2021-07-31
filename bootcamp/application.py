from flask import Flask

app = Flask(__name__)

@app.route("/")

def home_page():
    return "Hello world"
    
if __name__=="_main__":
     app.run()
