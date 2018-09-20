# Notes

### Flask setup

```
sudo apt-get install python3-venv
python3 -m venv venv
. venv/bin/activate
pip3 install --upgrade pip
pip3 install flask
pip3 install python-dotenv
```

### Virtual environment

#### Settings
After installaton of *python-dotenv* create .env file with following lines

```
FLASK_APP=1-task_1.py
FLASK_ENV=development
FLASK_RUN_PORT=8000
VERY_SECRET_KEY=qwerty
```

#### Commands
```
. venv/bin/activate     # to enter venv
deactivate              # to exit
```
