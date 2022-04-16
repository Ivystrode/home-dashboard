import json, requests
 
global posturl
posturl = "http://localhost:5000/post"

test_data = {"co2": {"time": "19:40", "level": 25566}, "nothing": {"wow":"working"}}

def send_db_file(posturl):
    with open("db.json") as sendfile:
        data = json.load(sendfile)
    
    p = requests.post(posturl, json=data)
    print(p)
    
def get():
    d = requests.get("http://localhost:5000/get")
    print(d)
    print(d.content)

def add_to_graph_data(data):
    
    p = requests.post(posturl, json=data)
    print(p)

if __name__ == '__main__':
    # send_db_file(posturl)
    get()
    # add_to_graph_data(test_data)
