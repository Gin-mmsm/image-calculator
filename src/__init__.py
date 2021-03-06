from flask import Flask

app = Flask(__name__)

# limit upload file size : 10MB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

import src.views
