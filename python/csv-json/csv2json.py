import sys
import pandas as pd
from datetime import datetime


def extract(filename):
    dataframe=pd.read_csv(filename)
    return dataframe

def load(targetfile,data_to_load):
    data_to_load.to_json(targetfile, orient='records',lines=True )

def log(message):
    timestamp_format="%Y-%h-%d-%H:%M:%S"
    now=datetime.now()
    timestamp=now.strftime(timestamp_format)
    with open('logfile.txt','a') as f:
        f.write(timestamp+','+message+'\n')

if __name__=="__main__":
    if len(sys.argv)!=3:
        print("Error")
        sys.exit(-1)
    
    infile=sys.argv[1]
    outfile=sys.argv[2]
    log('Conversion Started')
    extracted_data=extract(infile)
    log('Extraction Completed')
    load(outfile,extracted_data)
    log('Conversion Completed')

