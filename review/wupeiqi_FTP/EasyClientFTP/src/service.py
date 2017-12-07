#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import os
import re
import json
from config import settings
from lib import commons


def login(conn):
    while True:
        username = input('请输入用户名(q退出)：')
        pwd = input('请输入密码：')
        login_info = {'username': 'wupeiqi', 'pwd': '123'}
        conn.sendall(bytes(json.dumps(login_info), 'utf-8'))
        if str(conn.recv(1024), encoding='utf-8') == "4002":
            print('授权成功...')
            break
        else:
            print('用户名或密码错误...')


def cmd(conn, inp):
    conn.sendall(bytes(inp, 'utf-8'))
    basic_info_bytes = conn.recv(1024)
    basic_info_str = str(basic_info_bytes, 'utf-8')
    if basic_info_str == '4001':
        login(conn)
    else:
        conn.sendall(bytes("ack", 'utf-8'))   #防止粘包
        print(str(basic_info_bytes, 'utf-8'))
        result_length = int(str(basic_info_bytes, 'utf-8').split('|')[1])
        has_received = 0
        content_bytes = bytes()
        while has_received < result_length:
            fetch_bytes = conn.recv(1024)
            has_received += len(fetch_bytes)
            content_bytes += fetch_bytes
        cmd_result = str(content_bytes, 'utf-8')
        print(cmd_result)


def post(conn, inp):
    # inp  ===> post|D:/1.txt     2.txt
    method, file_paths = inp.split("|", 1)
    local_path, target_path = re.split('\s', file_paths, 1)
    # 获取本地文件大小
    file_byte_size = os.stat(local_path).st_size
    print(file_byte_size)
    # 获取本地文件名
    file_name = os.path.basename(local_path)
    # 获取本地文件md5值
    file_md5 = commons.fetch_file_md5(local_path)

    post_info = "post|%s|%s|%s|%s" % (file_byte_size, file_name, file_md5, target_path)

    conn.sendall(bytes(post_info, 'utf-8'))

    result_exist = str(conn.recv(1024), 'utf-8')

    if result_exist == '4001':
        login(conn)
        return

    has_sent = 0
    if result_exist == "2003":
        inp_continue = input('文件已经存在，是否续传？Y/N')
        if inp_continue.upper() == "Y":
            conn.sendall(bytes('2004', 'utf-8'))
            result_continue_pos = str(conn.recv(1024), 'utf-8')
            has_sent = int(result_continue_pos)
        else:
            conn.sendall(bytes('2005', 'utf-8'))

    file_obj = open(local_path, 'rb')
    file_obj.seek(has_sent)
    while file_byte_size > has_sent:
        data = file_obj.read(1024)
        conn.sendall(data)
        has_sent += len(data)
        commons.bar(has_sent, file_byte_size)
    file_obj.close()
    print('上传成功')


def get(conn, inp):
    '''
    download
    get|33.avi /Users/sujunjun/Desktop/333.avi
    :param conn:
    :param inp:
    :return:

    '''
    #获取服务端这个文件路径
    method, file_paths = inp.split( "|", 1 )
    source_file,target_path = re.split('\s',file_paths,1)
    get_info = "get|%s" % (source_file)
    conn.sendall(get_info.encode('utf8'))
    file_exists_info = conn.recv(1024).decode('utf8')#(1)

    if file_exists_info == '4004':
        print('服务器没有该文件')
    else:
        func, file_byte_size, file_name, file_md5 = file_exists_info.split( '|', 3 )
        has_received = 0
        file_byte_size = int( file_byte_size )
        if os.path.exists(target_path):
            local_file_size = os.stat(target_path).st_size
            print(local_file_size,file_byte_size)
            if file_byte_size == local_file_size:
                print('文件存在')
                return
            else:
                inp_continue = input( '文件已经存在，是否继续下载？Y/N' )
                if inp_continue.upper() == 'Y':
                    #查出此文件大小
                    conn.sendall(str(local_file_size).encode('utf8'))
                    has_received+= local_file_size
                    f = open( target_path, 'ab' )
                else:
                    conn.sendall( bytes( '-1', 'utf8' ) )
                    f = open( target_path, 'wb' )
        else:
            conn.sendall( bytes( '-1', 'utf8' ) )
            f = open( target_path, 'wb' )
        #循环收
        while file_byte_size > has_received:
            data = conn.recv(1024)
            f.write(data)
            has_received += len(data)
            commons.bar( has_received, file_byte_size )
        f.close()
        print( '下载成功' )
        return



def help_info():
    print("""
            cmd|命令
            post|文件路径
            get|下载文件路径
            exit|退出
        """)


def execute(conn):
    choice_dict = {
        'cmd': cmd,
        'get': get,
        'post': post,
    }
    help_info()
    while True:
        # cmd|ls
        # post|本地路径 服务器上路径
        # get|服务器路径 本地路径
        inp = input("please input:")
        if inp == 'help':
            help_info()
            continue
        choice = inp.split('|')[0]
        if choice == 'exit':
            return
        if choice in choice_dict:
            func = choice_dict[choice]
            func(conn, inp)


def main():
    ip_port = (settings.server, settings.port)
    conn = socket.socket()
    conn.connect(ip_port)
    welcome_bytes = conn.recv(1024)
    print(str(welcome_bytes, encoding='utf-8'))

    execute(conn)

    conn.close()



