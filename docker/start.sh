
# Create users database schema
python3 manage.py migrate

# Only load demo data the first time we mount the mysql volume
if [ ! -f "/var/lib/mysql/INITIALIZED" ]; then
  python3 manage.py loaddata resources/dumps/init/demo_data.json
  touch /var/lib/mysql/INITIALIZED
fi

mod_wsgi-docker-start varmed/wsgi.py --processes 2 --threads 5
