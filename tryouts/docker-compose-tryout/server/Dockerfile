FROM python:3.10-slim

ARG UID=40403
ARG GID=40403

RUN groupadd -g $GID -o mygroup && \
    useradd -m -u $UID -g $GID -o -r myuser

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 40403
COPY --chown=mygroup:myuser ./app /app
USER myuser

CMD [ \
    "uvicorn", "app.main:app", \
    "--host", "0.0.0.0", \
    "--port", "40403" \
    ]
