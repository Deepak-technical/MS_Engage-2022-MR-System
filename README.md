# MS_Engage-2022-Movie Recommendation  System
A interactive movie recommendation using ML algorithms &amp; sorting technique to display the best recommended movies on the users choice

This application provides all the details of the requested movie such as overview, genre, release date, rating, runtime, top cast, reviews, recommended movies, etc.

The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, I did web scraping to get the reviews given by the user in the IMDB site using beautifulsoup4 and performed sentiment analysis on those reviews.


Features of Movie-Desk 

Giving Detail information about the movies (like Movie Name , rating , Duration, Status, genere , etc.)


Displaying the information about the top characters


Displaying Top 10 recommended movies to the user based on the genere of the movie selected


Language translation feature supported by Google translate into 256 languages


Knowing which type of  movie is user frequently searching  using  sorting and ranking

How to run the project?


Clone or download this repository to your local machine.


Install all the libraries mentioned in the requirements.txt file with the command pip install -r requirements.txt


Get your API key from https://www.themoviedb.org/. (Refer the above section on how to get the API key) OR It is provieded not need(if you want you can create it)


Replace YOUR_API_KEY in both the places (line no. 15 and 29) of static/recommend.js file and hit save.


Open your terminal/command prompt from your project directory and run the file main.py by executing the command python main.py.


Go to your browser and type http://127.0.0.1:5000/ in the address bar.





