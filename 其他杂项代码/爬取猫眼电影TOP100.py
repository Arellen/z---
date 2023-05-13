import requests
from requests.exceptions import RequestException
import re
from requests.utils import requote_uri

def get_one_page(url):
    response = requests.get(url)
    # response.encoding = 'utf-8'
    response.encoding = response.apparent_encoding
    try:
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(/d+)</i>.*?title="(/s?)".*?"board-img".*?scr="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>.*?<i class="integer">(.*?)</i>.*?<i class="fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'name': item[2].strip(),
            'score': item[3].strip(),
            'time': item[4].strip(),
        }
def main():
    url = "https://www.maoyan.com/board/4?timeStamp=1681621039494&channelId=40011&index=3&signKey=ab9019b50673215a61637a6545347610&sVersion=1&webdriver=false&offset=0"
    html = get_one_page(url)
    print(html)
    # for item in parse_one_page(html):
    #     print(item)


if __name__ == '__main__':
    main()