from flask import Flask

application = Flask(__name__, template_folder='../templates', static_folder='./static')

from routes import *

if __name__ == '__main__':
    application.run(debug=True)

