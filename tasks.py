from celery import Celery
import time
from app import app

@app.task
def add(x, y):
    # time.sleep(10)
    print '%s+%s' % (x,y)
    return x + y

@app.task
def task_a(x, y):
    return x*y


# celery worker -A tasks -l info -c 5

