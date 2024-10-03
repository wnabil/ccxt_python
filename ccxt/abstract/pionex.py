from ccxt.base.types import Entry


class ImplicitAPI:
    public_get_Symbols = publicGetSymbols = Entry('common/symbols', 'public', 'GET', {'cost': 5})
    public_get_tickers = publicGetTickers = Entry('market/tickers', 'public', 'GET', {'cost': 1})
    public_get_book_tickers = publicGetBookTickers = Entry('market/bookTickers', 'public', 'GET', {'cost': 1})
    public_get_trades = publicGetTrades = Entry('market/trades', 'public', 'GET', {'cost': 1})
    public_get_depth = publicGetDepth = Entry('market/depth', 'public', 'GET', {'cost': 1})
    public_get_market_klines = publicGetMarketKlines = Entry('market/klines', 'public', 'GET', {'cost': 1})
    private_get_account_balances = privateGetAccountBalances = Entry('account/balances', 'private', 'GET', {'cost': 1})
    private_get_all_orders = privateGetAllOrders = Entry('trade/allOrders', 'private', 'GET', {'cost': 5})
    private_get_open_orders = privateGetOpenOrders = Entry('trade/openOrders', 'private', 'GET', {'cost': 5})
    private_get_order = privateGetOrder = Entry('trade/order', 'private', 'GET', {'cost': 5})
    private_get_order_by_client_order_id = privateGetOrderByClientOrderId = Entry('trade/orderByClientOrderId', 'private', 'GET', {'cost': 5})
    private_get_fills = privateGetFills = Entry('trade/fills', 'private', 'GET', {'cost': 5})
    private_get_fills_by_order_id = privateGetFillsByOrderId = Entry('trade/fillsByOrderId', 'private', 'GET', {'cost': 5})
    private_delete_cancel_order = privateDeleteCancelOrder = Entry('trade/order', 'private', 'DELETE', {'cost': 1})
    private_delete_all_orders = privateDeleteAllOrders = Entry('trade/allOrders', 'private', 'DELETE', {'cost': 1})
    private_post_new_order = privatePostNewOrder = Entry('trade/order', 'private', 'POST', {'cost': 1})
    private_post_new_mass_order = privatePostNewMassOrder = Entry('trade/massOrder', 'private', 'POST', {'cost': 1})
    