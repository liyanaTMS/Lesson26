import requests
from endpoints.base_endpoint import Endpoint


class DeleteObj(Endpoint):
    schema ={
        "type": "object",
        "properties": {
           "message": {"type":"string"}
        },
        "required": ["message"]
    }
    # метод удаления объекта (т.е. DELETE)
    def del_obj(self, id_to_del):
        self.response = requests.delete(f'{self.url}/objects/{id_to_del}')
        self.response_json = self.response.json()
        print("DELETE 'https://api.restful-api.dev' : ", self.response_json)

    def get_delete_message(self):
        return self.get_data()["message"]

    def get_delete_error(self):
        return self.get_data()["error"]

