# Football Player App
_This is my readme file for my football player webApp._

## Minimum Viable Product

With this being my first project, I am not expecting everything to go perfectly to plan and I understand that there will be times when I get stuck on certain areas. With this in mind I need to set the standard for the minimum viable product. This will be the absolute minimum that I intend to finish and have fully working by the time the project is due.
I will be using the MoSCoW method of planning so that I can look at everything I must, probably should, could and would do - if time and skill forbid it. I will be using Trello, which I have posted the link to under the 'Trello' header in this ReadMe file. This will help me in many ways. Firstly, it will help me to get everything out of my head on what I potentially could do with it to make it an amazing product. This will allow me to acknowledge that I could do this in the future, but given time and my current ability, it's probably not a good idea right now. This could be something like adding login information to the application.
I will dissect from the rest everything that I must compelete to be able to fullfill the breif. This includes:
- Having at least two tables within the database which have relationships with one another.
- Plan the tables relationships using ERD(s) 
- Give the user the ability to Create, Read, Update and Delete (CRUD) data from the tables.
- Plan for any potential risks (risk assessment)
- Deploy the app through a VM
- It has to be fully functional.

<br>

<br>

### ***Trello Board***

[Trello Link](https://trello.com/b/uFsnH9Cw/fantasy-football-python)

![Trello Board Day 1](/Misc_Files/images/OriginalTrelloBoard.jpg)

![Trello Board End of Day 2](/Misc_Files/images/TrelloBoard_eod2.jpg)

<br>

<br>

## ***User Stories***

As a user, I want to be able to create a player so I can build my player list.

As a user, I want to be able to view my player list.

As a user, I want to be able to change the name of my players in the list so that I can change it up.

As a user, when I am editing the players name I also want to be able to change the position of the player so that I can see what positions all of the players play in.

As a user, I need to be able to delete any player incase I have made a mistake.

<br>

<br>

## ***Acceptance Criteria***


Given the user is on the home page. When I click on 'Add Player', it then takes the user to the add player screen.

Given the user is now on the add player screen and when they type in the text box provided and they then click the 'add player' button. It then adds the player to the database.

Given the user has just added a player. They can now click on the 'Player List' page and see that their added player is in their list.

Given the user has just pressed 'Edit Player' the user will be taken to the 'edit player' screen. When the user changes the players name and hits the 'Change Name' button, the players name has been changed.

Given the player is on the 'Edit Player' page, they can select a new position for their player. However this does not currently save.

Given the player is on the 'Player List' page, they can view all of their changes made.

Given the player is on the 'Player List' page, and they click delete on one of their players. The player will be deleted from the database.

<br>

<br>


## _What does the user need to do with the minimum viable product?_


When the user lands on the webapp, on the player list page, they will see that there are no players currently in the list.

The user can then go and create some players using the create players page.

Once the user has create a player (or multiple) they can return to the player list page and see the changes that they have made.

The user should then be able to edit the player, by clicking the 'edit player' button. This will take them to the updates page where they can change the name of the player and also change the position of the player. 

The user can also delete players from the 'Player List' page.

<br>

<br>

## Definition of Ready (DoR)

- Player list should display an empty page with tabs at the top to enter the 'add player' page. 
- User can create a player name 
- User can edit the player name
- User can edit the player position
- Players appear in a list on the 'Player List' page
- user can delete a player

Once this list is complete, it will contain all CRUD features, as examples; creating the player(C), showing the players on the screen(R), update the players information(U) and deleting players(D).

<br>

## Relational Database

In this project I will be using a MySQL on GCP as well as the sqlite for local usage. sqlite will be helpful for initial testing to get my app functional. It is essential that I move onto GCP using the MySQL database there so that I can then move my app online and link it with a virtual machine and then with Jenkins. 

![ERD-V1](/Misc_Files/images/ERD_1.jpg)

![ERD-V2](/Misc_Files/images/ERD_2.jpg)

![ERD-V3](/Misc_Files/images/ERD_3.jpg)

<!-- ![(mvp)_ERD_002](https://user-images.githubusercontent.com/82821511/118515163-0a59ca00-b72d-11eb-97f9-638a48539e23.png) -->

As you can see from the above images, I have created 3 very different ERDs. The reason for this is because I created the first one around a week before I started this project and I overestimated my abiliy a by good ammount. I also added practically everything I thought could be a good idea for a fully functioning Fantasy Football application. This was a great idea at the time, but the closer I got to starting the project I was realising more and more that I wasn't be realistic at all.

This is when I came up with the second version, much more simple than the first ERD, and focussed on the core assets of a football squad builder. 

However, after starting the project I realised that how much harder it is to code and to fully understand what I am coding without using tutorials and demos. Whereas before, I thought I understood how to do most things quite well, but I quickly realised that maybe I hadn't understood as much as I thought I had. It was either this or I have just panicked and got into my own head saying that I'm not good enough to do this.

The final version of the ERD contains everything that I need for the minimum viable product for this project. A relational database and full CRUD capability. Looking back I would have chosen something much more simple from the start rather than wasting around half a day trying to plan out how I am going to write each bit of code and where it's going to go in the project. But that is what this project is partly for I think.


Documentation

I will talk about what I intend the app to do and how here.
Talk about:
- The architecture of the project.
- The Risk Assesment undertaken.

![ProjectArchitexture](/Mic_Files/ERD/ci-pipeline.jpg)

![CRUDProject_RiskAssessment](/Misc_Files/Risk_Management/updated-risk-assessment.jpg)


## Fully Functional CRUD Application

The fully functional version of my CRUD app will be in the main branch in this GitHub Repository.
I have set up a dev branch so I can ensure that everything is working before making any changes to the main branch.


## Testing

I have completed some unit testing as well as 1 integration test. 


![Unit Testing Results](/Misc_Files/Testing/Unit_Testing(67pc).jpg)

![Integration Test File](/Misc_Files/Testing/Integration_testing_test-file.jpg)

![Integration Test Results](/Misc_Files/Testing/Integration_testing.jpg)


As you can see from the images above, I have completed some unit testing receiving an 87% completion rate. I have tested to make sure that the user can add a player to the database. I then test to ensure that the user can see a player they have created in the database on the home page. Finally I have tested to check that the user can delete a player. Going forward to increase my completion rate, I need to test to ensure that the user can update the players name and also to see if they can change the players position.


For the integration testing I have checked to see if the user can go from one webpage to another. I have checked this by using the XPath of the link to the add player page. As you can see from the images above, this test passed, along with the basic test of ensuring that the server is up and running.


## What have I used?

- Trello
- Database: GCP MySQL Server.
- Programming language: Python
- Unit Testing with Python (Pytest)
- Integration Testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version Control: Git
- CI Server: Jenkins
- Cloud server: GCP Compute Engine




