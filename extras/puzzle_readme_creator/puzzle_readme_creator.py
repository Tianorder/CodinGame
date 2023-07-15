# 23.6.28
# 本脚本用于生成每个puzzle下的readme.md文件
# 需要手动从页面复制到paste_here.txt，后续或许可以考虑直接从网页抓


import os
import sys
import shutil
import json

writeList = []
with open("paste_here.txt", 'r', encoding = 'utf-8') as readfile:
    line = readfile.readline()
    writeList.append("# " + line)
    puzzleName = line.lower().replace(" ", "-").replace(".", "-").rstrip()
    readfile.readline()
    readfile.readline()
    readfile.readline()
    line = ' '
    listMode = False
    while line:
        line = readfile.readline()
        if " 	" in line:
            writeList.append("\n")
            if "The Goal" in line:
                writeList.append(line.replace(" 	", "## ⚽"))
            elif "Rules" in line:
                writeList.append(line.replace(" 	", "## ✔"))
            elif "Example" in line:
                writeList.append(line.replace(" 	", "## 🗒"))
            elif "Game Input" in line:
                writeList.append(line.replace(" 	", "## 📑"))
            else:
                writeList.append(line.replace(" 	", "## "))
            listMode = False
        elif line.rstrip() in ("Input", "Output"):
            writeList.append("\n")
            writeList.append("### " + line)
            listMode = False
        elif line.startswith("- "):
            writeList.append("  " + line)
            listMode = False
        elif ": " in line:
            line = line.replace(": ", "**: ")
            writeList.append("* **" + line)
            line = readfile.readline()
        elif line.rstrip() == "Example":
            writeList.append("\n")
            writeList.append("### " + line)
            while line:
                line = readfile.readline()
                if line.rstrip() in ("Input", "Output"):
                    writeList.append("\n")
                    writeList.append("    " + line)
                    writeList.append("\n")
                else:
                    writeList.append("        " + line)
            listMode = False
        elif line.rstrip() == "Constraints":
            writeList.append("\n")
            writeList.append("### " + line)
            listMode = True
        elif line.endswith(":"):
            listMode = True
        elif listMode:
            writeList.append("* " + line)
        else:
            writeList.append(line)

# 后面会考虑直接在目标处创建文件，而不是手动移动
if "clash-of-code" in puzzleName:
    modeName = puzzleName[16:].lower().replace("-", "_")
    with open("../../clash_of_code/" + modeName + "/readme.md", 'w', encoding = 'utf-8') as writefile:
        for line in writeList:
            writefile.write(line)
else:
    # puzzleName = "winamax-battle"
    puzzlePath = "../../puzzles"
    for difficultyDir in os.listdir(puzzlePath):
        puzzleNamePath = os.path.join(puzzlePath, difficultyDir, puzzleName)
        if os.path.exists(puzzleNamePath):
            with open(puzzleNamePath + "/readme.md", 'w', encoding = 'utf-8') as writefile:
                for line in writeList:
                    writefile.write(line)
                print("已生成文件" + puzzleNamePath)
            break
