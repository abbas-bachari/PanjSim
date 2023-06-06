from typing import Any



class User:
    def __init__(self, session) -> None:
        self.__session = session

    def get_balance(self) -> dict[str, Any]:
        

        endpoint = "/v1/user/profile"
        

        response = self.__session.get(endpoint)
        return response.json()

    

    def get_orders_history(self,category:str='activation', **args) -> list[dict[str, Any]]:
        """* Category: can be 'hosting' or 'activation'

        + limit:	Pagination limit
        + offset:	Pagination offset
        + order:	Pagination order, should be field name
        + reverse:	Is reversed history, true / false
        
        """
        
        endpoint = "/v1/user/orders"
        args["category"] =category
        payload=args

        response = self.__session.get(endpoint, payload)
        return response.json()
    def get_payments_history(self, **args) -> list[dict[str, Any]]:
        """ 
        + limit:	Pagination limit
        + offset:	Pagination offset
        + order:	Pagination order, should be field name
        + reverse:	Is reversed history, true / false
        
        """
        endpoint = "/v1/user/payments"
        

        response = self.__session.get(endpoint, args)
        return response.json()
    