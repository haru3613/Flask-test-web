from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/hello/<name>/<surname>")   # 傳入兩個參數
def hello_name(name, surname):
    return "<h1>Hello, {} {}</h1>".format(name, surname)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)