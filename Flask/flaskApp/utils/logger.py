from flask import request, jsonify
from flaskApp import app
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

logging.basicConfig(filename='Req_Res.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.after_request   
def after_request_callback(response):   
    response_value = response.get_data()   
    app.logger.debug(response_value.decode("utf-8"))   
    return response

@app.before_request   
def after_request_callback():   
    body = request.json
    param = request.args.to_dict()
    app.logger.debug({'param':param, 'body':body})