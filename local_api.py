import json
import requests

# send a GET using the URL http://127.0.0.1:8000
r = "http://127.0.0.1:8000"
request = requests.get(r) 


# TODO: print the status code
print(f"Status Code: {request.status_code}")
# TODO: print the welcome message
cleaned_text = request.text.strip('"')
print(f"Result: {cleaned_text}")



data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
r_post = r+"/data/"
t_post = requests.post(r_post, json=data)

# print the status code
print(f"Status Code: {t_post.status_code}")

# print the result
print(f"Result: {t_post.json()['result']}")
