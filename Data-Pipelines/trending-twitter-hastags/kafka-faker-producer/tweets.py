import random
import datetime
import time


from faker.providers import BaseProvider


class tweet(BaseProvider):
    
       
    def produce_msg(
            self,
            FakerInstance,
            count=1
            ):
        
        def hashtag():
            max_hashtags=5
            hashtags=[]
            hashtag_dict={}
            i=1

            max_hastags_iteration=random.randint(0,max_hashtags)

            if max_hastags_iteration==0:
                hashtags=[]    
            
            else:   
                while i <= max_hastags_iteration:
                    hashtag_dict["text"]=FakerInstance.word()
                    hashtag_dict["indices"]=[random.randint(1,100),random.randint(1,100)]            
                    hashtags.append(hashtag_dict)
                    i=i+1

            return hashtags



        message={
                "created_at": datetime.datetime.fromtimestamp(time.time()).strftime("%a %b %d %H:%M:%S %z %Y"),
                "id_str": FakerInstance.pyint(),
                "text": FakerInstance.text(max_nb_chars=140),
                "user": {
                  "id": FakerInstance.pyint(),
                  "name": FakerInstance.name(),
                  "screen_name": FakerInstance.user_name(),
                 },
                "entities": {
                  "hashtags": hashtag(),
                 },
                "place":{
                    "place_type":"city",
                    "country_code":"US",
                    "country":"United States",
                    "name":FakerInstance.state()
                }
              }

        
        key={"tweet":"tweet"}
        return message,key
