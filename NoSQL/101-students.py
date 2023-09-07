#!/usr/bin/env python3
import pymongo

# Function to return students sorted by average score
def top_students(mongo_collection):

  # Aggregation pipeline 
  # 1) Calculate average score for each student
  # 2) Sort students by descending average score
  results = mongo_collection.aggregate([
    {
      '$project': { 
        '_id': 0, # Exclude _id from results 
        'name': 1, # Include name field
        'averageScore': {  
          '$avg': '$scores' # Calculate average of scores array
        }
      }
    },
    {
      '$sort': {
        'averageScore': -1 # Sort by averageScore descending
      }
    }
  ])

  # Return aggregation results as a list
  return list(results) 

# Example usage:

# Connect to MongoDB 
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['students_db']
collection = db['grades'] 

# Call top_students function to get list of top students
top_students = top_students(collection)  

# Print top students
print(top_students)