import os
import json

with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
        # print(datas)
        check_item = datas.get("POJIE_COOKIE_LIST", [])[0]
        print(check_item)
# import os
# print(os.path.dirname(os.path.dirname(__file__)))