[![Abbas Bachari](https://img.shields.io/badge/Abbas%20Bachari-PanjSim-green?style=plastic&logo=codemagic)](https://github.com/abbas-bachari/PanjSim)
[![python](https://img.shields.io/badge/Python%20-3.6+-green?style=plastic&logo=Python)](https://python.org)

# معرفی PanjSim 
یک کتابخانه ساده پایتون نوشته شده برای [5sim.net](https://5sim.net)
#

# خدمات [5sim.net](https://5sim.net)
شماره های مجازی برای دریافت پیامک و فعال سازی هر سرویس
پس از ثبت نام در شبکه های اجتماعی، پیام رسان ها، پلتفرم های C2C و سایر وب سایت ها، فعال سازی حساب کاربری پیامکی الزامی است. 5SIM این فرصت را فراهم می کند تا با کمک یک شماره تلفن مجازی موقت، بدون استفاده از شماره شخصی، روند تأیید را دور بزنید. با دریافت کد تایید آنلاین، پروفایل های زیادی را در وب سایت ها ثبت کنید.

#

## راهنمای نصب
قبل از ادامه، باید یک حساب در [5sim.net](https://5sim.net/) و [یک کلید API شخصی](https://5sim.net/settings/security) برای استفاده ثبت کنید. 
#

نصب از سورس کد:

``` bash
pip install git+https://github.com/abbas-bachari/PanjSim.git
```

نصب از  [PyPI](https://pypi.org/project/PanjSim/):

```bash
pip install 5sim-python
```
<hr>

## راهنمای استفاده

###  Client - اتصال به سرویس

```python
from PanjSim import PanjSim

# کلید خود را جایگذین کنید
API_KEY = 'eyJhbGciOiJSUzUx.....' 

client = PanjSim(API_KEY) 
```
 

### Endpoints - منابع اولیه
Official docs [here-مستندات](https://docs.5sim.net/)
#


### U. اطلاعات حساب

```python

user=client.User()

# U. گرفتن موجودی حساب
balance=user.get_balance()


# U. گرفتن تاریخچه سفارشات
order_history=user.get_orders_history()


# U. گرفتن تاریخچه تراکنش ها
pyment_history=user.get_payments_history()

```
#
### P. قیمت و محصولات

```python

from PanjSim.Countrys import usa

country=usa
product=client.Products()

# P. گرفتن محصولات یک کشور بر اساس اوپراتور
operator=country.operators.virtual23.name
product.get_products(country=country.name,operator=operator)


# P. گرفتن قیمت تمام محصولات
product.get_prices()

# P. گرفتن قیمت محصولات بر اساس کشور
product.get_prices(country=usa.name)

# P. گرفتن قیمت محصول بر اساس کشور
product.get_prices(country=usa.name,product="telegram")

```
#
### O. خرید کردن

```python
from PanjSim.Countrys import usa

country=usa
Purchase=client.Purchase()


# o. خرید شماره جدید
operator=country.operators.virtual23.name
order=Purchase.buy_activation_number(country=country.name,operator=operator,product='telegram')

# o. بررسی وضعیت خرید - دریافت کد اس ام اس
Purchase.check_order(order_id=order['id'])

# o. مسدود کردن شماره
Purchase.ban_order(order_id=order['id'])

# o. لغو خرید
Purchase.cancel_order(order_id=order['id'])

# o. پایان دادن به خرید
Purchase.finish_order(order_id=order['id'])

# o. گرفتن لیست پیامها
Purchase.get_sms_inbox(order_id=order['id'])

# o. خرید مجدد
Purchase.rebuy_number(product="telegram",number='+177777')

# o. اجاره کردن شماره
Purchase.buy_hosting_number(country=country.name,operator='any',product='1day')
```
#
### M. امکانات بیشتر

```python
# m. گرفتن اعلان سایت
client.get_notification(lang='en')

# m. گرفتن لیست کشورها مراه با اپراتور و محصولات
client.get_countries_list()

# m. پیداکردن ارزانترین قیمت
client.find_low_price(product='telegram',limit=5)
```
Powered by [Abbas Bachari](https://github.com/abbas-bachari).
