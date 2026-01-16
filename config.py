PARTNER_CONFIG = {
    "acme": {
        "file_path": "data/acme_members.txt",
        "delimiter": "|",
        "partner_code": "ACME",
        "column_mapping": {
            "MBI": "external_id",
            "FNAME": "first_name",
            "LNAME": "last_name",
            "DOB": "dob",
            "EMAIL": "email",
            "PHONE": "phone",
        },
    },
    "bettercare": {
        "file_path": "data/bettercare_members.csv",
        "delimiter": ",",
        "partner_code": "BETTERCARE",
        "column_mapping": {
            "subscriber_id": "external_id",
            "first_name": "first_name",
            "last_name": "last_name",
            "birth_date": "dob",
            "email_address": "email",
            "phone_number": "phone",
        },
    },
}
