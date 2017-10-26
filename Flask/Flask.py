from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # hello_world2()
    return 'Hello World!'

def hello_world2():
    return  "my name is Dimon"

if __name__ == '__main__':
    app.run()












