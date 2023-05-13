import requests
import re
#获得网页
def getHTMLtext(url):
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        return('')
#分析处理网页，获得需要爬取的商品名称和价格
def parsepage(ilt, html):
    try:
        #查找商品价格的正则表达式
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        #查找对应商品名称的正则表达式
        tlt=re.findall(r'\"raw_title\"\:\".*?\"', html)
        #存储商品名称和价格信息
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')
#打印出爬取得到的商品名称和价格
def printGoodsList(ilt):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format('序号','价格','名称'))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count, g[0], g[1]))

def main():
    goods= goods_name #搜寻的关键词
    depth=2#爬取的网页数（翻页数）
    start_url='https://s.taobao.com/search?q='+goods#初始网页
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)#实现翻页操作
            html=getHTMLtext(url)
            parsepage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
goods_name = input("> ")
main()
