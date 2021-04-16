FROM grahamdumpleton/mod-wsgi-docker:python-3.4

WORKDIR /app
COPY . /app
RUN mod_wsgi-docker-build

COPY ./docker/settings_docker.py /app/varmed/settings/settings.py
RUN python3 setup.py install

EXPOSE 80
ENTRYPOINT ["/bin/bash"]

CMD ["/app/start.sh"]
