from endpoints.create_obj import CreateObj
from endpoints.get_obj import GetObj
from endpoints.put_obj import UpdateObj
from payload.payload import valid_create_payload
from payload.payload import invalid_create_payload
from payload.payload import valid_update_payload
from endpoints.delete_obj import DeleteObj


def test_e2e_scenario(create_obj_with_data):

    # создание объекта
    f_ob_id, f_object = create_obj_with_data

    f_object.check_response_is_200()
    f_object.validate(f_object.get_data())
    f_object.check_all_fields(valid_create_payload)
    #f_object.check_all_fields(invalid_create_payload)

    # гетнуть созданный объект
    get_object = GetObj()
    get_object.get_obj(f_ob_id)
    get_object.check_all_fields(valid_create_payload)
    get_object.check_response_is_200()
    get_object.validate(get_object.get_data())

    # обновить объект (добавить color=red)
    update_obj = UpdateObj()
    update_obj.put_obj(f_ob_id, valid_update_payload)
    update_obj.validate(update_obj.get_data())
    update_obj.check_response_is_200()
    update_obj.check_all_fields(valid_update_payload)
    #update_obj.check_all_fields(invalid_create_payload)

    # гетнуть обновленный объект
    get_object.get_obj(f_ob_id)
    get_object.check_all_fields(valid_update_payload)

    # удалить объект
    del_object = DeleteObj()
    del_object.del_obj(f_ob_id)
    del_object.check_response_is_200()
    del_object.validate(del_object.get_data())

    assert f"Object with id = {f_ob_id} has been deleted." == del_object.get_delete_message(), \
        'wrong message for deleting'

    # Еще раз попытаться удалить объект (уже удаленный)
    del_object.del_obj(f_ob_id)
    print(del_object.get_delete_error())







