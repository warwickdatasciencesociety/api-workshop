# WDSS API Workshop - Flask App - Part 2

## Task
- Set up GET and POST endpoints for general tables
- Set up GET, PUT, and DELETE endpoints for specific records

## Preqrequisites

- Have Python 3.x installed
- Basic understanding of python
- Basic terminal knowledge or how to install/run python without a terminal

## Set up GET and POST endpoints for general tables

1. The skeleton code provided gives the route and GET and POST endpoints. It also provides a function to easily retrieve the next id from a JSON table.
2. Try the GET endpoint first. It needs to retrieve all of the records for a given table - in this example, `data` is the dictionary holding the tables (as lists of dictionaries).
3. Test the GET endpoint. In your browser, go to http://localhost:5000/api/student, then http://localhost:5000/api/course, then http://localhost:5000/grade and compare these with the same respective endpoints of http://wdssapiworkshop.herokuapp.com - you will see that whilst it is formatted slightly differently, the data retrieved is largely the same.
4. Now try the POST endpoint. This is trickier. You want to retrieve the form data (have a look at Flask `request` class), and then add the new record (with fields given in this form) to the data.
5. Test the POST endpoint using `httpie` (make sure you are in the environment). Type in the following command: `http -f POST http://localhost:5000/api/student f_name=John l_name=Smith`. It should return a success code, but more importantly, when you then try the GET endpoint again, your new student should be there. (Note: you can also issue a GET endpoint using httpie, but the browser does it for us when you type in the URL. The syntax for this would be `http -f GET http://localhost:5000/api/student`).

## Get Coding 
Follow the comments in the file to complete the task, if you get stuck you can consult the documentation, or look at the solutions branch on the repo.

The first time you run the code, you will be redirected to the Google OAuth page, it will say the developer is unregistered and poses a security risk but just advance as you're the developer! After this the credentials are stored locally so it does not need to make this request every time the program is run.

Also, don't worry if you don't understand what all the code is doing, as long as you have a general idea of how the API is being connected to and used that's great.

Once you think your program is ready to run, use the following command to run it:

 `python3 gmail.py`

 Have fun!
## Interested in learning more?
This workshop was designed to give a brief intro into using APIs, as well as building them. As a result there is still a lot left uncovered and the possibilties of what you can do with them are endless.

If you would like get a better understanding of how OAuth works, Spotify has some great documentation outlining its process: https://developer.spotify.com/documentation/general/guides/authorization-guide/
