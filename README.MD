# Hurricane Relief PR

Puerto Rico se levanta with this REST API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3.6.0 to run the RESTAPI. We suggest you use the package virtualenv to install all dependencies
and run the server.

The Database Instance is postgresql. Please contact us for the schema.

```
virtualenv ENV
```


### Installing

When you clone this repository, install all the dependencies by:
```
pip install -r requirements.txt
```
### Running

Do the following to run said software:

```
set FLASK_APP=app.py
set FLASK_DEBUG=1
set DATABASE_URL=postgresql://appusr:appusr1@localhost/appdb
flask run
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](flask.pocoo.org/) - The web framework used
* [postgresql](https://www.postgresql.org/) - Database


## Acknowledgments

* Hat tip to ICOM5016
