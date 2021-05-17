# Fantasy_Football_App
This is the readme.md file for my Fantasy Football webApp.

CRUD App.

The requirements of the project are as follows:

A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.

A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.

Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.

A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board

Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.

A functioning front-end website and integrated API's, using Flask.
Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

You should consider the concept of MVP (Minimum Viable Product) as you
plan your project, completing all the requirements above before you add
extra functionality that is not specified above.


Trello Board

https://trello.com/b/uFsnH9Cw/fantasy-football-python


User Stories

What does the user need to do with the minimum viable product?

When the user lands on the webapp, they will be greeted "Welcome to the fantasy football app" and will be asked to enter their manager name. This can be anything they like including using symbols.
Once they have inputted their manager name, they will be able to see the formation (4-4-2) selected for them as I have chosen for the minimum viable product (mvp). They will then have the chance to select players, using buttons on the screen to filter the players. For the mvp, I will just be filtering using positions, as there isn't going to be that many players to choose from at first.
Once they have selected 11 players (using the formation as a guid - 1 goalkeeper, 4 defenders, 4 midfielders, 2 attackers) they will then be able to view their starting 11 in the 'Squads' page. 
Now that they have selected their squad, they can update it by changing players. They will also be able to update their managers name.
If they aren't happy and want to start again, of course, they can delete their team too start again.


Relational Database

Say what databases I will be using.
MySQL


![(mvp)_ERD_002](https://user-images.githubusercontent.com/82821511/118515163-0a59ca00-b72d-11eb-97f9-638a48539e23.png)



Talk about the minimum required and the minimum I will deliver.


Documentation

I will talk about what I intend the app to do and how here.
Talk about:
- The architecture of the project.
- The Risk Assesment undertaken.

[CRUDProject_RiskAssessment.xlsx](https://github.com/MattColemann72/Fantasy_Football_App/files/6495308/CRUDProject_RiskAssessment.xlsx)


Minimum Viable Product Needs:
Formation:
-   Will store 1 formation (4-4-2) - Isn't an essential part of the project to have more 
Players:
-   Will add players to the database from a variety of clubs to choose from (minimum of 2 per position (taking into account formations))
-   All players will have 1 position
User Name (Manager Name):
-   Takes the Users name so that it can be used as the managers name.
Squad:
-   I need the squad to display the first 11 (XII) - As the minimum requirement I won't include the subs.

Minimum Viable Table Relationships:
- Squad is going to consist of primarily foreign keys. 
-   Manager names
-   Player names
-   Player Positions
-   Player club
-   When assigning a player check to see if another player has already taken that position
-   Formation

Minimum Viable Visuals:
- I want to be able to have the players in a position that will sort of resemble the formation. But for the minimum requirement, they will just be shown in a list format.
-   I will be creating default layouts in the html files for the different formations - This should easily be expndable in the future using CSS3 to show formations rather than just a list.
-   Also the name of the manager (user) will be displayed at the top of the squad page. For example "Matt's XII"


Fully Functional CRUD Application

The fully functional version of my CRUD app will be in the main branch in this GitHub Repository.
I have set up a dev branch so I can ensure that everything is working before making any changes to the main branch.


Testing

I will be creating a test functions to ensure that everything is working exactly how it is supposed to and so that the testing is automatic.
As well as this I will also be performing basic tests on the WebApp so that I can double check to see that everything is working right in the front-end view.


What will I be using?

- Python, Flask, MySQL, PyMySQL, GCP, Jenkins etc...
- Kanban Board: Trello or an equivalent Kanban Board
- Database: GCP SQL Server or other Cloud Hosted managed Database.
- Programming language: Python
- Unit Testing with Python (Pytest)
- Integration Testing with Python (Selenium)
- Front-end: Flask (HTML)
- Version Control: Git
- CI Server: Jenkins
- Cloud server: GCP Compute Engine


Minimum Viable Product

With this being my first project, I am not expecting everything to go perfectly to plan and I understand that there will be times when I get stuck on certain areas. With this in mind I need to set the standard for the minimum viable product. This will be the absolute minimum that I intend to finish and have fully working by the time the project is due.
I will be using the MoSCoW method of planning so that I can look at everything I must, probably should, could and would do - if time and skill forbid it. I will be using Trello, which I have posted the link to under the 'Trello' header in this ReadMe file. This will help me in many ways. Firstly, it will help me to get everything out of my head on what I potentially could do with it to make it an amazing product. This will allow me to acknowledge that I could do this in the future, but given time and my current ability, it's probably not a good idea right now. This could be something like adding login information to the application.
I will dissect from the rest everything that I must compelete to be able to fullfill the breif. This includes:
- Having at least two tables within the database which have relationships with one another.
- Plan the tables relationships using ERD(s) 
- Give the user the ability to Create, Read, Update and Delete (CRUD) data from the tables.
- Plan for any potential risks (risk assessment)
- Deploy the app through a VM
- It has to be fully functional.

Once the breif has been satisified, I can start to make it look more presentable and add more functions and tables to the project and database.


Presentation

Present my work using slides and demo the app?
