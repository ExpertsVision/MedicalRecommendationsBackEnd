from __future__ import division
import json
from flask import Response
from flask import request
from app import app
from flask_cors import CORS
from app.models.database import *
from flask_autodoc import Autodoc
#from flask.ext.autodoc import Autodoc
import requests
import math
import json
import pandas as pd

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
    url = 'https://epssdata.ahrq.gov/'
    responses = requests.get(url)
    test = responses.json()
    test1 = test['tools']
    id_list=[]
    text_list=[]
    title_list=[]
    url_list=[]

    for x in test1:
        id_list.append(x)
        try:
            title= test1[x]['title']
            title_list.append(title)
        except Exception as e:
            title=None
            title_list.append("")
            print(e)
               
        try:
            url=str(test1[x]['url'])
            url_list.append(url)
        except Exception as e:
            url=None
            url_list.append(url)
            print(e)
                    
                    
        try:
            text= str(test1[x]['text'])
            text_list.append(text)
        except Exception as e:
            text=None
            text_list.append(text)
            print(e)

    df = pd.DataFrame({'id':id_list, 
                        'title':title_list,
                        'url_list':url_list,
                        'text':text_list
                        })
            
    df.to_csv('tools.csv')
    '''print(type(test1))
                print(type(test2))
                id_list=[]
                title_list=[]
                clinical_list=[]
                clinicalUrl_list=[]
                other_list=[]
                other_url_list=[]
                rationale_list=[]
                topic_list=[]
            
                for x in test1:
                    id_list.append(x)
                    try:
                        title= test1[x]['title']
                        title_list.append(title)
                    except Exception as e:
                        title=None
                        title_list.append("")
                        print(e)
               
                    try:
                        clinical=str(test1[x]['clinical'])
                        clinical_list.append(clinical)
                    except Exception as e:
                        clinical=None
                        clinical_list.append(clinical)
                        print(e)
                    
                    
                    try:
                        clinicalUrl= str(test1[x]['clinicalUrl'])
                        clinicalUrl_list.append(clinicalUrl)
                    except Exception as e:
                        clinicalUrl=None
                        clinicalUrl_list.append(clinicalUrl)
                        print(e)
                    
                    
                    try:
                        other= str(test1[x]['other'])
                        other_list.append(other)
                    except Exception as e:
                        other=None
                        other_list.append(other)
                        print(e)
                    
                    try:
                        other_url= str(test1[x]['otherUrl'])
                        other_url_list.append(other_url)
                    except Exception as e:
                        other_url=None
                        other_url_list.append(other_url)
                        print(e)
                
            
                    try:
                        topic=str(test1[x]['topic'])
                        topic_list.append(topic)
                    except Exception as e:
                        topic=None
                        topic_list.append(topic)
                        print(e)
                
                    try:
                        rationale = str(test1[x]['rationale'])
                        rationale_list.append(rationale)
                    except Exception as e:
                        rationale=None
                        rationale_list.append(rationale)
                        print(e)
                    
            
                    print(x, title, clinical, other, other_url, topic, rationale)
            
                df = pd.DataFrame({'id':id_list, 
                                    'title':title_list,
                                    'clinical':clinical_list, 
                                    'clinicalUrl':clinicalUrl_list,
                                    'other':other_list,
                                    'otherUrl':other_url_list,
                                    'topic':topic_list,
                                    'rationale':rationale_list
                                    })
            
                df.to_csv('general_recommendation.csv')'''

    response = Response(json.dumps(test1), status=404, mimetype='application/json')
    return response

@app.route('/docs')
def return_api_docs():
    """
    api docs route
    :return:
    """
    return auto.html()
