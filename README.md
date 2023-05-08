# Chat Flask
## For debug in local server
First you need to copy this repository to your computer.<br>
##### Download and unzip or with git: 
`git clone https://github.com/DerFacn/chat_flask.git`
##### Create and setup venv:
After downloading/cloning enter the chat_flask directory and run in terminal next: 

`python -m venv venv`  - creating python virtual environment 

`venv\Scripts\Activate` - activate virtual environment 

`pip install -r requirements.txt` - install requirements packages, which need for the app 

`python run.py` - create database with models for app 

`flask --app=app run --debug --host=0.0.0.0` - run application on the local server

**DON'T FORGET SET UP YOUR SECRET KEY IN `__init__.py`**