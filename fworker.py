import time
import logging
from faktory import Worker
from reddit import call_reddit_api

logging.basicConfig(level=logging.INFO)

time.sleep(5)

def call_api():
    try:
        call_reddit_api()
    except Exception as e:
        logging.error(f"Error in call_api: {e}")

w = Worker(queues=['default'], concurrency=1)
w.register('call_api', call_api)
w.run()


