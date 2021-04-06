# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN cd app
RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install
# copy entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh


# run entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
