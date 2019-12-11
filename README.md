https://docs.google.com/presentation/d/1RjkNUI4BVYoT0clRnXZObMbO2OmpbApUUo3wm4cVACA/edit#slide=id.g6c317da12d_1_1 presentation (presentation)

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
The purpose of this project was "to create a CRUD application with utilisation of supporting tools, methodologies and technologies" as part of my training at the QA academy to become a devops engineer. I have demonstrated my understanding of the devops techonologies I have learnt about 5 weeks into the training through creating a photography blog. Here users will be able to create an account and use this to post photos. 

I have met the basic CRUD fuctionality by; 

CREATE: Create a post, create and account

READ: Read the post displayed on the home.html page

UPDATE: Update users account

DELETE: Delete users account

At the moment, the blog fully encapsulates the devops tools I have learnt about, such as Jenkins, gunicorn and GCP.However due to time constraints it only covers the basic functionalities. Since submitting the project, I am going to increase the complexity of the application to further demonstrate my capabilites as a devops engineer. 

## User Stories

For this project, I have decided to make the application for my friend who is a photographer; this is to help me practice working in a real-life client scenario. In my meetings with my client, he explained to me about how he wanted a way to display his photos as a way to gain work as a professional photographer as shown in the photo below;

[Imgur](https://i.imgur.com/6P4WxuW.jpg)>

 
 Therefore, the user story is;
 
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

# Risk Assessment









# Testing

https://docs.google.com/document/d/1yJpHZXc18xZkpWp1crAIHZvsWIVXAcPJCufaC9ORrjw/edit?usp=sharing

Pytest was used for the unit testing. Overall the coverage was 41% and the coverage for the testing folder was 100%. All three unit tests were passed. 

# Future Improvements 
- Increase the complexity of the database to allow users to filter photos by continents and themes
- Front-End web design 
- Intergration testing using Selenium
- Create an actual link for the photo by converting the string format of the URL input to a URL for the image which can be displayed in the Posts section. 

