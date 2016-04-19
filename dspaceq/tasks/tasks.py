from celery.task import task
#from dockertask import docker_task
from subprocess import call,STDOUT
#import requests

#Default base directory 
#basedir="/data/static/"


#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result

@task()
def dspace_load(local_file_or_url,collection,operation="add",dspace_exec="/srv/shareok/dspace/bin/dspace"):
    """
        dspace_load arguments:
            local_file_or_url: Local file location
            collection: collection to insert or replace data elements
            operation: 'add' or 'replace' 
    """
    if operation.lower() =="add" or operation.lower() =="replace":
        call(["sudo","-u","tomcat",dspace_exec,"import","--{0}".format(operation),"--eperson=libir@ou.edu","--collection={0}".format(collection)])
        return "https://test.shareok.org/handle/{0}".format(collection)
    else:
        raise("operation argument must be add or replace")
