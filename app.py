from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"status": "ok", "message": "Hello from Manojeet's CI/CD pipeline"})


@app.route("/health")
def healthcheck():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
