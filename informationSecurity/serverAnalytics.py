# client side socket
import requests

from socket import *


def serverAnalytics(ip):
    try:
        clientSock = socket(AF_INET, SOCK_STREAM)
        clientSock.connect((ip, 3306))
        dbinfo = clientSock.recv(1024)
        if 'caching_sha2_password' in dbinfo.decode('latin1')[-30:]:
            print('DB 정보 : MySql 8.0 이상')
        else:
            print('DB 정보 : MySql 8.0 미만')
        clientSock.close()
    except TimeoutError:
        print('DB 정보 없음')
    except ConnectionRefusedError:
        print('DB 정보 없음')

    try:
        clientSock = socket(AF_INET, SOCK_STREAM)
        clientSock.connect((ip, 22))
        sshinfo = clientSock.recv(1024)
        print('SSH 정보 : ', sshinfo)
    except TimeoutError:
        print('SSH 정보 없음')
    except ConnectionRefusedError:
        print('SSH 정보 없음')

    url = 'http://'+ip
    response = requests.get(url)
    print('웹서버 정보 : ', response.headers)

serverAnalytics('13.125.109.155')