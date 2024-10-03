import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import ccxt  # noqa: F402
from ccxt.base.errors import BadRequest  # noqa E402

def test_json():
    exchange = ccxt.Exchange({
        'id': 'regirock',
    })
    # Test: object
    obj = {
        'k': 'v',
    }
    obj_json = exchange.json(obj)
    assert obj_json == '{"k":"v"}'
    # Test: list
    list = [1, 2]
    list_json = exchange.json(list)
    assert list_json == '[1,2]'
    try:
        raise BadRequest('some error')
    except Exception as e:
        err_string = exchange.json(e)
        assert err_string == '{"name":"BadRequest"}'
    # Test: json a string
    str = 'ccxt, rocks!'
    serialized_string = exchange.json(str)
    assert serialized_string == '"ccxt, rocks!"'
