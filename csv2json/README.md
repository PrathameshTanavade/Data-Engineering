# CSV2JSON
This is a python program that creates a json copy of the csv file.

##Usage:
``` python3 csv2json.py {csv filename} {json filename}```

User gets to decide the filename for the output json file. This program/code also generates a log file as logfile.txt

##Example:

###csv file: listings.csv
```
id,name,host_id,host_name,neighbourhood_group,neighbourhood,latitude,longitude,room_type,price,minimum_nights,number_of_reviews,last_review,reviews_per_month,calculated_host_listings_count,availability_365,number_of_reviews_ltm,license
2818,Quiet Garden View Room & Super Fast WiFi,3159,Daniel,,Oostelijk Havengebied - Indische Buurt,52.36435,4.94358,Private room,49,3,305,2022-08-30,1.86,1,14,25,0363 5F3A 5684 6750 D14D
20168,Studio with private bathroom in the centre 1,59484,Alexander,,Centrum-Oost,52.36407,4.89393,Private room,106,1,339,2020-04-09,2.22,2,0,0,0363 CBB3 2C10 0C2A 1E29
27886,"Romantic, stylish B&B houseboat in canal district",97647,Flip,,Centrum-West,52.38761,4.89188,Private room,136,2,231,2022-04-24,1.78,1,121,8,0363 974D 4986 7411 88D8
28871,Comfortable double room,124245,Edwin,,Centrum-West,52.36775,4.89092,Private room,75,2,428,2022-08-24,2.92,2,117,75,0363 607B EA74 0BD8 2F6F
29051,Comfortable single room,124245,Edwin,,Centrum-Oost,52.36584,4.89111,Private room,55,2,582,2022-08-29,4.16,2,160,86,0363 607B EA74 0BD8 2F6F
44391,Quiet 2-bedroom Amsterdam city centre apartment,194779,Jan,,Centrum-Oost,52.37168,4.91471,Entire home/apt,240,3,44,2022-08-20,0.30,1,0,3,0363 E76E F06A C1DD 172C
49552,Multatuli Luxury Guest Suite in top location,225987,Joanna & MP,,Centrum-West,52.38028,4.89089,Entire home/apt,245,3,433,2022-09-05,3.00,1,165,58,0363 576A D827 5085 6B83
```

###Command
```
$ python3 csv2json.py listings.csv listings.json
``` 
###Result/Output json file: listings.json
```
{"id":2818,"name":"Quiet Garden View Room & Super Fast WiFi","host_id":3159,"host_name":"Daniel","neighbourhood_group":null,"neighbourhood":"Oostelijk Havengebied - Indische Buurt","latitude":52.36435,"longitude":4.94358,"room_type":"Private room","price":49,"minimum_nights":3,"number_of_reviews":305,"last_review":"2022-08-30","reviews_per_month":1.86,"calculated_host_listings_count":1,"availability_365":14,"number_of_reviews_ltm":25,"license":"0363 5F3A 5684 6750 D14D"}
{"id":20168,"name":"Studio with private bathroom in the centre 1","host_id":59484,"host_name":"Alexander","neighbourhood_group":null,"neighbourhood":"Centrum-Oost","latitude":52.36407,"longitude":4.89393,"room_type":"Private room","price":106,"minimum_nights":1,"number_of_reviews":339,"last_review":"2020-04-09","reviews_per_month":2.22,"calculated_host_listings_count":2,"availability_365":0,"number_of_reviews_ltm":0,"license":"0363 CBB3 2C10 0C2A 1E29"}
{"id":27886,"name":"Romantic, stylish B&B houseboat in canal district","host_id":97647,"host_name":"Flip","neighbourhood_group":null,"neighbourhood":"Centrum-West","latitude":52.38761,"longitude":4.89188,"room_type":"Private room","price":136,"minimum_nights":2,"number_of_reviews":231,"last_review":"2022-04-24","reviews_per_month":1.78,"calculated_host_listings_count":1,"availability_365":121,"number_of_reviews_ltm":8,"license":"0363 974D 4986 7411 88D8"}
{"id":28871,"name":"Comfortable double room","host_id":124245,"host_name":"Edwin","neighbourhood_group":null,"neighbourhood":"Centrum-West","latitude":52.36775,"longitude":4.89092,"room_type":"Private room","price":75,"minimum_nights":2,"number_of_reviews":428,"last_review":"2022-08-24","reviews_per_month":2.92,"calculated_host_listings_count":2,"availability_365":117,"number_of_reviews_ltm":75,"license":"0363 607B EA74 0BD8 2F6F"}
{"id":29051,"name":"Comfortable single room","host_id":124245,"host_name":"Edwin","neighbourhood_group":null,"neighbourhood":"Centrum-Oost","latitude":52.36584,"longitude":4.89111,"room_type":"Private room","price":55,"minimum_nights":2,"number_of_reviews":582,"last_review":"2022-08-29","reviews_per_month":4.16,"calculated_host_listings_count":2,"availability_365":160,"number_of_reviews_ltm":86,"license":"0363 607B EA74 0BD8 2F6F"}
{"id":44391,"name":"Quiet 2-bedroom Amsterdam city centre apartment","host_id":194779,"host_name":"Jan","neighbourhood_group":null,"neighbourhood":"Centrum-Oost","latitude":52.37168,"longitude":4.91471,"room_type":"Entire home\/apt","price":240,"minimum_nights":3,"number_of_reviews":44,"last_review":"2022-08-20","reviews_per_month":0.3,"calculated_host_listings_count":1,"availability_365":0,"number_of_reviews_ltm":3,"license":"0363 E76E F06A C1DD 172C"}
{"id":49552,"name":"Multatuli Luxury Guest Suite in top location","host_id":225987,"host_name":"Joanna & MP","neighbourhood_group":null,"neighbourhood":"Centrum-West","latitude":52.38028,"longitude":4.89089,"room_type":"Entire home\/apt","price":245,"minimum_nights":3,"number_of_reviews":433,"last_review":"2022-09-05","reviews_per_month":3.0,"calculated_host_listings_count":1,"availability_365":165,"number_of_reviews_ltm":58,"license":"0363 576A D827 5085 6B83"}

```

###Result/Output log file: logfile.txt
```
2023-Feb-05-04:40:41,Conversion Started
2023-Feb-05-04:40:42,Extraction Completed
2023-Feb-05-04:40:42,Conversion Completed
```


