# MorningMessenger
This project is meant to simplify my morning by sending me a text with a summary of the weather for the day as well as my tasks for the day. Texts are sent from a free Twilio number, daily tasks are managed through the Google Tasks API, and weather data is fetched from OpenWeather's API.

The main script can be found in `messenger.py`. Other files such as `text.py` are experimental samples, and `quickstart.py` is a setup script from Google which will be relevant for setup. I also have a `Dockerfile` set up for the project but it is quite overkill for such a simple script.

I have this script set up on an AWS EC2 instance, and automated the text sending process by setting up a cron job that calls the script at 9:30 every morning. My choice for these technologies were arbitrary as it was just something I wanted to learn, use whatever is most convenient for you!

## Setup
Before starting it's important to note that this project requires a python version >= 3.11 to be compatible will all the dependencies.

### Virutal Environment (Optional)
Running the project in a virtual environment may be ideal to avoid conflicts.

To create an environment, clone the repo and inside the directory run the following:

```
python -m venv env
```

**"env"** can be replaced with whatever you would like to name the environment.

After creating the environment run either of the following to activate the environment:

For Windows
```
env\Scripts\activate
```

For Unix or Mac OS
```
source env/bin/activate
```
### API Setup

Create a `.env` file in the project directory to hold all sensitive keys and tokens. Below is an example file and a list of everything needed.
```
    TWILIO_ACCOUNT_SID = ...
    TWILIO_AUTH_TOKEN = ...
    TWILIO_PHONE_NUMBER = ...
    PERSONAL_PHONE_NUMBER = ...
    OPEN_WEATHER_API_KEY = ...
```

All APIs used offer free tiers or free credits which is what I used, but I would caution to be weary of your usage and not accidentally go past your free tier limit. The signup and setup for [Twilio](https://www.twilio.com/en-us) and [Open Weather](https://openweathermap.org/api) are very straight forward and just require you to register an account and generate the needed phone number/keys. From Twilio, you'll need your Account SID, Auth Token, and the Twilio phone number you generate. From Open Weather, you'll just need your API key.

Google's setup is a bit more complicated. This quickstart guide is a good walkthrough to get setup https://developers.google.com/tasks/quickstart/python. The main things needed is a `credentials.json` file and a `token.json` file for API authentification. You'll get the credentials while setting up your project with Google and will need to copy the file to this project's directory, and the token file will be generated after running the quickstart script at the bottom of the page.
>Note: The `quickstart.py` script mentioned in the guide is already in copied this project directory  

### Install Dependencies

To install the required dependencies run the following either in the project directory or in a virtual environment:

```
pip install -r requirements.txt
```

## Run 
To run the program run the following either in the project directory or in a virtual environment:

```
python messenger.py
```

Or:
```
python3 messenger.py
```

## Docker

Again, docker is overkill for something so simple, but I did it for the practice.

Create a docker image of the program with:

```
docker build -t morningmessenger . 
```

To run the docker image:

```
docker run morningmessenger  
```