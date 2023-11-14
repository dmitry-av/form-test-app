from flask import Flask, jsonify, request
from pymongo import MongoClient
import re
import datetime

app = Flask(__name__)


def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017,
                         username='rootuser',
                         password='beeandwasp',
                         authSource="admin")
    db = client["form_db"]
    return db


def validate_date(date_str):
    date_formats = ["%d.%m.%Y", "%Y-%m-%d"]
    for format_str in date_formats:
        try:
            return datetime.datetime.strptime(date_str, format_str)
        except ValueError:
            pass
    return None


def validate_phone(phone_str):
    phone_pattern = re.compile(r'^\+7\d{10}$')
    return bool(re.match(phone_pattern, phone_str))


def validate_email(email_str):
    email_pattern = re.compile(r'\S+@\S+\.\S+')
    return bool(re.match(email_pattern, email_str))


def get_field_type(value):
    if validate_date(value):
        return "date"
    elif validate_phone(value):
        return "phone"
    elif validate_email(value):
        return "email"
    else:
        return "text"


@app.route('/')
def ping_server():
    return "Welcome to the world of animals."


@app.route('/get_form', methods=['POST'])
def get_form():
    db = None
    try:
        data = request.form.to_dict()
        db = get_db()
        for template in db.form_tb.find():
            template_fields = {
                k: v for k, v in template.items() if k != "_id" and k != "name"}
            print(template_fields)
            if all(field_name in data and get_field_type(data[field_name]) == template_fields[field_name]
               for field_name in template_fields):
                return jsonify({"template_name": template["name"]})

        field_types = {key: get_field_type(data[key]) for key in data}
        return jsonify(field_types)

    except Exception as e:
        return jsonify({"error": str(e)})

    finally:
        if db is not None:
            db.client.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
