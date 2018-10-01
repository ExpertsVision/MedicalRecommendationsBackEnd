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
    print length
    print(res)
    '''if length==1 and "age" in res:
        Age = res['age'].lower()
        ret_data =get_age_recommendations(Age)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif length==1 and "gender" in res:
        
        Gender = res['gender'].lower()
        ret_data =get_gender_recommendations(Gender, mixgender)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif length==1 and "pregnant" in res:
        
        risknameP = res['pregnant']
        ret_data =get_risks_recommendations(risknameP,SA, TU,risknameN, risknameA,risknameO )
        #ret_data =get_risk_recommendations(risknameP, risknameO, risknameA, risknameN, TU, SA)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif length==1 and "sexuallyActive" in res:
        
        risknameS = res['sexuallyActive']
        pregnantrisk="Pregnant"
        ret_data =get_risks_recommendations(risknameS,risknameO, risknameA, risknameN, TU, pregnantrisk )
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif length==1 and "tobacco user" in res:
        risknameT = res['tobacco user']
        pregnantrisk="Pregnant"
        ret_data =get_risks_recommendations(risknameT,risknameO, risknameA, risknameN, SA, pregnantrisk )
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==2):
        if "age" in res and "gender" in res:
            Age=res['age']
            Gender=res['gender'].lower()
            ret_data =get_agegender_recommendations(Age, Gender,mixgender)
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "age" in res and "sexuallyActive" in res:
            Age=res['age']
            sexulysct=res['sexuallyActive']
            pregnantrisk="Pregnant"
            ret_data =get_ageandrisk_recommendations(Age, sexulysct, TU, pregnantrisk,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "age" in res and "tobacco user" in res:
            Age=res['age']
            sexulysct=res['tobacco user'].lower()
            pregnantrisk="Pregnant"
            ret_data =get_ageandrisk_recommendations(Age, sexulysct, SA, pregnantrisk,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
        elif "age" in res and "pregnant" in res:
            Age=res['age']
            sexulysct=res['pregnant']
            #pregnantrisk="Pregnant"
            ret_data =get_ageandrisk_recommendations(Age, sexulysct, SA, TU,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "sexuallyActive" in res and "pregnant" in res:
            #Age=res['age']
            sexulysct=res['pregnant']
            sexulysct2=res['sexuallyActive']
            #pregnantrisk="Pregnant"
            ret_data =get_risks_recommendations(sexulysct,sexulysct2, TU,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "tobacco user" in res and "pregnant" in res:
            #Age=res['age']
            sexulysct=res['pregnant']
            sexulysct2=res['tobacco user']
            #pregnantrisk="Pregnant"
            ret_data =get_risks_recommendations(sexulysct,sexulysct2, SA,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "tobacco user" in res and "sexuallyActive" in res:
            #Age=res['age']
            sexulysct=res['sexuallyActive']
            sexulysct2=res['tobacco user']
            pregnantrisk="Pregnant"
            ret_data =get_risks_recommendations(sexulysct,sexulysct2, pregnantrisk,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "gender" in res and "pregnant" in res:
            Gender=res['gender']
            sexulysct=res['pregnant']
            #pregnantrisk="Pregnant"
            ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, SA, TU,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "gender" in res and "sexuallyActive" in res:
            Gender=res['gender']
            sexulysct=res['sexuallyActive']
            pregnantrisk="Pregnant"
            ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, pregnantrisk, TU,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        elif "gender" in res and "tobacco user" in res:
            Gender=res['gender']
            sexulysct=res['tobacco user']
            pregnantrisk="Pregnant"
            ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, pregnantrisk, SA,risknameN, risknameA,risknameO )
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
    #elif (length==3) and ("age" in res and "gender" in res and "sexuallyActive" in res):
    elif (length==3) and ("age" in res and "gender" in res):
        Age=res['age']
        Gender=res['gender'].lower()
        for i in res:
            if i=="sexuallyActive":
                riskname=res['sexuallyActive']
                risknameP="Pregnant"
                ret_data =get_AGS_recommendations(Age, Gender,mixgender, riskname,risknameN,risknameA,risknameO, TU, risknameP)
                if ret_data is not None:
                #if Age in(product_dict[])
                    response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                    return response
                else:
                    ret_data = 'Products Not Found !'
                    response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                    return response
            elif i=="tobacco user":
                riskname=res['tobacco user']
                risknameP="Pregnant"
                ret_data =get_AGS_recommendations(Age, Gender,mixgender, riskname,risknameN,risknameA,risknameO, SA, risknameP)
                if ret_data is not None:
                #if Age in(product_dict[])
                    response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                    return response
                else:
                    ret_data = 'Products Not Found !'
                    response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                    return response
            elif i=="pregnant":
                riskname=res['pregnant']
                #risknameP="Pregnant"
                ret_data =get_AGS_recommendations(Age, Gender,mixgender, riskname,risknameN,risknameA,risknameO, SA, TU)
                if ret_data is not None:
                #if Age in(product_dict[])
                    response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                    return response
                else:
                    ret_data = 'Products Not Found !'
                    response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                    return response
        
    elif (length==3) and ("sexuallyActive" in res and "tobacco user" in res and "pregnant" in res):
        sexulysct=res['sexuallyActive']
        sexulysct2=res['tobacco user']
        pregnantrisk=res["pregnant"]
        ret_data =get_risks_recommendations(sexulysct,sexulysct2, pregnantrisk,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("age" in res and "tobacco user" in res and "pregnant" in res):
        Age=res['age']
        sexulysct=res['tobacco user']
        pregnantrisk=["pregnant"]
        ret_data =get_ageandrisk_recommendations(Age, sexulysct, SA, pregnantrisk,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("age" in res and "sexuallyActive" in res and "pregnant" in res):
        Age=res['age']
        sexulysct=res['sexuallyActive']
        pregnantrisk=["pregnant"]
        ret_data =get_ageandrisk_recommendations(Age, sexulysct, TU, pregnantrisk,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("age" in res and "sexuallyActive" in res and "tobacco user" in res):
        Age=res['age']
        sexulysct=res['sexuallyActive']
        sexulysct2=res['tobacco user']
        pregnantrisk="Pregnant"
        ret_data =get_ageandrisk_recommendations(Age, sexulysct, sexulysct2, pregnantrisk,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("gender" in res and "tobacco user" in res and "pregnant" in res):
        Gender=res['gender']
        sexulysct=res['pregnant']
        sexulysct2=res['tobacco user']
        #pregnantrisk="Pregnant"
        ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, SA, sexulysct2,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("gender" in res and "sexuallyActive" in res and "pregnant" in res):
        Gender=res['gender']
        sexulysct=res['pregnant']
        sexulysct2=res['sexuallyActive']
        #pregnantrisk="Pregnant"
        ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, TU, sexulysct2,risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==3) and ("gender" in res and "sexuallyActive" in res and "tobacco user" in res):
        Gender=res['gender']
        sexulysct=res['tobacco user']
        sexulysct2=res['sexuallyActive']
        pregnantrisk="Pregnant"
        ret_data =get_genderRisk_recommendations(Gender,mixgender, sexulysct, sexulysct2, pregnantrisk, risknameN, risknameA,risknameO )
        if ret_data is not None:
            #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response

    elif (length==4) and ("age" in res and "gender" in res and "tobacco user" in res and "sexuallyActive" in res):
        Age=res['age']
        Gender=res['gender'].lower()
        risknameT=res['tobacco user']
        risknameS=res['sexuallyActive']
        pregnantrisk="Pregnant"
        ret_data =get_AGST_recommendations(Age, Gender,mixgender, risknameT, risknameS, pregnantrisk, risknameN,risknameA,risknameO)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif (length==4) and ("age" in res and "gender" in res and "tobacco user" in res and "pregnant" in res):
        Age=res['age']
        Gender=res['gender'].lower()
        pregnantrisk=res['pregnant']
        risknameT=res['tobacco user']
        ret_data =get_SPT_recommendations(Age, Gender,mixgender, risknameT, SA, pregnantrisk, risknameN,risknameA,risknameO)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    elif ((length==4) and ("age" in res and "gender" in res and "sexuallyActive" in res and "pregnant" in res)):
        Age=res['age']
        Gender=res['gender'].lower()
        pregnantrisk=res['pregnant']
        riskname=res['sexuallyActive']
        ret_data =get_SPT_recommendations(Age, Gender,mixgender, TU, riskname, pregnantrisk, risknameN,risknameA,risknameO)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response'''

    elif (length==5) and ("age" in res and "gender" in res and "tobacco user" in res and "sexuallyActive" in res and "pregnant" in res):
        Age=res['age']
        if len(Age) ==0:
            Age=0
        pregnantrisk=res['pregnant']
        if len(pregnantrisk)==0:
            pregnantrisk="Pregnant"

        risknameT=res['tobacco user']
        if len(risknameT)==0:
            risknameT="Tobacco user"
        risknameS=res['sexuallyActive']
        if len(risknameS)==0:
            risknameS="Sexually Active"
        Gender=res['gender'].lower()
        if len(Gender)==0:
            GenderM="male"
            GenderF="female"
            ret_data =get_Recommendations(Age, Gender,mixgender, risknameT, risknameS,risknameA,risknameO,pregnantrisk)
            if ret_data is not None:
            #if Age in(product_dict[])
                response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
                return response
            else:
                ret_data = 'Products Not Found !'
                response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
                return response
        ret_data =get_AGSTP_recommendations(Age, Gender,mixgender, risknameT, risknameS,risknameA,risknameO,pregnantrisk)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response
    '''elif (length==3) and ("age" in res and "gender" in res and "pregnant" in res):
        Age=res['age']
        Gender=res['gender'].lower()
        pregnantrisk=res['pregnant']
        #riskname=res['tobacco user'].lower()
        ret_data =get_AGP_recommendations(Age, Gender,mixgender,SA, TU, risknameN,risknameA,risknameO,pregnantrisk)
        if ret_data is not None:
        #if Age in(product_dict[])
            response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
            return response
        else:
            ret_data = 'Products Not Found !'
            response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
            return response






    #Gender = res['gender'].lower()
    #TobaccoUser = res['tobacco user'].lower()
    #SexuallyActive = res['sexually active'].lower()
    #Pregnant=res['Pregnant'].lower()
    #print (res, Age, TobaccoUser, SexuallyActive,Pregnant)

    #data_list = []
    #ret_data =get_age_recommendations(Age)
    #print(len(ret_data))'''
    '''l=[]
    for val in ret_data:
        product_dict={
        "id":val[0],
        "Title":val[1],
        "grade":val[2],
        "gender":val[3],
        "agerange0":val[4],
        "agerange01":val[5],
        "recommendations":val[6]
            }
        l.append(product_dict)'''

    '''if ret_data is not None:
        #if Age in(product_dict[])
        response = Response(json.dumps(ret_data), status=200, mimetype='application/json')
        return response
    else:
        ret_data = 'Products Not Found !'
        response = Response(json.dumps(ret_data), status=404, mimetype='application/json')
        return response'''


@app.route('/docs')
def return_api_docs():
    """
    api docs route
    :return:
    """
    return auto.html()
