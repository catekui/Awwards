# Awwards

## AWWARDS 
#### <div dir="rtl">By **Catherine Wangui**</div>

## Description
A web application to post websites and other web projects as well as review posted projects.

## Features
* Users create an account.
* Users can log in to application and view other peoples projects once they have an account.
* Users can view other users' profiles and their projects.
* Users can search projects by title.
* Users can upload and post their projects.
* Users can view their profiles and edit their profile pictures and bio.
* Users can review and post a review on other users' projects.

# Specifications

## BDD
| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Users can sign up for an account | Input credentials in the registration form then click Sign Up | Users are prompted to login into their account |
| Users can view projects posted by other users | Click on a specific project's review button | When clicked, users are navigated to another page where they can post a review of the project |
| Users can view the full live site of a posted project | Click on the 'Go to Site' button | Users are directed to the live site of the posted project |
| Users can view and edit their profiles | Click on profile in the side navigation | Users are directed to their profile page with their posted projects displayed as well as their profile information and an option to edit it |
| Users can search projects | Click on the search icon on the navigation bar, type in a given project-title and press Enter | User will be able to view projects with that title |


## Setup/Installation Requirements
Here is a run through of how to set up the application:
* Step 1 : Clone this repository using the git clone link:
  * **`git clone https://github.com/catekui/Awwards.git`**
* Step 2 : Navigate to the directory:
  * **`cd Awwards`**
* Step 3 : Open the directory created with your favorite IDE. If Atom type **`atom .`** if VSCode type **`code .`** . This will launch the editor with the project setup,
* Now feel free to hack around the project.

## Getting started
### Prerequisites
* python
* virtual environment
* pip

### Cloning
* In your terminal:

       $ git clone https://github.com/catekui/Awwards

## Running the Application
* Install virtual environment using `$ python3 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3 pip install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations photos
        $ python3 manage.py migrate 

* To run the application, in your terminal:

        $ python3 manage.py runserver
        
## Testing the Application
* To run the tests for the class file:

        $ python3 manage.py test photos
        
## Technologies Used
- Python 
- Django MVC framework
- HTML, CSS and Bootstrap
- Postgressql
- Heroku

### License
[MITlicense](LICENSE) 2021 