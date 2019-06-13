# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:32:58 2019

@author: RISHABH
"""
import pandas as pd;
import numpy as np;
from sklearn.preprocessing import LabelEncoder,OneHotEncoder;
import time;

time_in_seconds = time.time()


files=['Thursday-WorkingHours-Afternoon-Infilteration.csv',
       'Thursday-WorkingHours-Morning-WebAttacks.csv',
       'Tuesday-WorkingHours.csv',
       'Wednesday-workingHours.csv',
       'Friday-WorkingHours-Afternoon-DDos.csv',
       'Friday-WorkingHours-Afternoon-PortScan.csv',
       'Friday-WorkingHours-Morning.csv',
       'Monday-WorkingHours.csv']

read_path  = 'F:/Minor/Dataset/minorProject/cleaning/Uncleaned_Data/';
write_path =r'F:/Minor/Dataset/'

flag=True;

for i in range(len(files))  :

    df=pd.read_csv( read_path+files[i] , low_memory = False , encoding = "cp1258" );
    
    #dropping same column 
    #df.drop(df.columns[[55]],axis=1,inplace=True)
    #or df[' Fwd Header Length.1']

    df.drop(columns=[' Fwd Header Length.1'],axis=1,inplace=True)
    
    #replacing NaN by 0
    df.fillna(0,inplace=True);
    
    #replacing infinity by -1
    df = df.replace([np.inf, -np.inf], -1)

    #removing NaN value if necessary
    #df.dropna()

    #replacing Infinity value from dataset by -1 
    df.replace({'Flow Bytes/s': 'Infinity', ' Flow Packets/s': 'Infinity'}, -1,inplace=True)

    #replacing – value from dataset by - and removing faulty rows    
    symbol="–";
    col=df.shape;

    for i in range(col[0]):
        if(df[' Label'][i]==symbol):
            df[' Label'][i]="-"

    #counting number of zeros 
    #df["sum_0"] = df.apply(lambda row: sum(row[0:78]==0) ,axis=1)
    df["sum_0"] = df.apply(lambda row: sum(row[0:col[1]]==0) ,axis=1)
    
    #deleting the rows which have large number of zero entries in a row
    rows_to_delete=df[(df['sum_0']>=35)].index;
    df.drop(rows_to_delete, inplace=True)
    
    #deleting the faulty rows 
    faulty_rows=df[(df[' Label']=="FAULTY")].index;
    df.drop(faulty_rows, inplace=True)
    
    # To use LabelEncoder for converting categorical values in dataframe
    
    # LabelEncoder variable
    le = LabelEncoder()
    
    # apply "le.fit_transform" ->this will transform the whole dataframe 
    # df_encoded = df.apply(le.fit_transform)
    
    #labels=[' Flow ID', ' Source IP', ' Destination IP', ' Timestamp', ' External IP']
    labels=['Flow Bytes/s' ,' Flow Packets/s' ,' Label']
    for i in range(len(labels)):
        df_encoded=le.fit_transform( df[ labels[i] ] )
        df[ labels[i] ]=df_encoded;

    #dropping the extra column
    df.drop(columns=['sum_0'],axis=1,inplace=True)
    
    if(flag):
        export_csv = df.to_csv (write_path+'all.csv', index = None, header=True, mode = 'w', encoding='cp1258')
        flag=False;        
    else:
        export_csv = df.to_csv (write_path+'all.csv', index = None, header=False, mode = 'a', encoding='cp1258')
        
    print("Total operation time: = ",time.time()- time_in_seconds ,"seconds");
    
    
    
    
    
    
    
    