#!/usr/bin/env python

#---------------------------------------------------------
# File:   lottery.py                                      
# Author: Andrew Hersh <etch.himself@gmail.com>           
# Desc:   Get the most recent winning lottery numbers     
#---------------------------------------------------------

import requests
import json
import argparse
import logging

def get_most_recent_drawing(lottery, date):
    """Gets the most recent winning numbers for the given lottery type

    Args:
         lottery: a string representing the lottery to check

    Returns:
         A string of the winning numbers.
    """
    if lottery == 'mm':
        url = 'https://data.ny.gov/resource/h6w8-42p9.json?draw_date=%s' % date
        response = json.loads(requests.get(url).text)
        if len(response) > 0:
            return 'Winning numbers: %s, Megaball: %s' % (response[0]['winning_numbers'],response[0]['mega_ball'])
        else:
            return 'No drawing for %s' % date
    elif lottery == 'pb':
        url = 'https://data.ny.gov/resource/8vkr-v8vh.json?draw_date=%s' % date
        response = json.loads(requests.get(url).text)
        if len(response) > 0:
            return 'Winning numbers: %s, Multiplier: %s' % (response[0]['winning_numbers'],response[0]['multiplier'])
        else:
            return 'No drawing for %s' % date

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('lottery_type', help="The type of lottery to retrieve numbers for. Choices are megamillions, "
                                             "powerball")
    parser.add_argument('drawing_date', help="The date of the drawing to get numbers for.")
    args = parser.parse_args()
    print get_most_recent_drawing(args.lottery_type, args.drawing_date)