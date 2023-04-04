FROM python:3.10

ARG UID=3021
ARG GID=3021
RUN groupadd -g $GID -o aesop && useradd -m -u $UID -g $GID -o -r aesop

RUN mkdir /aesop && chown aesop:aesop /aesop
WORKDIR /aesop
RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY --chown=aesop:aesop ./pyproject.toml /aesop/pyproject.toml
COPY --chown=aesop:aesop ./poetry.lock /aesop/poetry.lock

RUN poetry install --only main
COPY --chown=aesop:aesop ./app /aesop/app

USER aesop
EXPOSE 3000

CMD [ \
    "uvicorn", "app.main:app", \
    "--host", "0.0.0.0", \
    "--port", "3000" \
    ]
