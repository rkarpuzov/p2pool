import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 11080
ADDRESS_VERSION = 0
RPC_PORT = 21080
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
        (yield helper.check_genesis_block(bitcoind, '0000000040a867146dcc50bee85f69ac20addc33080c2a769c01200920251955')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 10000*100000000 >= (height)//20000
POW_FUNC = data.hash256
BLOCK_PERIOD = 60 # s
SYMBOL = 'AU'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Aurumcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Aurumcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/'), 'coin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
