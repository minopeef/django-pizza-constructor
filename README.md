# Pizza-constructor

Pizza-constructor is a Django app to constructor your own pizza from available ingredients. Then order it. And recieve a confirmation by email.

## Live example

View demo [here at heroku](https://pizza-constructor.herokuapp.com/)

## Quick start

1. Activate virtual environment
2. Configure Gmail account and allow login from less secure apps.
3. Provide your Email and Password in environment variables or in settings.py file.
4. Install dependencies `pip install -r requirements.txt`
5. Run in the terminal `python manage.py migrate`.
6. Create superuser in the terminal `python manage.py createsuperuser`.
7. Start the development server by running the command `python manage.py runserver`
8. Open your web browser and visit http://127.0.0.1:8000/
9. Populate db with your options and toppings.

## Ideas for improvements

- design models schema to follow ACID properties
- make home page responsive for mobile users.
- do not allow more then 500 grams of toppings per pizza.
- calculate order price not only on the back end, but also on the client side.
