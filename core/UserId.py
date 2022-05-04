import sys
from pathlib import Path
from tarksr import Arknights, AkCall
import httpx
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
    player_list = AkCall.Social(ark).searchPlayer(
        [x["uid"] for x in search_player["result"]])
    for players in player_list["players"]:
        nickName = str(players["nickName"])
        nickNumber = str(players["nickNumber"])
        lastOnlineTime = str(players["lastOnlineTime"])
        uid = str(players["uid"])
        level = str(players["level"])
        charId = []
        for assistCharList in players["assistCharList"]:
            charId.append(assistCharList["charId"])
        charId1 = charId[0]
        charId2 = charId[1]
        charId3 = charId[2]
    data = {}
    content = json.loads(json.dumps(data))
    content['code'] = '200'
    content['NickName'] = nickName + '#'+ nickNumber
    content['Level'] = level
    content['UserId'] = uid
    content['LastOnlineTime'] = lastOnlineTime
    charId = []
    charId = charId1, charId2, charId3
    content['charId'] = charId
    return json.dumps(content, ensure_ascii=False)


if __name__ == '__main__':
    php_get()
