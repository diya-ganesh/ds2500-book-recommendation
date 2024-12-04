#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:20:59 2024

@author: diyakadakia

Diya Ganesh, Diya Kadakia, and Deekshita Madhalam
DS 2500 Project 
Book Recommendation System: by similar books 
April 12, 2024
"""

# import libraries 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as ssd
import numpy as np
from sklearn.decomposition import IncrementalPCA
import random

books = "/Users/diyakadakia/Downloads/ds 2500/project/books_1.Best_Books_Ever.csv"


def assign_centroids(df, centroids, x, y):
    
    ''' given a dataframe, the centroids, and lists of x and y values, 
        determine which centroid each point is assoicated with   
    '''
    

    centroid_assignments = []

    for i in range(len(df)):
        curr_point = df.iloc[i][[x, y]]
        min_dist = float("inf")
        min_centroid = -1

        for j in range(len(centroids)):
            curr_centroid = centroids[j]
            dist = ssd.euclidean(curr_point, curr_centroid)
            if dist < min_dist:
                min_dist = dist
                min_centroid = j
        centroid_assignments.append(min_centroid)

    return centroid_assignments


def main():
    
    # read in the dataframe and clean data
    df = pd.read_csv(books)
    df = df.drop(columns=['bookId', 'isbn', 'firstPublishDate',
                 'setting', 'coverImg', 'bbeScore', 'bbeVotes', 'price'])
    df['description'] = df['description'].apply(lambda x: '' if pd.isna(x) else x)

    # initalize 
    vectorizer = TfidfVectorizer(max_features=1000)
    ipca = IncrementalPCA(n_components=2, batch_size=1000)
    
    chunk_size = 10000  
    num_chunks = len(df["description"]) // chunk_size + 1
    
    
    # in a for loop, vectorize and find the incremental PCA's 
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(df["description"]))
        chunk = (df["description"])[start_idx:end_idx]
    
        X_chunk = vectorizer.fit_transform(chunk)
    
        ipca.partial_fit(X_chunk.toarray())
        
    # initalize
    X_pca = np.empty((0, 2))
    
    # in a for loop, transfrom the chunk
    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = min((i + 1) * chunk_size, len(df["description"]))
        chunk = (df["description"])[start_idx:end_idx]
    
        # vectorize the chunk
        X_chunk = vectorizer.transform(chunk)
        

        # transform the chunk using incremental PCA
        X_chunk_pca = ipca.transform(X_chunk.toarray())
        X_pca = np.vstack((X_pca, X_chunk_pca))
    
    # add pca's to dataframe
    df[["pca1", "pca2"]] = X_pca
    

    # set a reasonable value of K 
    K = 9
    
    # find the centroids 
    centroids = df.sample(K)[["pca1", "pca2"]]
    centroids = [(df.iloc[i]["pca1"], df.iloc[i]["pca2"])
                 for i in range(len(centroids))]
    
    # assign each point to a cnetroid
    assignments = assign_centroids(df, centroids, x="pca1", y="pca2")
    df["cluster"] = assignments
    
    # colors
    color = np.select([df["cluster"] == 0, df["cluster"] == 1, 
                       df["cluster"] == 2, df["cluster"] == 3,
                       df["cluster"] == 4, df["cluster"] == 5, df["cluster"] 
                       == 6, df["cluster"] == 7,  df["cluster"] == 8] ,
                      ["green", "navy", "pink", "purple", "black", "orange", 
                       "brown", "blue", "gray"])
    
    
    # plot 
    plt.scatter(df["pca1"], df["pca2"], c=color, s=5)
    plt.title("KMeans Clusters after PCA")
    plt.xlabel('PCA1')
    plt.ylabel('PCA2') 

    # ask the user to choose a book and find the row number
    book = input("Choose a book: ")
    filtered_rows = df[df['title'].str.contains(book)]
    row_wanted = filtered_rows.iloc[0]
    cluster_num = row_wanted['cluster']

    cluster = df.at[cluster_num, 'cluster']
    
    # create a list of similar books 
    similar_books = []
    for i in range(len(df['cluster'])):
        if (df['cluster'][i]) == cluster:
            similar_books.append(df['title'][i])

    # choose a random book from the list 
    random_book = random.choice(similar_books)  
    position = df['title'].tolist().index(random_book)
    value = df.iloc[position]['description']
    author = df.iloc[position]['author']

    # print its title, author, and description
    print(f"You should read: {random_book} by {author}")
    print(f"This description of this book: {value}")



# call the main function
if __name__ == "__main__":
    main()
    
    

