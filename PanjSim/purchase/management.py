from typing import Any





class Management:
    def __init__(self,http_manager) -> None:
        self.__session = http_manager

    def check_order(self,order_id:str) -> dict[str, Any]:
        endpoint = f"/v1/user/check/{order_id}"
        response = self.__session.get(endpoint)
        return response.json()
    def finish_order(self,order_id:str) -> dict[str, Any]:
        endpoint = f"/v1/user/finish/{order_id}"
        response = self.__session.get(endpoint)
        return response.json()

    def cancel_order(self,order_id:str) -> dict[str, Any]:
        endpoint = f"/v1/user/cancel/{order_id}"
        response = self.__session.get(endpoint)
        return response.json()
    
    def ban_order(self,order_id:str) -> dict[str, Any]:
        endpoint = f"/v1/user/ban/{order_id}"
        response = self.__session.get(endpoint)
        return response.json()
    def get_sms_inbox(self,order_id:str) -> dict[str, Any]:
        endpoint = f"/v1/user/sms/inbox/{order_id}"
        response = self.__session.get(endpoint)
        return response.json()
    
    