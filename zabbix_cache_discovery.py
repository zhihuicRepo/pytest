#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import json
import subprocess
import sys
import MySQLdb

def mysqlconn():
    try:
        sqlcmd = "select name,app_id from app_desc where status='2' and type='2'"
        conn = MySQLdb.connect(host='172.x.x.1',user='cacheuser',passwd='passwd123',db='cachecloud2',port=3306)
        curl = conn.cursor()
        curl.execute(sqlcmd)
        res = curl.fetchall()
        curl.close()
        conn.close()
        return res

    except MySQLdb.Error,e:
        print 'Mysql Error Msg:',e

#appType=cluster
#appId=33
#{u'shardNum': 6, u'status': 1, u'message': u'client is up to date, Cheers!', u'shardInfo': u'172.30.33.236:6387 172.30.33.237:6381 172.30.33.238:6381 172.30.33.239:6381 172.30.33.240:6381 172.30.33.241:6381', u'appId': 33}

def get_request(appType,appId):
    url = "http://cache.xxxx.com/cache/client/redis/%s/%s.json?clientVersion=1.0-SNAPSHOT"%(appType,appId)
    req = urllib2.Request(url)
    try:
        res = urllib2.urlopen(req,timeout=10)
        content = json.loads(res.read())
        #print content
        return content
    except:
        #print 'rul_cannot'
        return 'url_cannot_connect'

def check_stat(ip,port):
    try:
        cmd_status = "redis-cli -h %s -p %s cluster info |grep cluster_state: |awk -F: '{print $2}'"%(ip,port)
        res1 = subprocess.Popen(cmd_status, stdout=subprocess.PIPE, shell=True)
        res1 = res1.stdout.read().strip()
        return res1
    except:
        return 'error'

def check_fail(ip,port):
    try:
        cmd_fail = "redis-cli -h %s -p %s cluster info |grep cluster_slots_fail: |awk -F: '{print $2}'" % (ip, port)
        res2 = subprocess.Popen(cmd_fail, stdout=subprocess.PIPE, shell=True)
        res2 = res2.stdout.read().strip()
        return res2
    except:
        return '22'

def cache_name_discovery(result):
    print '{',
    print '"data":[',
    i=0
    for cache_data in result:
        print '{',
        print '"{#CACHE_NAME}":"%s"}'%cache_data[0],
        if i < len(result)-1:
            print ',',
            i +=1
    print ']',
    print '}'

if __name__=='__main__':
    dict_cache = {}
    result = mysqlconn()
    for m,n in result:
        dict_cache.setdefault(m,n)
    if sys.argv[1]=='discovery':
        cache_name_discovery(result)
    elif sys.argv[1]=='stat':
        appType = sys.argv[2]
        cache_name = sys.argv[3]
        appId = dict_cache.get(cache_name)
        content = get_request(appType,appId)
        ipp_list = content['shardInfo'].split(' ')
        for ipp in ipp_list:
            ip,port = ipp.split(':')
            res = check_stat(ip,port)
            if res!='ok':
                sys.exit('error')
        print "ok"
    elif sys.argv[1]=='slotsfail':
        appType = sys.argv[2]
        cache_name = sys.argv[3]
        appId = dict_cache.get(cache_name)
        content = get_request(appType, appId)
        ipp_list = content['shardInfo'].split(' ')
        for ipp in ipp_list:
            ip, port = ipp.split(':')
            res = check_fail(ip, port)
            if res != '0':
                print int(res)
                sys.exit()
        print 0
    else:
        sys.exit()
