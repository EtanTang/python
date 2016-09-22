#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import string
import time

#main        
if __name__ == '__main__':

    print("=========== start copy =========")

#系统时间
    print('====== '+time.strftime('%Y-%m-%d %H:%M:%S')+' =====')
    str_time=time.strftime('%Y%m%d%H%M%S')
    
#路径
    curr_dir = sys.path[0]

    if not os.path.exists("D:\\pyBackup\\copy\\%s" %str_time):
        os.mkdir("D:\\pyBackup\\copy\\%s" %str_time)
#遍历目录
    for rt, dirs, files in os.walk(curr_dir):
        for file in files:
            if os.path.splitext(file)[0] == 'cpbck':
                print('-'+ file)
            else:
                shutil.copy(os.path.join(rt,file), "D:\\pyBackup\\copy\\%s" %str_time)
                print('+'+ file)
        
#    input('\n\nwaiting......')
    shutil.move("cpbck.py", "D:\\pyBackup\\copy\\%s" %str_time)
#    os.remove("amend_c.py")
'''
#文件处理        
    src_files = os.listdir()

    for file in src_files:
#目录isdir
        if os.path.isdir(os.path.join(curr_dir,file)):
            print(file)
            
#文件isfile
        else:
            if os.path.splitext(file)[1] == '.h': 
                new_file = os.path.splitext(file)[0]+'.h' 
                old_file = 'backup_'+os.path.splitext(file)[0]+'.h'
                os.rename(file, old_file)
                delete_c_comment(old_file, new_file)
                shutil.move(old_file,"D:\\pyBackup\\%s" %str_time)
                #os.remove(old_file)
            if os.path.splitext(file)[1] == '.c': 
                new_file = os.path.splitext(file)[0]+'.c' 
                old_file = 'backup_'+os.path.splitext(file)[0]+'.c'
                os.rename(file, old_file) 
                delete_c_comment(old_file, new_file)
                shutil.move(old_file,"D:\\pyBackup\\%s" %str_time)
                #os.remove(old_file)
'''


'''
            if os.path.splitext(file)[1] == '.h': 
                new_file = os.path.splitext(file)[0]+'.h' 
                old_file = 'backup_'+os.path.splitext(file)[0]+'.h'
                os.rename(file, old_file)
                delete_c_comment(old_file, new_file)
                #shutil.move(old_file,"D:\\pyBackup\\%s" %str_time)
                #os.remove(old_file)
            if os.path.splitext(file)[1] == '.c': 
                new_file = os.path.splitext(file)[0]+'.c' 
                old_file = 'backup_'+os.path.splitext(file)[0]+'.c'
                os.rename(file, old_file) 
                delete_c_comment(old_file, new_file)
                shutil.move(old_file,"D:\\pyBackup\\%s" %str_time)
                #os.remove(old_file)
            
             


当前路径path = sys.path[0]

time.strftime('%Y-%m-%d',time.localtime(time.time()))

最后用time.strftime()方法，把刚才的一大串信息格式化成我们想要的东西，现在的结果是：
2010-07-19

time.strftime里面有很多参数，可以让你能够更随意的输出自己想要的东西：
下面是time.strftime的参数：
strftime(format[, tuple]) -> string
将指定的struct_time(默认为当前时间)，根据指定的格式化字符串输出
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12） 
%M 分钟数（00=59）
%S 秒（00-59）

%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
'''    
