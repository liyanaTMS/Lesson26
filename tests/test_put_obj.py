
from endpoints.put_obj import UpdateObj
from payload.payload import valid_update_payload
from endpoints.get_obj import GetObj


def test_update_object(create_obj_with_data):
    f_ob_id, f_object = create_obj_with_data

    # обновить объект (добавить color=red)
    update_obj = UpdateObj()
    update_obj.put_obj(f_ob_id, valid_update_payload)
    # валидация полей на типы данных по схеме
    update_obj.validate(update_obj.get_data())
    # проверка респонса 200
    update_obj.check_response_is_200()
    # проверка полей на точное соответствие
    update_obj.check_all_fields(valid_update_payload)

    # гетнуть обновленный объект
    get_object = GetObj()
    get_object.get_obj(f_ob_id)
    get_object.check_all_fields(valid_update_payload)









