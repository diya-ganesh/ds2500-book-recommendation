#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:54:44 2024

@author: deekshitamadhalam
"""

import csv 
import matplotlib.pyplot as plt 

BOOKS = "/Users/deekshitamadhalam/Downloads/books_1.Best_Books_Ever.csv"

def read_file(filename):
    ''' given the name of a csv file (string),
        read in the contents and return as a 2d list
        of strings 
    '''
    data = []
    with open(filename, "r") as infile:
        csvfile = csv.reader(infile)
        for row in csvfile:
            data.append(row)
    return data

def find_index(data, type1): 
    '''
        given the list of lists of all 50000+ books and
        the criteria that the user wants to filter on, returns the 
        index value where the criteria is located at by using a for loop 
        and going through it till the string matched a value in the list
    '''
    
    for index, data in enumerate(data[0]):
        if data == type1: 
            return index 
                 
def count(data,  ans1, index):
    '''
    given list of lists of all 50000+ books, the
    specific sub category within the criteria they want to filter with, and 
    the index value where the criteria is listed in, it returns 
    The number of times that the ans1 appears in the column by using a for
    loop and looking for that word 

    '''
    count = 0
    for i in (data): 
        if ans1 in (i[index]):
            count += 1 
    return count
   
def total_data(data, genre, ind1, pub_year, ind2, min_rating, ind3):
    '''
    given the list of lists of all 50000+ books, the three different filter 
    words within the criteria they are using, and the three 
    different indicies for each of the criteria, it returns a count of the 
    number of books in all of them by using a for loop and only adding to the 
    count if ALL are a part of it. 
    '''
    count = 0
    for j in data: 
        if genre in j[ind1] and pub_year in j[ind2] and min_rating in j[ind3]: 
            count += 1 

    return count
  
def main(): 
    data = read_file(BOOKS)
    print(f'choose from one of the following for filter: {data[0]}\n')
    
    # ask user what categories and what thing in each category they want
    # to filter
    type1 = input('what do you want to filter on first\n')
    ans1 = input(f'what {type1} do you want\n')

    type2 = input('what do you want to filter on second\n')
    ans2 = input(f'what {type2} do you want\n')

    type3 = input('what do you want to filter on third\n')
    ans3 = input(f"what {type3} do you want\n")
 
    # find number of books that fit each category and the number of books
    # that fit all the categories and then plot them on a bar graph
    num_index = find_index(data, type1)
    value_one = count(data, ans1, int(num_index))
    plt.bar(ans1, value_one)
    
    num_index_two = find_index(data, type2)
    value_two = count(data, ans2, int(num_index_two))
    plt.bar(ans2, value_two)
    
    num_index_3 = find_index(data, type3)
    value_3 = count(data, ans3, int(num_index_3))
    plt.bar(ans3, value_3)
     
    total = total_data(data,ans1, num_index, ans2, num_index_two, ans3, 
                       num_index_3)
    
    plt.bar("total", total)
    plt.title("Number of books per Catergory")
    plt.ylabel("Number of books")
    plt.xlabel("Categories")

if __name__ == "__main__":
    main()