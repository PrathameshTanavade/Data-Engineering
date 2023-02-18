# PYSPARK- STREAMEDJSON2CSV  
In this notebook, JSON records are being streamed continuously via netcat and are processed to store in csv format using pyspark.

### To transmit JSON records using netcat
    ` $ netcat -l -i 1 -p 9999 < sample.json `
    
   sample.json file contains JSON records which are transmitted at a rate of 1 record per second through localhost port 9999.
    
 
