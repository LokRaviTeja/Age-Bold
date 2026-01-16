import os

os.makedirs("data", exist_ok=True)

# -------- ACME FILE (Pipe-delimited .txt) --------
acme_data = """MBI|FNAME|LNAME|DOB|EMAIL|PHONE
A12345|john|doe|03/15/1955|JOHN.DOE@EMAIL.COM|5551234567
A67890|jane|smith|12/01/1960|JANE.SMITH@EMAIL.COM|555-222-3333
"""

with open("data/acme_members.txt", "w") as f:
    f.write(acme_data)

# -------- BETTERCARE FILE (Comma-delimited .csv) --------
bettercare_data = """subscriber_id,first_name,last_name,birth_date,email_address,phone_number
B111,james,brown,1965-08-10,james.brown@email.com,5554445555
B222,linda,white,1970-01-05,linda.white@email.com,555-666-7777
"""

with open("data/bettercare_members.csv", "w") as f:
    f.write(bettercare_data)

print("Sample input files generated successfully.")
