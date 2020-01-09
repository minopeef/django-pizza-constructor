# Pizza-constructor

Pizza-constructor is a Django app to constructor your own pizza from available ingredients. Then order it. And recieve a confirmation by email.

## Live example

View demo [here at heroku](https://https://pizza-constructor.herokuapp.com/)

## Quick start

1. Activate virtual environment
2. Configure Gmail account tp allow login from less secure apps.
3. Provide Email and Password in settings.py file
4. Run in the terminal `python manage.py migrate`.
5. Start the development server by running the command `python manage.py runserver`
6. Open your web browser and visit http://127.0.0.1:8000/

## Ideas for improvements

- design models schema to follow ACID properties
- make home page responsive for mobile users.
- do not allow more then 500 grams of toppings per pizza.
- calculate order price not only on the back end, but also on the client side.
