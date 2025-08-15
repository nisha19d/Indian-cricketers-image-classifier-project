from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/identify_image', methods = ['GET','POST'])
def identify_image():

    image_data = request.form['image_data']

    response = jsonify(util.identify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting python flask server for cricketers image classification")
    util.load_saved_artifacts()
    app.run(port=5000)