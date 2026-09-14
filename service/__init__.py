"""
Service Package
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This must be imported after the Flask app is created
from service import routes
from service.common import log_handlers

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info(" S E R V I C E   R U N N I N G ".center(70, "*"))
app.logger.info(70 * "*")
