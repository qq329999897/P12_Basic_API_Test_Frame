#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: common_api.py
# @time: 2020/7/8 8:48 下午

import requests
from common.localconfig_utils import local_config

def get_access_token_api(session,grant_type,appid,secret):
    params={
        "grant_type":grant_type,
        "appid":appid,
        "secret":secret
    }
    response = session.get(url=local_config.URL+"/cgi-bin/token",
                            params = params
                            )
    return response

def get_access_token_value(session):
    get_access_token_response = get_access_token_api(session,
                                                     'client_credential',
                                                     local_config.APPID,
                                                     local_config.SERCET
                                                     )
    token_id = get_access_token_response.json()['access_token']
    return token_id



def create_user_tag_api(session,access_token,tag_json):  # 方式一：建议
    params = {
        "access_token": access_token
    }
    json_data = tag_json
    response = session.post(url=local_config.URL+"/cgi-bin/tags/create",
                            params = params,
                            json=json_data)
    return response

def create_user_tag_api(session,access_token,tag):  # 方式二：不建议
    params = {
        "access_token": access_token
    }
    json_data = { "tag" : { "name" : tag } }
    response = session.post(url=local_config.URL+"/cgi-bin/tags/create",
                            params = params,
                            json=json_data)
    return response

def delete_user_tag_api(session,access_token,tagid_json):
    params = {
        "access_token": access_token
    }
    json_data = tagid_json
    response = session.post(url=local_config.URL+"/cgi-bin/tags/delete",
                            params = params,
                            json=json_data)
    return response
