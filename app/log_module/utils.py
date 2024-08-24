import json
import os

import requests

from .models import Log
from .serializers import LogCreateSerializer


# Download file via URL
def download_file(url, file_name):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_name


# Read file from local storage line by line
def read_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


# Parse data in a file and create Log objects in 1000 sized batches
def process_log_file(file_path, batch_size=1000) -> list:
    batch = []
    errors = []
    for line in read_log_file(file_path):
        log_entry = LogCreateSerializer(data=json.loads(line))
        if log_entry and log_entry.is_valid():
            batch.append(json.loads(line))
        else:
            errors.append({'obj': log_entry.data, 'errors': log_entry.errors})

        if len(batch) >= batch_size:
            serializer = LogCreateSerializer(data=batch, many=True)
            serializer.is_valid()
            serializer.save()
            batch = []

    if batch:
        serializer = LogCreateSerializer(data=batch, many=True)
        serializer.is_valid()
        serializer.save()

    return errors


def process_file_from_url(url) -> list:
    file = download_file(url, 'log_file.log')
    errors = process_log_file(file)

    os.remove(file)

    return errors
