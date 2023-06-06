from typing import Any





class Vendor:
    def __init__(self, session) -> None:
        self.__session=session

    def get_vendor(self) -> dict[str, Any]:
        '''
        To receive the name, the price, quantity of all products, available to buy.

        https://5sim.net/docs/?python#products-request
        '''

        endpoint = "/v1/user/vendor"
        

        response = self.__session.get(endpoint)
        return response.json()

    

    def wallets_reserve(self) -> list[dict[str, Any]]:
        
        endpoint = "/v1/vendor/wallets"
        
        
        response = self.__session.get(endpoint)
        return response.json()
    
    def orders_history(self,category:str='activation',**args) -> list[dict[str, Any]]:
        
        endpoint = "/v1/vendor/orders"
        args["category"] =category
        payload=args

        response = self.__session.get(endpoint, payload)
        return response.json()
        
        
    def payments_history(self,**args) -> list[dict[str, Any]]:
        
        endpoint = "/v1/vendor/payments"
        
        payload=args if len(args.keys()) > 0 else None
        
        response = self.__session.get(endpoint, payload)
        return response.json()
    def withdraw(self,receiver:str,method:str,amount:str,fee:str="unitpay") -> dict[str, Any]:
        '''
        + receiver: Receiver
        + method  : Output method visa / qiwi / yandex
        + amount  : Amount
        + fee 	  : Payment system fkwallet / payeer / unitpay
        
        * return:


        '''
        endpoint = "/v1/vendor/withdraw"
        
        data='{"receiver":"%s","method":"%s","amount":"%s","fee":"%s"}'%(receiver,method,amount,fee)

        response = self.__session.post(endpoint, data=data)
        return response.json()
    
    