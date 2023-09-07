#!/usr/bin/env python3
"""This script defines a funcion 
that returns list of
 schools thath hace a specific subject
"""
import pymongo


def schools_by_topics(mongo_collection, topic):
    """Returns list of dictionaries representing schools 
    that have a specific topic
    """
    schools = mongo_collection.find({"topics": {"$in": [topic]}})
    return schools