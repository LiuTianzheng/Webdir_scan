import threading
import requests

'''
Author：Tianzheng
Date: 2020/01/14
Version: v1.0
'''


def geturl():
    url_str = input("请输入url(开头加上http/https)：")
    end_str = url_str[-1]

    if end_str == '/':
        url_str = url_str[:-1]

    return url_str


def full_url(url_fount):
    with open("dir.txt", encoding="utf-8") as file_obj:
        lines = file_obj.readlines()

    dir_list = []

    for line in lines:
        dir_list.append(line.rstrip())

    host_list = []
    for a in dir_list:
        host_list.append(url_fount + a)
    return host_list


def req(host):
    print('request %s...' % host)
    r = requests.get(host)
    code = r.status_code
    if code == 403 or code == 200:
        print(str(code) + ':' + host)


def main():
    url = geturl()
    a = full_url(url)

    for i in a:
        t = threading.Thread(target=req, args=(i,))
        t.start()


if __name__ == '__main__':
    main()