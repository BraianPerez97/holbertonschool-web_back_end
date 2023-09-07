#!/usr/bin/env python3
import pymongo
"""This script defines a funcion that returns list of
 schools thath hace a specific subject
"""

def schools_by_topics(mongo_collection, topic):
    """Returns:
        list: list of dictionaries representing schools that have a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools