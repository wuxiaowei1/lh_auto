import datetime
import json
class CJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            # �������ͳһ�޸���Ҫ�ĸ�ʽ
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            # �������ͳһ�޸���Ҫ�ĸ�ʽ
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)