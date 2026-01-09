#! /usr/bin/python3
import json

with open("/home/qa/ansible_key", "r") as keyfile:
  key = keyfile.read()

with open("data.json", "w") as out:
  data = {"data": {"sshkey": key}}
  json.dump(data, out)