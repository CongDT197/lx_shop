# role
CUSTOMER = 1
ADMIN = 2

# gender
MALE = 1
FEMALE = 2
OTHER = 3

# cart status
CONFIRMING = 1
CONFIRMED = 2
SHIPPING = 3
RECEIVED = 4

# product type
DIGITAL = 1
MEN_WEAR = 2
WOMEN_WEAR = 3
HEAL = 4
BABY = 5
FASHION = 6
GENERAL = 7

# size of wear
S = 1
M = 2
L = 3
XL = 4
NONE_SIZE = 5

# color of wear
RED = 1
YELLOW = 2
BLACK = 3
BLUE = 4
NONE_COLOR = 5

# pay_type
PAYBYCARD = 1
PAYOFFLINE = 2

#
# def validate_product_info(self, value):
#     for new_cart_product in value:
#         product_info = new_cart_product['product_info_id']
#         quantity = new_cart_product['quantity']
#         if (product_info.quantity - quantity) < 0:
#             raise ValidationError('ENOUGH_PRODUCT_QUANTITY')
#
#     return value
#
