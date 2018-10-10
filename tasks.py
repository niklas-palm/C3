from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')
app.config_from_object('celeryconfig')

#Give a certain task low priority
#task_routes = {
#    'tasks.add': 'low-priority',
#}

#A certain task can only be processed 10 times per minute
#task_annotations = {
#    'tasks.add': {'rate_limit': '10/m'}
#}


@app.task
def add(x, y):
    return x + y
