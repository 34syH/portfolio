from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def portfolio():
    return send_from_directory(app.root_path, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
