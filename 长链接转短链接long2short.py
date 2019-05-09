import requests
def long2short(long_url):
    SC = requests.get(long_url).status_code
    if SC == 200:
        querystring = {"url":long_url}
        url = "http://suo.im/api.php"
        response = requests.request("GET", url, params=querystring).text
    else:
        response = 'cannot reach this url'
    return response
if __name__ == '__main__':
    long_url1 = "https://blog.csdn.net/qq_42874994/article/details/892985"# 这是一个404无法访问的网站
    long_url2 = 'https://pypi.org/project/pyspark/'
    res1 = long2short(long_url1)
    res2 = long2short(long_url2)
    print(res1)
    print(res2)
