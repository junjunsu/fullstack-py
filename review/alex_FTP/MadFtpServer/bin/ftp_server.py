

import os,sys,re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import main

if __name__ == "__main__":



    main.ArvgHandler()
    #test
    # base_dir = '/Users/sujunjun/PycharmProjects/fullstack_s2/review/alex_FTP/MadFtpServer'
    # abs = '/Users/sujunjun/PycharmProjects/fullstack_s2/review/alex_FTP/MadFtpServer/home/alex';
    # relative_path = re.sub( "^%s" % base_dir, '', abs )
    # print( ("relative path", relative_path, abs) )
    # exit()

    # cmd_list = ['get', 'cc.py', '--md5']
    # if '--md5' in cmd_list:
    #     print( 'ok' )
    # exit()



