import logging
import os

from interface.utils.file_tools import FileTools

logger = logging.getLogger(__name__)
file_path = os.sep.join([FileTools.get_interface_dir(),'logs'])
#没有文件夹就先创建一个
if not os.path.exists(file_path):
    os.mkdir(file_path)

#日志格式设置
formatter = logging.Formatter('[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')
# formatter = logging.Formatter('[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]: %(message)s')
fileHandler = logging.FileHandler(filename=file_path+"/apitest.log",encoding='utf8')
fileHandler.setFormatter(formatter)
#控制台句柄
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)

logger.addHandler(fileHandler)
logger.addHandler(streamHandler)
logger.setLevel(logging.INFO)