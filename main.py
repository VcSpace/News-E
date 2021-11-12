import time
import os

from src.Platform import pt
from src.CNN_Economy import Cnn
from src.FOX_Economy import Fox

def get_News(platform, filename, debug):
    #debug True开启
    if debug:
        Cnn.create_file(filename)
        Fox.main(filename)
        return
    Cnn.main(filename)
    Fox.main(filename)

def get_filename(platform):
    if platform == True:
        win_file = pt.win_filename()
        return win_file
    else:
        linux_file = pt.linux_filename()
        return linux_file

if __name__ == '__main__':
    Debug = False
    m_platform = pt.get_platform() #判断系统
    filename = get_filename(m_platform)
    get_News(m_platform, filename, Debug) #获取信息

    pt.file_move(m_platform) #文件移动 重命名操作

    if m_platform == True:
        pt.pause()
