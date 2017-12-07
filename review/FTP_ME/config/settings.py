#-*- coding:utf-8 _*-
""" 
@author:sujunjun 
@file: settings.py 
@time: 2017/12/02 
"""
import logging,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_LEVEL = logging.INFO
LOG_TYPES = {
	'access':'access.log'
}

DATEBASE = {
	'engine':'file_storage',
	'name':'user_data',
	'path':os.path.join(BASE_DIR,'db')

}

FTP_INFO = {
	'ip_address':'127.0.0.1',
	'port':8098
}