from __future__ import division
import json
from flask import Response
from flask import request
from app import app
from flask_cors import CORS
from app.models.database import *
from flask_autodoc import Autodoc
#from flask.ext.autodoc import Autodoc

import math
import json

CORS(app)
auto = Autodoc(app)


@app.route('/')
def index_route():
    """
    Index route
    TODO: Need to handle it properly
    :return:
    """
    return '/'


@app.route('/recommendations', methods=['GET', 'POST'])
@auto.doc()
def return_recommendations():
    """
    Returns category and sub-categories
    """
    res = request.get_json()
    Age = res['Age'].lower()
    Gender = res['Gender'].lower()
    TobaccoUser = res['TobaccoUser'].lower()
    SexuallyActive = res['SexuallyActive'].lower()
    print (res, Age, TobaccoUser, SexuallyActive)
    '''
    ret_data = get_recommendations(Age, Gender, TobaccoUser, SexuallyActive)


    data_list = []
    #ret_data =get_recommendations(id)
    print(ret_data)
    l=[]
    for val in ret_data:
        product_dict={
        "id":val[0],
        "Title":val[1],
        "grade":val[2],
        "gender":val[3],
        "recommendations":val[4]
            }
        l.append(product_dict)

    if ret_data is not None:
        response = Response(json.dumps(l), status=200, mimetype='application/json')
        return response
    else:
        ret_data = 'Products Not Found !'
        response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
    '''
    return "Thanks your dat has been recieved"


@app.route('/docs')
def return_api_docs():
    """
    api docs route
    :return:
    """
    return auto.html()
