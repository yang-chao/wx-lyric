#coding:utf-8
from bs4 import BeautifulSoup
import requests

# url = 'http://music.163.com/#/discover/artist/cat?id=1002'
url = 'http://music.163.com/#/discover/artist/cat?id=1001&initial=65'
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    'Referer': 'http://music.163.com/',
    'Cookie': 'vjuids=bb2f71c7.13c8fd58e63.0.526055ab; ALLYESID4=00130209142213933388358; pgv_pvi=9704409088; SID=99e269cd-97df-44c6-b36e-56ebd2550e83; hasPay=0; mail_psc_fingerprint=1839500596; _ga=GA1.2.126106441.1448683715; _ntes_nnid=fa0bc4b4c44a218dcdc5eb69a7f0ba39,1499650656366; _ntes_nuid=fa0bc4b4c44a218dcdc5eb69a7f0ba39; SERVER_ID=90; TOKEN=bFdKWKC8kDJRlLbt; __utma=187553192.126106441.1448683715.1500357846.1500369700.3; __utmc=187553192; NTES_CMT_USER_INFO=4112738%7Clongsurvivor%7Chttps%3A%2F%2Fsimg.ws.126.net%2Fe%2Fcms-bucket.nosdn.127.net%2F465df94e2fae4f279ba8cab0f4418e0320170801165704.jpg.39x39.100.jpg%7Cfalse%7CeWFuZ2NoYW8yOTRAMTI2LmNvbQ%3D%3D; vjlast=1359622803.1505297203.12; ne_analysis_trace_id=1505297203110; vinfo_n_f_l_n3=e5655f61fe829491.1.30.1412149722731.1449288878286.1505297209174; s_n_f_l_n3=e5655f61fe8294911449310040130; Qs_lvt_73318=1504744805%2C1505265948%2C1509798854; Qs_pv_73318=3600702246289897500%2C2302498089758868500%2C1271704622791393000%2C1066600583527749900; _jzqa=1.3370063108192486000.1526891362.1526891362.1526891362.1; _jzqc=1; _jzqy=1.1526891362.1526891362.1.jzqsr=baidu.-; __f_=1526891362536; PRINTUPLOADID=DC346017EE0FDC6DC93FF02011A0DEA0.app-54-28009; usertrack=ezq0pVsfaMt199upC0bhAg==; Province=010; City=010; CIRCLETRACK=172.17.0.75.1528785402822437; starttime=; NTES_SESS=Qn4Q0hA_xgke1VpsTVEDE7qeB5_57bHvqxd.ti.9XWs_MqYXamwM5Xidb.NUaqcBl9q2Ix9Qqm0LTyziTn8tGgpNcaOEDQMP7lD6GcHMqGKpWsl7IHjrnoGp3KHfiTzUKOjxl70rWnqIGALys.kKBe244vEZPqL47AT_kTxT_GFrBA6QWc.DjUDQllxd3D7WF; S_INFO=1528785739|0|3&40##|y_yangchao#y_yangchao@126.com#yangchao294@126.com; P_INFO=y_yangchao@163.com|1528785739|0|mail163|11&18|bej&1527316935&yxp#bej&null#10#0#0|&0|yxp|y_yangchao@163.com; nts_mail_user=y_yangchao@163.com:-1:1; df=mail163_letter; MUSIC_EMAIL_U=138ea797cef4013587a93d8c90bc84175956e2c62ec1556983a3d28e98c03e3c261fb260c2d1e133a56edab6c0e405500aab8dee2285404b8bafcdfe5ad2b092; _iuqxldmzr_=32; playliststatus=visible; oulink_h=779; __utmc=94650624; __utma=94650624.126106441.1448683715.1529481369.1529487199.3; __utmz=94650624.1529487199.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); JSESSIONID-WYYY=IApiDk3tMhSwtVqSNmy%5C4Y1V770GuN2xY%5CFME8GB2DvC5mMN9eUHMbIKcHjo8aza9UqfKnJGicxY2HrAYzAj6%2Fp9n%5CiWszJWfXcg9sPmVwBNo3Xw6mPnYbvHvvJP%2FI632FH7dweUDkSDat2%2B635bVyWR%5CT2rhekdUHo6nas04uzZH6tc%3A1529492531360; WM_TID=6XbF3ccy%2FqP0vC4WToVJ24Bwqwa%2FmONV; MUSIC_U=8b06274f4b6251d1cff54adc48d0ae04708ec92d197a695671736d3e61e2e1c3cb6cf4fdb8e45e8c49ec8eb1624cb4198bafcdfe5ad2b092; __remember_me=true; __csrf=888d0de9fac161858113bee264e4b36a; __utmb=94650624.26.10.1529487199'
}

def getArtist():
    r = requests.get(url, headers=headers)
    print(r.text)
    print(r.status_code)
    soup = BeautifulSoup(r.text)
    for artist in soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'}):
        print(artist.string)


if __name__ == "__main__":
    getArtist()