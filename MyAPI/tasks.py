from celery import shared_task # type: ignore

@shared_task
def test_func():
    print("🧪 Test Celery Task Running")
    return "Test done!"

@shared_task
def send_welcome_email():
    print("🎉 Sending welcome email...")
    return "Email sent!"
