from socket import *

def searchServer(ip):
    port = [20,21,22,23,25,53,80,110,123,161,443,1433,3306,1521,8080,8090,137,139,445,3389]
    for i in port:
        try:
            clientSock = socket(AF_INET, SOCK_STREAM)

            clientSock.connect((ip, i))

            data = clientSock.recv(1024)

            print(i)
            print(data)
            clientSock.close()
        except OSError:
            print(i)
            print('해당 포트가 닫혀있습니다.')

searchServer('13.125.109.155')

# 20 FTP 데이터
# 21 FTP 전송
# 22 SSH
# 23 Telnet
# 25 SMTP
# 53 DNS
# 80 HTTP
# 110 POP3
# 123 NTP
# 161 SNMP
# 443 HTTPS
# 1433 MS-SQL
# 3306 MYSQL
# 1521/8080 ORACLE
# 8090 TOMCAT
# 137~139/445 넷바이오스
# 3389 MS 원격 터미널 서비스