import json

import requests

session = requests.session()


#加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}

def save_cookies():
    url = ' https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php'
    data = {
        'log': 'spiderman',  # 写入账户
        'pwd': 'crawler334566',  # 写入密码
        'wp-submit': '登录',
        'redirect_to': 'https://wordpress-edu-3autumn.localprod.forc.work',
        'testcookie': '1'
    }
    session.post(url,headers=headers,data=data)
    # 将 cookies 转化为字典
    cookies_dict = requests.utils.dict_from_cookiejar(session.cookies)
    print(cookies_dict)
    # 调用 json 模块的 dumps 函数把 cookies 从字典转化为字符串
    cookies_str = json.dumps(cookies_dict)
    print(cookies_str)
    f = open("cookies.txt", "w")
    f.write(cookies_str)
    f.close()

def read_cookies():
    cookies_txt = open("cookies.txt", "r")
    cookies_str = cookies_txt.read()
    # 将字符串转化为字典
    cookies_dict = json.loads(cookies_str)
    # 把字典格式的 cookies 转换为本来的格式
    cookies = requests.utils.cookiejar_from_dict(cookies_dict)
    return cookies

try:
    cookies = read_cookies()
    session.cookies = cookies
except FileNotFoundError:
    save_cookies()


url_4 = "https://wordpress-edu-3autumn.localprod.forc.work/wp-comments-post.php"
data_4 = {
    'comment': input('请输入你想要发表的评论：'),
    'submit': '发表评论',
    'comment_post_ID':'23',
    'comment_parent': '0'
}
comment = session.post(url_4,headers=headers,data=data_4)
print(comment.status_code)