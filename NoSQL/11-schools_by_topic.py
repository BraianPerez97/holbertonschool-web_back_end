#!/usr/bin/env python3
"""
This script defines a function for updating topics in a Mongo DB  collection.
"""

def update_topic(mongo_collection, name, topics):
    """
    Update the 'topics' field for documents with the specifies 'name' in MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collectipn to update documents in.
        name (str): The name to identifi the documents to be updated.
        topics (list): The list of topics to set for the documents.
    Returns:
    pymongo.result.UpdateResult: The results of the updated operation, including the number of documents modified
    """
    result = mongo_collection.update.many(
        {"name": name}, {'$set' : {'topics': topics}})

    return result