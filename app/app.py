from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from loguru import logger

RES = {
    "data" : "",
    "status_code":200,
    "message":"success"
}

logger.info(f"Starting server . . . ")

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
#----
logger.info(f"Server started successfully")


@app.route("/")
def extract():
    return jsonify(RES)



def main():
    app.run()

    

if __name__ == "__main__":
    main()
