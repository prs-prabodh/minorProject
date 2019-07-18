# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 01:28:20 2019

@author: RISHABH
"""

import pandas as pd;
import time;


time_in_seconds = time.time()

files=[
       'cleaned_benign.csv',
       'cleaned_bot.csv',
       'cleaned_DDoS.csv',
       'cleaned_infiltration.csv',
       'cleaned_patator.csv',
       'cleaned_portScan.csv',
       'cleaned_restAll_Attack.csv',
       'cleaned_web_attack.csv',
      ]

read_path  = 'F:/Minor/New folder/';
write_path =r'F:/Minor/New folder/'

flag=True;

for i in range(len(files)):
    
    df=pd.read_csv( read_path+files[i] , low_memory = False , encoding = "cp1258" );
    
    print(df.shape,"Begninng of ",files[i])
    
    if(flag):
        export_csv = df.to_csv (write_path+'combined.csv', index = None, header=True, mode = 'w', encoding='cp1258')
        flag=False;        
    else:
        export_csv = df.to_csv (write_path+'combined.csv', index = None, header=False, mode = 'a', encoding='cp1258')
    
    print("combined -> ",files[i])
    
    print("Total operation time: = ",time.time()- time_in_seconds ,"seconds");



