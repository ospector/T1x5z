from flask import Flask
import logging
from time import gmtime, strftime

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('usage.log')
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)


app = Flask(__name__)


@app.route("/")
def hello():
    now = strftime("%a %b %d %Y %H:%M:%S %Z%z", gmtime())


    logger.log(msg="read at %s" % now, level=logging.INFO)
    return "Time is %s" % now
