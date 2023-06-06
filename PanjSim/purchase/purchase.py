from typing import Any
from PanjSim.purchase.management import Management




class Purchase(Management):
    def __init__(self, session) -> None:
        self.__session=session
        Management.__init__(self,self.__session)
    def buy_activation_number(self,country:str,operator:str,product:str,**query) -> dict[str, Any]:
        '''
        * Query Parameters 
        
        + forwarding: Whether or not to enable forwarding
        + number: 	  Number for which the call will be forwarded, only the Russian numbers, 11 digits, without the + sign
        + reuse: 	  If equal to "1" buy with the ability to reuse the number, if available
        + voice: 	  If equal to "1" buy with the ability to receive a call from the robot, if available
        + ref: 	      Your referral key if you have it, if you are developer of the software, you can read terms here
        '''

        endpoint = f"/v1/user/buy/activation/{country}/{operator}/{product}"
    

        response = self.__session.get(endpoint,query)
        return response.json()

    

    def buy_hosting_number(self,country:str,operator:str,product:str) -> dict[str, Any]:
        """
        country:    The country, "any" - any country
        operator:   The operator, "any" - any operator
        product:    Product name, {3hours, 1day}
        """
        
        endpoint = f"/v1/user/buy/hosting/{country}/{operator}/{product}"
        response = self.__session.get(endpoint)
        return response.json()
    
    def rebuy_number(self, product:str,number:str) -> list[dict[str, Any]]:
        
        endpoint = f"/v1/user/reuse/{product}/{number}"
        response = self.__session.get(endpoint)
        return response.json()