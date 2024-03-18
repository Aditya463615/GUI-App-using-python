import sys
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore
from PyQt5 import QtGui
import subprocess
import requests
from multiprocessing import Process


appName = open('info.txt','r').readline()
print(appName)


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
