# HoodNews
  A web application that allows a user to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Author
Fredrick Wambua

## User Stories
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Set up and Installation Requirements
### Prerequisites
- python 3.8
- django
- pipenv (for creating virtual environment)
- dotenv

ng the api endpoints

## Cloning the repository
- Fork the repository
```
$ git clone https://github.com/FredrickWambua/hoodnews
```
- Navigate to the repository.
### Running the application
- Creating virtual environment
```
$ python3 pipenv shell
$ pip freeze > requirements.txt
$ . .env
```
- Runing application
```
$ make server 
$ make makemigrations (this creates database migrations)
$ make migrate (this performs migrations)
$ make createsuperuser
```
- Posting as an admin
Navigate to the admin site by adding /admin to the site url and log in as a super user with your created credentials. You can now post and view the posts on the browser.

## Deployment
View the working deployed application [here](https://hoodcatchupnews.herokuapp.com/)
Follow [heroku documentation](https://devcenter.heroku.com/articles/git) to know more about deploying app to heroku.

## License
Copyright 2021 Fredrick Wambua

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
