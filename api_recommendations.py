#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 5 14:15:25 2024

@author: Diya Ganesh
"""

import http.client
import json

API_KEY = #INSERT API KEY HERE


def get_recommendation(key, rec_type, genre1='fiction', genre2='fantasy', 
                       lower='3', upper='5'):
    ''' given an API key, a recommendation type (genre, rating, or page count),
        and parameters relevent to that type (if genre, enter 2 genres, 
        if rating/page count, enter upper and lower bounds), return a list of
        dictionaries where each dictionary is a book that fits the requests
    '''
    conn = http.client.HTTPSConnection("books-api7.p.rapidapi.com")
    
    headers = {
        'X-RapidAPI-Key': key,
        'X-RapidAPI-Host': "books-api7.p.rapidapi.com"
    }
    
    if rec_type == 'genre':
        conn.request("GET", f"/books/find/genres?genres%5B%5D={genre1}&genres%5B%5D={genre2}", 
                     headers=headers)
    elif rec_type == 'rating':
        conn.request("GET", f"/books/find/rating?lte={upper}&gte={lower}&p=1", 
                     headers=headers)
    elif rec_type == 'page count':
        conn.request("GET", f"/books/find/pages?lte={upper}&gte={lower}&p=1", 
                     headers=headers)
        
    res = conn.getresponse()
    data = res.read()
    return json.loads(data.decode("utf-8"))


def clean_response(lst_dct):
    ''' given a list of dictionaries where each dictionary is a different
        response, finds the title and author of the first two responses
        and returns them in a readable sentence
    '''
    
    title1 = lst_dct[0]['title']
    author1 = f"{lst_dct[0]['author']['first_name']} {lst_dct[0]['author']['last_name']}"
    title2 = lst_dct[1]['title']
    author2 = f"{lst_dct[1]['author']['first_name']} {lst_dct[1]['author']['last_name']}"
    
    response = f"You may enjoy {title1} by {author1} or {title2} by {author2}."
    
    return response
        

def main():
    # determines if user is interested in recommendation by genre, rating
    # or page count, then asks for more information regarding their choice
    # and calls the corresponding API request
    get_by = input(
        "Would you like recommendations by genre, rating, or page count?\n")
    
    if get_by.lower() == "genre":
        # asks for users two favorite genres
        genres = input(
            "What are your 2 favorite genres, separated by spaces?\n")
        genres_lst = genres.split()
        genre_1, genre_2 = genres_lst[0], genres_lst[1]
        rec = get_recommendation(API_KEY, 'genre', genre1=genre_1, 
                                 genre2=genre_2)
        print(clean_response(rec))
        
    elif get_by.lower() == "rating":
        # asks for an upper and lower bound for ratings
        lower_bound = input("What is your lower bound for ratings?\n")
        upper_bound = input("What is your upper bound for ratings?\n")
        rec = get_recommendation(API_KEY, 'rating', lower=lower_bound, 
                                 upper=upper_bound)
        print(clean_response(rec))
        
    elif get_by.lower() == "page count":
        # asks for an upper and lower bound for page count
        lower_bound = input("What is your lower bound for page count?\n")
        upper_bound = input("What is your upper bound for page count?\n")
        rec = get_recommendation(API_KEY, 'page count', lower=lower_bound, 
                                 upper=upper_bound)
        print(clean_response(rec))
    
    # asks user if they want to see the plots of the books, if yes
    # it prints the plot of both the recommended books from earlier
    plot_request = input("Would you like a description of the plots?\n")
    if plot_request.lower() == "yes":
        print(f"\n{rec[0]['title']}'s plot is: {rec[0]['plot']}\n\n\n")
        print(f"{rec[1]['title']}'s plot is: {rec[1]['plot']}")

if __name__ == "__main__":
    main()
