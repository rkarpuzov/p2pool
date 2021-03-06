import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 11012
ADDRESS_VERSION = 0
RPC_PORT = 21012
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'mobiuscoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'MOBI'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Mobiuscoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Mobiuscoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.mobiuscoin'), 'mobiuscoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
