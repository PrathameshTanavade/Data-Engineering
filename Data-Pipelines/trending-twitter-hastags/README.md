# TRENDING TWITTER HASHTAG

## Data Pipeline
![](https://github.com/PrathameshTanavade/Data-Engineering/blob/master/Data-Pipelines/trending-twitter-hastags/media/figure1.png)


## Faker-Kafka Tweet Producer

```
{
    {
        'created_at': 'Wed Jun 28 00:31:23  2023', 
        'id_str': 4840, 
        'text': 'Almost identify those. Three second him computer.\nClaim bed rest strong. Policy century mother certainly.', 
        'user': {
            'id': 2631, 
            'name': 'Michele Wilson', 
            'screen_name': 'hannah77'
            }, 
        'entities': {
            'hashtags': [
                {
                    'text': 'chocolate', 
                    'indices': [67, 40]
                }
                
                ]
            }, 
        'place': {
            'place_type': 'city', 
            'country_code': 'US', 
            'country': 'United States', 
            'name': 'Mississippi'}
    }
```

The structure of tweet data is the same as described in [twitter API documentation](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/example-payloads). Fields that are irrelevant to this project are ommitted but the structure of relevant fields have not been altered keeping data in the original format.

The location for tweets is limited to the cities in United States of America.

## React APP

![](https://github.com/PrathameshTanavade/Data-Engineering/blob/master/Data-Pipelines/trending-twitter-hastags/media/trending_twitter_hashtag_ReactApp.gif)