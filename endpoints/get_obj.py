import requests
import jsonschema
from endpoints.base_endpoint import Endpoint


class GetObj(Endpoint):
    # метод получения объекта (т.е. GET)
    def get_obj(self, get_id):
        self.response = requests.get(f'{self.url}/objects/{get_id}')
        self.response_json = self.response.json()
        print("GET 'https://api.restful-api.dev' : ", self.response_json)
