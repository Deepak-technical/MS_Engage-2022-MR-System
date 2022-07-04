# MS_Engage-2022-Movie Recommendation  System
Movie -Desk is a interactive movie recommendation using ML algorithms &amp; sorting technique to display the best recommended movies on the users choice

This application provides all the details of the requested movie such as overview, genre, release date, rating, runtime, top cast, reviews, recommended movies, etc.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using beautifulsoup4 and performed sentiment analysis on those reviews.


# Features of Movie-Desk 

1. Giving Detail information about the movies (like Movie Name , rating , Duration, Status, genere , etc.)


2. Displaying the information about the top characters


3.Displaying Top 10 recommended movies to the user based on the genere of the movie selected


4.Language translation feature supported by Google translate into 256 languages


5.Knowing which type of  movie is user frequently searching  using  sorting and ranking

# How to run the project?


1. Clone or download this repository to your local machine.


2. Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt



Video Link:https://youtu.be/ENi62yUy_L0
3. Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key) OR It is provieded not need(if you want you can create it)
   Do not worry my api key is given so no need to install it


4. Replace YOUR_API_KEY in required places of static/recommend.js file and hit save.

   if you make own api key the !!! DO not add it is already given


5. Open your terminal/command prompt from your project directory and run the file app.py by executing the command python app.py.


6. Go to your browser and type http://127.0.0.1:5000/ in the address bar.

# Architecture

![mx](https://user-images.githubusercontent.com/75557390/169880379-74b25d99-8aa4-4f80-9511-94c1c16c6b07.png)


# Description of this project is given in this Presentation
https://docs.google.com/presentation/d/1DT4Xyh6J7QULg_rsIkrIO15UMzX3nOU5/edit?usp=sharing&ouid=100521934796007286039&rtpof=true&sd=true


# Dataset 

Movie Dataset From kaggle

American Movies 2018 From Wikepedia by Web scrapping

American Movies 2019 From Wikepedia by Web scrapping

American Movies 2020 From Wikepedia by Web scrapping

American Movies 2021 From Wikepedia by Web scrapping




