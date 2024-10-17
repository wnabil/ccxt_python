from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_common_symbols = publicGetCommonSymbols = Entry('common/symbols', 'public', 'GET', {'cost': 5})
    public_get_market_trades = publicGetMarketTrades = Entry('market/trades', 'public', 'GET', {'cost': 1})
    public_get_market_depth = publicGetMarketDepth = Entry('market/depth', 'public', 'GET', {'cost': 1})
    public_get_market_tickers = publicGetMarketTickers = Entry('market/tickers', 'public', 'GET', {'cost': 1})
    public_get_market_booktickers = publicGetMarketBookTickers = Entry('market/bookTickers', 'public', 'GET', {'cost': 1})
    public_get_market_klines = publicGetMarketKlines = Entry('market/klines', 'public', 'GET', {'cost': 1})
    private_get_account_balances = privateGetAccountBalances = Entry('account/balances', 'private', 'GET', {'cost': 1})
    private_get_trade_order = privateGetTradeOrder = Entry('trade/order', 'private', 'GET', {'cost': 1})
    private_get_trade_orderbyclientorderid = privateGetTradeOrderByClientOrderId = Entry('trade/orderByClientOrderId', 'private', 'GET', {'cost': 1})
    private_get_trade_openorders = privateGetTradeOpenOrders = Entry('trade/openOrders', 'private', 'GET', {'cost': 5})
    private_get_trade_allorders = privateGetTradeAllOrders = Entry('trade/allOrders', 'private', 'GET', {'cost': 5})
    private_get_trade_fills = privateGetTradeFills = Entry('trade/fills', 'private', 'GET', {'cost': 5})
    private_get_trade_fillsbyorderid = privateGetTradeFillsByOrderId = Entry('trade/fillsByOrderId', 'private', 'GET', {'cost': 5})
    private_post_trade_order = privatePostTradeOrder = Entry('trade/order', 'private', 'POST', {'cost': 1})
    private_post_trade_massorder = privatePostTradeMassOrder = Entry('trade/massOrder', 'private', 'POST', {'cost': 1})
    private_delete_trade_order = privateDeleteTradeOrder = Entry('trade/order', 'private', 'DELETE', {'cost': 1})
    private_delete_trade_allorders = privateDeleteTradeAllOrders = Entry('trade/allOrders', 'private', 'DELETE', {'cost': 1})
