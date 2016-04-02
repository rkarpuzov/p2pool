from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['mobiuscoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'fc70035c7abebc6f'.decode('hex')
PREFIX = '2472ef181abed37b'.decode('hex')
P2P_PORT = 9012
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9321
BOOTSTRAP_ADDRS = 'zetool.cointech.net pool.mobiuscoin.com 199.180.115.115 p2pool1.cointech.net p2pool.cointech.net 142.0.42.33'.split(' ')
ANNOUNCE_CHANNEL = '#mobiuscoin'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Bitcoin to >=0.8.6!' if v < 70001 else None
