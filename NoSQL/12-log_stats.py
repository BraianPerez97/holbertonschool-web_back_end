#!/usr/bin/env python3
"""
This script defines a function for retrieving schools by a specific topic from a MongoDB collection.
"""

def schools_by_topic(mongo_collection, topic):
    """
    Retrieve schools that match a specific topic from a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection containing school data.
        topic (str): The topic to search for within the 'topics' field of the documents.

    Returns:
        pymongo.cursor.Cursor: A cursor containing the results of the search query.
    """
    return mongo_collection.find({"topics": topic})