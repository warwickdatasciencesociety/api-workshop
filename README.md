# WDSS API Workshop

You have reached the codebase for WDSS's API workshop. Here is some useful info if you get stuck with navigating the repository

## Workbooks
Here are the links to the workbook and solutions for the first task!
- Workbook: https://colab.research.google.com/drive/1eMEuAanjYz8JCUICieNXg_Y--6V4zDbD?usp=sharing
- Solutions: https://colab.research.google.com/drive/1cwDEzRl2Vff9v5UJNMBlx1ltf5wgdeX-?usp=sharing

## Branches
If you are not familiar with `git`, you may find it easier to manually navigate to each branch to get the code changes. Simply click the tree-like logo (currently selected at `master`), and use the dropdown to navigate to the branch of your choice. The following branches correspond to the following topics:

- `notebook-extension` corresponds to part 1 extension, sending an e-mail using the gmail API
- `notebook-solution` corresponds to the solution to the above
- `flask-partx` corresponds to the different parts of the creation of the flask app (in order)
- `flask-extension` provides the extension to the flask app task
- `flask-solution` provides the final flask solution

## Venv
`venv` will be very useful for ensuring that, despite which environment you have Python installed on, the code you run will run on any device inside the `venv` environment. Below are some useful commands you might need to use:

- `pip3 install virtualenv` to install `venv` to Python (only needed to be done once)
- `python3 -m venv venv` to set up the virtual environment folder (only needed to be done once) 
- `. venv/bin/activate` to enter the virtual environment
- `deactivate` to exit the virtual environment
- `pip3 install -r requirements.txt` to install libraries inside the virtual environment (need to be in the `venv`)

## Git
Using `git` will be very useful for progressing through this workshop, since it will allow you to keep your apps and environments running whilst the code itself changes from branch to branch. It is also very useful (and ubiquitous) in any software development context. Here are some useful `git` commands:

- `git clone https://insert-git-url-here.git` to download the repository (codebase) to your local current working directory
- `git add .` followed by `git commit -m "Insert useful progress message here"` to "save" your changes locally - you may need to initially set up git credentials, by following the messages given if these commands fail
- `git checkout origin/insert-branch-name-here` followed by `git checkout insert-branch-name-here` to move to another branch

## Check out WDSS

Warwick Data Science Society (WDSS) is focused on bridging the gap between disciplines to help all students answer the questions that matter to them. Through our talks, teaching and research we aim to educate and inspire everyone about data science. For example: we are running a cloud computing workshop next week, as well as running a social media speaker series featuring guests from Facebook, Snapchat and LadBible.

Keep up to date through our Facebook: https://link.wdss.io/facebook
