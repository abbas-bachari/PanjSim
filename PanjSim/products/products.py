from typing import Any





class Products:
    def __init__(self, session) -> None:
        self.__session=session

    def get_products(self,country:str,operator:str) -> dict[str, Any]:
        '''
        To receive the name, the price, quantity of all products, available to buy.

        https://5sim.net/docs/?python#products-request
        '''

        endpoint = f"/v1/guest/products/{country}/{operator}"
        

        response = self.__session.get(endpoint)
        return response.json()

    

    def get_prices(self,country:str|None=None,product:str|None=None) -> list[dict[str, Any]]:
        
        endpoint = "/v1/guest/prices"
        payload={}
        if country:
            payload['country']=country
        if product:
            payload['product']=product

        if len(payload.keys())==0:
            payload=None
        
        response = self.__session.get(endpoint, payload)
        return response.json()

