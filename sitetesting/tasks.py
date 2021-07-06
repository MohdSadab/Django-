from celery import shared_task

@shared_task
def add(x,y):
    print(x,y)
    return x+y

@shared_task
def update_website_status(data):
    print(data,">>>>>>")
    # here we can use request module and data have url and we can use that url and request to the
    # web site and if the status is ok then we can update the status of the site 
