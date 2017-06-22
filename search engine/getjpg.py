#coding: utf-8

"""
urllib模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据。
首先我们定义getHtml()函数；
然后我们筛选页面中想要的数据，函数getImg()；
最后我们将页面筛选的数据保存到本地。
"""

import re
import urllib



def getHtml( url ):
    """
    url: URL地址
    """
    #urllib.urlopen()方法用于打开一个URL地址
    page = urllib.urlopen( url )
    #read()方法用于读取URL上的数据
    html = page.read()
    return html


def getImg( html ):
    #正则表达式用来筛选html网页代码
    reg = r'src="(.+?\.jpg)" pic_ext'
    image = re.compile( reg )  #编译正则表达式，提高筛选速度
    imglist = re.findall( image, html )

    return imglist
    

if __name__ == '__main__':
    html = getHtml( "http://tieba.baidu.com/p/2460150866" )
    print( getImg( html ) )
