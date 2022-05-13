import requests
from datetime import datetime


def get_ticker_info_from_yobit(request):
    try:
        names_of_coins = request.lower()[6:].split(" to ")
        req = requests.get(f"https://yobit.net/api/3/ticker/"
                           f"{names_of_coins[0].strip()}_{names_of_coins[1].strip()}")
        response = req.json()
        info_of_ticker = response[f"{names_of_coins[0].strip()}_{names_of_coins[1].strip()}"]
        items = ["High", "Low", "Avg", "Vol", "Last", "Buy", "Sell"]
        answer = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n" \
                 f"Информация по паре {names_of_coins[0].strip()} to {names_of_coins[1].strip()}:\n\n"
        for item in items:
            answer += f"{item}: {info_of_ticker[item.lower()]}\n"
        return answer
    except Exception as ex:
        print(ex)

        return "Оооу... Что-то пошло не так, возможно, данная пара не торгуется на выбранной вами бирже," \
               " попробуйте снова:("


def get_orders_info_from_yobit(request):
    try:
        names_of_coins = request.lower()[6:].split(" to ")
        req = requests.get(f"https://yobit.net/api/3/depth/"
                           f"{names_of_coins[0].strip()}_{names_of_coins[1].strip()}"
                           f"?limit={5}&ignore_invalid=1")
        response = req.json()
        info_of_orders = response[f"{names_of_coins[0].strip()}_{names_of_coins[1].strip()}"]
        items = ["asks", "bids"]
        answer = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n" \
                 f"Наиболее выгодные предложения по паре" \
                 f" {names_of_coins[0].strip()} to {names_of_coins[1].strip()}:\n"

        for item in items:
            array_of_orders = info_of_orders[item]
            map = {"asks": "Покупка", "bids": "Продажа"}
            answer += f"\n{map[item]}:\n"
            for order in array_of_orders:
                answer += f"Цена: {order[0]},   Объем: {order[1]}\n"
        return answer
    except Exception as ex:
        print(ex)

        return "Оооу... Что-то пошло не так, возможно, данная пара не торгуется на выбранной вами бирже," \
               " попробуйте снова:("