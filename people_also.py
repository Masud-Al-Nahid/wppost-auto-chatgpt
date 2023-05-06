
def get_people_also_ask(query):
    import requests
    from bs4 import BeautifulSoup
    url = f"https://www.google.com/search?q={query}"

    # Add headers with cookies and user-agent
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'cookie': 'VISITOR_INFO1_LIVE=JfnFCXIj0D8; __Secure-3PAPISID=1-xJYNwD5W9AxxJi/A-5KUcRkECj8xyVir; __Secure-3PSID=VwhPGe60mjTVJgydnMAAAEIMAkVA-4A1Bim2IZfoIHQTH92iagVyKH4dmodww_snAwq1WQ.; LOGIN_INFO=AFmmF2swRQIhAMHAJn2rJl43YHszpXhDRzuyOI71_aqXCGuJBvLqafTtAiAL7M-nbNQVUZKdPNyKnBvagxtXhSusWWGOY33rYMVNuQ:QUQ3MjNmd1dncUN6eFdtbmF2Z3JsdDJmd3NIX1pCcGNxNXRNZ2ZuUkhkUzFWMERZaEk3LXNaRlZJVUtwV3JJVENrYmdJRWExWTM4anh6WGM4RHhfbndfQ0JuRGs5dWFMd0VNR0d6YVV2Y043b092ZVV0cFB4RXJFazU0cGhNN3hEN2xQNVNZMndveS1WVUpmN0R0bGlMdld4V3F6QjJDMmhVQ1BIRGdJaWtqN21FallJM1N4Mkk3V0tPRlRIaWQ5ZlJ0dTZJbTNoSlBuS2ZheE9Na0twc1hBQk0zVnZGSndFQQ==; YSC=955vMyTTL08; __Secure-3PSIDCC=AP8dLtz6rXKZpiBZtwppTiDsLjMxuA-UUZLHflmP5Iib-TLPa1RoKsS_RvsiO6oHNc3ybTZeiTo',
        
    }
    proxies = {
        'http': 'http://94.103.97.61:8080',
        'http': 'http://65.108.230.239:34253',
        'http': 'http://51.159.0.236:3128',
        'http': 'http://65.108.230.239:40657',
        'http': 'http://174.138.167.181:8888',
        'http': 'http://64.225.8.82:9965',
        'http': 'http://200.106.187.246:999',
        'http': 'http://43.156.100.152:80',
        'http': 'http://40.119.236.22:80',
        'http': 'http://92.51.31.193:8080',
        'http': 'http://103.118.175.71:3127',
        'http': 'http://122.154.66.132:8080',
        'http': 'http://65.108.230.239:34727',
        'http': 'http://5.161.110.95:50272',
        'http': 'http://160.19.232.85:3128',
        'http': 'http://190.90.233.17:8080',
        'http': 'http://179.63.149.2:999',
        'http': 'http://158.69.53.98:9300',
        'http': 'http://102.68.128.219:8080',
        'http': 'http://89.237.33.193:37647',
        'http': 'http://181.115.67.9:999',
        'http': 'http://45.123.1.101:8080',
        'http': 'http://201.76.218.220:9898',
        'http': 'http://180.178.103.70:8080',
        'http': 'http://102.68.128.212:8080',
        'http': 'http://45.70.236.194:999',
        'http': 'http://45.94.73.133:8080',
        'http': 'http://201.71.2.103:999',
        'http': 'http://169.239.85.113:8080',
        'http': 'http://200.105.104.185:999',
        'http': 'http://201.77.108.149:999',
        'http': 'http://180.191.40.112:8081',
        'http': 'http://45.190.170.254:999',
        'http': 'http://202.180.54.97:8080',
        'http': 'http://200.24.130.138:999',
        'http': 'http://181.204.45.179:999',
        'http': 'http://131.100.51.161:999',
        'http': 'http://181.189.135.90:8080',
        'http': 'http://201.71.2.6:999',
        'http': 'http://103.190.112.244:8080',
        'http': 'http://103.36.35.135:8080',
        'http': 'http://64.225.8.82:9949',
        'http': 'http://103.74.229.133:8080',
        'http': 'http://191.102.49.145:8080',
        'http': 'http://158.69.27.94:9300',
        'http': 'http://110.78.112.198:8080',
        'http': 'http://103.154.230.102:5678',
        'http': 'http://180.119.137.33:7890',
        'http': 'http://191.102.51.254:8080',
        'http': 'http://201.71.2.93:999',
        'http': 'http://181.13.254.52:999',
        'http': 'http://64.225.4.29:9495',
        'http': 'http://103.178.43.5:8181',
        'http': 'http://174.138.167.179:8888',
        'http': 'http://201.77.110.1:999',
        'http': 'http://200.215.250.100:999',
        'http': 'http://159.69.245.208:56466',
        'http': 'http://72.69.147.230:8081',
        'http': 'http://103.123.234.25:8080',
        'http': 'http://178.218.88.12:8123',
        'http': 'http://103.75.52.65:9090',
        'http': 'http://103.78.105.85:8989',
        'http': 'http://103.1.50.243:3125',
        'http': 'http://103.146.189.86:8080',
        'http': 'http://45.174.79.101:999',
        'http': 'http://103.48.68.35:83',
        'http': 'http://103.207.97.77:8080',
        'http': 'http://102.69.32.1:8080',
        'http': 'http://174.138.167.182:8888',
        'http': 'http://200.125.168.222:999',
        'http': 'http://45.174.77.243:999',
        'http': 'http://45.189.112.65:999',
        'http': 'http://45.189.113.63:999',
        'http': 'http://103.159.194.228:8080',
        'http': 'http://103.178.43.100:8181',
        'http': 'http://202.150.132.53:8080',
        'http': 'http://188.132.221.3:8080',
        'http': 'http://46.249.123.146:514',
        'http': 'http://45.160.78.37:999',
        'http': 'http://190.208.40.190:9480',
        'http': 'http://38.51.48.189:999',
        'http': 'http://103.153.136.188:8080',
        'http': 'http://64.225.8.82:9989',
        'http': 'http://91.231.61.1:8091',
        'http': 'http://45.70.200.49:999',
        'http': 'http://62.3.30.135:8080',
        'http': 'http://181.143.85.91:80',
        'http': 'http://186.96.2.89:999',
        'http': 'http://103.16.119.4:8181',
        'http': 'http://64.225.8.82:9947',
        'http': 'http://45.235.123.45:999',
        'http': 'http://45.234.61.173:999',
        'http': 'http://66.231.77.203:6969',
        'http': 'http://202.72.220.83:8080',
        'http': 'http://94.154.152.94:8079',
        'http': 'http://201.71.2.115:999',
        'http': 'http://45.174.248.24:999',
        'http': 'http://103.105.76.65:8080',
        'http': 'http://213.6.99.106:8080',
        'http': 'http://201.219.247.34:999',
        'http': 'http://190.131.250.105:999',
        'http': 'http://167.99.116.111:8001',
        'http': 'http://103.167.68.51:8080',
        'http': 'http://182.48.78.28:8081',
        'http': 'http://190.131.210.19:999',
        'http': 'http://190.93.189.28:999',
        'http': 'http://45.234.61.181:999',
        'http': 'http://143.0.67.19:8080',
        'http': 'http://149.57.11.17:8181',
        'http': 'http://196.216.132.196:8082',
        'http': 'http://190.124.166.228:999',
        'http': 'http://94.74.163.220:80',
        'http': 'http://201.220.150.1:999',
        'http': 'http://103.146.196.13:8080',
        'http': 'http://64.225.8.82:9986',
        'http': 'http://103.220.206.110:59570',
        'http': 'http://103.48.68.36:84',
        'http': 'http://177.85.2.244:9595',
        'http': 'http://144.48.110.208:8085',
        'http': 'http://103.105.55.149:8080',
        'http': 'http://64.225.4.29:9480',
        'http': 'http://200.123.15.251:999',
        'http': 'http://174.138.167.180:8888',
        'http': 'http://116.197.130.71:80',
        'http': 'http://123.231.221.180:8080',
        'http': 'http://46.161.195.104:1976',
        'http': 'http://65.108.230.239:41625',
        'http': 'http://200.123.15.252:999',
        'http': 'http://103.48.68.108:83',
        'http': 'http://181.49.217.254:8080',
        'http': 'http://34.146.64.228:3128',
        'http': 'http://64.225.4.12:9992',
        'http': 'http://46.175.1.65:8080',
        'http': 'http://65.108.230.239:38543',
        'http': 'http://196.6.235.26:8080',
        'http': 'http://102.38.17.153:8080',
        'http': 'http://203.89.29.53:6060',
        'http': 'http://36.93.33.171:4480',
        'http': 'http://187.84.242.51:8080',
        'http': 'http://168.0.239.225:8787',
        'http': 'http://103.75.199.142:8080',
        'http': 'http://45.233.169.12:999',
        'http': 'http://158.69.71.245:9300',
        'http': 'http://102.223.88.29:8080',
        'http': 'http://63.250.52.82:8118',
        'http': 'http://45.175.237.161:999',
        'http': 'http://187.63.156.92:999',
        'http': 'http://202.158.69.126:80',
        'http': 'http://138.118.105.131:999',
        'http': 'http://187.102.217.21:999',
        'http': 'http://45.233.170.109:999',
        'http': 'http://171.243.26.155:10006',
        'http': 'http://190.2.212.20:999',
        'http': 'http://103.154.231.237:8080',
        'http': 'http://27.70.161.172:10039',
        'http': 'http://186.125.235.253:999',
        'http': 'http://162.0.220.216:22402',
        'http': 'http://47.96.5.207:7890',
        'http': 'http://1.4.214.178:8080',
        'http': 'http://206.161.97.2:31337',
        'http': 'http://102.38.5.233:8080',
        'http': 'http://85.114.120.177:9999',
        'http': 'http://165.16.96.92:8080',
        'http': 'http://89.218.5.108:37717',
        'http': 'http://103.48.68.109:83',
        'http': 'http://196.251.221.30:8104',
        'http': 'http://191.102.49.129:8080',
        'http': 'http://185.108.141.74:8080',
        'http': 'http://160.226.132.33:8080',
        'http': 'http://138.117.230.241:999',
        'http': 'http://197.246.10.151:8080',
        'http': 'http://46.161.195.105:1981',
        'http': 'http://180.149.234.248:8080',
        'http': 'http://200.24.204.247:999',
        'http': 'http://179.42.78.64:999',
        'http': 'http://187.49.191.17:999',
        'http': 'http://38.10.69.110:9090',
        'http': 'http://190.119.102.251:999',
        'http': 'http://38.9.56.97:8080',
        'http': 'http://185.82.99.42:9093',
        'http': 'http://179.189.48.255:8080',
        'http': 'http://177.93.38.25:999',
        'http': 'http://65.108.230.239:42701',
        'http': 'http://177.234.212.188:999',
        'http': 'http://201.71.2.181:999',
        'http': 'http://103.118.175.199:8181',
        'http': 'http://64.225.8.82:9976',
        'http': 'http://184.82.130.44:8080',
        'http': 'http://190.85.141.170:9090',
        'http': 'http://103.196.40.222:3125',
        'http': 'http://185.169.183.182:8080',
        'http': 'http://43.243.140.198:8080',
        'http': 'http://181.212.41.171:999',
        'http': 'http://64.225.8.82:9974',
        'http': 'http://103.162.154.3:8888',
        'http': 'http://185.103.181.2:8080',
        'http': 'http://187.62.64.155:45005',
        'http': 'http://64.225.8.82:9992',
        'http': 'http://103.166.10.71:32650',
        'http': 'http://144.49.99.145:8080',
        'http': 'http://138.68.195.70:31290',
        'http': 'http://185.33.170.210:9999',
        'http': 'http://139.255.10.237:8080',
        'http': 'http://45.70.236.193:999',
        'http': 'http://131.72.69.41:45005',
        'http': 'http://14.160.32.23:8080',
        'http': 'http://41.76.219.23:8088',
        'http': 'http://177.93.45.156:999',
        'http': 'http://190.97.247.210:999',
        'http': 'http://63.239.220.5:8080',
        'http': 'http://168.90.252.17:999',
        'http': 'http://64.225.8.82:9999',
        'http': 'http://192.141.93.91:999',
        'http': 'http://190.103.87.3:8080',
        'http': 'http://177.53.214.208:999',
        'http': 'http://45.224.119.15:999',
        'http': 'http://64.225.4.29:9475',
        'http': 'http://36.91.68.149:8080',
        'http': 'http://200.24.132.196:999',
        'http': 'http://189.90.241.202:8080',
        'http': 'http://45.190.185.101:8080',
        'http': 'http://144.91.81.25:3128',
        'http': 'http://45.174.172.205:999',
        'http': 'http://167.250.180.107:999',
        'http': 'http://103.127.95.125:8888',
        'http': 'http://167.250.51.243:999',
        'http': 'http://117.54.238.62:8080',
        'http': 'http://165.16.27.36:1976',
        'http': 'http://64.225.8.82:9953',
        'http': 'http://161.97.82.179:5566',
        'http': 'http://157.245.27.9:3128',
        'http': 'http://64.225.8.82:9997',
        'http': 'http://64.225.8.82:9980',
        'http': 'http://64.225.8.82:9963',
        'http': 'http://181.129.208.27:999',
        'http': 'http://194.213.18.81:50328',
        'http': 'http://105.19.63.217:9812',
        'http': 'http://64.225.4.29:9816',
        'http': 'http://46.161.195.104:1981',
        'http': 'http://103.167.109.31:80',
        'http': 'http://46.46.180.13:9580',
        'http': 'http://103.94.125.110:8080',
        'http': 'http://103.140.188.134:8080',
        'http': 'http://181.191.226.69:999',
        'http': 'http://103.180.112.120:8080',
        'http': 'http://64.225.8.82:9983',
        'http': 'http://64.225.4.29:9492',
        'http': 'http://112.78.146.244:8080',
        'http': 'http://132.255.210.117:999',
        'http': 'http://64.225.4.29:9479',
        'http': 'http://37.205.14.92:5566',
        'http': 'http://143.202.97.171:999',
        'http': 'http://103.36.11.89:8181',
        'http': 'http://103.248.197.11:3125',
        'http': 'http://103.145.200.15:6969',
        'http': 'http://64.225.4.29:9491',
        'http': 'http://103.1.51.68:3125',
        'http': 'http://157.119.221.22:8080',
        'http': 'http://64.225.4.29:9493',
        'http': 'http://45.171.108.253:999',
        'http': 'http://103.165.251.133:3125',
        'http': 'http://64.225.4.29:9484',
        'http': 'http://45.189.234.43:999',
        'http': 'http://45.167.253.129:999',
        'http': 'http://191.7.216.31:8080',
        'http': 'http://190.82.91.203:999',
        'http': 'http://172.104.41.13:16379',
        'http': 'http://190.124.166.226:999',
        'http': 'http://103.146.185.107:3127',
        'http': 'http://45.229.58.33:999',
        'http': 'http://45.71.186.93:6969',
        'http': 'http://31.7.66.88:8082',
        'http': 'http://203.80.189.33:8080',
        'http': 'http://204.199.197.14:999',
        'http': 'http://200.106.187.247:999',
        'http': 'http://167.99.116.111:8000',
        'http': 'http://188.132.222.44:8080',
        'http': 'http://114.7.27.98:8080',
        'http': 'http://103.66.168.20:80',
        'http': 'http://103.152.232.84:8080',
        'http': 'http://45.70.237.39:8888',
        'http': 'http://45.189.112.1:999',
        'http': 'http://103.161.31.249:83',
        'http': 'http://200.59.184.170:999',
        'http': 'http://157.119.221.23:8080',
        'http': 'http://94.247.208.4:8123',
        'http': 'http://138.118.38.3:999',
        'http': 'http://41.85.16.1:8080',
        'http': 'http://190.110.35.18:999',
        'http': 'http://103.151.177.106:80',
        'http': 'http://27.54.118.2:8989',
        'http': 'http://187.102.216.161:999',
        'http': 'http://179.43.9.129:8085',
        'http': 'http://190.113.41.130:999',
        'http': 'http://190.109.16.145:999',
        'http': 'http://122.166.193.145:3127',
        'http': 'http://103.131.19.31:8085',
        'http': 'http://103.141.109.209:8080',
        'http': 'http://213.82.87.21:443',
        'http': 'http://138.121.161.84:8095',
    }

    # Send the request
    response = requests.get(url, headers=headers, proxies=proxies)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the "People Also Ask" section
    people_also_ask = soup.find('div', {'class': 'Wt5Tfe'})

    # questions = []

    # # Find all the questions and answers
    for item in people_also_ask.find_all('div', {'class': 'wQiwMc related-question-pair'})[:1]:
        
        # questions.append(question)
        question = item.text
    return question

        

