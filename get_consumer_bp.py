from flask import Flask, Blueprint, jsonify, request
from lib.logger import logger
import json
from lib.get_consumer import get_consumer

get_consumer_bp = Blueprint("get_consumer", __name__)


@get_consumer_bp.route('/get', methods=["GET"])
def create():
    logger.info("started...")
    logger.info("Logger is initialized successfully.")
    headers = request.headers

    if request.args.get('criteria'):
        search_criteria = request.args.get('criteria')
        search_params = search_criteria.split(',')
    else:
        response_body = {"transactionId": headers.get("TransactionId"), "message": "parameters error", "code": 904}
        return jsonify(response_body), 404

    print(search_criteria)
    print(search_params)

    status, output = get_consumer(search_params)
    print(status)
    print(output)
    if status:
        return jsonify({"message": "Consumer details retrieved successfully", "sections": output}), 200
    else:
        return jsonify({"message": "User not found", "sections": output}), 404

