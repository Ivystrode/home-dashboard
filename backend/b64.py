# import base64 

# with open("index.jpeg", "rb") as file:
#     file_string = "data:image/jpeg;base64," + base64.b64encode(file.read()).decode("utf-8")
#     file_string
    
# with open("string.txt", "a") as f:
#     f.write(file_string)


# cmd = 'cd /home/pi/vid_streamer/mjpg-streamer/mjpg-streamer-experimental && ./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"'

# l = cmd.split(" ")
# print(l)

import requests, json, time

r = requests.get("http://192.168.1.84:5000/get/detections")
# d = str(r)
d = json.dump(r.content)
# print(r)

for k in d:
    print(k)
    time.sleep(2)