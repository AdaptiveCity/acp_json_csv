import json
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")
args = parser.parse_args()

readings = []

with open(args.filename) as f:
    for jsonObj in f:
        reading = json.loads(jsonObj)
        readings.append(reading)

for reading in readings:
    acp_id = reading.get("acp_id",0)
    acp_ts = reading.get("acp_ts",0)
    dt = datetime.fromtimestamp(int(float(acp_ts)))
    date = dt.strftime('%Y-%m-%d')
    time = dt.strftime('%H:%M:%S')
    payload_cooked = reading.get("payload_cooked")
    if payload_cooked:
        motion = payload_cooked.get("motion","")
        co2 = payload_cooked.get("co2","")
    print(f'{acp_id},{date},{time},{acp_ts},{motion},{co2}')
