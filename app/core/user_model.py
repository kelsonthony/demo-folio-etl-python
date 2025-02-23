class User:
    def __init__(self, row):
        self.username = row["username"]
        self.first_name = row["firstName"]
        self.last_name = row["lastName"]
        self.middle_name = row.get("middleName", "")
        self.preferred_first_name = row.get("preferredFirstName", "")
        self.email = row["email"]
        self.phone = row["phone"]
        self.mobile_phone = row["mobilePhone"]
        self.address = {
            "addressLine1": row["addressLine1"],
            "addressLine2": row["addressLine2"],
            "city": row["city"],
            "region": row["region"],
            "postalCode": row["postalCode"],
            "addressTypeId": "93d3d88d-499b-45d0-9bc7-ac73c3a19880",
            "countryId": "BR"
        }
    
    def to_json(self):
        return {
            "active": True,
            "personal": {
                "addresses": [self.address],
                "firstName": self.first_name,
                "preferredContactTypeId": "002",
                "lastName": self.last_name,
                "middleName": self.middle_name,
                "preferredFirstName": self.preferred_first_name,
                "email": self.email,
                "phone": self.phone,
                "mobilePhone": self.mobile_phone
            },
            "username": self.username,
            "patronGroup": "ad0bc554-d5bc-463c-85d1-5562127ae91b",
            "expirationDate": "2025-09-07T23:59:59Z",
            "barcode": self.username,
            "enrollmentDate": "2024-09-07T00:00:00.000Z",
            "externalSystemId": self.username,
            "departments": []
        }
