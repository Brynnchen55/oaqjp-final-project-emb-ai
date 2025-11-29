"""
This is the main server file for the Emotion Detector Web Application.
It defines Flask routes for the home page and the emotion detection API.
"""
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request, jsonify
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application page over the Flask channel
    '''
    return render_template('index.html')

@app.route('/emotionDetector')
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the result for the 
        provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400

    return {
        "message": (f"For the given statement, the system response is "      
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}, "
        f"The dominant emotion is {result['dominant_emotion']}.")
    }

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
