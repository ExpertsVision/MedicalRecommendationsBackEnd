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
    print(len(res))
    mixgender="men and women"
    risknameN="None"
    risknameA="Age"
    risknameO="Other"
    SA="Sexually Active"
    TU="Tobacco user"
    #print(res.keys())
    length=len(res)
    #print length
    #print(res)

    #elif (length==5) and ("age" in res and "gender" in res and "tobacco user" in res and "sexuallyActive" in res and "pregnant" in res):
    Age=res['age']
    pregnantrisk=res['pregnant']
    risknameT=res['tobaccoUser'].lower()
    risknameS=res['sexuallyActive']
    Gender=res['gender'].lower()
    if len(str(Age)) ==0:
        if len(pregnantrisk)==0:
            pregnantrisk="Pregnant"
        if len(risknameT)==0:
            risknameT="Tobacco user"
        if len(risknameS)==0:
            risknameS="Sexually Active"
        if len(Gender)==0:
            GenderM="male"
            GenderF="female"
            ret_data =get_AgeRecommendations(GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk)
            if ret_data is not None:
                #print ret_data
                #for i in ret_data:
                i=0
                recommendations=[]
                for i in range(len(ret_data)):
                    ret_general_data=[]
                    ret_general_data=functoin_retrieve_data_againsst_general_id(ret_data[i][6])
                    if ret_general_data is not None:
                        for x in ret_general_data:
                            #Title=x[0]
                            #topic=x[1]
                            #print(ret_general_data)
                            general_dict={
                                "clinical":x[0],
                                "clinicalurl":x[1],
                                "Other":x[2],
                                "discussion":x[3],
                                "rationale":x[4],
                                "Title":x[5],
                                "topic":x[6]
                            }
                    ret_tools_data=functoin_retrieve_data_againsst_tools_id(ret_data[i][7], ret_data[i][8], ret_data[i][9])
                    print(ret_tools_data)
                    if ret_tools_data is not None:
                        print(ret_tools_data)
                        j=0
                        try:
                            for j in range(len(ret_tools_data)):
                                tools_dict={
                                "Title":ret_tools_data[j][0],
                                "url":ret_tools_data[j][1]

                                }
                                j+=1
                        except:
                            tools_dict={}
                            pass

                    product_dict = {
                        "Title": ret_data[i][0],
                        "Grade": ret_data[i][1],
                        "Recomendation": ret_data[i][2],
                        "Frequency of Service": ret_data[i][3],
                        "Risk Factor Information": ret_data[i][4],
                        "Rationale": ret_data[i][5],
                        "General":general_dict,
                        "tools":tools_dict
                        
                        
                        }
                    i+=1
                    recommendations.append(product_dict)
                #print product_dict
                    #print recommendations
            #if Age in(product_dict[])
                response = Response(json.dumps(recommendations), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        else:
            ret_data =get_AgeGenderRecommendations(Gender, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk)
            if ret_data is not None:
                i=0
                recommendations=[]
                for i in range(len(ret_data)):
                    ret_general_data=functoin_retrieve_data_againsst_general_id(ret_data[i][6])
                    if ret_general_data is not None:
                        for x in ret_general_data:
                            #Title=x[0]
                            #topic=x[1]
                            #print(ret_general_data)
                            general_dict={
                                "clinical":x[0],
                                "clinicalurl":x[1],
                                "Other":x[2],
                                "discussion":x[3],
                                "rationale":x[4],
                                "Title":x[5],
                                "topic":x[6]
                            }
                         
                    ret_tools_data=functoin_retrieve_data_againsst_tools_id(ret_data[i][7], ret_data[i][8], ret_data[i][9])
                    print(ret_tools_data)
                    if ret_tools_data is not None:
                        print(ret_tools_data)
                        j=0
                        try:
                            for j in range(len(ret_tools_data)):
                                tools_dict={
                                "Title":ret_tools_data[j][0],
                                "url":ret_tools_data[j][1]

                                }
                                j+=1
                        except:
                            tools_dict={}
                            pass
                    product_dict = {
                        "Title": ret_data[i][0],
                        "Grade": ret_data[i][1],
                        "Recomendation": ret_data[i][2],
                        "Frequency of Service": ret_data[i][3],
                        "Risk Factor Information": ret_data[i][4],
                        "Rationale": ret_data[i][5],
                        "General":general_dict,
                        "tools":tools_dict
                        }
                    
                    i+=1
                    recommendations.append(product_dict)
                response = Response(json.dumps(recommendations), status=200, mimetype='application/json')
                return response
            #if Age in(product_dict[])
                #response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                #return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response

    if len(pregnantrisk)==0:
        pregnantrisk="Pregnant"
    if len(risknameT)==0:
        risknameT="Tobacco user"
    if len(risknameS)==0:
        risknameS="Sexually Active"
    if len(Gender)==0:
        GenderM="male"
        GenderF="female"
        ret_data =get_Recommendations(Age, GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk)
        if ret_data is not None:
            i=0
            recommendations=[]
            for i in range(len(ret_data)):
                ret_general_data=functoin_retrieve_data_againsst_general_id(ret_data[i][6])
                if ret_general_data is not None:
                    for x in ret_general_data:
                        general_dict={
                            "clinical":x[0],
                            "clinicalurl":x[1],
                            "Other":x[2],
                            "discussion":x[3],
                            "rationale":x[4],
                            "Title":x[5],
                            "topic":x[6]
                        }
                ret_tools_data=functoin_retrieve_data_againsst_tools_id(ret_data[i][7], ret_data[i][8], ret_data[i][9])
                print(ret_tools_data)
                if ret_tools_data is not None:
                    print(ret_tools_data)
                    j=0
                    try:
                        for j in range(len(ret_tools_data)):
                            tools_dict={
                            "Title":ret_tools_data[j][0],
                            "url":ret_tools_data[j][1]

                            }
                            j+=1
                    except:
                        tools_dict={}
                        pass 

                product_dict = {
                        "Title": ret_data[i][0],
                        "Grade": ret_data[i][1],
                        "Recomendation": ret_data[i][2],
                        "Frequency of Service": ret_data[i][3],
                        "Risk Factor Information": ret_data[i][4],
                        "Rationale": ret_data[i][5],
                        "General":general_dict,
                        "tools":tools_dict
                        }
                        
                i+=1    
                recommendations.append(product_dict)
            response = Response(json.dumps(recommendations), status=200, mimetype='application/json')
            return response
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    ret_data =get_AGSTP_recommendations(Age, Gender,mixgender, risknameT, risknameS,risknameA,risknameO,pregnantrisk)
    if ret_data is not None:
        print("******")
        i=0
        recommendations=[]
        for i in range(len(ret_data)):
            if ret_data[i][7] is not None:
                tool=ret_data[i][7]
                #print((tool))
            ret_general_data=functoin_retrieve_data_againsst_general_id(ret_data[i][6])
            if ret_general_data is not None:
                for x in ret_general_data:
                    general_dict={
                        "clinical":x[0],
                        "clinicalurl":x[1],
                        "rationale":x[4],
                        "Title":x[5],
                        "topic":x[6]
                    }
                    other={
                        "discussion":x[3],
                        "Other":x[2]
                    }
            #if ret_data[i][7] is not None:
                #print(ret_data[i][7])
            #if ret_data[i][8] is not None:
                #print(ret_data[i][8])
            #if ret_data[i][9] is not None:
               # print(ret_data[i][9])
            ret_tools_data=functoin_retrieve_data_againsst_tools_id(ret_data[i][7], ret_data[i][8], ret_data[i][9])
            print(ret_tools_data)
            if ret_tools_data is not None:
                print(ret_tools_data)
                j=0
                try:
                    for j in range(len(ret_tools_data)):
                        tools_dict={
                        "Title":ret_tools_data[j][0],
                        "url":ret_tools_data[j][1]

                        }
                        j+=1
                except:
                    tools_dict={}
                    pass
            product_dict = {
                    "Title": ret_data[i][0],
                    "Grade": ret_data[i][1],
                    "Recomendation": ret_data[i][2],
                    "Frequency of Service": ret_data[i][3],
                    "Risk Factor Information": ret_data[i][4],
                    "Rationale": ret_data[i][5],
                    "General":general_dict,
                    "Others":other,
                    "tools":tools_dict
                    }
                    
            i+=1        
            recommendations.append(product_dict)
        response = Response(json.dumps(recommendations), status=200, mimetype='application/json')
        return response
    #if Age in(product_dict[])
        #response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
        #return response
    else:
        ret_data = 'Products Not Found !'
        response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
        return response


@app.route('/docs')
def return_api_docs():
    """
    api docs route
    :return:
    """
    return auto.html()
