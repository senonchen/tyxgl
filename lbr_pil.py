#!/usr/bin/env python
#coding:utf-8
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')


from PIL import Image,ImageFont,ImageDraw



def invitate():
    NAMEFONTSIZE = 30
    IDFORMSIZE = 26
    namelist = loadName()
    print namelist
    for i in range(200,400):
        im=Image.open('/Users/chenliang/Coding/1.png') 
        draw=ImageDraw.Draw(im)  
        idfont = ImageFont.truetype('/Library/Fonts/小米兰亭字体.ttf',size=IDFORMSIZE)
        namefont = ImageFont.truetype('/Library/Fonts/小米兰亭字体.ttf',size=NAMEFONTSIZE)
        number=0
        if (i+1) <10:
            number='00%s'%(i+1)
        elif (i+1) >=10 and (i+1) <99:
            number='0%s'%(i+1)
        else:
            number = (i+1)
        draw.text((40,48),'NO.SGXZ008%s'%(number),(255,255,255),font=idfont)
        name = namelist[int('%s'%i)]
        # import pdb; pdb.set_trace()
        #名字长度
        length = len(name)
        na = re.sub('[\u4e00-\u9fa5]','',name)
        na_len = len(na)
        not_chinese = length-na_len
        chinese = na_len/3
        print name
        print na
        print(u"名字长度%s"%length)
        print(u"中文个数%s"%chinese)
        print(u"非中文个数%s"%not_chinese)
        print(u"字符总数%s"%(chinese*3+not_chinese))
        sum_cha = int(not_chinese+chinese)
        print(u"总字数%s"%sum_cha)
        print(u'字符串总长度%s'%(sum_cha*NAMEFONTSIZE))
        namex = int((750-(chinese*NAMEFONTSIZE+not_chinese*16))/2)
        print namex
        draw.text((namex,515),u'%s'%name,fill=(174,174,174),font=namefont)
        # im.show()
        im.save('/Users/chenliang/Coding/XGXZ/XGXZ_%s.png'%(i+1))

def loadName():
    import pdb; pdb.set_trace()
    f=open('sgxz_name.txt','rb')
    fr = f.read()
    fa = fr.split('\n')
    return fa

def telephoneNum4():
    f = open('telephoneNum4.txt','rb')
    fr = f.read()
    fa = fr.split('\n')
    teleNumList = []
    tele_num = 0
    for item in fa:
        if item == '':
            teleNumList.append('0')
        else:
            tele_num = tele_num+1
            teleNumList.append(item)
    import pdb; pdb.set_trace()

    fopen = open('telephoneNum4_cpl.txt', 'w')
    for item in teleNumList:
        fopen.write('*')
        fopen.write(item[7:12])
        fopen.write('\n')
    fopen.close()


# def writeFile(teleNumList):
#     fopen = open('telephoneNum4_cpl.txt', 'w')
#     fopen.write('dfdf')
#     fopen.close()




if __name__ == "__main__":
    invitate()
    # telephoneNum4()