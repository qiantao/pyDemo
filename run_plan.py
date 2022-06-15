import requests
import base64


# url = "http://xocean.demo.perfma.cn/"
url = "http://10.10.220.23:8089/"

# productId = "PROD224"
productId = "PROD2"

# planId = "P6"
planId = "P10"

key = "XAccessKey:U2FsdGVkX1/GGZG1vdctM9+BnB8MJKWcbHJKOsijI+8="

bytesStr = key.encode(encoding='utf-8')
bytesStr.decode()
b64str = base64.b64encode(bytesStr)
print(b64str)
print(type(b64str))


headers = {
    "Authorization": "Basic {}".format(str(b64str, encoding="utf-8")),
    "Content-Type": "application/json",
}
print(headers)

body = {"productId": productId,
        "env": "开发",
        "planId": planId,
        "needReport": "true",
        "operator": "testYuniqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq",
        "biz": "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
        }

print(body)
res = requests.post(url="{}api/xocean/openapi/authorization/scene/run".format(url), json=body, headers=headers)
print(res.status_code)
print(res.text)
print(res.json()["object"]["runId"])


print({"runId": res.json()["object"]["runId"]})
res2 = requests.post(url="{}api/xocean/openapi/authorization/scene/run/result".format(url), json={
    "runId": res.json()["object"]["runId"]
}, headers=headers)
print(res2.status_code)
print(res2.text)


print({
        "productId": productId,
        "planId": planId
    })
res3 = requests.post(url="{}api/xocean/openapi/authorization/scene/run/lastReport".format(url), json={
        "productId": productId,
        "planId": planId
    }, headers=headers)
print(res3.status_code)
print(res3.text)
