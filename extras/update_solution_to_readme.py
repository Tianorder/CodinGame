# 23.6.27
# 本脚本用于把Puzzle以人数排序
# 数据写入Readme.md，以表格呈现


import os
import datetime

# cwd_path = os.getcwd()
# readme_path = os.path.join(cwd_path, "..", "README.md")
with open("../README.md", 'r', encoding = 'utf-8') as readfile:
    data = readfile.read()

puzzlePath = "../puzzles"
for difficultyDir in os.listdir(puzzlePath):
    puzzleNamePath = os.path.join(puzzlePath, difficultyDir)
    if os.path.isdir(puzzleNamePath):
        for puzzleName in os.listdir(puzzleNamePath):
            filePath = os.path.join(puzzleNamePath, puzzleName)
            if os.path.isdir(filePath):
                haveNewFile = False
                replaceStr = ""
                fileList = os.listdir(filePath)
                # 用sorted排序比for循环更快。但如果在这里直接判断创建日期，没有最近的文件则直接不进行后面的循环会不会更快？
                fileList = sorted(fileList, key=lambda x: os.path.getctime(os.path.join(filePath, x)))

                for filename in fileList:
                    if filename.endswith('py'):
                        replaceStr += (", [Python](https://github.com/Tianorder/CodinGame/tree/main/puzzles/"
                                       + difficultyDir + "/" + puzzleName + "/" + filename + ")")
                    elif filename.endswith('java'):
                        replaceStr += (", [Java](https://github.com/Tianorder/CodinGame/tree/main/puzzles/"
                                       + difficultyDir + "/" + puzzleName + "/" + filename + ")")
                    elif filename.endswith('js'):
                        replaceStr += (", [Java](https://github.com/Tianorder/CodinGame/tree/main/puzzles/"
                                       + difficultyDir + "/" + puzzleName + "/" + filename + ")")
                    elif filename.endswith('bat'):
                        replaceStr += (", [Bash](https://github.com/Tianorder/CodinGame/tree/main/puzzles/"
                                       + difficultyDir + "/" + puzzleName + "/" + filename + ")")

                    # 检查文件的创建日期是否在七天内
                    file_path = os.path.join(filePath, filename)
                    creation_time = os.path.getctime(file_path)
                    creation_datetime = datetime.datetime.fromtimestamp(creation_time)
                    current_datetime = datetime.datetime.now()
                    time_diff = current_datetime - creation_datetime

                    # 判断是否在最近七天内
                    if time_diff.days <= 7:
                        haveNewFile = True

                # 替换README文件数据
                if haveNewFile:
                    loc = data.find("|",data.find("/" + puzzleName + ")")) + 15
                    replaceStr = replaceStr[2:].ljust(400)
                    data = data[:loc] + replaceStr + "|" + data[loc + 401:]

with open("../README.md", 'w', encoding = 'utf-8') as writefile:
    writefile.write(data)
