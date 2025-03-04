from payload.payload import valid_create_payload
from endpoints.get_obj import GetObj


def test_get_object(create_obj_with_data):
    f_ob_id, f_object = create_obj_with_data

    # гетнуть объект
    get_object = GetObj()
    get_object.get_obj(f_ob_id)
    # проверка респонса 200
    get_object.check_response_is_200()
    # валидация полей на типы данных по схеме
    get_object.validate(get_object.get_data())
    # проверка полей на точное соответствие
    get_object.check_all_fields(valid_create_payload)
    # get_object.check_all_fields(invalid_create_payload)

