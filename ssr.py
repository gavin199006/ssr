#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-4-25 下午1:02
# @Author  : Gavin
# @Site    : 
# @File    : ssr.py
# @Software: PyCharm

import requests
import base64
import re
def add_stri(stri,value):
        stri_len = len(stri)
        value = int(value)
        cover = value - stri_len % value
        if cover == value:
                stri = stri
        else:
                stri = stri + '=' * cover

        en_stri = stri.encode()
        return en_stri

def ssr(stri):
        dictFile ={
                "server":"51.15.255.228",
                "sever_ipv6":"::",
                "server_port":18421,
                "local_address":"192.168.1.27",
                "local_port":1088,
                "password":"https://linkfq.com/26",
                "timeout":120,
                "method":"aes-256-cfb",
                "protocol":"origin",
                "obfs":"plain",
                "obs_param":"",
                "redirect":"",
                "dns_ipv6":"false",
                "fast_open":"true",
                "workers":1
        }


        stri = stri.replace('ssr://','').replace('–','+').replace('_','/').rstrip()

        #####第一次解析
        '''
        第一次解析会得到 ip、端口、协议、加密方法、混淆方式。
                        server：ip
                        server_port:端口
                        protocol:协议
                        method:加密方法
                        obfs:混淆方式
        '''
        en_stri = add_stri(stri,3)
        stri = base64.b64decode(en_stri).decode()
        ssr_list = stri.split(':')


        server = ssr_list[0]
        server_port = ssr_list[1]
        protocol = ssr_list[2]
        method = ssr_list[3]
        obfs = ssr_list[4]

        password_stri = ssr_list[-1].split('/')[0]

        ######第二次解析
        '''
        得到密码
        '''
        password_stri = password_stri.replace('ssr://','').replace('–','+').replace('_','/')
        en_password = add_stri(password_stri,3)

        password = base64.b64decode(en_password).decode()



        dictFile["server"] = server
        dictFile["server_port"] = server_port
        dictFile["password"] = password
        dictFile["method"] = method
        dictFile["protocol"] = protocol
        dictFile["obfs"] = obfs


        # dictFileOder = OrderedDict()

        dictList = ["server","sever_ipv6","server_port","local_address","local_port","password","timeout","method","protocol","obfs","obs_param","redirect","dns_ipv6","fast_open","workers"]
        result= '{'+'\n'
        for key in dictList:
            if dictFile.get(key) is not None:#python2用的是row.has_key(key)
                    if str(dictFile.get(key)).isdigit():
                        result = result + '        "{0}":{1}\n'.format(key,dictFile.get(key))

                    else:
                        result = result + '        "{0}":"{1}"\n'.format(key, dictFile.get(key))
            else:
                    result = result + '}'

        return result

###############


##创建session对象

def ssr_get():
start_url = 'https://linkfq.com/26'
requests_con = requests.get(start_url)
content = requests_con.text
content = content.replace('\n','')
regex = re.compile(r'<pre class="prettyprint linenums">(.*?)</pre>')
ssr_list = regex.findall(content)

return ssr_list

for stri in ssr_list:
    print(stri)
    result = ssr(stri)
    print(result)


