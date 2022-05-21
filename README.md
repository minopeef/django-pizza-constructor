# Pizza-constructor

Pizza-constructor is a Django app to constructor your own pizza from available options and ingredients. Order it. And
receive a confirmation by email.

This basic web app is just an example of a Django application with the ability to send emails.

## Live example

View demo [on heroku](https://pizza-constructor.herokuapp.com/).

## Usage

If you want to run this application locally, you need to follow the steps below:

1. To be able to send emails from the app you need an email account. If you choose Google, you need to
   configure [Sign in with App Passwords]( https://support.google.com/accounts/answer/185833?hl=en) for this account.
2. Then provide your email and password from email account into environment variables `EMAIL_HOST_USER`
   and `EMAIL_HOST_PASSWORD`.
3. Activate virtual environment
4. Install dependencies `pip install -r requirements.txt`
5. Run in the terminal `python manage.py migrate`.
6. Run in the terminal `python manage.py loaddata ./pizza_app/fixtures/initial_data.json`.
7. Create superuser in the terminal `python manage.py createsuperuser`.
8. Start the development server by running the command `python manage.py runserver`.
9. Go to `http://127.0.0.1:8000/`.

## Ideas for improvement

- make the home page responsive for mobile users.
- custom 404 page.
