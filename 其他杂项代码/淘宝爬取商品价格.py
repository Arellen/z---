import requests
import re

def getHtmlText(url):
    try:
        header = {'authority': 'gm.mmstat.com',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'cna=1a++HNJgOWsCAXUdugLK7ANH; sca=90e2458d; cnaui=681187386; aui=681187386; tbsa=8768cddf32c93cc90084a376_1681382679_1; atpsida=3676ffb5d3e516c03859dbaf_1681382679_1',
    'referer': 'https://s.taobao.com/',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    }
        r = requests.get(url, headers=header)
        r.raise_for_status()
        r.encoding = r.apparent_encoding

        return r.text
    except:
        print("爬取失败")
        return ""


def parsePage(ilist, html):
    try:
        plt = re.findall(r'\"view_price\":\"\d+\.\d*\"', html)
        tlt = re.findall(r'\"raw_title\":\".*?\"', html)
        # print(tlt)
        print(len(plt))
        for i in range(len(plt)):
            price = eval(plt[i].split('\"')[3])
            title = tlt[i].split('\"')[3]
            ilist.append([title, price])
        # print(ilist)
    except:
        print("解析出错")


def printGoodsList(ilist, num):
    print("=====================================================================================================")
    tplt = "{0:<3}\t{1:<30}\t{2:>6}"
    print(tplt.format("序号", "商品名称", "价格"))
    count = 0
    for g in ilist:
        count += 1
        if count <= num:
            print(tplt.format(count, g[0], g[1]))
    print("=====================================================================================================")


def main():
    goods = "篮球"
    depth = 1
    start_url = "https://s.taobao.com/search?page=1&q=" + goods
    infoList = []
    num = 20
    for i in range(depth):
        try:
            url = start_url + '$S=' + str(44 * i)
            html = getHtmlText(url)
            parsePage(infoList, html)
        except:
            continue

    printGoodsList(infoList, num)


main()