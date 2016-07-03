#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : whieet
# @File    : url_to_hyperlink.py


import re
s = "strathttp://github.com end"
def add_hyperlink(text):
    t = text
    link = ''
    while True:
        link_tmp = re.search(r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?",t)
        try:
            pos = link_tmp.span()
        except Exception,e:
            print e
            link += t
            break
        else:
            link += t[0:pos[0]] + '<a href="%s">网页链接(hyperlink)</a>'%t[pos[0]:pos[1]]
            t = t[pos[1]:len(t)]
    return link

print add_hyperlink(s)

