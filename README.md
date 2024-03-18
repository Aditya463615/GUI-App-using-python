# GUI App using Python & Flask

We can create beautiful websites and webpages using Flask, but now we can use the same website as a local desktop application.

## Modules

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following modules:

```bash
pip install PyQt5.Qt
pip install PyQt5.QtWebEngineWidgets
pip install PyQt5.QtWidgets
pip install PyQt5
pip install flask
```
```bash
pip install subprocess
pip install requests
pip install multiprocessing
pip install sys
pip install os
pip install signal
pip install logging
```

## Server.py
Edit the routes of the server only.
```python
appName = open('info.txt','r').readline()
print(appName)

app = Flask(appName)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/")
def mainPage():                                              #main page 
    return "Hello World!"

@app.route("/info")                                          #App's info page
def greet():
    return f"{open('info.txt','r').read()}"
    
@app.route('/shutdown/true', methods=['GET'])                #to close the server 
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(port=4321)
```

## App.pyw
```python
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.web = QWebEngineView()
        self.setCentralWidget(self.web)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle(appName)
        
    def closeEvent(self, event):
        print("Window has been closed!")
        requests.get('http://localhost:4321/shutdown/true') # closing the server
        event.accept()

def run_flask_server():
    subprocess.run(['pyw', 'server.pyw']) # run the server before starting app

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName(appName)

    window = MainWindow()
    window.web.load(QUrl("http://localhost:4321/")) # opening the window to serve the server
    window.show()

    # Start the Flask server in a separate process
    flask_process = Process(target=run_flask_server)
    flask_process.start()

    sys.exit(app.exec_())
```
## info.txt
1st line refers the name of the application.
```
MyApp__v1.9.0
```
## Screenshot
![Screenshot](https://github.com/Aditya463615/GUI-App-using-python/blob/main/Screenshot.png?raw=true)
