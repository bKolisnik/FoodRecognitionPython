from flask import Flask
from flask import request
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json


clapp = ClarifaiApp(api_key='a2a53df5eede4b7d8ca4c81fbc87975e')
model = clapp.models.get('food-items-v1.0')

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/pictureEndPoint",methods=['POST'])
def receivePicture():
    img = request.files['image']
    if(img is not None):
        print("yup")
    #image = ClImage(url="https://samples.clarifai.com/food.jpg")
    image = ClImage(file_obj=img)

    res = model.predict([image])
    #print(res)
    res = res["outputs"][0]["data"]["concepts"]
    #res = json.dumps(res, ensure_ascii=False)
    print(res)
    list=[]
    list2=[]
    for i in range(len(res)):
        print(i)
        list2.insert(i, res[i]["name"])
        list2.insert(i+1, res[i]["value"])
        #print(list2)
        #list.insert(i, res[i]["name"])
        list.insert(i,list2[:])
        list2.clear()
    print(list)
    return json.dumps(list)

if __name__ == "__main__":
    app.run()
