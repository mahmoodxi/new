import requests
from time import sleep
import subprocess
import os
import flask
from flask import request

priv = subprocess.Popen("ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1'", shell=True, stdout=subprocess.PIPE).stdout
privip =  priv.read()
priv8 = privip.decode()
privfinish = priv8.replace("\n","")

app=flask.Flask(__name__)
@app.route("/aws-nasl2")
def main():
  secret = request.args.get('secret')
  tag = request.args.get('tag')
  tag2 = request.args.get('tag2')
  tls = request.args.get('tls')
  thread = request.args.get('thread')
  port = request.args.get('port')
  get = requests.get("https://icanhazip.com/")
  ip = str(get.text)
  ipfinish = ip.replace("\n","")

  os.system("rm -rf /etc/systemd/system/mtp.service")
  with open("/etc/systemd/system/mtp.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/MTProxy/objs/bin
ExecStart=/var/MTProxy/objs/bin/mtproto-proxy -u nobody -p 5000 -H """+str(port)+""" -S """+str(secret)+""" -P """+str(tag)+""" --nat-info """+str(privfinish)+":"+str(ipfinish)+""" --aes-pwd proxy-secret proxy-multi.conf -M """+str(thread)+"""
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp.service")
  return "Its OK"


@app.route("/aws-nasl3")
def main2():
  secret = request.args.get('secret')
  tag = request.args.get('tag')
  tag2 = request.args.get('tag2')
  tls = request.args.get('tls')
  thread = request.args.get('thread')
  port = request.args.get('port')
  get = requests.get("https://icanhazip.com/")
  ip = str(get.text)
  ipfinish = ip.replace("\n","")

  os.system("rm -rf /etc/systemd/system/mtp.service")
  with open("/etc/systemd/system/mtp.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/MTProxy/objs/bin
ExecStart=/var/MTProxy/objs/bin/mtproto-proxy -u nobody -p 5001 -H """+str(port)+""" -S """+str(secret)+""" -P """+str(tag)+""" -D """+str(tls)+""" --nat-info """+str(privfinish)+":"+str(ipfinish)+""" --aes-pwd proxy-secret proxy-multi.conf -M """+str(thread)+"""
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp.service")
  return "Its OK"


@app.route("/nasl2")
def main3():
  secret = request.args.get('secret')
  tag = request.args.get('tag')
  tag2 = request.args.get('tag2')
  tls = request.args.get('tls')
  thread = request.args.get('thread')
  port = request.args.get('port')
  get = requests.get("https://icanhazip.com/")
  ip = str(get.text)
  ipfinish = ip.replace("\n","")

  os.system("rm -rf /etc/systemd/system/mtp.service")
  with open("/etc/systemd/system/mtp.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/MTProxy/objs/bin
ExecStart=/var/MTProxy/objs/bin/mtproto-proxy -u nobody -p 5000 -H """+str(port)+""" -S """+str(secret)+""" -P """+str(tag)+""" --aes-pwd proxy-secret proxy-multi.conf -M """+str(thread)+"""
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp.service")
  return "Its OK"


@app.route("/nasl3")
def main4():
  secret = request.args.get('secret')
  tag = request.args.get('tag')
  tag2 = request.args.get('tag2')
  tls = request.args.get('tls')
  thread = request.args.get('thread')
  port = request.args.get('port')
  get = requests.get("https://icanhazip.com/")
  ip = str(get.text)
  ipfinish = ip.replace("\n","")

  os.system("rm -rf /etc/systemd/system/mtp.service")
  with open("/etc/systemd/system/mtp.service","a") as kos3:
    kos3.write(str("""[Unit]
Description=MTProxy
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/MTProxy/objs/bin
ExecStart=/var/MTProxy/objs/bin/mtproto-proxy -u nobody -p 5000 -H """+str(port)+""" -S """+str(secret)+""" -P """+str(tag)+""" -D """+str(tls)+""" --aes-pwd proxy-secret proxy-multi.conf -M """+str(thread)+"""
Restart=on-failure

[Install]
WantedBy=multi-user.target"""))
  kos3.close()
  os.system("systemctl daemon-reload")
  os.system("systemctl restart mtp.service")
  return "Its OK"



app.run(host="0.0.0.0",port=4444,debug=True)
