import faktory
import time

time.sleep(5)

with faktory.connection() as client:
    while True:
        client.queue('call_api')
        time.sleep(5)