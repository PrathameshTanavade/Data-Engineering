# TRENDING TWITTER HASHTAG

## Data Pipeline
![](https://github.com/PrathameshTanavade/Data-Engineering/blob/master/Data-Pipelines/trending-twitter-hastags/media/figure1.png)


## Faker-Kafka Tweet Producer

```
{
    'created_at': 'Wed Jun 28 00:31:23  2023', 
    'id_str': 5696, 
    'text': 'Level country position reason none compare Mr. Assume plant person accept bank green draw treatment.', 
    'user': {
        'id': 9870, 
        'name': 'Ariel Graves', 
        'screen_name': 'hruiz'
        }, 
    'entities': {
        'hashtags': [
            {
                'text': 'sunshine', 
                'indices': [19, 34]
            }, 
            {
                'text': 'liverpool', 
                'indices': [90, 1]
            }, 
            {
                'text': 'football', 
                'indices': [38, 99]
            }
            ]
        }, 
    'place': {
        'place_type': 'city', 
        'country_code': 'US', 
        'country': 'United States', 
        'name': 'Texas'
        }
}
```

The structure of tweet data is the same as described in [twitter API documentation](https://developer.twitter.com/en/docs/twitter-api/v1/data-dictionary/object-model/example-payloads). Fields that are irrelevant to this project are ommitted but the structure of relevant fields have not been altered keeping data in the original format.

The location for tweets is limited to the cities in United States of America.

## React APP

![](https://github.com/PrathameshTanavade/Data-Engineering/blob/master/Data-Pipelines/trending-twitter-hastags/media/trending_twitter_hashtag_ReactApp.gif)