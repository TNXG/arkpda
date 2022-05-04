import sys
from pathlib import Path
from tarksr import Arknights, AkCall
import json
from config import 明日方舟账号, 明日方舟密码, 设备标识

def php_get():
    print(获取用户信息(sys.argv[1]))


ark = Arknights(
    username=明日方舟账号,                         # phone number
    password=明日方舟密码,                             # password
    device_id=设备标识,   # device_id
    relogin=True,                                  # auto relogin
    use_cache=True,                                 # use session cache
    session_dir=Path("accs"),                       # session_dir
)


def 获取用户信息(userId):
    ark.login()
    search_player = AkCall.Social(ark).getSortListInfo(userId, "")
    player_list = AkCall.Social(ark).searchPlayer([x["uid"] for x in search_player["result"]])
    return player_list


if __name__ == '__main__':
    php_get()