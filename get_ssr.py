#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-5-15 下午3:25
# @Author  : Gavin
# @Site    : 
# @File    : get_ssr.py
# @Software: PyCharm

import requests
import re

url = 'https://linkfq.com/26'

req = requests.get(url)

content = req.text
# print(content)


# content = '''<pre class="prettyprint linenums">ssr://MTQ5LjI4LjE5LjYxOjE4NTA3Om9yaWdpbjphZXMtMjU2LWNmYjpwbGFpbjpabUZ1WjJWeGFXRnVaeTVqYjIwLz9vYmZzcGFyYW09JnJlbWFya3M9TURVd09DM21sNlhtbkt6a3VKemt1cXd0TXpBd1MwSXZVeTNscG9MbHBMSG1sWWpsajZfb3JyX3BsNjRnYUhSMGNITTZMeTltWjNFeUxtTnZiU0RvanJmbGo1Ym1uSURtbHJEbGlxam1nSUVn
# </pre>'''
content = content.replace('\n','')
regex = re.compile(r'<pre class="prettyprint linenums">(.*?)</pre>')
print(regex.findall(content))