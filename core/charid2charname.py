import sys
import httpx
import json


def php_get():
    print(干员id换名称(sys.argv[1]))


def 干员id换名称(charId):
    kkdyapi = 'https://test.api.kokodayo.fun/data/char?id='
    content = httpx.get(kkdyapi + charId)
    json_str = json.loads(content.text)
    data = json_str['result']['data']['name']
    return '{"code":"200","CharName":"' + data + '"}'


if __name__ == '__main__':
    php_get()
