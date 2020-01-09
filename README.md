# Pizza-constructor

Pizza-constructor is a Django app to constructor your own pizza from available options and ingredients. Order it. And receive a confirmation by email.

## Live example

View demo [here at heroku](https://pizza-constructor.herokuapp.com/)

## Usage

1. To be able to send emails from the app you need a Gmail account. Also, do not forget to allow login from less secure apps in your Gmail account.
2. Provide your Email and Password from Gmail account in environment variables or in settings.py file.
3. Activate virtual environment
4. Install dependencies `pip install -r requirements.txt`
5. Run in the terminal `python manage.py migrate`.
6. Create superuser in the terminal `python manage.py createsuperuser`.
7. Start the development server by running the command `python manage.py runserver`
8. Open your web browser and visit http://127.0.0.1:8000/
9. Populate sqlite3 database with your options and toppings.

## Ideas for improvement

- design models schema to follow ACID properties
- make the home page responsive for mobile users.
- do not allow more than 500 grams of toppings per pizza.
- calculate the order price not only on the back end but also on the client-side.
