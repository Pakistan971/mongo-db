import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/neurlab")

database =client["NeuroLab"]

colle