#!/bin/bash

for f in sensors_data/elsys-co2-0558b3/*.txt; do python acp_json_csv.py $f; done
