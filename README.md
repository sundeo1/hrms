# Human Resource Management System

Run `git clone https://github.com/sundeo1/hrms` to clone the project onto your machine

# Backend

Found in folder hrms_backend

   Run the command `cd hrms/hrms_backend` to go to the backend directory

# Setting Up

1. Create `local.py in hrms/env/local.py ` to override settings like databases and sms keys to match your local env.
   You can use the example provided in `hrms/env/local-example.py`.

   For testing purposes, you can use `db.sqlite` as a database

2. For the SMS service to run to receive the verification code, you can get a free API key at https://www.infobip.com/signup?signup_source=InfobipProductPageSMS to use for the

   ```
   SMS_BASE_URL
   SMS_API_KEY
   ```

   variables.

3. Starting the project

    - Shell setup
    - 
      run these commands from project root after setting up a python virtual environment
        ```
        pip install -r requirements.txt
        python manage.py migrate

        python manage.py runserver
        
        ```

4. Access the API Documentation at http://127.0.0.1:8000/docs/ and the api at http://127.0.0.1:8000/api in your browser


# Frontend

Found in folder hrms_frontend

run the command 

   ```
   cd ..
   cd hrms_frontend
   ```

to go to the frontend directory

# Set Up

1. Create a .env file in the root of the hrms_frontend folder and set the value to the `REACT_APP_API_BASE_URL` variable to point to the url where the backend is running
   for example `REACT_APP_API_BASE_URL="http://localhost:8000/api"`
   if backend is running on localhost

2. Run the following commands from project root 

```

npm install
npm start

```

3. Access the frontend at http://127.0.0.1:3000 in your browser

