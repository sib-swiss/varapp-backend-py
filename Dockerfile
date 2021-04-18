FROM grahamdumpleton/mod-wsgi-docker:python-3.4

WORKDIR /app
COPY . /app

# Install dependencies and configure black magic stuff
RUN mod_wsgi-docker-build

# Build the rest of dependencies, in particular the C extensions
RUN python3 setup.py install

# Move startup script to top level
COPY docker/start.sh /app/start.sh

EXPOSE 80
ENTRYPOINT ["/bin/bash"]

CMD ["/app/start.sh"]
