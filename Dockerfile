FROM python:alpine
COPY . /usr/src/ytviewer
WORKDIR /usr/src/ytviewer

# Upgrade apk, install latest https certs.
RUN apk --update upgrade && \
    apk add ca-certificates && \
    update-ca-certificates

# install requirements for app.
RUN pip install -r requirements.txt

# install gunicorn
RUN pip install gunicorn

EXPOSE 53628

CMD [ "/usr/local/bin/gunicorn", "-b", ":53628", "-w", "4", "-t", "0", "--reload", "-p", "ytviewer.pid", "app:app" ]
