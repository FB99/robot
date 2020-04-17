from threading import Thread
import requests
import time

KERAS_REST_API_URL = "http://localhost/predict"
IMAGE_PATH = "test.png"

NUM_REQUESTS = 500
SLEEP_COUNT = 0.05

def call_predict_endpoint(n):
	image = open(IMAGE_PATH, "rb").read()
	payload = {"image": image}

	r = requests.post(KERAS_REST_API_URL, files=payload).json()

	if r["success"]:
		print("[INFO] thread {} OK".format(n))

	else:
		print("[INFO] thread {} FAILED".format(n))

for i in range(0, NUM_REQUESTS):
	t = Thread(target=call_predict_endpoint, args=(i,))
	t.daemon = True
	t.start()
	time.sleep(SLEEP_COUNT)

time.sleep(300)