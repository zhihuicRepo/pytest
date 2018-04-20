#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
#BGP-NETAM-01
__author__ = "kaiz"

import sys,os,requests,time,re,json
cur_time = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))

def handle(hostname,log_path,bak_path_,save_days):
  resp = session.post('http://1.x.x.3:7991', json=[{
      'client': 'local',
      'tgt': hostname,
      'fun': 'state.sls',
      'arg': ['logrotate'],
      'kwarg': {"pillar":{"log_path":log_path,"bak_path_":bak_path_,"save_days":save_days}},
    }])
  return json.dumps(resp.json())

if __name__ == "__main__":
  global log_std,log_err
  session = requests.Session()
  session.post('http://1.x.x.3:7991/login', json={
    'username': 'LSALTUSER',
    'password': 'PASSWORD',
    'eauth': 'pam',
  })
  try:
    hostname = sys.argv[1]
    log_path = sys.argv[2]
    bak_path_ = sys.argv[3]
    save_days = sys.argv[4]
#    resp = session.post('http://1.x.x.3:7991', json=[{
#      'client': 'local',
#      'tgt': hostname,
#      'fun': 'state.sls',
#      'arg': ['logrotate'],
#      'kwarg': {"pillar":{"log_path":log_path,"bak_path_":bak_path_,"save_days":save_days}},
#    }])
    a = handle(hostname=hostname,log_path=log_path,bak_path_=bak_path_,save_days=save_days)
    log_std =  "INFO:" + a
    m = re.search("is running as PID",a)
    if m is not None:
      #若能匹配到The function \"state.sls\" is running as PID这个，则取出jid
      print "The function \"state.sls\" is running as PID"
      list = a.strip().split()
      index = list.index("jid")+1
      jid = re.search("\d+",list[index])
      jid = jid.group()
      print type(jid),hostname
      #取出jid后执行类似salt '*' saltutil.signal_job 20140211102239075243 15
      resp = session.post('http://1.x.x.3:7991', json=[{
      'client': 'local',
      'tgt': hostname,
      'fun': 'saltutil.signal_job',
      'arg': [ jid ,15],
    }])
      aa = json.dumps(resp.json())
      print "INFO:"+"saltutil.signal_job jid 15"+str(aa)
      log_std = aa
      a = json.dumps()
    with open("/tmp/logrotate_std.log","w") as f:
      f.write(cur_time+':'+str(log_std)+"\n")
    print log_std
#  except Exception, e:
  except TypeError, e:
  
    err = str(e)
    err = "EROR"+":"+cur_time+":"+err 
    print err
    #with open("/tmp/logrotate_err.log","w+") as f:
    #  f.write(err)
