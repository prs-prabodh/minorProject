from sklearn.neighbors import KNeighborsClassifier
import subprocess
import joblib as jl
import os
import pandas as pd
import scapy.all as sp

#sniffing  for 10 seconds

cap = sp.sniff(iface='Npcap Loopback Adapter', timeout= 10)

#generating pcap

sp.wrpcap('C:/users/hp/desktop/live_captured.pcap', cap, append=True)

#calling bat file

subprocess.call([r'C:/Users/hp/Desktop/Self_code/BatFileToCallCFMandPassValues.bat'])

#generation of csv after passing through CICFlowMeter

df=pd.read_csv('C:/users/hp/desktop/Self_code/live_captured.pcap_Flow.csv')

#drop unnecessary columns

df.drop(['Flow ID', 'Src IP', 'Src Port', 'Dst IP', 'Dst Port', 'Protocol',
       'Timestamp', 'Tot Fwd Pkts','Fwd Pkt Len Min','Bwd Pkt Len Max', 'Bwd Pkt Len Min','Flow Pkts/s', 'Flow IAT Mean','Fwd IAT Mean', 'Fwd IAT Std', 'Fwd IAT Max', 'Fwd IAT Min',
       'Bwd IAT Tot', 'Bwd IAT Mean', 'Bwd IAT Std', 'Bwd IAT Max',
       'Bwd IAT Min', 'Fwd PSH Flags', 'Bwd PSH Flags', 'Fwd URG Flags',
       'Bwd URG Flags', 'Fwd Header Len', 'Bwd Header Len', 'Fwd Pkts/s',
       'Bwd Pkts/s', 'Pkt Len Min', 'Pkt Len Max', 'Pkt Len Mean',
       'Pkt Len Std', 'Pkt Len Var', 'FIN Flag Cnt', 'SYN Flag Cnt',
       'RST Flag Cnt', 'PSH Flag Cnt', 'ACK Flag Cnt', 'URG Flag Cnt',
       'CWE Flag Count', 'ECE Flag Cnt', 'Down/Up Ratio', 'Pkt Size Avg',
       'Fwd Seg Size Avg', 'Bwd Seg Size Avg', 'Fwd Byts/b Avg',
       'Fwd Pkts/b Avg', 'Fwd Blk Rate Avg', 'Bwd Byts/b Avg',
       'Bwd Pkts/b Avg', 'Bwd Blk Rate Avg', 'Subflow Fwd Pkts',
       'Subflow Fwd Byts', 'Subflow Bwd Pkts', 'Subflow Bwd Byts',
       'Init Fwd Win Byts', 'Init Bwd Win Byts', 'Fwd Act Data Pkts',
       'Fwd Seg Size Min', 'Active Mean', 'Active Std', 'Active Max',
       'Active Min', 'Idle Mean', 'Idle Std', 'Idle Max', 'Idle Min'], axis= 1 , inplace = True )


#rename the columns

new=df.rename(columns = {"Tot Bwd Pkts":"Total Backward Packets", "TotLen Fwd Pkts":"Total Length of Fwd Packets","TotLen Bwd Pkts":"Total Length of Bwd Packets", "Fwd Pkt Len Max":"Fwd Packet Length Max", "Fwd Pkt Len Mean":"Fwd Packet Length Mean", "Fwd Pkt Len Std":"Fwd Packet Length Std", "Bwd Pkt Len Mean":"Bwd Packet Length Mean", "Bwd Pkt Len Std":"Bwd Packet Length Std", "Flow Byts/s":"Flow Bytes/s", "Fwd IAT Tot":"Fwd IAT Total"})

#generate the CSV

new.to_csv(r'C:/users/hp/desktop/Self_code/testable.csv')

#loading the trained model

model = jl.load('C:/users/hp/desktop/Self_code/final_trained_model.pkl')

#get prediction

#getting the dimensions of csv
size=new.shape


#converting csv into 1D array
data_array=new.values;

correct_prediction=0;

#predicting the behaviour of each packet
for i in range(size[0]):
        
    prediction=model.predict([data_array[i]])
    if prediction:
        print('Malicious Packet');
    else:
        print('Benign Packet')