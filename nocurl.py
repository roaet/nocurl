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
    def __init__(self, name, url, port, route, token, method):
        self.name = name
        self.url = url
        self.port = port
        self.route = route
        self.token = token
        self.method = method
    
    def __str__(self):
        return 'curl -s -i http://{}:{}/{} -X {} -H "X-Auth-Token: {}"'.format(
            self.url, self.port, self.route, self.method, self.token)
      

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
            if len(token) < 8:
                token = default_token
            p = Payload(section, url, port, route, token, method)
            payloads.append(p)
        return payloads
    
    def prompt_payload(self):
        self.cls()
        print("Select payload:")
        for i, payload in enumerate(self.payloads):
            print("{}. {}".format(i, payload.name)) 
        selection = input("?> ")
        return self.payloads[selection]

def exec_payload(payload):
    url = 'http://{}:{}/{}'.format(payload.url, payload.port, payload.route)
    headers = {'X-Auth-Token': payload.token}
    r = requests.get(url, headers=headers)
    print json.dumps(r.json(), indent=4, separators=(',', ': '))
    #print r.json()


if __name__ == "__main__":
    print "Hi"
    menu = Menu()
    payload = menu.prompt_payload()
    print str(payload).replace(payload.token,
            payload.token[:2] + '...' + payload.token[-2:])
    print
    exec_payload(payload)
