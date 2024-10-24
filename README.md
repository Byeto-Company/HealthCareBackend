### HealthCareBackend API Doc

# 1. Set up a Python environment:
   ```bash
   sudo apt install pip
   pip install -r requirements.txt
   sudo apt install python3.10-venv
   python -m venv .env 
   source .env/bin/activate
   ```

# 2. Install requirements:
   ```bash
   pip install -r requirements.txt 
   pip install gunicorn
   ```

# 3. Migrate and initialize the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

# 4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

# 5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

# 6. Start server manually:
   ```bash
   gunicorn --bind 0.0.0.0:8000 HealthCareProject.wsgi:application
   ```

# 7. Configure Gunicorn to start on server boot:

To have Gunicorn automatically start when the server boots, create a systemd service file:

1. **Create the service file:**

   ```bash
   sudo nano /etc/systemd/system/gunicorn.service
   ```

2. **Add the following content to the file:**

   ```ini
   [Unit]
   Description=Gunicorn instance to serve HealthCareProject
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/root/HealthCareBackend
   ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 HealthCareProject.wsgi:application

   [Install]
   WantedBy=multi-user.target
   ```

   - Adjust `WorkingDirectory` to the path of your project.
   - Ensure the correct path to Gunicorn (`/usr/bin/gunicorn`).

3. **Reload systemd and enable the service:**

   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start gunicorn
   sudo systemctl enable gunicorn
   ```

4. **Check the status of the Gunicorn service:**

   ```bash
   sudo systemctl status gunicorn
   ```

Now, Gunicorn will automatically start on server reboot.
