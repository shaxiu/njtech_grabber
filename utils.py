
import configparser
import requests

CONF_FILE = './config.ini'
cf = configparser.ConfigParser()
cf.read(CONF_FILE)  # 读取配置文件
JSESSIONID = cf.get("baseConfig", "JSESSIONID")
QINGCLOUDELB=cf.get("baseConfig", "QINGCLOUDELB")
kklxdm=cf.get("baseConfig","kklxdm")
xkxnm=cf.get("baseConfig","xkxnm")
xkxqm=cf.get("baseConfig","xkxqm")
njdm_id=cf.get("baseConfig","njdm_id")
Ck='QINGCLOUDELB='+QINGCLOUDELB+'; JSESSIONID='+JSESSIONID
xkkz_id = cf.get("baseConfig", "xkkz_id")
header = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
                'Cookie':Ck
            }

def getCourseList(keyW):
    url = 'https://jwgl.njtech.edu.cn/xsxk/zzxkyzb_cxZzxkYzbPartDisplay.html'
    data = {'xkxnm':xkxnm,'xkxqm':xkxqm,'kklxdm':kklxdm,'kspage':1,'jspage':20,'yl_list[0]':1}
    if keyW!="":
        data['filter_list[0]']=keyW
    req = requests.post(url,data,headers=header)#发送post请求，第一个参数是URL，第二个参数是请求数据
    return(req.json())

def getCourseDetail(kch):
    url = 'https://jwgl.njtech.edu.cn/xsxk/zzxkyzbjk_cxJxbWithKchZzxkYzb.html'
    data = {'bklx_id':0,'njdm_id':njdm_id,'xkxnm':xkxnm,'xkxqm':xkxqm,'kklxdm':kklxdm,'kch_id':kch,'xkkz_id':xkkz_id}
    req = requests.post(url,data,headers=header)#发送post请求，第一个参数是URL，第二个参数是请求数据
    return(req.json())

def getChoosedList():
    url = 'https://jwgl.njtech.edu.cn/xsxk/zzxkyzb_cxZzxkYzbChoosedDisplay.html'
    data = {'xkxnm':2021,'xkxqm':12}
    req = requests.post(url,data,headers=header)#发送post请求，第一个参数是URL，第二个参数是请求数据
    return(req.json())

def chooseCourse(jxb_ids,kch_id):
    url = 'https://jwgl.njtech.edu.cn/xsxk/zzxkyzbjk_xkBcZyZzxkYzb.html'
    data = {'jxb_ids':jxb_ids,'kch_id':kch_id,'qz':0}
    req = requests.post(url,data,headers=header)#发送post请求，第一个参数是URL，第二个参数是请求数据
    return(req.json())

def quitCourse(jxb_ids):
    url = 'https://jwgl.njtech.edu.cn/xsxk/zzxkyzb_tuikBcZzxkYzb.html'
    data = {'jxb_ids':jxb_ids}
    req = requests.post(url,data,headers=header)#发送post请求，第一个参数是URL，第二个参数是请求数据
    return(req.json())