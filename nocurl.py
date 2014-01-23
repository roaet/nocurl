#!/usr/bin/python

#
# Hit JSON API endpoints with a CLI
#

import subprocess as sp
import ConfigParser as cfgp
import json
import os
import requests

class Payload(object):
    def __init__(self, name, url, port, route, token, method, data,
            headers={'X-Auth-Token':None, 'Content-Type':'application/json'}):
        self.name = name
        self.url = url
        self.port = port
        self.route = route
        self.token = token
        self.method = method
        self.data = data
        self.headers = headers
        if not self.headers['X-Auth-Token']:
            self.headers['X-Auth-Token'] = self.token

    def __str__(self):
        return 'curl -s -i http://{}:{}/{} -X {} -H (headers)'.format(
            self.url, self.port, self.route, self.method)
      

class Menu(object):
    def __init__(self):
        self.cls()
        self.tokens_file = 'tokens.conf'
        self.payload_file = 'payloads.conf'
        self.payloads = self.init_payloads()

    def cls(self):
        sp.call('clear', shell=True)

    def init_payloads(self):
        payloads = []
        config_tokens = cfgp.ConfigParser()
        config_tokens.read('tokens.conf')
        default_token = config_tokens.get('default', 'token')
        config = cfgp.ConfigParser()
        config.read('payloads.conf')
        for section in config.sections():
            url = config.get(section, 'url')
            port = config.get(section, 'port')
            route = config.get(section, 'route')
            token = config.get(section, 'token')
            method = config.get(section, 'method')
            try:
                data = json.loads(config.get(section, 'data'))  # needs to be in json format
            except Exception:
                data = None
            if len(token) < 1:
                token = default_token
            p = Payload(section, url, port, route, token, method, data)
            payloads.append(p)
        return payloads
    
    def prompt_payload(self):
        self.cls()
        print("Select payload:")
        for i, payload in enumerate(self.payloads, start=1):
            print("{}. {}".format(i, payload.name)) 
        selection = input("?> ")
        return self.payloads[selection - 1]

def exec_payload(payload):
    url = 'http://{}:{}/{}'.format(payload.url, payload.port, payload.route)
    headers = payload.headers
    method = payload.method.upper()
    if method == "GET":
        r = requests.get(url,  headers=headers)
    elif method == "POST":
        r = requests.post(url, data=json.dumps(payload.data, ensure_ascii=True), headers=headers)
    elif method == "OPTIONS":
        r = requests.options(url, data=payload.data, headers=headers)
    elif method == "PUT":
        r = requests.put(url, data=payload.data, headers=headers)
    elif method == "PATCH":
        r = requests.patch(url, data=payload.data, headers=headers)
    elif method == "DELETE":
        r = requests.delete(url, data=payload.data, headers=headers)
    elif method == "HEAD":
        r = requests.head(url, data=payload.data, headers=headers)
    else:
        print("Method {} unknown.".format(payload.method))
        return
    decorator = ''
    if r.status_code != requests.codes.ok:
        decorator = u"\u2614"
    print(u"Status code: {} {}".format(r.status_code, decorator))
    print("Headers:")
    for k, v in r.headers.iteritems():
        print("\t{}: {}".format(k, v))
    print(u"\u00B7"*80)
    try:
        print(json.dumps(r.json(), indent=4, separators=(',', ': ')))
    except ValueError:
        print(r.text)
    

if __name__ == "__main__":
    print "Hi"
    while 1:
        menu = Menu()
        payload = menu.prompt_payload()
        print str(payload)
        print("data: {}".format(json.dumps(payload.data, ensure_ascii=True)))
        print(u"\u26A1 "*40)
        print
        exec_payload(payload)
        print
        print(u"\u26A1 "*40)
        raw_input("Press ENTER to continue...")
