# WDSS API Workshop Part One Extension
  
## Task
- Set up GET and POST endpoints for a permanent database
- Set up GET, PUT and DELETE endpoints for a permanent database

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

## Interested in learning more?
This workshop was designed to give a brief intro into using APIs, as well as building them. As a result there is still a lot left uncovered and the possibilties of what you can do with them are endless.

If you would like get a better understanding of how OAuth works, Spotify has some great documentation outlining its process: https://developer.spotify.com/documentation/general/guides/authorization-guide/
