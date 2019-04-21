import requests
import json
openid1="oWMkE0dXD-eQ4GTdH2PYAL30magQ"
openid2="oWMkE0Uc-QcMWARKwDZOHXLzx1DE"
id="08"
#re=requests.get("https://www.bupt404.cn/datedetail.php?task_id="+id)
#re=requests.get("https://www.bupt404.cn/permission.php?task_id="+id)
'''
re=requests.post("https://www.bupt404.cn/mark.php",
                data={"task_id":"08",
                "openid":openid2,
                "o_punctual_mark":3,
                "o_focus_mark":2,
                "o_attitude_mark":4})
'''

#re=requests.get("https://www.bupt404.cn/handshake.php?task_id=33&openid="+openid2+"&task_status=0")
re=requests.get("https://www.bupt404.cn/getmarks.php?openid="+openid1)

print(re.url)
print(re.text)
