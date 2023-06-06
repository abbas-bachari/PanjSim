[![Abbas Bachari](https://img.shields.io/badge/Abbas%20Bachari-PanjSim-green?style=plastic&logo=codemagic)](https://github.com/abbas-bachari/PanjSim)
[![python](https://img.shields.io/badge/Python%20-3.7+-green?style=plastic&logo=Python)](https://python.org)

# What is PanjSim ?
A simple Python API for [5sim.net](https://5sim.net)
#

# About [5sim.net](https://5sim.net)
Virtual numbers for receiving SMS and activation of any service

Upon registration on social networks, messengers, C2C platforms and on other websites, an SMS activation of account is required. 5SIM provides the opportunity to bypass verification procedure with the help of a temporary virtual phone number, without using the personal one. Register many profiles on websites, by receiving a confirmation code online.
#

## Installation guide
Before proceeding, you should register an account on [5sim.net](https://5sim.net/) and [generate a personal API key](https://5sim.net/settings/security) to use. 


#

Install from source:
``` bash
pip install git+https://github.com/abbas-bachari/PanjSim.git
```

Alternatively, install from [PyPI](https://pypi.org/project/PanjSim/):

```bash
pip install PanjSim
```
<hr>

## user manual

###  Client 

```python
from PanjSim import PanjSim

# Replace your API key...
API_KEY = 'eyJhbGciOiJSUzUx.....' 

client = PanjSim(API_KEY) 
```
 

### Endpoints 
Official docs [here](https://docs.5sim.net/)
#


### Account Information

```python

user=client.User()

# Get account balance
balance=user.get_balance()


# Get Orders history
order_history=user.get_orders_history()


# Get payments history
pyment_history=user.get_payments_history()

```
#
### Price and products

```python

from PanjSim.Countrys import usa

country=usa


product=client.Products()

# Receive the name, the price, quantity of all products, available to buy.
operator=country.operators.virtual23.name
product.get_products(country=country.name,operator=operator)


# Get all product prices
product.get_prices()

# Get product prices by country
product.get_prices(country=usa.name)

# Get product prices for a specific product
product.get_prices(product="telegram")

# Get product prices by country and specific product
product.get_prices(country=usa.name,product="telegram")

```
#
### Purchase

```python
from PanjSim.Countrys import usa

country=usa
Purchase=client.Purchase()


# Buy activation number
operator=country.operators.virtual23.name
order=Purchase.buy_activation_number(country=country.name,operator=operator,product='telegram')

# Check order (Get SMS)
Purchase.check_order(order_id=order['id'])

# Ban order
Purchase.ban_order(order_id=order['id'])

# Cancel order
Purchase.cancel_order(order_id=order['id'])

# Finish order
Purchase.finish_order(order_id=order['id'])

# Get SMS inbox list
Purchase.get_sms_inbox(order_id=order['id'])

# Re-buy number
Purchase.rebuy_number(product="telegram",number='+177777')

# Buy hosting number
Purchase.buy_hosting_number(country=country.name,operator='any',product='1day')
```
#
### More features

```python
# Get notifications
client.get_notification(lang='en')

# Get countries list
client.get_countries_list()

# Find the cheapest price
client.find_low_price(product='telegram',limit=5)
```
Powered by [Abbas Bachari](https://github.com/abbas-bachari).
