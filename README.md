# Django REST Framework

This project is an [API](https://github.com/lucapwn/django-rest-framework) for user registration in CRUD format, which uses the [Django REST Framework](https://www.django-rest-framework.org/) for its operation.

![Badge](https://img.shields.io/static/v1?label=license&message=MIT&color=1E90FF)
![Badge](https://img.shields.io/static/v1?label=build&message=passing&color=00d110)

## Content

- [About](#about)
- [Routes](#routes)
- [Support](#support)
- [Running](#running)
- [Notes](#notes)
- [Screenshot](#screenshot)
- [Author](#author)
- [License](#license)

## About

Through this API (Application Programming Interface), you can perform a CRUD (Create, Read, Update and Delete) and access all HTTP methods of a Rest API to manipulate user data.

For added security, this application features [JWT](https://jwt.io/) authentication integration. In other words, to be able to access the routes of this API, you will need to be authenticated like our application [example](https://github.com/lucapwn/django-rest-framework/blob/main/example.py).

To perform authentication via JWT, we simply send the Django user and password in the request header to get the token for our authentication.

### Routes

Through the ```/users``` route we can register and get the users' data. These are the HTTP methods available for this route: ```GET```, ```POST```, ```HEAD``` and ```OPTIONS```.

Through the ```/users/<id>``` route we can delete and update user data. These are the HTTP methods available for this route: ```PUT``` and ```DELETE```. Where ```<id>``` is the ID of the user registered in the database.

## Support

This software is compatible with Windows and GNU/Linux operating systems.

I could not test it on macOS, but I believe it is functional as well.

## Running

Install the project dependencies:

~~~console
foo@bar:~$ pip3 install -r ./requirements.txt
~~~

Apply the changes to the database, create an administrator user and run the application:

~~~console
foo@bar:~$ python3 ./api/manage.py migrate
foo@bar:~$ python3 ./api/manage.py createsuperuser
foo@bar:~$ python3 ./api/manage.py runserver
~~~

Now you can run the example:

~~~console
foo@bar:~$ python3 ./example.py
~~~

After running the Django server, you can access the API interface at this address: [```http://127.0.0.1:8000/```](http://127.0.0.1:8000/.).

### Notes

The user and password you defined above should be used in JWT authentication, as per the [example](https://github.com/lucapwn/django-rest-framework/blob/c5a24bcc20e2003d34a66e001f02e5017e2053ca/example.py#L96):

~~~python3
api = API(username="admin", password="admin")
~~~~

To disable JWT authentication for this application, simply comment out line 9 of the [./api/users/api/viewsets.py](https://github.com/lucapwn/django-rest-framework/blob/c5a24bcc20e2003d34a66e001f02e5017e2053ca/api/users/api/viewsets.py#L9) file:

~~~python3
# permission_classes = (IsAuthenticated,)
~~~

## Screenshot

The image below illustrates the API interface.

![](https://lh3.googleusercontent.com/u/1/drive-viewer/AFDK6gPnlKNB0-Dn9ilQb1aE6J1C8e7CSW1G0-3-nR8hHd3WG4nBcT362nraKwclbOQ-rickMoTeULRUZHMqiyodQ_pj0Cal5w=w1920-h947)

## Author

Developed by [Lucas Araújo](https://github.com/lucapwn).

## License

This software is [MIT](https://choosealicense.com/licenses/mit/) licensed.
