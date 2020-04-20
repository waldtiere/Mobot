import sys
sys.path.append('../../../')
import pandas as pd
from typing import TypeVar
from src.utils.Exporter.ExportInterface import ExportInterface
from src.utils.Interface.ManagerInterface import ManagerInterface


ExportType = TypeVar('ExportType', object, ExportInterface)


class ExportManager(ManagerInterface):
    def __init__(self, export_type: ExportType):
        self._export_type = export_type

    def exec(self,dataframe: pd.DataFrame, target_dir: str, file_name: str):
        return self._export_type.save_file(dataframe,target_dir,file_name)


if __name__ == '__main__':
    print('### ExportManager ###')