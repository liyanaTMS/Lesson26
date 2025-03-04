from payload.payload import valid_create_payload
from payload.payload import invalid_create_payload
from endpoints.get_obj import GetObj

def test_create_object(create_obj_with_data):
    f_ob_id, f_object = create_obj_with_data

    f_object.check_response_is_200()
    f_object.validate(f_object.get_data())
    f_object.check_all_fields(valid_create_payload)

    # гетнуть созданный объект
    get_object = GetObj()
    get_object.get_obj(f_ob_id)
    get_object.check_all_fields(valid_create_payload)


