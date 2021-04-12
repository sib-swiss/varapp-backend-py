FROM grahamdumpleton/mod-wsgi-docker:python-3.4-onbuild

RUN mv /app/varmed/settings/settings_docker.py /app/varmed/settings/settings.py
RUN apt-get update
RUN apt-get install -y redis-server
RUN python3 setup.py install

EXPOSE 80
ENTRYPOINT ["/bin/bash"]

CMD ["/app/start.sh"]
