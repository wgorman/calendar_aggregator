from bs4 import BeautifulSoup
import json
from datetime import datetime
from dateutil import parser
import dateutil.tz as tz
import urllib.request

#
# extract the necessary meetup info from the DOM
#
def parseEvent(soup):
    # Find the event container
    event_div = soup.find('div', class_='rounded-md bg-white p-4 shadow-sm sm:p-5')
    
    if event_div is None:
        return None

    # Extract date
    date = event_div.find('time').get_text(strip=True)
    
    # Extract title
    title = event_div.find('span', class_='ds-font-title-3 block break-words leading-7 utils_cardTitle__sAAHG').get_text(strip=True)
    
    # Extract location
    location = event_div.find('span', class_='text-gray6').get_text(strip=True)

    # Extract description
    description_div = event_div.find('div', class_='utils_cardDescription__1Qr0x max-h-[60px] text-sm')
    description_paragraphs = description_div.find_all('p')
    description = '\n'.join(p.get_text(strip=True) for p in description_paragraphs)

    tzinfos = {
        "CST": tz.gettz("America/Chicago"),
        "CDT": tz.gettz("America/Chicago"),                
        "EST": tz.gettz("America/Eastern"),
        "EDT": tz.gettz("America/Eastern")                 
    }

    date_obj = parser.parse(date, tzinfos = tzinfos)
    # Print the datetime object
    # print(date_obj)

    # Create a dictionary with the extracted information
    event_info = {
        'date': str(date_obj),
        'title': title,
        'location': location,
        'description': description
    }

    # Convert the dictionary to a JSON string
    event_info_json = json.dumps(event_info, indent=4)
    # print(event_info_json)
    return event_info

#
# Traverse the dom for meetup events
#
def readPage(html):
    soup = BeautifulSoup(html, features="lxml")
    unordered_lists = soup.find_all('ul')
    # Print out each unordered list
    foundUpcoming = False
    for ul in unordered_lists:
        val = ul.prettify()
        if foundUpcoming:
            if 'https://www.meetup.com/orlandopreneur/events/' in val:
                # loop through the li of the ul
                list_items = ul.find_all('li')
                events = []
                for li in list_items:
                    # skip list items that are empty
                    if len(li.get_text()) > 0:
                        events.append(parseEvent(li))
                # we're done, return all the events
                return events
        if 'Upcoming' in val:
            # if the list contains upcoming, the next list will be our events
            foundUpcoming = True
    # no events found :-(
    return []

def downloadMeetupEvents(downloadUrl):
    print('downloading meetup events page: ', downloadUrl)
    with urllib.request.urlopen(downloadUrl) as response:
        html = response.read()
        return readPage(html)
    