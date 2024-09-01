# Install Python

Check to see if you already have Python installed on your system by running:

On a Mac:
`python3 --version`

On Windows:
`python --version`

If you already have Python installed, check to be sure it’s Python 3.8 or up. (For example, 3.11 is great!) We suggest waiting on 3.12 to give any dependencies time to be updated.

If you are using a Windows machine, it is possible that you don’t have Python installed. You’ll need to pause here for a moment and proceed to install it. See this document for more [information](https://docs.google.com/document/d/14diNu_g6uhouBscRt8zIezolANTRQA6HobKRP4Lgu5Q/copy).

# Setting up to run scripts to work with Python.

The script will be run in a virtual environment. Start by creating a virtual environment. Navigate to to the project folder in the command line and run:

On a Mac:
`python3 -m venv venv`

On Windows:
`python -m venv venv`

<br>
After creating the virtual environment, you need to activate it:

On a Mac:
`source venv/bin/activate`

On Windows:
`source venv/Scripts/activate`

<br>
Once the virtual environment is activated, the beginning of your terminal prompt should display (venv).

<br>
Install the modules by running (in both a Mac and Windows):

`pip install matplotlib requests pandas seaborn`

You'll see a venv folder has been added to the directory with all of the installed dependencies.

<br>

The scripts in this class can by run with these commands:

On a Mac:
`python3 <filename>`

On Windows:
`python <filename>`

For instance, to run the code in the main.py file the command would be:

On a Mac:
`python3 main.py`

On Windows:
`python main.py`

And to run the solution code:

On a Mac:
`python3 solution.py`

On Windows:
`python solution.py`

<br>

When finished, close the virtual environment by running:

`deactivate`

<br>

Each of the folders has been named for the lesson. So some of the folder names are verrrry long! To make navigating the folders in the command line easier be sure to use the tab key. Start with `cd` and a space. Then type the first few letters of the lesson's folder and hit the tab key. The remainder of the name should appear. If there's more than one option, continue to tab until the right folder appears.

During the class you'll run the same commands repeatedly. In the command line you can scroll through the list of commands you've previously run using the up and down arrow keys in the bottom right of your keyboard. So much faster!

<br>
