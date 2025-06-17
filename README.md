🛠️ Django DRF + Celery + Telegram Bot Project

This is a full-featured Django project with:

- 🔐 Token-based authentication using Django REST Framework
- ✅ CRUD APIs for managing tasks
- 📬 Email sending via Celery (Async Task Queue)
- 🤖 Telegram Bot integration with webhook support

---
For Check API with Urls

API Endpoints – How to Check via URL
🔓 Public Endpoint (No Authentication)
URL: http://127.0.0.1:8000/api/public/

Method: GET

Description: Returns a simple public message (test endpoint).
🔐 Authentication Flow
Register a New User

URL: http://127.0.0.1:8000/api/register/

Method: POST

Body:

json

{
  "username": "testuser",
  "password": "testpass123"
}



🔓 Login to Get Token

URL: http://127.0.0.1:8000/api/login/

Method: POST

🚀 Celery Setup & Testing
✅ Step-by-Step Instructions to Run Celery
Make sure you’ve already configured Celery in your Django project (celery.py, __init__.py, tasks.py, etc.).
Start Redis Server
Celery uses Redis as a message broker.




brew services start redis
# or (if you installed via apt)
redis-server
Make sure Redis is running at default port 6379.

2. Start Celery Worker
In a new terminal (inside your virtual environment):




celery -A core worker --loglevel=info
✅ This will start the Celery worker using your Django app (core is your main Django project folder name).


▶️ Running the Telegram Bot Manually
To run the Telegram bot manually from your local machine or server (for testing purposes), follow the steps below:

✅ Step-by-Step Instructions
Ensure your virtual environment is activated (if you're using one):




source venv/bin/activate  # for Linux/Mac
# or
venv\Scripts\activate  # for Windows
Make sure your TELEGRAM_BOT_TOKEN is set correctly in either settings.py or an .env file loaded in your script.

Run the Telegram bot script:


python telegram_bot.py
✅ After running the above command, you should see:


✅ Telegram bot is Started.....
