from pymongo import MongoClient
from elasticsearch import Elasticsearch

mongo = MongoClient("mongodb://localhost:27017/")
db = mongo["tip_db"]
indicators = db["indicators"]

es = Elasticsearch("http://localhost:9200")

print("Sending data to Elasticsearch...")
count = 0

for doc in indicators.find():
    doc.pop("_id", None)
    es.index(index="tip-indicators", document=doc)
    count += 1
    print(f"Sent: {doc.get('value')}")

print(f"Done! Sent {count} records to Elasticsearch.")
