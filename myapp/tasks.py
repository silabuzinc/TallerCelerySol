from celery import shared_task
from time import sleep

@shared_task
def send_book(nombre, mail):
    sleep(20)  # Simulate expensive operation(s) that freeze Django
    print(
        nombre + " " + mail
    )