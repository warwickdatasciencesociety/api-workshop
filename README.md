# WDSS API Workshop - Flask App - Part 1

## Task
- Set up the Flask environment
- Create a "Hello world" endpoint

## Preqrequisites
- Have Python 3.x installed
- Basic understanding of python
- Basic terminal/command-line knowledge

## Setup
1. Install the dependencies listed in requirements.txt

	I recommend setting up a virtual environment in Python. All this does is isolate the dependencies so you don't get any weird issues but it's not needed to get things going.

	On OSX (Terminal), Linux (Terminal) or Windows (PowerShell/Command Prompt, preferably PowerShell) do the following:

	`pip3 install virutalenv`

	`python3 -m venv venv`

	`. venv/bin/activate`

	`pip3 install -r requirements.txt`

2. Start running Flask with the command `python3 app.py`. I recommend doing this in a dedicated window - each time you save `app.py` it will automatically regenerate the API and site. Then you can work on the code separately (note, you'll need to enter just `. venv/bin/activate` in any new terminal instance)

## Get Coding 
1. There is a task to create a / endpoint displaying a JSONified "hello world". Have a look at Flask routes and the jsonify class, and see if you can implement this.
2. Test that your solution works. Remember, `app.py` will automatically regenerate, so head over to http://localhost:5000/ and see if you get the same results as visiting http://wdssapiworkshop.herokuapp.com/
3. Move onto part 2.

## Check out WDSS
Warwick Data Science Society (WDSS) is focused on bridging the gap between disciplines to help all students answer the questions that matter to them. Through our talks, teaching and research we aim to educate and inspire everyone about data science. For example: we are running a cloud computing workshop next week, as well as running a social media speaker series featuring guests from Facebook, Snapchat and LadBible.

Keep up to date through our Facebook: https://link.wdss.io/facebook
