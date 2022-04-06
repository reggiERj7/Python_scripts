# -*- coding: utf-8 -*-
from pyzabbix import ZabbixAPI
def login():
    zapi = ZabbixAPI("http://172.16.0.19")
    zapi.login(user="Admin", password="zabbix")

def main():
    with open("adresses.txt", "r") as file:
        for i in file:
            ip = i.split(".")
            name = ip[3].replace("\n", "")
            zapi.host.create(
                host = f"a230w{name}",
                status= 0,
                available = 1,
                interfaces=[{
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": i.replace("\n", ""),
                    "port": 10050,
                    "dns": ""
                }],
                groups=[{
                    "groupid": 31
                }],
                templates=[{
                    "templateid": 10500
                }])

login()
main()