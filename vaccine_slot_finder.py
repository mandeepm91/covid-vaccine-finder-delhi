import requests
import json
import pprint
import time
import webbrowser
from datetime import datetime

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={district_id}&date=13-05-2021"

districts_map = {
    141: 'Central Delhi',
    140: 'New Delhi',
    143: 'North West Delhi',
    149: 'South Delhi',
    144: 'South East Delhi',
    150: 'South West Delhi',
    142: 'West Delhi'
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'authority': 'cdn-api.co-vin.in',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'dnt': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}

def current_time_string():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_18_plus_centers(centers):
    result = []
    for center in centers:
        for session in center['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] > 0:
                result.append(center)
    return result

def print_center_details(center):
    print(center['name'])
    print(center['address'])
    for session in center['sessions']:
        if session['available_capacity'] > 0:
            print('date', session['date'], 'available_capacity', session['available_capacity'])

def print_centers_of_interest(centers):
    for center in centers:
        print_center_details(center)
        print('--------------------------------------------------------------------------------')

def get_centers_for_district(district_id, district_name):
    print('Fetching results for district {} -- {}'.format(district_name, current_time_string()))
    r = requests.get(
        url.format(district_id=district_id),
        headers=headers
    )
    result = json.loads(r.text)
    centers = result['centers']
    print('number of centers', len(centers))
    centers_of_interest = get_18_plus_centers(centers)
    return centers_of_interest

if __name__ == "__main__":
    while True:
        for (district_id,district_name) in districts_map.items():
            try:
                centers_of_interest = get_centers_for_district(district_id, district_name)
                if len(centers_of_interest) > 10:
                    print_centers_of_interest(centers_of_interest)
                    webbrowser.open("https://www.youtube.com/watch?v=rP1qjuFsV7w")
                    exit()
                elif len(centers_of_interest) > 0:
                    print("Less slots found                     ----------                              {}".format(len(centers_of_interest)))
                    print('\007')
                else:
                    print("No slots found")
                print('-------------------------------------------------------')
            except:
                print('unhandled exception')
            time.sleep(10)
        print('-----------------------------------------------------------------------------------------------------')
