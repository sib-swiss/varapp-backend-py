
python3 manage.py migrate
python3 manage.py loaddata resources/dumps/init/demo_data.json

mod_wsgi-docker-start varmed/wsgi.py --processes 2 --threads 5
