from flask import Flask, jsonify
from loguru import logger

RES = {
    "data" : "",
    "status_code":200,
    "message":"success"
}

logger.info(f"Starting server . . . ")
app = Flask(__name__)

logger.info(f"Server started successfully")


@app.route("/")
def extract():
    return jsonify(RES)



def main():
    app.run()

    

if __name__ == "__main__":
    main()
