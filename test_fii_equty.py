from nse_arc_lib import fii_latest_values as fii
import os 
import pandas as pd


# df_obj = fii()
# print(df_obj)


if __name__ == '__main__' :

    current_fii_dii_value = fii()
    if(type(current_fii_dii_value) == None):
        print("status not retrived")
        exit()
    # import pdb;pdb.set_trace()
    # import pdb;pdb.set_trace()
    
    path_status = os.path.exists("./fii_dii.csv")
    if(path_status == True  ):
        Source_df = pd.read_csv("./fii_dii.csv")
        Source_df  = Source_df[['category', 'date', 'buyValue', 'sellValue', 'netValue']]
        current_fii_dii_value = current_fii_dii_value.append(Source_df, ignore_index=True)


    current_fii_dii_value.to_csv('./fii_dii.csv')

    
