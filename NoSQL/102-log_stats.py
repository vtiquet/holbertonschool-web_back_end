#!/usr/bin/env python3
""" Provides some stats about Nginx logs, including the top 10 IPs """
from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs and the top 10 IPs.
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

    status_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_count} status check")

    # Top 10 IPs
    print("IPs:")
    ip_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = list(logs_collection.aggregate(ip_pipeline))

    for ip_data in top_ips:
        print(f"\t{ip_data.get(_id)}: {ip_data.get(count)}")
