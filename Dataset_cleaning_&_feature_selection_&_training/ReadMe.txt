Note:
1) Every Attack and Model is trained according to 15 attributes which is the union of all the attributes required for any attack

2) All the filtered csv for indivdual attacks is on drive under the folder Dataset for Individual Attack with code.

3) The trained model is uploaded on drive as its size is exceeding under the folder Trained Model.

link:     https://drive.google.com/drive/u/0/folders/16-wMSUM9JGtcJp9E8qZWBy89Jfc84jgE
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Code Folder:

1) This folder consist of python code for individual cleaning of all attacks.

2) Also contain merging.py file for merging all the attack into one csv(i.e combined.csv) which is used for training the model.


Extra Folder:

1) This folder contain python files for normalization of data and Model training file.

2)final_trained_model is the final and combined trained model with:
   
#KMeans Accuracy:  0.7041077384723899
#KNN Accuracy:  0.9878387748514591

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
These are the numbers used to represent attacks:
 
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



These are the attributes used:

               ' Flow Duration',
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