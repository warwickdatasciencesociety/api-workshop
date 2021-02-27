# WDSS API Workshop - Flask App - Part 2

## Task
- Set up GET and POST endpoints for general tables
- Set up GET, PUT, and DELETE endpoints for specific records
- Try and explore the newgrades route

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

## Set up GET, PUT and DELETE endpoints for specific records of tables

1. The skeleton code provided also gives the route for record-specific GET, PUT and DELETE endpoints. In similar fashion to the above GET, try and fill out the record-specific GET.
2. Remember to test this, either using your browser or the `http` command on your command-line! For example, `http -f GET http://localhost:5000/api/student/2` should return information about the student with ID 2.
3. I would then advise trying the delete endpoint. By specifying the table and ID, it should remove the record with the ID given from the table, so that a subsequent GET request for the information would fail, or a GET request for the whole table will not have the record in it anymore.
4. Finally, try and implement the PUT endpoint. This one is tough, since you will need to check what fields have been provided (and thusly need updating).
5. You should now be familiar enough with your `http` command (or any other service you're using to test your API endpoints) to be able to sufficiently check your endpoints are working. However, if you have any issues, let me know or consult the relevant documentation!

## Try and explore the newgrades route

1. You'll see in your `app.py` that there is a `/newgrades` route. This demonstrates how we can use HTML forms to pass data to and from endpoints. It also will provide a more user-friendly interface for someone to enter a grade, since remembering the IDs for each student is not very human-friendly!
2. Have a look and play around with the interaction between `app.py` and `templates/new.html`, and try to understand what it does. This is an example of the interaction between a backend and frontend through the use of an API, which is very prevalent in a lot of online services and web apps.
3. When you're ready, move onto part 3.

## Check out WDSS
Warwick Data Science Society (WDSS) is focused on bridging the gap between disciplines to help all students answer the questions that matter to them. Through our talks, teaching and research we aim to educate and inspire everyone about data science. For example: we are running a cloud computing workshop next week, as well as running a social media speaker series featuring guests from Facebook, Snapchat and LadBible.

Keep up to date through our Facebook: https://link.wdss.io/facebook
