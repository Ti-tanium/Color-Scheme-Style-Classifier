# -*- coding: utf-8 -*-
# chenlong
import re
import urllib.request
import os
import chardet   #需要导入这个模块，检测编码格式
import csv
import colorsys
from colorthief import ColorThief

# 抓取网页图片


# 根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    encode_type = chardet.detect(html)  
    html = html.decode(encode_type['encoding'])
    return html


# 创建保存图片的文件夹
def mkdir(path):
    path = path.strip()
    # 判断路径是否存在
    # 存在    True
    # 不存在  Flase
    isExists = os.path.exists(path)
    if not isExists:
        print("Created new folder:",path)
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已经存在
        return False


# 输入文件名，保存多张图片
def saveImages(imglist, path,style):
    global count
    for imageURL in imglist:
        splitPath = imageURL.split('.')
        fTail = splitPath.pop()
        if len(fTail) > 3:
            fTail = 'jpg'
        fileName = path + "/" +style+"_"+str(count[style]) + "." + fTail
        # 对于每张图片地址，进行保存
        try:
            u = urllib.request.urlopen(imageURL)
            data = u.read()
            f = open(fileName, 'wb+')
            f.write(data)
            f.close()
            
            ## extrac color scheme
            color_thief = ColorThief(fileName)

            # build a color palette
            palette = color_thief.get_palette(color_count=5,quality=1)

            # sort palette by lightness
            def sortByLight2(elem):
                hls=colorsys.rgb_to_hls(*elem)
                return hls[1]
            palette.sort(key=sortByLight2,reverse=True)

            with open("train.csv",'a+',newline='') as csvfile:
                writer = csv.writer(csvfile)
                row=[]
                for color in palette:
                    row.extend(color)
                row.extend([style])
                writer.writerow(row)
            print("Saving:",fileName)
        except urllib.request.URLError as e:
            print (e.reason)
        count[style]+=1


        # 获取网页中所有图片的地址


def getAllImg(html):
    # 利用正则表达式把源代码中的图片地址过滤出来
    reg = r'data-src="(.+?=jpg)"'
    pattern = re.compile(reg)
    imglist = pattern.findall(html)  # 表示在整个网页中过滤出所有图片的地址，放在imglist中
    print("Len",len(imglist))
    return imglist

count={}
# 创建本地保存文件夹，并下载保存图片
if __name__ == '__main__':
    style=['cute','fresh','business']
    for s in style:
        count[s]=0
    for query in style:
        for i in range(1,400):
            print("Page:",i)
            html = getHtml("https://www.freepik.com/search?page="+str(i)+"&query="+query+"&sort=popular")  # 获取该网址网页详细信息，得到的html就是网页的源代码
            path = u"/home/u22893/style_classifier/Style_classifier/data/"+query
            mkdir(path)  # 创建本地文件夹
            imglist = getAllImg(html)  # 获取图片的地址列表
            saveImages(imglist, path,query)  # 保存图片
    for s in style:
        print(s+":",count[s])