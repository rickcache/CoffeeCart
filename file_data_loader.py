import json

class DataLoad:

    def json_load_checkout(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["name"],
                    item["email"]
                )
                for item in data["users"]
            ]