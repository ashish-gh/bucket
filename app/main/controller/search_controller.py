from flask import Blueprint, g, jsonify, make_response, request

from ..services.extraction.filter import NameFilter

RES = {
    "data" : "",
    "status_code":200,
    "message":"success",
    "metadata":{}
}


search_bp = Blueprint("search_bp", __name__)


@search_bp.route("/company/<name>/", methods=["GET"])
def documents_data(name):
    print("search controller")
    res = NameFilter(name=name).filter()
    RES["data"] = res
    return jsonify(RES)


