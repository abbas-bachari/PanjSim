from PanjSim.user.user import User
from PanjSim.products.products import Products
from PanjSim.purchase.purchase import Purchase
from PanjSim.http_client import HttpClient
from typing import Any




class PanjSim:
    
    def __init__(self,api_key:str,proxy:dict|None=None) -> None:
        self.session=HttpClient(api_key,proxy)
        
    
    def User(self):
        return User(self.session)
    
    
    def Products(self):
        return Products(self.session)
    
   
    def Purchase(self):
        return Purchase(self.session)
    
    def get_countries_list(self) -> list[dict[str, Any]]:
        '''

        {   
            'afghanistan': 
                {'iso': {'af': 1}, 'prefix': {'+93': 1}, 'text_en': 'Afghanistan', 'text_ru': 'Афганистан', 'virtual21': {'activation': 1}, 'virtual23': {'activation': 1}, 'virtual32': {'activation': 1}, 'virtual35': {'activation': 1}, 'virtual4': {'activation': 1}},
            
            'albania': 
                {'iso': {'al': 1}, 'prefix': {'+355': 1}, 'text_en': 'Albania', 'text_ru': 'Албания', 'virtual21': {'activation': 1}, 'virtual23': {'activation': 1}, 'virtual32': {'activation': 1}, 'virtual4': {'activation': 1}},
            ....
        }
        
        '''
        endpoint = "/v1/guest/countries"
        

        response = self.session.get(endpoint)
        return response.json()
    
    def get_notification(self,lang:str) -> dict[str, Any]:
        '* lang: Language of notification, ru/en'
        endpoint = f"/v1/guest/flash/{lang}"
        response = self.session.get(endpoint)
        return response.json()
    def find_low_price(self,product:str,limit:int=10) -> dict|list:
        '''
        * if limit = 1 return dict low country price else return cost list
        + return {'cost': 8.4, 'count': 2741, 'rate': 6.84, 'contry': 'india', 'operator': 'virtual4'}
        + or: 
        + return [{'cost': 8.4, 'count': 2741, 'rate': 6.84, 'contry': 'india', 'operator': 'virtual4'}]
        '''
        product_price=self.Products().get_prices(product=product)
        product_price_data=product_price.get(product)
        
        new=[]
        
        for k in product_price_data:
            v=product_price_data[k]
            nv=[]
            for x,y in v.items():
                
                if y['count'] >=100:
                    nv.append((x,y))

            
            _sorted = sorted(nv, key=lambda x:x[1].get('cost'))
            if _sorted:
                dat=_sorted[0][1]
                dat['contry']=k
                dat['operator']=_sorted[0][0]
                new.append(dat)
        
        _sorted = sorted(new, key=lambda x:x.get('cost'))
        
        
        return _sorted[:limit] if limit > 1 else _sorted[0]