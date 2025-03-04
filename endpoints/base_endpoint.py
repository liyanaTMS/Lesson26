import jsonschema
import settings


class Endpoint:
    response = None
    response_json = None
    response_status = None
    schema = {}
    url = settings.url

    def check_response_is_200(self):
        assert self.response.status_code == 200,\
            f'{self.response.status_code}'

    def check_response_is_400(self):
        assert self.response.status_code == 400,\
            f'{self.response.status_code}'

    def validate(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def get_data(self):
        return self.response.json()

    def get_id(self):
        return self.get_data()['id']

    def get_name(self):
        return self.get_data()['name']

    def get_year(self):
        return self.get_data()['data']['year']

    def get_price(self):
        return self.get_data()['data']['price']

    def get_cpu_model(self):
        return self.get_data()['data']['CPU model']

    def get_hard_disk_size(self):
        return self.get_data()['data']['Hard disk size']

    def check_all_fields(self, expected_data):
        assert self.get_name() == expected_data['name'], 'wrong name'
        assert self.get_year() == expected_data['data']['year'], 'wrong year'
        assert self.get_price() == expected_data['data']['price'], 'wrong price'
        assert self.get_cpu_model() == expected_data['data']['CPU model'], 'wrong cpu'
        assert self.get_hard_disk_size() == expected_data['data']['Hard disk size']