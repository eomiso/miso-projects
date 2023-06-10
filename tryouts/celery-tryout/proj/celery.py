from celery import Celery

app = Celery(
    "tasks",
    backend="rpc://",
    broker="pyamqp://guest@localhost//",
    include=["proj.tasks"],
)

app.conf.update(
    result_expires=3600,
)

if __name__ == "__main__":
    app.start()
