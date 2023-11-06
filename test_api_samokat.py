# Петришин Дмитрий, 10-й поток — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


# тест на проверку, что по трек номеру можно получить данные о заказе
def test_create_and_get_order():
    response = sender_stand_request.post_new_order()
    track = response.json()["track"]

    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200
