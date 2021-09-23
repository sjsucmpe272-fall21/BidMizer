# Team-Project-16
# Proposal 1 : Worldwide News
# Introduction
A news recommendation system which will recommend news based on the category selected by the user viz. Sports, Education, Entertainment.  
# Abstract
News dataset will be collected from various websites using NEWS API. In the data we get to know the category of news and we can classify it and categorize it. After the user selects to read a particular category’s news the backend will find the most relevant and latest news using Machine Learning algorithms. The web app will be deployed using Docker.
# Approach
Using NEWS API we get data in JSON format with header and description. Using the category selected by the user we find most relevant news using K-Means, Naive Bayes algorithm. For the front end we will be using Flask/DJANGO  and finally we Dockerize it.
# Persona
People can get news of their interests divided into categories. 
# Dataset Links 
We will be using the NEWS API or news-please library of python for extracting the news from various websites using web scraping. 



# Proposal 2 : Team formation Assistant
# Introduction
Build an assistant which will take the project requirements, team members availability, skill level, preferred tools, etc. as input and assign the members to the new team.
# Abstract
We are planning to implement an assistant which will help in forming teams based on the specific requirements. The requirements for team formation will be collected on an online form and with the help of machine learning clustering algorithm teams will be generated based on the inputs provided by users and results will be displayed
# Approach
We will be using python ML libraries for clustering algorithms. Data of the team members will be stored in Mysql database. Front end implementation will be done using html,javascript where in a form will be presented to the user to collect the required data to form teams and the final list of teams will be displayed on the dashboard.
# Persona
Team formation assistant will help people to build a team with members having diversified areas of expertise and skill set.
# Dataset links
We will be using dummy data to test the team formation assistance. Data will be entered through a form which will be stored in the mysql database from where it will be used to train and test the ML algorithm.




# Proposal 3 : Music Preference
# Introduction
A music recommendation web app that suggests music suited to the weather around the user, their current mood and preferred genre
# Abstract
We will build a music recommendation application that recommends music to the user based on the preferences they give. The requirements for this are the weather of the user's location,  user’s current mood and his favorite music genre. Based on the inputs we will make use of Machine Learning algorithms and Spotify API, we will display music which fits the user’s mood and also can help the user discover new music.
# Approach
We will be using python ML libraries for ML algorithms. The user’s preferences  will be stored in the Mysql database. Front end implementation will be done using html, css and javascript. We will make use of Spotify API for displaying music and we will use the geolocation API to get the user’s location.
# Persona
People can listen to music based on their preferences and can also learn about new song suggestions that suit their taste.
# Dataset links
For our dataset we will use a million song dataset.

