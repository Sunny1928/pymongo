# install pymongo first by `pip install pymongo`
import pymongo

# connect to database by url
client = pymongo.MongoClient("mongodb://localhost:27017/")

# connect to database
db_name = "test"
db = client[db_name]

# connect to collection
table = db["user"]

# rule
# if item['ge'] == 'fe' -> item['gender'] = 'female'
# if item['ge'] == 'ma' -> item['gender'] = 'male'
rule = {
    "fe": "female",
    "ma": "male",
}

# find all data in collection
data = table.find({})

for item in data:
    # using _id to find object and then set 'gender' to the rule
    table.update_one({'_id' : item['_id']}, {'$set' : {'gender' : rule[item['ge']]}}) 

    # print(item['_id'])

print('done')

