#!/usr/bin/env python3
"""
MongoDB manipulation in Python
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of docs by topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools