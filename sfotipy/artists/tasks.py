#Tareas asincronas con celery
from celery import task
import time

#Decorador para volverla asincrona:
@task
def demorada():
	time.sleep(5)
	print 'acabe'