import json
from flask import Blueprint, request, jsonify
from lib.logger import logger
import datetime
import uuid
from lib.add_product import add_product

add_product_bp = Blueprint('product', __name__)


@add_product_bp.route('/add_product', methods=['POST'])
def create():
    logger.info("started...")
    logger.info("Logger is initialized successfully...")
    request_body = json.loads(request.data)

    job_run_env = "DEV"
    load_date = datetime.date.today()
    job_run_id = "apicall-" + str(uuid.uuid4())

    details = f"initializing {job_run_id} in {job_run_env} on {load_date}..."
    logger.info(details)

    products = request_body.get("products")
    status = add_product(products)
    if status:
        print("Insert Successful")
        return jsonify({"message": "Insert Successful...", "status": "success"}), 201
    else:
        print("Some error came up, please look around!")
        return jsonify({"message": "Insert Failed", "status": "error"}), 500
