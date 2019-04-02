from app.common.db.postgres import PgPool
from app.models.config.queries import QUERIES
from mock.categories import *
import random


pg_ = PgPool()

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
def get_AgeGenderRecommendations(Gender, mixgender, risknameT, risknameS,risknameA,risknameO, pregnantrisk):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetAGRecommendations"]
    params = (Gender,mixgender,risknameA,risknameO,risknameS,risknameT,pregnantrisk,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def functoin_retrieve_data_againsst_general_id(general_id):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetGeneralData"]
    params = (general_id,)

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None
def functoin_retrieve_data_againsst_tools_id(tool0, tool1, tool2):
    """
    Returns a product information to product route
    :param asin_no: product asin
    :param category_id: id of category
    :return:
    """
    pg_conn, pg_cursor = pg_.get_conn()
    query = QUERIES["GetToolsData"]
    params = (tool0, tool1, tool2 )

    try:
        recommendation = pg_.execute_query(pg_cursor, query, params)
        pg_.commit_changes(pg_conn)
        pg_.put_conn(pg_conn)
        return recommendation
    except Exception as e:
        pg_.put_conn(pg_conn)
        return None