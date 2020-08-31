# (Sn)Ack Bot

> A simple slack bot application to help your team communicate

This is Flask + Vue.js application.

In addition it utilizes:
- Bootstrap for UI components.
- SQL Alchemy as an ORM.
- Flask Admin.
- Blueprint for API creation.
- Pytest for unit testing


## Backend Flask Setup
This part might work w/out the other parts...
``` bash
# Check if you got python3
python --version
python3 --version

brew install python3

# Get pipenv
brew install pipenv

pip install Flask
```

## Trouble shooting - Maaaybe setup Python and Pip and all 
Run with Python3 and Pip3. 
``` bash
# Get me some pip3 installed
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

pip3.8 --version
```

Suggested linking python > python3 and pip > pip3. Add to your .zshrc or .bashrc file:
``` bash
alias python=python3
alias pip=pip3.8
```

Check it and install flask:
``` bash
source .zshrc
python --version
pip --version

pip install Flask

pip install python-dotenv

pipenv run flask db init 
pipenv run flask migrate
```

To run the development server using pipenv:
```
pipenv run flask run
```

## Frontend Vue.js Build Setup

Make sure you have node and npm ... need yarn. Install the Vue CLI:
``` bash
node --version # v13.12.0 should be good on OSX

brew install npm
brew install yarn

yarn global add @vue/cli
```

Then everything for the app should be hot:
``` bash
cd <path to app>
```

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Lints and fixes files
```
yarn lint
```

## Troubleshooting - ESLint issues
``` bash
yarn add -D eslint eslint-plugin-vue
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


## General Helful Stuff
``` bash
# Install Heroku CLI
brew tap heroku/brew && brew install heroku

# Tail Heroku Logs
heroku logs --tail
```


## Run ngrok for slack event api when no domain
``` bash
# Get and run ngrok sevice with same port as app
./ngrok http 5000

# Set request URL on the slack api setting. https://api.slack.com/apps/.../event-subscriptions with ngrok URL.
```


## Run celery worker
``` bash
# Run redis server
sudo systemctl restart redis.service

# Run celery worker
celery worker -A app.services.slack.celery --loglevel=info --pool=solo
```
