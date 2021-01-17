# pyreact
This is python react project

# Creating django project
## Backend
```
django-admin startproject pyreactbkend
```
### Running django project
```
python manage.py startapp todo
python manage.py migrate
python manage.py runserver
```
> `Step-1`: Registering the todo application

Setup for the backend to recognise `todo` app
Let’s start with the more advanced things like registering the todo application as an installed app so that Django can recognise it. Open the backend/settings.py file and update the INSTALLED_APPS
```
# backend/settings.py

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo' # add this
  ]
```
> `Step-2`: Defining the Todo model at `todo/models.py` 

The completed property is the status of a task; a task will either be completed or not completed at any time. Because we have created a Todo model, we need to create a migration file and apply the changes to the database, so let’s run these commands:
```
python manage.py makemigrations todo
python manage.py migrate todo
```
>`Step-3`: Register your model in `todo/admin.py`
>`Step-4`: Create a super user
```
python manage.py createsuperuser

# Username (leave blank to use 'xxxxxx'):
# Email address: xxxxxx@gmail.com
# Password:
# Password (again):
# Superuser created successfully.
```
>`Step-5`: Add `localhost:3000` to whitelist in `todo/settings.py`
```
CORS_ORIGIN_WHITELIST = (
     'localhost:3000/'
 )
```
> `Step-6`: Create serializers for the Todo model `todo/serializers.py`



## Frontend
`Step-1`: Install create-react-app unsing npm
```
npm install -g create-react-app
```
### Create frontend app using reactJs
```
create-react-app frontend
cd frontend
npm run eject
```


# FRONT END Documentation -- GK

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
