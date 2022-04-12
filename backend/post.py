import json, requests 


def send(posturl):
    with open("db.json") as sendfile:
        data = json.load(sendfile)
    
    p = requests.post(posturl, json=data)
    print(p)
    
def get():
    d = requests.get("http://localhost:5000/get")
    print(d.content)

if __name__ == '__main__':
    send("http://localhost:5000/post")
    # get()