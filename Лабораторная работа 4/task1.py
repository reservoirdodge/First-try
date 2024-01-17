# TODO решите задачу
import json
def task() -> float:
    file = "input.json"
    with open(file) as x:
        json_d = json.load(x)
    sum_ = sum([item["score"] * item["weight"] for item in json_d])
    return round(sum_, 3)
print(task())





