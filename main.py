from DDns import DDns
from urllib import request
import json
wanip = json.load(request.urlopen('http://jsonip.com'))['ip']
# 要更改解析记录的域名
domain = ' '
# 阿里云获取accesskeyid
accessKeyId = ' '
# 阿里云获取的accesskeysecret
accessSecret = ' '
# 获取全部解析记录
DDns.save_records(accessKeyId,accessSecret,domain)
# 要更改的解析记录
DDns.update_record(accessKeyId,accessSecret,'@','A',wanip)
