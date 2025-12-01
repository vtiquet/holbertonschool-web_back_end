#!/usr/bin/env python3
""" Returns all students sorted by average score """


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    The average score must be part of each item
    returned with key = averageScore.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "topics": {"$first": "$topics"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return list(mongo_collection.aggregate(pipeline))
