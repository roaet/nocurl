nocurl
======

Instead of using curl and copypasta, put your commonly-used curl commands
in payloads.conf and run them with a CLI menu. The output json is pretty-printed.

Obviously requires more development.

example
=======

Select payload:
1. keystone tokens
2. neutron routes GET
3. neutron routes POST
4. neutron networks GET
5. broken
?> 2
curl -s -i http://0.0.0.0:9696/v2.0/routes -X GET -H (headers)
data: null
⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡

Status code: 200
Headers:
        date: Thu, 23 Jan 2014 04:57:40 GMT
        content-length: 157
        content-type: application/json; charset=UTF-8
················································································
{
    "routes": [
        {
            "subnet_id": "836c8678-9a4d-4aac-a866-ba2d82808d41",
            "cidr": "0.0.0.0/0",
            "id": "5cef8bbd-d5a9-4a0f-a79b-53536dfca215",
            "gateway": "10.0.0.1"
        }
    ]
}

⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡ ⚡
Press ENTER to continue...
