#!/usr/bin/env python3
"""
MongoDB manipulation in Python
"""
import pymongo


def top_students(mongo_collection):
    """
    Returns students by average score
    """
    students = mongo_collection.aggregate([
        {"$project" : {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}}
        },
        {
            "$sort": {
                "averageScore": -1
                }}
            ])
    return students