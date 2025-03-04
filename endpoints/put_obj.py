import requests
from endpoints.base_endpoint import Endpoint


class UpdateObj(Endpoint):
    schema ={
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"},
                    "color": {"type":"string"}
                },
                "required": ["year", "price", "CPU model", "Hard disk size", "color"]
            }

        },
        "required": ["id", "name", "data"]
    }
    # метод обновления объекта (т.е. PUT)
    def put_obj(self, put_id, payload):
        self.response = requests.put(f'{self.url}/objects/{put_id}', json=payload)
        self.response_json = self.response.json()
        print("PUT 'https://api.restful-api.dev' : ", self.response_json)



