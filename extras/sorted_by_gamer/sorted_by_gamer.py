# 23.6.27
# 本脚本用于把Puzzle以人数排序
# 数据写入Readme.md，以表格呈现


import os
import sys
import shutil
import json

gameList = []
fileList = os.listdir()
for filename in fileList:
    if filename.endswith('.json'):
        with open(filename, 'r', encoding = 'utf-8') as readfile:
            json_data = json.load(readfile)
        gameList.extend(json_data)

# 按照 solvedCount 字段进行排序
gameList = sorted(gameList, key=lambda x: int(x["solvedCount"]), reverse=True)[:300]

# 按格式输出
with open("copytoREADME", 'w', encoding = 'utf-8') as writefile:
    for i, game in enumerate(gameList):
        writefile.write("| " + str(i + 1).ljust(4) + "| "
              + str(game["solvedCount"]).ljust(7) + "| ["
              + (game["title"] + "](https://www.codingame.com" + game["detailsPageUrl"] + ")").ljust(130) + "| "
              + game["level"].ljust(11) + "| "
              + "".ljust(400) + "|")
        writefile.write('\n')
