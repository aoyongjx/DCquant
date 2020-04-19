import ccxt
exchange = ccxt.huobipro() # default id
okcoin1 = ccxt.huobipro({ 'id': 'okcoin1' })
okcoin2 = ccxt.huobipro({ 'id': 'okcoin2' })
id = 'huobipro'
btcchina = eval ('ccxt.%s ()' % id)
gdax = getattr (ccxt, 'gdax') ()

# from variable id
exchange_id = 'huobipro'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET',
    'timeout': 30000,
    'enableRateLimit': True,
})