import requests

KERAS_REST_API_URL = "http://localhost:5000/predict"
IMAGE_PATH = "test.png"


image = open(IMAGE_PATH, "rb").read()
payload = {"image": image}


r = requests.post(KERAS_REST_API_URL, files=payload).json()


if r["success"]:
	for (i, result) in enumerate(r["point"]):
		print("{}. {}: {:.4f} {:.4f}".format(i + 1, result["label"],
			result["point_x"], result["point_y"]))

else:
	print("Request failed")