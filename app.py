from __future__ import absolute_import
from celery import Celery

app = Celery(__name__, include=['tasks'])

_host = 'localhost'
_port = 6379

app.conf.update(
    BROKER_URL='redis://%s:%s/0' % (_host, _port),
    CELERY_RESULT_BACKEND='redis://%s:%s/1' % (_host, _port),
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ACCEPT_CONTENT=['application/json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ROUTES = {
        'tasks.add': {'queue': 'hipri'}
    }
)


def start():
    app.worker_main()


if __name__ == '__main__':
	app.worker_main() 
