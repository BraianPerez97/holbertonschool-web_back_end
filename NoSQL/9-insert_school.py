#!/usr/bin/env python3
"""
This script defines a function for inserting data into a MongoDB collection.
"""


def insert_school(mongo_collection, **kwargs):
        """
    Inserts a document into a MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The MongoDB collection to insert the document into.
        **kwargs: Keyword arguments representing the document to be inserted.

    Returns:
        ObjectId: The ObjectId of the inserted document.
    """
        inserted_id = mongo_collection.insert_one(kwargs).inserted_id
        return inserted_id