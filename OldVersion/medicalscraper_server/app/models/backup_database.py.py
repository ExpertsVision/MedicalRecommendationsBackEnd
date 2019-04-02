from app.common.db.postgres import PgPool
from app.models.config.queries import QUERIES
from mock.categories import *
import random


pg_ = PgPool()


def get_age_recommendations(Age):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAgeRecommendations"]
    params = (Age,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_Recommendations(Age, GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetRecommendations"]
    params = (Age,GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_AgeRecommendations(GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAgeRecommendations"]
    params = (GenderM, GenderF, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_gender_recommendations(Gender,mixgender):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetGenderRecommendations"]
    params = (Gender,mixgender,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_agegender_recommendations(Age,Gender,mixgender):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAgeGenderRecommendations"]
    params = (Age,Gender,mixgender,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_ageandrisk_recommendations(Age, sexulysct, TU, pregnantrisk,risknameN, risknameA,risknameO):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAgeRiskRecommendations"]
    params = (Age, sexulysct, TU, pregnantrisk,risknameN, risknameA,risknameO,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_risks_recommendations(risknameT,risknameO, risknameA, risknameN, SA, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetRiskRecommendations"]

    params = (risknameT,risknameO, risknameA, risknameN, SA, pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_genderRisk_recommendations(Gender,mixgender,sexulysct, pregnantrisk, SA,risknameN, risknameA,risknameO):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetGenderRiskRecommendations"]
    params = (Gender,mixgender, sexulysct, pregnantrisk, SA,risknameN, risknameA,risknameO,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_AGS_recommendations(Age, Gender, mixgender, riskname, risknameN, risknameA, risknameO, TU, riskname2):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGSRecommendations"]
    params = (Age,Gender,mixgender,riskname,risknameN,risknameA,risknameO,TU,riskname2,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_AGT_recommendations(Age, Gender, mixgender, riskname, risknameN, risknameA, risknameO, SA):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGSRecommendations"]
    params = (Age,Gender,mixgender,riskname,risknameN,risknameA,risknameO,SA,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_AGST_recommendations(Age, Gender, mixgender, TU, pregnantrisk, risknameN, risknameA, risknameO, SA):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGSTRecommendations"]
    params = (Age,Gender,mixgender,risknameN,risknameA,risknameO,SA,TU,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_AGSTP_recommendations(Age, Gender, mixgender, TU, risknameA, risknameO, SA, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGSTPRecommendations"]
    params = (Age,Gender,mixgender,risknameA,risknameO,SA,TU,pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def get_SPT_recommendations(Age, Gender,mixgender, TU, SA, pregnantrisk, risknameN,risknameA,risknameO):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGPTRecommendations"]
    params = (Age, Gender,mixgender, TU, SA, pregnantrisk, risknameN,risknameA,risknameO,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

def get_AGP_recommendations(Age, Gender, mixgender,SA, TU, risknameN, risknameA, risknameO, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGPRecommendations"]
    params = (Age,Gender,mixgender,SA, TU,risknameN,risknameA,risknameO, pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None

