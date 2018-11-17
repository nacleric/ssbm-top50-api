# Melee Top50 H2H api
API that parses through Tafo H2H 2018 stats and converts it to json


## Getting Started
Set up your virtual environment (I personally use venv if you use to conda or virtualenv then it will be a bit different)
```
python3 -m venv env
source env/bin/activate
```
Install the packages
```
pip install -r requirements.txt
```
Create the env variable
```
export FLASK_APP=api.py
export FLASK_DEBUG=1
```
Install the packages
```
pip install -r requirements.txt
```
Run the api
```
flask run
```
### Notes
-melee.py contains the function to query the csv file
-api.py is the main flask app
-clean.py cleans tafo's data (currently only turns everything to lowercase)
-will try to decrease the amount of manual changes and add them to clean.py


### Manual csv changes
-removed the first 2 columns that contained their past and current ranks 
-added underscores to peoples names with spaces
-removed the last columns about SET COUNT 

### Built With
* Flask

### Future Plans 
Would like to support top50 placings in the future and lower the amount of manual changes


