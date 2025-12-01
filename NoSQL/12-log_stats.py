#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs in the logs database, nginx collection.
    """
    client = MongoClient(mongodb://127.0.0.1:27017)
    logs_collection = client.logs.nginx

    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
