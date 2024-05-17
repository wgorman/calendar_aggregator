## Accelerate Orlando's Calendar Aggregator

Welcome to Orlando's Techno Capital Community Aggregator

The purpoose of this tool is to aggregate all the tech and business events in Orlando that are of interest to the Accelerate Orlando community.

### Current Event Sources Monitored
- Orlandopreneur: https://www.meetup.com/orlandopreneur


### Format of Events
```
{
    date: 'YYYY-MM-DD HH:MM:SS',
    title: 'Title of Event',
    location: 'Location of Event',
    description: 'Description of Event',
    link: 'Link to Event'
}
```

### Setting up and running
These scripts are meant to be configured in the cloud, scheduled to run on a regular basis, publishing the results to a public location for ease-of-use.  To run the scripts locally, you'll need to:
1. install python 3
2. run 'pip install -e .' to install the necessary dependencies
3. run the cli: python calendar-aggregator/main.py
4. to run unit tests: python -m unittest discover tests