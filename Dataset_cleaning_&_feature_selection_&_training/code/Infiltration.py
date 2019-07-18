# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:56:37 2019

@author: RISHABH
"""

"""
Points which may differ:

1) Columns such as (Flow ID, Source IP, Destination IP, Timestamp, External IP)
   are missing in the dataset.
2) Spacing in the column name may differ.
    
"""
import pandas as pd;
import numpy as np;
from sklearn.preprocessing import LabelEncoder,OneHotEncoder;
import time;
from sklearn import preprocessing


time_in_seconds = time.time()


files=['Thursday-WorkingHours-Afternoon-Infilteration.csv',
       'Thursday-WorkingHours-Morning-WebAttacks.csv',
       'Tuesday-WorkingHours.csv',
       'Wednesday-workingHours.csv',
       'Friday-WorkingHours-Afternoon-DDos.csv',
       'Friday-WorkingHours-Afternoon-PortScan.csv',
       'Friday-WorkingHours-Morning.csv',
       'Monday-WorkingHours.csv']


dict_attack={
"BENIGN":0,
"Web Attack – Brute Force":1,
"Web Attack – XSS":2,
"Web Attack – Sql Injection":3,
"Bot":4,
"DDoS":5,
"DoS GoldenEye":6,
"DoS Hulk":7,
"DoS Slowhttptest":8,
"DoS slowloris":9,
"FTP-Patator":10,
"Heartbleed":11,
"Infiltration":12,
"PortScan":13,
"SSH-Patator":14
}


write_columns=[' Flow Duration',
               ' Total Backward Packets',
               'Total Length of Fwd Packets',
               ' Total Length of Bwd Packets',
               ' Fwd Packet Length Max',
               ' Fwd Packet Length Mean',
               ' Fwd Packet Length Std',
               ' Bwd Packet Length Mean',
               ' Bwd Packet Length Std',
               'Flow Bytes/s',
               ' Flow IAT Std',
               ' Flow IAT Max',
               ' Flow IAT Min',
               'Fwd IAT Total',
               ' Label'
               ]


read_path  = 'F:/Minor/cleaning/Uncleaned_Data/';
write_path =r'F:/Minor/New folder/'

df=pd.read_csv( read_path+'Thursday-WorkingHours-Afternoon-Infilteration.csv' , low_memory = False , encoding = "cp1258" );

df.drop(columns=[' Fwd Header Length.1'],axis=1,inplace=True)
 
#replacing NaN by 0
df.fillna(0,inplace=True);
#replacing infinity by -1
df.replace([np.inf, -np.inf], -1,inplace=True)

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
    


#deleting the faulty rows 
faulty_rows=df[(df[' Label']=="FAULTY")].index;
df.drop(faulty_rows, inplace=True)


object_label_type=[];

label_list=list(df)
for ii in label_list:
    if(df[ii].dtypes=="object"):
        if(ii!=" Label"):
            object_label_type.append(ii);
            


df.replace({' Label': 'BENIGN'},0,inplace=True)
df.replace({' Label': 'Infiltration'},12,inplace=True)


# To use LabelEncoder for converting categorical values in dataframe

# LabelEncoder variable
le = preprocessing.LabelEncoder()

# apply "le.fit_transform" ->this will transform the whole dataframe 
# df_encoded = df.apply(le.fit_transform)

#labels=[' Flow ID', ' Source IP', ' Destination IP', ' Timestamp', ' External IP']
#object_label_type=['Flow Bytes/s' ,' Flow Packets/s']
for i in (object_label_type):
     df[i]=le.fit_transform(df[i].astype(str))


# saving the dataframe to new csv
export_csv = df.to_csv (write_path+'cleadned_Infiltration.csv', index = None, columns=write_columns,header=True, mode = 'w', encoding='cp1258')


print("Total operation time: = ",time.time()- time_in_seconds ,"seconds");
