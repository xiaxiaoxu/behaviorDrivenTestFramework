﻿#encoding=utf-8
# language: zh-CN

特性: 在百度网址搜索IT相关书籍
    能够搜索到书的作者，比如吴晓华

    场景: 在百度网站搜索IT相关书籍
        如果将搜索词设定为书的名字"<书名>"
        当打开百度网站
        和在搜索输入框中输入搜索的关键词，并点击搜索按钮后
        那么在搜索结果中可以看到书的作者"<作者>"

    例如:
        | 书名                         | 作者   |
        | Selenium WebDriver实战宝典   | 吴晓华 |
        | HTTP权威指南                 | 协议 |
        | Python核心编程               | Python |
