import azure.functions as func
import pymongo
from bson.objectid import ObjectId
from config import Config

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()

    if request:
        try:
            url = Config.MONGO_URL
            client = pymongo.MongoClient(url)
            database = client[Config.MONGO_DB_NAME]
            collection = database['advertisements']
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": request}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

