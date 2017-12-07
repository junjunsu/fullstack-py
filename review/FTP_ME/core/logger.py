#-*- coding:utf-8 _*-  
""" 
@author:sujunjun 
@file: logger.py 
@time: 2017/12/02 
"""
import logging
from config import settings

def logger(logger_type):
	#create logger
	logger = logging.getLogger(logger_type)
	logger.setLevel(settings.LOG_LEVEL)
	print(logger)


