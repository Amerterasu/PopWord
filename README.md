# PopWord

#### Description
A game about how well you know the trends in your area. Given a trending topic you must enter a single noun that is most likely to be found in the same tweet as the topic. You are given one point each time the noun is used. Text based game game. Made with Python. I've removed my personal API's in the 

#### Requirements
* Python Twitter API KEY
* Wordnik API KEY
* openMapQuest API (Geopy)

#### How it Works
Using Geopy I can gain latitude and longitude of the major cities I've selected across America to search for the tweets in the trending category. Trending categories are received from the Twitter API. There are multiple checks on the user input to make sure that satisfies the following conditions: It's a noun, not the trending topic name itself, not a word that you've already entered, and finally that it's longer than one character('I', 'a', etc.) In order to check if it is a noun I used the Wordnik API. This api is essentially a dictionary and based on the word you enter it will do a serach in the Wordnik dictionary to find your entered word with the filter that its part of speech be a noun. If nothing is returned then you didn't enter a noun. Twitter API will reutrn all the tweets that pertain to the trending category. From that list search through the tweets and give a point to each time it matches user input.

#### Major Cities used to search for tweets:
* Los Angeles
* Denver (Colorado Represent!)
* New York City
* Chicago
* Houston
* San Diego

