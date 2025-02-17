# you can use it on a cloud VM or w/e you prefer

from flask import Flask, request, jsonify

app = Flask(__name__)
clipboard_data = {"text": ""}

@app.route("/post", methods=["POST"])
def post_clipboard():
    global clipboard_data
    clipboard_data["text"] = request.json.get("text", "")
    return jsonify({"message": "Clipboard updated!"})

@app.route("/get", methods=["GET"])
def get_clipboard():
    return jsonify(clipboard_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=5000)