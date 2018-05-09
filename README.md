# Allevi Coding Challenge!

### Prompt:
"Using this dataset, we would like you to build a web application using any stack you are comfortable with to build a tool for our customers and for our internal team to analyze print information and results. We'll leave the details of the application up to you and what you think would be important for the users of the application. Send us your final code on Github and we'll take a look at what you built!"

I built a simple website using Django's Python Webframework. Print data is stored in a SQLite database locally. The tables displaying print data I simply created with CSS, and the labled graphs are generated using the Google Charts JS API. I used Bootstrap as a base CSS style and added onto it as necessary.

### Features:

- View general statistics on the homepage (User statistics, average print statistics)
- Search for a user
- - - View statistics for each user at /search/user/{email}
- Search for a device serial number
- - - NOT COMPLETED! You can search for a serial number and you will be redirected accordingly, but all it will do is tell you your search term.

### Notes:
The data was computer generated, so the numbers are a little boring (100 users each with 100 prints), but with the way the site it set up you could continuously update the database with new entries and all pages would update instantly.

## RUN INSTRUCTIONS:
1. Download the source into a directory.
2. In the root directory, run these commands:
> $ python manage.py makedb
> $ python manage.py runserver
3. View the page by navigating in browser to "localhost:8000/"


## Usage Instructions:
On the homepage, you will see three accordion sections.
__User Statistics__ will display the number of registed users and the average number of prints all users have completed.
__Average Statistics__ shows some high-level data about every print job ever completed
__Best Of__ displays a list of the 100 best prints (where "best" means "highest live percentage")

Search for a user by typing their email (ex: user0@gmail.com) into the search bar under the "User" setting. This will take you to user0's statistics page. Here you will immediately see their name, their # of completed prints, and the number of printers they own. The accordion sections below list this user's 10 most successful prints as well as their full print history respectively.

You may return to the homepage by clicking the Allevi logo in the header.

