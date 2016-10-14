from flask import render_template
from app import app
import csv

@app.route('/')
@app.route('/Home')
def home():
    return render_template("Home.html",
                           title='Home')

@app.route('/MakeaMatch')
def makeamatch():
    return render_template("MakeaMatch.html",
                           title='Make a Match!')

@app.route('/Game')
def game():
    return render_template("Game.html",
                           title='Game')

@app.route('/ListofDogs')
def listofdogs():
    return render_template("ListofDogs.html",
                           title='List of Dogs')
                           
@app.route('/About')
def about():
    return render_template("About.html",
                           title='About')
                           
@app.route('/Contact')
def contact():
    return render_template("Contact.html",
                           title='Contact')
                           
@app.route('/MatchResult')
def matchresult():
    class DogBreed:
        def __init__(self, br, per, si, lif, hou, cli):
            self.breed = br
            self.personality = per
            self.size = si
            self.lifestyle = lif
            self.housing = hou
            self.climate = cli
            self.match = 0

    #List that will contain class DogBreed
    ListOfBreeds = []

    data_file = open('app/static/Dog-Data.csv')
    csv_file = csv.reader(data_file)

    for row in csv_file:
        #print (row) #will print the csv file
        #print (row[2]) #will print element of that row
        dog_breed = DogBreed(row[0],row[1].lower().split(", "),row[2].lower(),row[3].lower(),row[4].lower(),row[5].lower())
        ListOfBreeds.append(dog_breed)

    data_file.close()

	    #query user for top 3 preferred dog personality
	    #uc_p1 = request.form['']
	    #uc_p2 = request.form['']
	    #uc_p3 = request.form['']
    uc_p1 = 'easygoing'    #sample user choice for testing
    uc_p2 = 'affectionate'
    uc_p3 = 'playful'
	    #query user for their preferred dog size
	    #uc_size = request.form['']
    uc_size = 'medium'    #sample user choice for testing
	    #query user for their lifestyle
	    #uc_lif = request.form['']
    uc_lif = 'moderate'    #sample user choice for testing    
	    #query user for their housing
	    #uc_hou = request.form['']
    uc_hou = 'apartment'    #sample user choice for testing 
	    #query user for their country's geographical temperature
	    #uc_cli = request.form['']
    uc_cli = 'either'    #sample user choice for testing


    #updates match points for every dog breeds in the list
    for dog_breed in ListOfBreeds:
        if (uc_p1 in dog_breed.personality):
            dog_breed.match += 12
        if (uc_p2 in dog_breed.personality):
            dog_breed.match += 10
        if (uc_p3 in dog_breed.personality):
            dog_breed.match += 8
        if (uc_size in dog_breed.size):
            dog_breed.match += 20
        if (uc_lif in dog_breed.lifestyle):
            dog_breed.match += 20
        if (uc_hou in dog_breed.housing) or ('either' in dog_breed.housing):
            dog_breed.match += 15
        if (uc_cli in dog_breed.climate) or ('either' in dog_breed.climate):
            dog_breed.match += 15
            

	#calculating the max match percentage
    ListOfMatch = []
    for temp in ListOfBreeds:
        ListOfMatch.append(temp.match)
    max_percentage = max(ListOfMatch)

	#print (max_percentage) #to test/see highest match point
	#print (ListOfMatch) #to test/see all dog breed match points

    ListOfDD = []

	#returns dog breeds that has this percentage
    for dream_dog in ListOfBreeds:
        if (dream_dog.match == max_percentage):
            #print (dream_dog.breed) to test/see the dog breed with highest match point
            ListOfDD.append(dream_dog)


    return render_template("MatchResult.html",
                           title='Match Result',
                           score=max_percentage,
                           posts=ListOfDD)
