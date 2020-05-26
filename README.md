# PicsGallary
PicsGallery is a django application that allows users display their photos for others to see.

#### Author
> Dolphine Atieno

## Setup Instructions:
##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/Atienodolphine01/Picsgallery.git
   ```
 or download a zip file of the project from github

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ``` 

#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] View different photos that interest me.
- [X] Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
- [X] Search for different categories of photos. (ie. Travel, Food)
- [X] Copy a link to the photo to share with my friends.
- [X] View photos based on the location they were taken.


## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request

## LICENSE
[LICENSE](license)


__Copyright (c) {2020} AtyenohD.__

## Contacts
Reach me on:
>awuordolphine65@gmail.com