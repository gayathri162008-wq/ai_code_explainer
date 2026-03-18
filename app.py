from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "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"

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/explain", methods=["POST"])
def explain():
    code = request.json["code"]

    # Simple smart logic (demo AI)
    explanation = ""

    if "print" in code:
        explanation += "This line is used to display output on the screen.\n\n"

    if "int " in code:
        explanation += "This line declares an integer variable.\n\n"

    if "=" in code:
        explanation += "This line assigns a value to a variable.\n\n"

    if "for" in code:
        explanation += "This is a loop that repeats a block of code multiple times.\n\n"

    if "while" in code:
        explanation += "This is a loop that runs while a condition is true.\n\n"

    if explanation == "":
        explanation = "This code performs some operations. It can be further expanded for detailed explanation."

    return jsonify({"explanation": explanation})
if __name__ == "__main__":
    app.run(debug=True)
