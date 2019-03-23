FROM python:3.6-slim
MAINTAINER Jan Pivarnik

# - dependencies for mysqlclient
#   default-libmysqlclient-dev, gcc

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PORT 8000
ENV APP_DIR /opt/project
ENV PYTHONUNBUFFERED 1

COPY pip.conf /root/.pip/
RUN pip3 install pipenv

EXPOSE ${PORT}

RUN mkdir -p ${APP_DIR}
WORKDIR ${APP_DIR}
COPY Pipfile* ./
RUN pipenv install --system --three

WORKDIR ${APP_DIR}
COPY . ${APP_DIR}

ENTRYPOINT ["/opt/project/start_app.sh", "-r"]
