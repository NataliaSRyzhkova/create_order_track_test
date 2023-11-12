import configuration
import requests

# Создаётся новый заказ
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)
# Запрос на получение заказа по номеру трека
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(track))
