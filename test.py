# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import platform
import os
import sys
import re
from selenium.webdriver import ChromeOptions



def ppl(val):
    print("\033[0;36;40m"+val+"\033[0m")


drugMap = {
    '凡德他尼': 130,
    '帕博西尼': 120,
    '阿西替尼': 94,
    '马法兰': 112,
    '艾乐替尼': 76,
    '威罗菲尼': 124,
    '帕托珠单抗': 119,
    '尼达尼布': 74,
    '达雷木单抗': 134,
    '雷莫芦单抗': 97,
    '苏金单抗': 115,
    '尼拉帕尼': 111
}

linkMap = {
    "凡德他尼": "www.headkonhc.com/jiazhuangxianai/337.html",
    "帕博西尼": "www.headkonhc.com/ruxianai/83.html",
    "阿西替尼": "www.headkonhc.com/shenai/55.html",
    "马法兰": "www.headkonhc.com/duofaxinggusuiai/97.html",
    "艾乐替尼": "www.headkonhc.com/feiai/284.html",
    "威罗菲尼": "www.headkonhc.com/heisesuliu/342.html",
    "帕托珠单抗": "www.headkonhc.com/ruxianai/84.html",
    "尼达尼布": "www.headkonhc.com/feiai/340.html",
    "达雷木单抗": "www.headkonhc.com/duofaxinggusuiai/320.html",
    "雷莫芦单抗": "www.headkonhc.com/weiai/62.html",
    "苏金单抗": "www.headkonhc.com/yinxiebing/329.html",
    "尼拉帕尼": "www.headkonhc.com/luanchaoai/319.html"
}


def getWebDriver():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        return "./chromedriver.exe"
    if (sysstr == "Darwin"):
        return "./chromedriver"


keys = drugMap.keys()

# regx = r'[。？?!！]'
# allFiles = [d for d in os.listdir('.') if os.path.splitext(d)[-1] == '.txt']
# titleFlag = False
# title = ''
# mainKey = ''
# tags = ''
# typeid = 0
# tempContentLast = ''
# contentList = []
# stringBuilder = []
# wordEntry = []
# file_object = open(allFiles[0], 'r')
# try:
#     for line in file_object:
#         line.strip()
#         stringBuilder = []
#         if (len(line) == 1):
#             if (len(contentList) > 0):
#                 tempContentLast = contentList[len(contentList) - 2]
#                 stringBuilder = list(tempContentLast)
#                 stringBuilder.insert(
#                     stringBuilder.index(";") + 1, "color:#E53333;")
#                 tempContentLast = "".join(stringBuilder)
#                 contentList[len(contentList) - 2] = tempContentLast

#                 tempContentLast = contentList[len(contentList) - 1]
#                 tempContentLast = "<strong>" + tempContentLast+"</strong>"
#                 contentList[len(contentList) - 1] = tempContentLast
#                 contentList.pop(0)
#                 wordEntry.append({
#                     "title": title,
#                     "tags": tags,
#                     "typeid": typeid,
#                     "content": "".join(stringBuilder),
#                 })
#                 contentList = []
#         else:
#             if (len(contentList) == 0):
#                 title = line
#                 titleFlag = True
#                 contentList.append(line)
#             elif (len(contentList) == 1 and titleFlag):
#                 stringBuilder.append("<p><span style=\"font-size:16px;\">")
#                 if (re.search(regx, line)):
#                     reStrs = re.split(regx, line)
#                     for k in keys:
#                         if (reStrs[0].find(k) >= 0):
#                             mainKey = k
#                             tags = k
#                             typeid = drugMap.get(k)
#                             break
#                     stringBuilder.append("<strong>")
#                     stringBuilder.append(
#                         line[line.index(reStrs[0]):len(reStrs[0]) + 1])
#                     stringBuilder.append("</strong>")
#                     line = "".join(line[len(reStrs[0]) + 1:len(line)-1])
#                 stringBuilder.append(
#                     "<a href=\"http://" + linkMap.get(mainKey) + "\">")
#                 stringBuilder.append(mainKey)
#                 stringBuilder.append("</a>")
#                 stringBuilder.append(
#                     line[line.index(mainKey)+len(mainKey):len(line)])
#                 stringBuilder.append(
#                     "</span></p><br /><p style=\"text-align: center;\"><span style=\"font-size:16px;\"><img "
#                     + "alt=\"" + contentList[0] + "\" "
#                     + "src=\"/uploads/allimg/180920/10-1P920224153563.jpg\" " + "style=\"width: "
#                     + "240px; height: 180px;\" /></span><br /></p><p>")
#                 contentList.append("".join(stringBuilder))
#                 titleFlag = False
#             else:
#                 if (line == contentList[0]):
#                     stringBuilder.append(
#                         "<p><span style=\"font-size:16px;\"><span style=\"color:#ff0000;\">")
#                     stringBuilder.append(line)
#                     stringBuilder.append("</span></span><br />&nbsp;</p>")
#                 else:
#                     stringBuilder.append("<p><span style=\"font-size:16px;\">")
#                     stringBuilder.append(line)
#                     stringBuilder.append("</span><br />&nbsp;</p>")
#                 contentList.append("".join(stringBuilder))
# finally:
#     file_object.close()


options = ChromeOptions()
options.set_headless(True)
driver = webdriver.Chrome(executable_path=getWebDriver(),chrome_options=options)
driver.get("http://www.baidu.com")
ppl( driver.title)
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
driver.close()
