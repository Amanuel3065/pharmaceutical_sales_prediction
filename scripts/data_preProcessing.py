import pandas as pd
import numpy as np
import os, sys

sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))
from logger import App_Logger

app_logger = App_Logger("logs/data_preProcessing.log").get_app_logger()


class dataProcessor:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.logger = App_Logger(
            "../logs/data_preProcessing.log").get_app_logger()


### DATA_CLEANER ###

    def drop_duplicates(self) -> pd.DataFrame:
        droped = self.df[self.df.duplicated()].index
        return self.df.drop(index=droped, inplace=True)

    def convert_to_numbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        return self.df

    def convertByteMB(self, coll) -> pd.DataFrame:
        for col in coll:
            self.df[col] = (self.df[col]) / 1*10e+5
            self.df.rename(
                columns={col: f'{col[:-7]}(MegaBytes)'}, inplace=True)
        print('Byte to MB change error')
        return self.df
    

###DATA_INFO_COLLECTION_FUNTIONS###

    def show_datatypes(self) -> pd.DataFrame:
        return self.df.dtypes

    def show_data_description(self) -> pd.DataFrame:
        return self.df.describe()

    def show_data_information(self) -> pd.DataFrame:
        return self.df.info()

    def show_statistical_info(self) -> pd.DataFrame:
        return self.df.agg(['mean'])

    def show_correlation(self) -> pd.DataFrame:
        return self.df.corr()

    def collective_grouped_mean(self, colomnName: str) -> pd.DataFrame:
        groupby_colomnName = self.df.groupby(colomnName)
        return groupby_colomnName.mean()

    def list_coloumn_names(self) -> pd.DataFrame:
        return self.df.columns
    
###MISSING_DATA_MANIPULATORS###

    def columns_WithMissingValue(self):
        miss = []
        dff = self.df.isnull().any()
        sum = 0 
        for col in dff:
            if col == True:
                miss.append(dff.index[sum])
            sum += 1 
        return miss
    
    def c_missing_percentage(self):  ###column based###
        c_null = self.df.isnull().sum()
        total_entries = self.df.shape[0]
        missing_percentage = []
        for missing_entries in c_null:
            value = str(
                round(((missing_entries/total_entries)*100),2)
            ) + " %"
            missing_percentage.append(value)
            
        missing_df = pd.DataFrame(c_null, columns=['total_missing_values'])
        missing_df['missing_percentage'] = missing_percentage
        return missing_df
    
    
