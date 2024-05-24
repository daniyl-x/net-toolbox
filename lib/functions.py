import json
import subprocess


def run_cmd(args: list[str], capture_output: bool = True) -> dict | None:
    result = subprocess.run(args, capture_output=capture_output)
    data = {
            "stdout": result.stdout.decode(),
            "stderr": result.stderr.decode(),
            }
    return data


def serialize_json(data: dict) -> dict:
    serialized_data = json.dumps(data, indent=4)
    return serialized_data
