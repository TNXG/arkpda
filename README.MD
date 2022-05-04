# 明日方舟玩家数据获取API
## Arknights Player Data Acquisition API
如果有在使用宝塔面板的用户请取消禁用php exec函数

在使用前请先安装Python3.9.9，再CD到core文件夹中执行

```cmd
pip install -r requirements.txt
```

之后前往`config.py`填写配置项

调用提示

`http://ip:port/api/games/arknights/data/user/userdata.php?type=all&id=`
`http://ip:port/api/games/arknights/data/user/userdata.php?id=`

charid2charname.php是一个干员id换名称的，当然这个可以直接用php写，但有之前写的现成的Python代码我为什么要再造一遍PHP呢（大雾）

## PHP 优雅 永不过时