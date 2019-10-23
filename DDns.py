from Utils import Utils
import json
import os

class DDns:
    @staticmethod
    def save_records(accessKeyId,accessSecret,domain):
        response = str(Utils.get_records(accessKeyId,accessSecret,domain))[2:-1]
        jsonfile = json.loads(response)
        # print(jsonfile)
        with open('records.json','w') as recordsfile:
            json.dump(jsonfile, recordsfile, sort_keys=True, indent=4, separators=(',', ': '))  

    @staticmethod
    def update_record(accessKeyId,accessSecret,record_RR,record_type,wanip):
        with open('records.json','r') as recordsfile:
            jsonfile = json.load(recordsfile)
            records = jsonfile["DomainRecords"]["Record"]
            for record in records:
                if record["RR"] == record_RR and record["Type"] == record_type:
                    if record["Value"] != wanip:
                        recordid = record["RecordId"]
                        Utils.update_record(accessKeyId,accessSecret,recordid,record_RR,record_type,wanip)
                        break
                    else :
                        break
                else:
                    continue
    