#!/usr/bin/node
import requests

r = requests.get(“https://swapi-api.alx-tools.com/api/people/”)
r.json()

for result in r.json()[“results”]:
  print(result[“name”])
  print(“\n”)
