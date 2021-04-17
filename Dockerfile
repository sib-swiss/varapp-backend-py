FROM grahamdumpleton/mod-wsgi-docker:python-3.4

WORKDIR /app
COPY . /app

# Install dependencies and configure black magic stuff
RUN mod_wsgi-docker-build

# Replace settings with docker-specific ones
COPY docker/settings.py /app/varmed/settings/settings.py

# Build the rest of dependencies, in particular the C extensions
RUN python3 setup.py install

EXPOSE 80
ENTRYPOINT ["/bin/bash"]

CMD ["/app/start.sh"]
