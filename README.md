### HealthCareBackend API Doc

#	1.	Set up a Python environment:
        sudo apt install pip
        pip install -r requirements.txt
        sudo apt install python3.10-venv
        python -m venv .env 
        source .env/bin/activate


#	2.	Install requirements:

        pip install -r requirements.txt 
        pip install gunicorn


#	3.	Migrate and initialize the database:

        python manage.py makemigrations
        python manage.py migrate


#	4.	Collect static files:

        python manage.py collectstatic


#	5.	Create superuser:

        python manage.py createsuperuser


#	6.	start server:
         gunicorn --bind 0.0.0.0:8000 HealthCareProject.wsgi:application
