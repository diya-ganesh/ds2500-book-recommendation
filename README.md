# Book Recommendation System

This project, developed for the DS2500 course, is a book recommendation system that suggests books to users and visualizes similarities between books using various algorithms.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [API Key Setup](#api-key-setup)
- [Contributors](#contributors)

## Introduction

The Book Recommendation System employs algorithms such as K-Means clustering to analyze book data and provide personalized recommendations. It also generates visualizations to illustrate the relationships and similarities between different books.

## Features

- Personalized book recommendations based on user input.
- Visualization of book similarities using graphs.
- Implementation of K-Means clustering for grouping similar books.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/diya-ganesh/ds2500-book-recommendation.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd ds2500-book-recommendation
   ```

## Usage

1. **Run the recommendation script:**
   ```bash
   python api_recommendations.py
   ```
   This script provides book recommendations based on user input.

2. **Generate recommendation graphs:**
   ```bash
   python recommendation_graphs.py
   ```
   This script creates visualizations to display similarities between books.

3. **Apply K-Means clustering for recommendations:**
   ```bash
   python kmeans_recommendations.py
   ```
   This script uses K-Means clustering to group similar books and provide recommendations.

## Dependencies

Ensure that the following Python packages are installed:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

These can be installed using the `requirements.txt` file provided in the repository.

## API Key Setup

This project uses the [Books API7](https://rapidapi.com/akshithp111/api/books-api7) from RapidAPI to fetch book data. To use the API, follow these steps:

1. Visit the [Books API7](https://rapidapi.com/akshithp111/api/books-api7) page on RapidAPI.
2. Sign in or create an account on RapidAPI.
3. Subscribe to the API to get your API key.
4. Add the API key to the api_recommendations.py file. The file should look like this:
   ```env
   API_KEY=your_api_key_here
   ```
5. The scripts will automatically read the API key from the `.env` file.

## Contributors

- Diya Ganesh
- Diya Kadakia
- Deekshita Madhalam
