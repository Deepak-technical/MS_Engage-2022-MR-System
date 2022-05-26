from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, render_template, request,redirect,session,url_for
from flask_mongoengine import *
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

import bs4 as bs
import pandas as pd

from flask_mongoengine import MongoEngine 
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
 
app = Flask(__name__)


app.secret_key = "msengage2020moviedesk"
# Database Connection MongodbAtlas 
app.config['MONGODB_SETTINGS'] = {
    'host': 
"mongodb+srv://deepak:deepakprasad@cluster0.bhnka.mongodb.net/Movie-DESK?retryWrites=true&w=majority"
,
    
}
db = MongoEngine()
db.init_app(app)

# Schema of DataBase Document
 
class User(db.Document):
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    reg_date = db.DateTimeField(datetime.now)
    session=db.StringField()
    genre=db.ListField()


    
# User signup page
@app.route('/signup',methods=['POST','GET'])
def signUp():  
 
    today = datetime.today()    
    
    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
            users = User.objects(email=_email).first()
            if not users:
                usersave = User(name=_name, email=_email, password=_hashed_password, reg_date=today)
                usersave.save()

                return  redirect('/login')
            else:
                msg = f"It seems that {_email} You have already Registered"
            
                return render_template('signup.html',msg=msg)
        else:
            msg="Please enter email address & required details"
            render_template("signup.html", msg=msg)
    else:
        return render_template("signup.html")
 

#User Login Page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       
        # Get Form Fields
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
        # Get user by username
        users = User.objects(email=_username).count() 
        print(users) # result 1
        if users > 0:
            # Get stored hash
            user_rs = User.objects(email=_username).first()
            password = user_rs['password']
            print(password)
            # Compare Passwords 
            if check_password_hash(password, _password):
                # Passed
                session['sessionusername'] = user_rs['name']
                return redirect('/')
            else:
                error = "Invalid Login / Check Your Username And Password"
                return render_template('login.html', errormsg=error)
        else:
            error = "No User Exists"
            return render_template('login.html', errormsg=error)
    
    return render_template('login.html')
     

#Logout session
 
@app.route('/logout')
def logout():
    session.pop('sessionusername', None)
    return redirect('/')

# Home page
@app.route("/")

def home():
    # Checking user is logged or not
    if not session.get('sessionusername'):
        suggestions = get_suggestions()
        return render_template('home1.html',suggestions=suggestions)
    else:
        #if logged in the displaying the intrest of user 
        # i.e which type of movie does user like or seems watched more
        
        #fetching user data from data base
        session_id= session['sessionusername']
        user_g=User.objects(name=session_id)
        list2=[]
        for u in user_g:
            list2.append((u.genre))
        suggestions = get_suggestions()
        count_movie=np.array(list2)[0]
        
        
  
        df = pd.DataFrame({
            "A":count_movie
            
        })
        # Sorting the user type of movie searched(genere) based on the frequency and 
        # sorting in  descending order and dispalying top 5 most searched movie type
        freq =dict((df.groupby(['A']).size()/df['A'].count()*100).round(2).astype(float))
        freq2=sorted(freq.items(), key=lambda kv: kv[1],reverse=True)[:5]
        print(freq2)
        return render_template('home1.html',suggestions=suggestions,result=dict(freq2))
        


    
      

def create_similarity():
    data = pd.read_csv('final_data.csv')
    # creating a count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(data['comb'])
    # creating a similarity score matrix
    similarity = cosine_similarity(count_matrix)
    return data,similarity

def recommended(m):
    m = m.lower()
    try:
        data.head()
        similarity.shape
    except:
        data, similarity = create_similarity()
    if m not in data['movie_title'].unique():
        return('Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies')
    else:
        i = data.loc[data['movie_title']==m].index[0]
        # excluding first item since it is the requested movie itself
        lst = list(enumerate(similarity[i]))
        # Sorting the similar movie using sorting algorithm using 
        # inbuild python sorting algorithm (Tim Sort)
        # on basis of smallest cosine similarty values on the top of the list
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)
        lst = lst[1:11]

        # saving user search movie on the user schema
        if not session.get('sessionusername'):
            pass
        else:

            session_id= session['sessionusername']
            movie_data=data.loc[data['movie_title']==m]
            movie_genere=movie_data['genres']
            g=movie_genere.to_numpy()[0]
            User.objects(name=session_id).update(push__genre=g)


        l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l   


  
        

  
        
# converting list of string to list (eg. "["abc","def"]" to ["abc","def"])
def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')
    my_list[-1] = my_list[-1].replace('"]','')
    return my_list

def get_suggestions():
    data = pd.read_csv('main_data.csv')
    return list(data['movie_title'].str.capitalize())




@app.route("/similarity",methods=["POST"])
def similarity():
    movie = request.form['name']
    recome = recommended(movie)
    if type(recome)==type('string'):
        return recome
    else:
        m_str="---".join(recome)
        return m_str


@app.route("/movie_recommended",methods=["POST"])
def recommend():
    # getting data from AJAX request
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    # get movie suggestions for auto complete
    suggestions = get_suggestions()

    # call the convert_to_list function for every string that needs to be converted to list
    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)
    
    # convert string to list (eg. "[1,2,3]" to [1,2,3])
    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","")
    cast_ids[-1] = cast_ids[-1].replace("]","")
    
    # rendering the string to python string
    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\"','\"')
    
    # combining multiple lists as a dictionary which can be passed to the html file so that it can be processed easily and the order of information will be preserved
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    
    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

    cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}

   

    

    # passing all the data to the html file
    return render_template('movie_recommended.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_cards,casts=casts,cast_details=cast_details)


if __name__ == '__main__':

    app.run(debug=True)
