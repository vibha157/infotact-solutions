from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["tip_db"]
indicators = db["indicators"]
indicators.create_index("value", unique=True)

def save_ip(ip, source):
    try:
        indicators.update_one(
            {"value": ip},
            {"$setOnInsert": {
                "value": ip,
                "type": "ip",
                "source": source,
                "timestamp": datetime.utcnow()
            }},
            upsert=True
        )
        print(f"Saved: {ip}")
    except Exception as e:
        pass  # duplicate, skip it

if __name__ == "__main__":
    save_ip("192.168.1.1", "test")
    print("MongoDB working!")
