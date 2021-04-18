# Crisis Management System
The Crisis Management System is an information exchange portal in which a variety of stakeholders are able to share data, policies and communicate with users regarding the COVID-19 pandemic.

## Installation

First install django by running:

	$ pip install django

Clone the repository from Github and switch to the new directory:

	$ git clone git@github.com/looloo223/SEproject.git 
	$ cd SEproject/seproject

Install project dependencies:

	$ pip install -r requirements.txt

Then simply apply the migrations:

	$ python manage.py migrate

You can now run the development server:

	$ python manage.py runserver
  
## User Usage

Open http://127.0.0.1:8000 in web browser. <br/><br/>

★	Click the site's Login button to login or navigate to Register page. <br/>
★	View Covid-19 statistics with the website's Dashboard page. <br/> <br/>

★	User the navigation bar on the top of the page to view Contact Information and FAQ pages. <br/>
★	Use the menu on the side of the page to access Policies, Operations, Technologies, Forum, or Symptom Screener pages. <br/>

★	On Forum page, select the catagory of forums to view or make a post under. <br/>
Select "New Discussion" on category forum page to create new post. <br/>
Select forum posts to Like or reply to it. <br/> <br/>

★	Sort the forum posts under each category by newest, oldest, or number of likes by using sort button on each categor page. <br/>
★	View the posts made by the account logged in my selecting the hypertext username visible in the user portlet. <br/>
★	Logout by selecting the "Logout" button located on the navigation bar. <br/>

## Admin Usage
Create a superuser by running:

  	$ python manage.py createsuperuser
  
Access the admin dashboard for the website by opening http://127.0.0.1:8000/admin in web browser and logging in with superuser information. <br/> <br/>

★	View list of users by selecting "Users". <br/>
Select a user to access the user's "Change user". <br/>
Use this page to edit each user's first and last name, email address, permissions, and groups. <br/> <br/>

★	View list of groups by selecting "Groups". <br/>
Use this page to edit permission for each group. <br/> <br/>

★	View list of Forum posts by selecting "Forums". <br/>
Use this page to edit each forum posts contributor name, topic, section, description, likecount, dislikecount, users that have liked this post, and determine wheter the post is made by a health or technology expert. <br/><br/>

★	View list of Forum posts by selecting "Forums". <br/>
Use this page to edit each forum posts forum name, discussing content, contributor name, and determine wheter the post is made by a health or technology expert. <br/><br/>

## Future Ideas

★	Implementing a user profile page to display all of a user's information and include a profile picture. <br/>
★	Allowing a database to store page information so admins can edit information without going into a pages's html file.

## Authors
George Laney <br/>
Rebecca Mitchell <br/>
Troy Peterson <br/>
Devarian Tarver <br/>
Randy Griffin <br/>

## Project Status
Completed
