https://docs.google.com/presentation/d/1RjkNUI4BVYoT0clRnXZObMbO2OmpbApUUo3wm4cVACA/edit#slide=id.g6c317da12d_1_1 presentation 

http://34.89.6.5:8080  (jenkins)

http://35.235.54.226:5000     (app)


http://34.89.6.5:5000/coverage  (coverage report)


**Table of Contents**

* [The Brief](#the-brief)

* [User Stories](#user-stories)

* [Architecture](#architecture)

* [CI Pipeline](#CI-Pipeline)

* [Future Improvements](#Future-Improvements)


# The Brief
"To create a CRUD application with utilisation of supporting tools, methodologies and technologies that encapsulate all core modules covered during training."

To demonstrate this I will be creating a photography blog page where users can create an account and post thier photos.

CREATE: Create a post, create and account
READ: Read the post displayed on the home.html page
UPDATE: Update users account
DELETE: Delete users account 

## User Stories
***As a*** photographer 

***I want*** a website where I can share my photos 

***So that*** I can gain attraction for my work and get inspiration from the photography community

## Trello Board

https://trello.com/b/4V7C4Paj


# Architecture 
## Database Structure
The tables in grey were not implemented and the tables in white were implemented. The next stage would be to create a many to many reationship between a themes table anf the users allowing the user to filter out photo by themes.

https://docs.google.com/document/d/1yJpHZXc18xZkpWp1crAIHZvsWIVXAcPJCufaC9ORrjw/edit?usp=sharing


# CI Pipeline
Source Code; Python
Version Control System; Git
Project Tracking; Trello
CI Server; Jenkins
Testing Environment; Pytest (on GCP)
As live Environment; GCP

# Testing

https://docs.google.com/document/d/1yJpHZXc18xZkpWp1crAIHZvsWIVXAcPJCufaC9ORrjw/edit?usp=sharing

Pytest was used for the unit testing. Overall the coverage was 41% and the coverage for the testing folder was 100%. All three unit tests were passed. 

# Future Improvements 
- Increase the complexity of the database to allow users to filter photos by continents and themes
- Front-End web design 
- Intergration testing using Selenium
- Create an actual link for the photo by converting the string format of the URL input to a URL for the image which can be displayed in the Posts section. 

