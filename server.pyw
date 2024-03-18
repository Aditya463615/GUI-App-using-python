from flask import Flask, request
import os
import signal
import logging


appName = open('info.txt','r').readline()
print(appName)


app = Flask(appName)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/info")
def greet():
    return f"{open('info.txt','r').read()}"
    
@app.route('/shutdown/true', methods=['GET'])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run(port=4321)
