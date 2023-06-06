class InvalidMethodException(Exception):
    """Raised when an invalid method is used"""
    pass






class ClientError(Exception):
    BUISNESS_ERROR_CODES = {
        100001: "signature verification failed",
        100202: "Insufficient balance",
        100400: "Invalid parameter",
        100440: "Order price deviates greatly from the market price",
        100500: "Internal system error",
        100503: "Server busy",
        80001: "request failed",
        80012: "service unavailable",
        80014: "Invalid parameter",
        80016: "Order does not exist",
        80017: "position does not exist"
    }

    def __init__(self, error_code: int, error_message: str) -> None:
        self.error_code = error_code
        self.error_message = error_message
        super().__init__(self.error_message if len(self.error_message) > 0 else self.BUISNESS_ERROR_CODES.get(self.error_code, "Unknown Error"))


class ServerError(Exception):
    ERROR_CODES = {
        400: "Bad Request - Invalid request format",
        401: "Unauthorized - Invalid API Key",
        403: "Forbidden - You do not have access to the requested resource",
        404: "Not Found",
        429: "Too Many Requests - Return code is used when breaking a request rate limit.",
        418: "return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.",
        500: "Internal Server Error - We had a problem with our server",
        503: "Limit requests per second",
        504: "return code means that the API server has submitted a request to the service center but failed to get a response. It should be noted that the 504 return code does not mean that the request failed. It refers to an unknown status. The request may have been executed, or it may have failed. Further confirmation is required."
    }

    def __init__(self, error_code: int, error_message: str) -> None:
        self.error_code = error_code
        self.error_message = error_message
        super().__init__(self.error_message if len(self.error_message) > 0 else self.ERROR_CODES.get(self.error_code, "Unknown Error"))
