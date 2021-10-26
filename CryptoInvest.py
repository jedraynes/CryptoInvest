"""
This program is intended to deposit a set amount into my Coinbase Pro account and purchase designated crypto assets using the deposited funds. It's my understanding that this feature only exists in Coinbase (regular) and is not available in Coinbase Pro. Given that Coinbase Pro has lower transaction fees, it makes sense to have this process on Coinbase Pro.

Packages: cbpro
- https://github.com/danpaquin/coinbasepro-python

Thanks to Rhett Reisman for the layer assistance.
- https://rhett.blog/2021/02/05/buy-bitcoin-everyday-2/

jedraynes.com
"""


# import packages
import cbpro
import json



"""
# sandbox parameters
sandbox_key = "[SECRET]"
sandbox_b64secret = "[SECRET]"
sandbox_passphrase = "[SECRET]"
sandbox_url = "https://api-public.sandbox.pro.coinbase.com"
"""

# production parameters
production_key = "[SECRET]"
production_b64secret = "[SECRET]"
production_passphrase = "[SECRET]"



def lambda_handler(event, context):

    # initialize the client
    auth_client = cbpro.AuthenticatedClient(key = production_key, 
                                            b64secret = production_b64secret, 
                                            passphrase = production_passphrase) # api_url = sandbox_url

    # order parameters
    currency = "USD"
    production_payment_method_id = auth_client.get_payment_methods()[0]["id"]
    #sandbox_payment_method_id = "[SECRET]"
    deposit_amount = "100.00"
    btc_amount = "75.00"
    eth_amount = "25.00"
    btc_product = "BTC-USD"
    eth_product = "ETH-USD"

    # deposit funds
    auth_client.deposit(currency = currency, 
                        payment_method_id = production_payment_method_id,
                        amount = deposit_amount)

    # purchase BTC
    auth_client.place_market_order(product_id = btc_product, 
                                   side = "buy", 
                                   funds = btc_amount)
    
    # purchase ETH
    auth_client.place_market_order(product_id = eth_product, 
                                   side = "buy", 
                                   funds = eth_amount)
                                                                      
                                   
    return {
        'statusCode': 200,
        'body': json.dumps(f"Bought ${btc_amount} of {btc_product[0:3]} and ${eth_amount} of {eth_product[0:3]}.")
    }