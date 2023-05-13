import requests
from lxml import etree

url = 'https://so.szlcsc.com/global.html?k=%25E7%2594%25B5%25E9%2598%25BB&hot-key=ADXL355BEZ-RL7'
headers = {
    # 防盗链
    'referer': 'https://so.szlcsc.com/',
    # 浏览器信息
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 '
}
resp = requests.get(url, headers=headers)
print(resp.text)
tree = etree.HTML(resp.text)
names = tree.xpath(
    '//*[@id="shop-list"]/table/tbody/tr[1]/td/div[2]/div[2]/div[3]/div[1]/div[1]/ul/li[2]/div/p/@originalprice')
print(names)
for item in names:
    print(item)

# # 解析出所有的数量对应的价格组合
# soup.find_all('tr', class_='sample_list_tr')

# # 解析出一行中的采购数量
# number_tag = tag.find('td', align='right')
# if number_tag is None:
#     return 'None'
# else:
#     price = re.search('[1-9]{1}[\\d ~\\s]*\\d',
#                       next(number_tag.stripped_strings),
#                       re.S).group()
#     strinfo = re.compile('[\\s]')
#     return re.sub(strinfo, '', price)

# # 解析出一行中的价格信息
# price_tag = tag.find('p', class_='goldenrod')
# if price_tag is None:
#     return 'None'
# else:
#     price = [price for price in price_tag.stripped_strings]
#     return re.search('[1-9]{1}[\\d\\.]*', price[0], re.S).group()
