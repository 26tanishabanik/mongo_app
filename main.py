import pymongo
import streamlit as st
# client = pymongo.MongoClient(**st.secrets["mongo"])
client = pymongo.MongoClient("mongodb+srv://"+st.secrets["mongo"]["username"]+":"+st.secrets["mongo"]["password"]+"@cluster0.zph5i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print("Welcome to PyMongo")
db = client['Owls']
collection = db['Poem']

def create(name, rawText):   
    dictionary = {'PoemName': name, 'Content': rawText}
    collection.insert_one(dictionary)

def GetPoem(name):
    return collection.find_one({'PoemName': name}, {'PoemName':0, '_id':0})['Content']

def GetPoemName(prev):
    if collection.find_one(prev, {'_id':0}):
        return 1
    else:
        return None
def update(prev, new):
    collection.update_one(prev, new)

def delete(name):
    collection.delete_one(name)

def getAll():
    allDocs = collection.find()
    return [rec['PoemName'] for rec in list(allDocs)]
    
# if __name__ == "__main__":
#     client = pymongo.MongoClient("mongodb://localhost:27017/")
#     print("Welcome to PyMongo")
#     db = client['Owl']
#     collection = db['poems']
#     dictionary = {'PoemName': 'abc', 'Status': 'Done'}
#     collection.insert_one(dictionary)
#     allDocs = collection.find({})
#     print(list(allDocs))
#     for doc in allDocs:
#         print(doc)