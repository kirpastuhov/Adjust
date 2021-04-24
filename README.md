Adjust Home Task
===

##  Description

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.
Dataset is expected to be stored and processed in a relational database.

## Getting started
Go to project directory and apply migrations:

```
python3 manage.py migrate
```
Next you need to import dataset from csv file into our database:

Open up the shell

```
python3 manage.py shell
```

And paste following lines into it to upload the dataset.

```
import csv

from AdjustHomeTask.api.models import DatasetModel

with open('dataset.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         r = DatasetModel(date=row['date'], channel=row['channel'], country=row['country'], os=row['os'], impressions=row['impressions'], clicks=row['clicks'], installs=row['installs'], spend=row['spend'], revenue=row['revenue'])
         r.save()
```

## Supported parameters:
1. `sort_by={field}` - Sort resulting dataset by given field. Default sorting order is ascending, if you want to sort the dataset in descending order, just add minus sign before the field just like this `sort_by=-{field}`
2. `group_by={field1,field2}` - Group resulting dataset by one or more columns from this list: date, channel, country, os.
3. Filter dataset by fields from this list: date, channel, country, os:
   
   - ```date_before={YYYY-MM-DD}```
   - ```date_after={YYYY-MM-DD}```
   - ```channel={channel}```
   - ```country={two-letter country codes (ISO)}```
   - ```os={operating system}```
   
   
## Common API use-cases:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
   
    ```GET /dataset/?date_before=2017-06-01&group_by=channel,country&sort_by=-clicks```
   

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
   
   ```GET /dataset/?os=ios&date_after=2017-05-01&date_before=2017-05-31&group_by=date&sort_by=date```

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
   
    ```GET /dataset/?date_after=2017-06-01&date_before=2017-06-01&group_by=os&sort_by=-revenue```

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
    
    ```GET /dataset/?country=CA&group_by=channel&sort_by=-cpi```