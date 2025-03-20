from flask import Flask, request, jsonify, Blueprint
import json
import uuid
import sys
import datetime
from lib.process_all import insert_backend, update_backend
from lib.utils import get_global_id
from lib.logger import logger


consumer_bp = Blueprint('consumer', __name__)


@consumer_bp.route("/insert", methods=["POST"])
def create():
    logger.info("started...")
    request_body = json.loads(request.data)
    logger.info("Logger is initialized successfully.")
    # # This is when we are actually providing environment via parameters
    # if len(sys.argv) < 2:
    #     print("Usage: Environment is missing {dev, qa, prod}")
    # job_run_env = sys.argv[1].upper()

    job_run_env = "DEV"
    load_date = datetime.date.today()
    job_run_id = "apicall-" + str(uuid.uuid4())

    print(f"initializing {job_run_id} in {job_run_env} on {load_date}...")

    data = request_body.get("consumers")[0]
    global_id = data.get("GlobalId")
    pii = data.get("pii")
    address = data.get("address")
    social_contact = data.get("social_contact")
    purchases = data.get('purchases')[0]

    database_global_id = ""
    flag = True
    if global_id in ("", None):
        database_global_id, flag = get_global_id(pii.get("FirstName"))
        print(database_global_id)
        print(flag)
        if not flag:
            status = insert_backend(pii, address, social_contact, purchases)
            if status:
                print("Insert Successful")
                return jsonify({"message": "Insert Successful...", "status": "success"}), 201
            else:
                print("Some error came up, please look around!")
                return jsonify({"message": "Insert Failed", "status": "error"}), 500

        else:
            status = update_backend(database_global_id, pii, address, social_contact, purchases)

    else:
        status = update_backend(global_id, pii, address, social_contact, purchases)

    return jsonify({"message": "Insert/Update Successful...", "status": "success", "data": request_body}), 200

