#!/usr/bin/env python3
import pymongo
"""Module to get top students from MongDB"""

def top_students(mongo_collection):
    """Get students sorted by average score

    Args:
        mongo_collection: PyMongo collection object

    Returns:
        list: List of dictionaries eith students name and averager score.
    """
    results = mongo_collection.aggregate([
    {
      '$project': { 
        '_id': 0, 
        'name': 1,
        'averageScore': {  
          '$avg': '$scores'
        }
      }
    },
    {
      '$sort': {
        'averageScore': -1 
      }
    }
  ])
    return list(results) 

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['students_db']
collection = db['grades'] 

top_students = top_students(collection)
print(top_students)