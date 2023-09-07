#!/usr/bin/env python3
"""
This script defines a function for listing all documents in a MongoDB collection.
"""

def list_all(mongo_collection):
    """
    Returns a list of all documents in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to list documents from.

    Returns:
        list: A list containing all documents in the collection.
    """ 
    if mongo_collection is None:
        return []
    result = mongo_collection.find()
    return [results for results in result]