from flask import Flask, jsonify



app = Flask(__name__)

@app.route("/")
def myData():

    #  Dictionary of Data
    data = {"Name": "Mohammed Drame",
     "Title": "iOS Engineer",
     "School": "Make School"}


    return jsonify(data)



if __name__ == "__main__":
    app.run(debug=True)




