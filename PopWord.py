import twitter
from geopy.geocoders import OpenMapQuest
from wordnik import *
#can't be a preposition. Nouns only
#reduce goecode calls to find city locations every time
#categories
#can't enter the word itself in
#map out density of word in different cities
#no repeats
places = ['Los Angeles, CA', 'Denver, CO', 'New York City, New York', 'Chicago, IL', 'Houston, TX', 'San Diego, CA']
cities = dict()
keepPlaying = True
usedWords = list()
#creates a list of category and let's user select form the list
def intro():
    io = open("intro.txt", "r")
    data = io.readlines()
    for line in data:
        print line
    io.close()

def selectCategory(api):
    try:
        global trends
        trends = api.GetTrendsWoeid(id = 23424977,exclude = 'hashtags')
    except:
        print "ASCII error"
    counter = 1
    for trend in trends:
        print counter , trend.name
        counter +=1 
    select = int(raw_input ("Enter the number of the category you wish to play"))
    return select - 1

    
#creates dictionary
def createDict(geo):
    for city in places:
        addr, (latitude, longitude) = geo.geocode(city)
        cities[city] = (latitude, longitude)
#checks that input was a noun
def word(wordApi, category):
    proper_word = False
    while not(proper_word):
        word = raw_input("Enter a word: ")
        noun = wordApi.reverseDictionary(word, includePartOfSpeech = 'noun').results
        if not noun:
            print "please enter a noun"
        elif word in category:
            print "Good idea, but no."
        elif word in usedWords:
            print "Please enter a noun you haven't used yet."
        elif len(word) <= 1:
            print "Enter a word that is longer than one character."
        else:
            proper_word = True
        usedWords.append(word)
    return word
        

#plays the game
'''
    args: api(str), geo(geopy api), wordApi(wordniks api)
'''
def play(api, geo, wordApi, category):
    score = 0
    keepPlaying = True
    usr_input = ""
    tries = 0
    while keepPlaying and tries < 3:
        usr_input = word(wordApi, category)
        for city in cities:
            (latitude, longitude) = cities[city]
            tweets = api.GetSearch(term = category, geocode = (latitude, longitude,'500km'),count=1000)
            for tweet in tweets:
                    if usr_input in tweet.text:
                        print tweet.text
                        print city
                        print "\n"
                        score += 1
                        
        print "Current Score:", score
        print "Current Word:", category
        print "Tries: ", tries + 1
        if tries <= 2:            
            user_input = raw_input("(C)ontinue or (Q)uit")
            if user_input.lower() == 'q':
                keepPlaying = False
            elif user_input.lower() == 'c':
                keepPlaying = True
                tries += 1
    return score
            
#sets up api and calls methods
def main():
    #twitter api key
    consumer_key = 'XXXXXX'
    consumer_secret = 'XXXX'
    access_token = 'XXXXX'
    access_token_secret = 'XXXX'
    api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)
    #wordnik api
    apiUrl = 'http://api.wordnik.com/v4'
    apiKey = 'XXXX'
    client = swagger.ApiClient(apiKey, apiUrl)
    wordApi = WordsApi.WordsApi(client)
    
    geoLocator = OpenMapQuest()
    #creates dictionary
    createDict(geoLocator)
    intro()
    selection = selectCategory(api)
    category = trends[selection].name
    final =  play(api, geoLocator, wordApi, category)
    print "Final Score:", final
main()
