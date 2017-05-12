#! usr/bin/python
#coding=utf-8   //这句是使用utf8编码方式方法， 可以单独加入python头使用。

import os
import os.path
import shutil
#此函数用于二级文件夹内部文件复制到一级文件内
def dirToFile():
    rootdir = '/Users/chenliang/Coding/6'                                 
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in  dirnames:                      
             print "parent is:" + parent
             # print  "dirname is" + dirname

        for filename in filenames:
            if filename != '.DS_Store':                        
                print "parent is:"+ parent
                print "filename is:" + filename

                par_name = parent.split('/')[-1]
                # import pdb; pdb.set_trace()
                print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
                shutil.copy('%s'%os.path.join(parent,filename),'/Users/chenliang/Coding/6/%s.jpg'%par_name)
                # os.rename('%s'%os.path.join(parent,filename),'/Users/chenliang/Coding/5/%s/1.png'%img_name)

#此函数用于给每个文件建立自己的文件夹
def fileToDir():
    rootdir = '/Users/chenliang/Coding/6'                                 
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in  dirnames:                      
             print "parent is:" + parent
             print  "dirname is" + dirname

        for filename in filenames:
            if filename != '.DS_Store':  
                # import pdb; pdb.set_trace()                      
                # print "parent is:"+ parent
                # print "filename is:" + filename
                # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
                img_name = filename.split('.')[0]
                print img_name
                # import pdb; pdb.set_trace()
                os.makedirs('/Users/chenliang/Coding/6/%s'%img_name)
                shutil.copy('%s'%os.path.join(parent,filename),'/Users/chenliang/Coding/6/%s/1.jpg'%img_name)


if __name__ == "__main__":
    # invitate()
    fileToDir()
    # dirToFile()