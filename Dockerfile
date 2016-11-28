FROM python:alpine
COPY . /usr/src/ytviewer
WORKDIR /usr/src/ytviewer

# Upgrade apk, install latest https certs.
RUN apk --update upgrade && \
    apk add ca-certificates && \
    update-ca-certificates

# install requirements for app.
RUN pip install -r requirements.txt

EXPOSE 53627

CMD [ "python3", "app.py" ]
