# WDSS API Workshop Part One Extension
  
## Task
- Set up GET and POST endpoints for a permanent database
- Set up GET, PUT and DELETE endpoints for a permanent database
- Explore the newgrades route

## Preqrequisites

- Have Python 3.x installed
- Basic understanding of python
- Basic terminal knowledge or how to install/run python without a terminal  
- Basic understanding of relational databases and SQL

## Setting up the endpoints
1. You'll see that the code has been populated with lots of new imports and database-specific configurations. In a real web-app, you'll want to store your data changes permanently. SQL is the dominant industry database interaction language, and it pairs well with an API and web-app.
2. Have a look at the code and try and understand it. Then, try to recreate the endpoints of part 2, with database interaction this time! (Hint: the `sqlalchemy` documentation will be your friend for this)
3. If you ever corrupt your database, navigate to the `scripts` folder and run the python file in there.
4. Use your endpoint-testing application to test the endpoints as normal.
5. Well done! You have created a RESTful API which interacts with a database in Flask. If you're feeling adventurous, move onto the extension to add some security to it!

## Try and explore the newgrades route

1. You'll see in your `app.py` that there is a `/newgrades` route. This demonstrates how we can use HTML forms to pass data to and from endpoints. It also will provide a more user-friendly interface for someone to enter a grade, since remembering the IDs for each student is not very human-friendly!
2. Have a look and play around with the interaction between `app.py` and `templates/new.html`, and try to understand what it does. This is an example of the interaction between a backend and frontend through the use of an API, which is very prevalent in a lot of online services and web apps.
3. When you're ready, move onto part 3.

## Check out WDSS
Warwick Data Science Society (WDSS) is focused on bridging the gap between disciplines to help all students answer the questions that matter to them. Through our talks, teaching and research we aim to educate and inspire everyone about data science. For example: we are running a cloud computing workshop next week, as well as running a social media speaker series featuring guests from Facebook, Snapchat and LadBible.

Keep up to date through our Facebook: https://link.wdss.io/facebook
