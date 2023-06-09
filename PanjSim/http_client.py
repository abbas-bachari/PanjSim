from json.decoder import JSONDecodeError
from typing import Any
from PanjSim.errors import *
import requests



class HttpClient:
    __BASE_URL = "https://5sim.net"
   

    def __init__(self, api_key: str,proxies:dict|None=None) -> None:
        
        
        self.__session = requests.Session()
        self.__session.headers.update({'Authorization': f'Bearer {api_key}','Accept': 'application/json'})
        if proxies:
            self.__session.proxies=proxies

   

    def _generate_query_string(self, payload: dict[str, Any] = {}) -> str:
        """
        It takes a payload and returns a query string

        + payload: The payload that you want to convert to a query string
        * return: A string of the query string
        """

        
        query_string = '&'.join(f'{k}={v}' for k, v in payload.items() if v)
        
        return query_string

    def _request(self, method: str, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {},data=None) -> requests.Response:
        """
        It takes a method, endpoint, payload, and headers, and returns a respons
        + method: The HTTP method to use (GET, POST, PUT, DELETE)
        + endpoint: The endpoint you want to hit i.e. /v1/guest/countries
        + payload:  The data to be sent to the server
        + headers:  This is a dictionary of headers that will be sent with the request
        + data:     The data to be sent to the server by post metod
        """
        if headers:
            self.__session.headers.update(headers)

        url = f"{self.__BASE_URL}{endpoint}?{self._generate_query_string(payload)}" if payload else f"{self.__BASE_URL}{endpoint}"
        match method:
            case "GET":
                req = self.__session.get(url)
            case "POST":
                req = self.__session.post(url,data=data)
            case "PUT":
                req = self.__session.put(url)
            case "DELETE":
                req = self.__session.delete(url)
            case _:
                raise InvalidMethodException(f"Invalid method used: {method}")

        if req.status_code != 200:
            
            raise ServerError(req.status_code, req.text)

        try:
            req_json: dict[str, Any] = req.json()
        
        except JSONDecodeError: 
            raise ErrorJSONDecode(req.status_code,req.text)
        
        else:
            if isinstance(req_json, dict):
               return req
            
            raise ClientError(req.status_code, req.text)
            

    def get(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a GET request to the given endpoint with the given payload and headers

        + endpoint: The endpoint you want to hit i.e. /v1/guest/countries
        + payload: The data to be sent to the server
        + headers: This is a dictionary of headers that will be sent with the request
        * return: A response object
        """

        return self._request("GET", endpoint, payload, headers)

    def post(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {},data=None) -> requests.Response:
        """
        It makes a POST request to the given endpoint with the given payload and headers

        + endpoint: The endpoint you want to hit i.e. /v1/guest/countries
        + payload: The data to be sent to the server
        + headers: This is a dictionary of headers that will be sent with the request
        + data:     The data to be sent to the server by post metod
        * return: A response object
        """

        return self._request("POST", endpoint, payload, headers,data=data)

    def put(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a PUT request to the given endpoint with the given payload and headers

        + endpoint: The endpoint you want to hit i.e. /v1/guest/countries
        + payload: The data to be sent to the server
        + headers: This is a dictionary of headers that will be sent with the request
        * return: A response object
        """

        return self._request("PUT", endpoint, payload, headers)

    def delete(self, endpoint: str, payload: dict[str, Any] = {}, headers: dict[str, Any] = {}) -> requests.Response:
        """
        It makes a DELETE request to the given endpoint with the given payload and headers

        + endpoint: The endpoint you want to hit i.e. /v1/guest/countries
        + payload: The data to be sent to the server
        + headers: This is a dictionary of headers that will be sent with the request
        * return: A response object
        """

        return self._request("DELETE", endpoint, payload, headers)