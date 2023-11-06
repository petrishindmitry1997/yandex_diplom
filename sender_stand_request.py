import requests
import configuration
import data


# запрос на создание нового заказа
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.body,
                         headers=data.headers)


# запрос на получения закааз по треку
def get_order_by_track(track):
    params = {'t': track}
    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                            params=params,
                            headers=data.headers)
    return response
