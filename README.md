
# WDSS API Workshop Part One Extension

  
## Task
- Register to an OAuth API
- Send an email from your gmail address to your university address
## Preqrequisites

- Have Python 3.x installed
- Basic understanding of python
- Basic terminal knowledge or how to install/run python without a terminal  

## Setup

1. Clone the repository to your computer, if you're not familiar with git, feel free to download it as a zip

2. Install the dependencies listed in requirements.txt

	I recommend setting upa virtual environment in Python. All this does is isolate the dependencies so you don't get any weird issues but it's not needed to get things going.

	On OSX or Linux do the following:

	`pip3 install virutalenv`

	`python3 -m venv venv`

	`source /venv/venv/bin/activate`

	`pip3 install -r requirements.txt`
3.   Head to this link and hit the Enable the Gmail API button: https://developers.google.com/gmail/api/quickstart/python
	a. Enter "WDSS API Workshop" for the project name
	b. Select Desktop App
	c. Download the credentials.json file and replace the existing credentials.json file with it

*Please note this contains your client id and client secret. You should make sure to not expose this information otherwise people could maliciously use your credentials. *

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
