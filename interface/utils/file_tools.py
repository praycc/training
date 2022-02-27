import os.path

import yaml


class FileTools:
    @classmethod
    def get_interface_dir(self):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return path

    @classmethod
    def read_yaml(self,file_name):
        file_path = FileTools.get_interface_dir()
        yaml_path = os.sep.join([file_path,'data',file_name+'.yaml'])
        with open(yaml_path,encoding='utf8') as fp:
            return yaml.safe_load(fp)

if __name__ == '__main__':
    FileTools.read_yaml('secrets')
