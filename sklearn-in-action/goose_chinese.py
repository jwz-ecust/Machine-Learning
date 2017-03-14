# -*- coding: utf-8 -*-
# @Date    : 2017-03-14 22:03:55
# @Author  : "zhangjiawei"
# @Email  : "aaronzjw@icloud.com"
# @Link    : ${https://github.com/jwz-ecust}
# @Version : $Id$

from goose import Goose
from goose.text import StopWordsChinese

url = "https://zhuanlan.zhihu.com/p/25765321"
g = Goose({"stopwords_class": StopWordsChinese})
article = g.extract(url=url)

print article.cleaned_text
