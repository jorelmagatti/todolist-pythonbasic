FROM python:3.11-slim-bullseye

ENV TZ=America/Sao_Paulo

RUN apt-get -qq update && apt-get -qqy install tzdata \
    && groupadd -g 1001 todouser \
    && mkdir -p /home/todouser \
    && useradd -g 1001 -G todouser -u 1001 todouser  \
    && chown todouser:todouser -R /home/todouser \
    && echo "$TZ" > /etc/timezone \
    && rm -f /etc/localtime \
    && ln -sf /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get -qqy install gcc make \
       pkg-config default-libmysqlclient-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN pip install --no-cache-dir 'poetry==1.6.1'

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry config installer.max-workers 10 \
    && poetry install --no-cache --no-interaction --no-ansi --no-root

COPY --chown=todouser:todouser todo_list /app/todo_list

WORKDIR /app

USER todouser

CMD ["uvicorn", "--host", "0.0.0.0", "todo_list.__main__:app"]
