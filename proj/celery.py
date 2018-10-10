
from __future__ import absolute_import, unicode_literals
from celery import Celery

#ilclude specifies which tasts to import when the celery instance (app) is created
app = Celery('proj',
             broker='amqp://',
             backend='rpc://',
             include=['proj.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
