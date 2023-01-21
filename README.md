# BoilermakeX TweetEQ
## Made by Calvin Madsen, Pravar Annadanam, John Slater, and Aadit Bennur.

##
### From the frontend, we allow the user to meet the team, interact with and learn the project idea.
### On the main page, the user can enter a keyword and a time range to run a query and gather data.
### When the user submits the query, it gets fed into the python script that goes uses the twitter api. From the twitter api, there are tweets with the keyword in the time frame gathered and sent to the algorithm.
##
## The algorithm:
### We used tensorflow, trained it on a natural language database, and got it to analyze sentiment.
### It takes tweets and returns one of 6 sentiments: joy, sadness, anger, surprise, love, and fear based on its analysis of the sentence(s).
### With this data, we compile it and send it to the python script which reads it and formats it such that we can display a pie chart on the site of the results of the 6 sentiments that we get back.
##

##Purposes:
### Possible can be used by individuals and companies to see recent trends and the general perception of them, their business, or some keyword that they want to search for. 

##
## Future Endeavors:
### The next steps would be to train the model more given more time and more data. Furthermore, on the frontend, creating a way for users to export data would help. Finally, and most importantly to language on twitter, would be to integrate emojis into the overall processing of the algorithm
