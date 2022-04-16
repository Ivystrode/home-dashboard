import json, requests
 
global posturl
posturl = "http://localhost:5000/post"

test_data = []

def send_db_file(posturl):
    with open("db.json") as sendfile:
        data = json.load(sendfile)
    
    p = requests.post(posturl, json=data)
    print(p)
    
def get(col):
    d = requests.get(f"http://localhost:5000/get/{col}")
    print(d)
    print(d.content)

def add_multiple_to_collection():
    
    for entry in test_data:
        p = requests.post(posturl, json=entry)
        print(p)
    
def add_single(collection, test):
    p = requests.post(f"{posturl}/{collection}", json=test)
    print(p) 

if __name__ == '__main__':
    # send_db_file(posturl) # SENT to atlas testdb testcol
    get("cameras")
    # add_to_graph_data()
    # add_single("co2", {"time":"00:40", "level": 260})
