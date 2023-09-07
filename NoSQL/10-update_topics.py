#!/usr/bin/env python3
"""
This script defines a function for updating topics in a MongoDB collection.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates the topics field for documents with the specified name in a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to update documents in.
        name (str): The name of the documents to be updated.
        topics (list): The list of topics to update in the documents.

    Returns:
        pymongo.results.UpdateResult: The result of the update operation, including the number of documents modified.
    """
    result = mongo_collection.update_many(
        {"name": name}, {'$set': {'topics': topics}})
    return result