
# flask_db_health.py — готовый Blueprint с /db_health
from flask import Blueprint
from dbx import healthcheck

dbhealth = Blueprint("dbhealth", __name__)

@dbhealth.route("/db_health")
def db_health():
    return ("OK", 200) if healthcheck() else ("DB ERROR", 500)
