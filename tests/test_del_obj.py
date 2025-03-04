from endpoints.delete_obj import DeleteObj


def test_delete_object(create_obj_with_data):
    f_ob_id, f_ject = create_obj_with_data

    # удалить объект
    del_object = DeleteObj()
    del_object.del_obj(f_ob_id)
    del_object.check_response_is_200()
    del_object.validate(del_object.get_data())

    assert f"Object with id = {f_ob_id} has been deleted." == del_object.get_delete_message(), \
        'wrong message for deleting'

    # Еще раз попытаемся удалить объект (уже удаленный)
    del_object.del_obj(f_ob_id)
    print(del_object.get_delete_error())

