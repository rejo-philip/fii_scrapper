import datetime
from io import StringIO
import logging
import requests
import time
import pandas as pd
import sys
import json
import time

from requests.models import ReadTimeoutError 

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG,filename='logger.log')


def pretty_response(test):
    pass
    
    

def fao_participant_oi(start_date, end_date=None):
    '''
    Sample url used for downloading FO participants data
    https://archives.nseindia.com/content/nsccl/fao_participant_oi_11082021.csv
    https://archives.nseindia.com/content/nsccl/fao_participant_oi_ddMMYYYY.csv

    '''

    
    no_of_days = None
    if end_date == None:
        no_of_days = 0 
    else :
        no_of_days = (end_date - start_date).days
    
    df_total = pd.DataFrame()
    for i in range(no_of_days+1):
        
        try :
            date_datetime_obj = (start_date + datetime.timedelta(days=i))
            date_string= date_datetime_obj.strftime('%d%m%Y')
            url_path = f'https://archives.nseindia.com/content/nsccl/fao_participant_oi_{date_string}.csv'
            logger.debug(f'URL path : {url_path}')
            # time set for days for which data is not present
            response = requests.get(url_path,timeout=5)
            logger.debug('*'*100)            
            logger.debug(response.text)
            # stringIO is used os that text can be passed instead of name of file
            text = '\n'.join(response.text.split('\n')[1:])
            df = pd.read_csv(StringIO(text))
            # remove the last total row and total column
            df = df.iloc[0:4, :-2]
            df['Date'] = date_datetime_obj
            # df = df.set_index('Date')
            print(df.dtypes)
            logger.info(df.head())
            # print(df.index)
            logger.debug('*'*100)
            time.sleep(1)
            print(type(df_total))
            print(df_total.empty)
            if df_total.empty == False:     
                df_total = df_total.append(df,ignore_index=True)
            else : 
                df_total = df
                      
            # input("enter to go to next")
        except requests.exceptions.ReadTimeout:
            logger.warning(f'Response not present for {date_string}')
    
    print('3'*50)
    print(df_total)
    return df_total

def fii_latest_values():
    '''
    For equity fii , there is no way to check archived data(can be done for dii) so we need to store data in day to day bases

    '''


    url_path = f'https://www.nseindia.com/api/fiidiiTradeReact'
    header = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
"cache-control": "max-age=0",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "none",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
'authority': 'www.nseindia.com',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
    # time set for days for which data is not present
    flag = False

    while flag == False:
        time.sleep(2)
        try :
            response = requests.get(url_path,timeout=1,headers=header)
            print(response.text)
        
            json_object = json.loads(response.text)

            # stringIO is used os that text can be passed instead of name of file
            df = pd.DataFrame(json_object)
            flag = True
            return df

            # json_object = json.loads(response.text)

            # return json_object
                        
            # input("enter to go to next")
        except :
            logger.warning(f'Response timeed out')
        time.sleep(4)
    

    return None
    
            
        



if __name__ == '__main__' :
    logging.basicConfig(level=logging.DEBUG,filename='logger.log')
    fh = logging.FileHandler('a.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    logger = logging.getLogger()
    logger.addHandler(ch)
    logger.addHandler(fh)
    print(logger)
    first_date = '01112021'
    last_date = "29112021"
    # fao_participant_oi(datetime.strptime("11082021",'%d%m%Y'))
    if(len(sys.argv)>1):
        first_date = sys.argv[1]
        if(len(sys.argv)>2):
            last_date = sys.argv[2]
        else:
            last_date = None 
    first_date_time = datetime.datetime(*(time.strptime(first_date,'%d%m%Y')[0:6]))
    last_date_time = datetime.datetime(*(time.strptime(last_date,'%d%m%Y')[0:6])) if last_date != None else None 
    print(time.strptime("03082021",'%d%m%Y')[0:6])  
    total = fao_participant_oi(first_date_time,last_date_time)
    
    total = total.rename(columns = {'Future Stock Short\t':'Future Stock Short'})
    print(total.columns)
    
    total.to_csv('archive_data_csv.csv')
    

    
        
        
        
        
    
    
    
    
    