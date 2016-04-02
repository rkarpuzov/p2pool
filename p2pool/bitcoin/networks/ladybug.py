import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 12333
ADDRESS_VERSION = 0
RPC_PORT = 22333
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
        (yield helper.check_genesis_block(bitcoind, '0000000066247638c1b022cb6f224c2600e6ad8d3d1bb48e869bb7a153f3be1d')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 10000*100000000 >= (height)//20000
POW_FUNC = data.hash256
BLOCK_PERIOD = 60 # s
SYMBOL = 'BUGS'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Ladybug') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Ladybug/') if platform.system() == 'Darwin' else os.path.expanduser('~/.ladybug'), 'ladybug.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/address/'
TX_EXPLORER_URL_PREFIX = 'http://mobiblocks.cointech.net/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
