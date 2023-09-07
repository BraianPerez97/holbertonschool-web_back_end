#!/usr/bin/env python3
import pymongo
"""This script defines a funcion that returns list of
 schools thath hace a specific subject
"""

def schools_by_topics(mongo_collection, topic):
    """Returns list of schools that hace a specific topic

    Args:
        mongo_collection: the pymongo collection object
        topic (str): the topic name to search for.
    
    Returns:
        list: list of dictionaries representing schools that have a specific topic
    """

    query = {'topic': topic}
    project = {'name': 1}
    schools = []

    for school in mongo_collection.find(filter=query, projection=project):
        schools.append(school)

    return schools