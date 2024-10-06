# Human Resource Management System

# Backend

Found in folder hrms_backend


# Installation

Run the following commands from project root (preferably in a virtualenv)

```
cd hrms_backend
pip install -r requirements.txt
python manage.py migrate

```

# Development

1. Create `local.py in hrms/env/local.py ` to override settings like databases and sms keys to match your local env.
   You can use the example provided in `hrms/env/local-example.py`

2. Starting the project

    - Shell setup
      run these commands from project root 
        ```
        cd hrms_backend
        python manage.py runserver
        python manage.py rqworker iras_email_queue iras_sms_queue
        ```

3. Access the API Documentation at http://127.0.0.1:8000/docs/ and the backend at http://127.0.0.1:8000/admin/ in your browser


# Frontend

Found in folder hrms_frontend


# Installation
1. Create a .env file in the hrms_frontend folder and set the value to the `REACT_APP_API_BASE_URL` variable to point to the url where the backend is running for example `REACT_APP_API_BASE_URL="http://localhost:8000/api"` if backend is running on localhost

2. Run the following commands from project root 

```
cd hrms_frontend
npm install
npm start

```

3. Access the frontend at http://127.0.0.1:3000 in your browser

