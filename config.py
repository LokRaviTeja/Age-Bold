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
      "partner_code": "BETTERCARE",
      "file_path": "/FileStore/tables/bettercare_members.csv",
      "delimiter": ",",
      "has_header": True,
      "column_mapping": {
        "subscriber_id": "external_id",
        "first_name": "first_name",
        "last_name": "last_name",
        "birth_date": "dob",
        "email_address": "email",
        "phone_number": "phone"
      },
      "dob_input_format": "yyyy-MM-dd"
    }
}
