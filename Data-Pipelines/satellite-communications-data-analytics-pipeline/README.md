# SATELLITE COMMUNICATIONS DATA ANALYTICS PIPELINE

This project is a recreation of [AWS architecture](https://aws.amazon.com/blogs/publicsector/creating-satellite-communications-data-analytics-pipelines-aws-serverless-technologies/) using open-source technologies.

## Data Pipeline
![](https://github.com/PrathameshTanavade/Data-Engineering/blob/master/Data-Pipelines/satellite-communications-data-analytics-pipeline/media/figure1.png)


Airflow is used to schedule batch processing spark-jobs at per hour rate due to the update rate of MongoDB Charts Dashboard being 1 hour making stream processing impractical.

## Kafka - Generator
```
{
    'datetime': '2023-06-27 22:57:11', 
    'remoteId': 'C1710',
    'beamId': 136,
    'beamName': 'BeamS07', 
    'satLong': -129.2, 
    'fwdModCodId': [10], 
    'fwdSNR': 5.6, 
    'packetsLost': 315, 
    'latitude': 60.4, 
    'longitude': -113.8, 
    'rxFreq': 12200150, 
    'txFreq': 14700580, 
    'fwdBitRate': 14.0
    }
```

## Dashboard
![]()