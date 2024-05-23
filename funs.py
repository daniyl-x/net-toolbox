import json


def serialize_json(data: dict) -> dict:
    serialized_data = json.dumps(data, indent=4)
    return serialized_data
