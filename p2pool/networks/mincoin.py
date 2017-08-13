from p2pool.bitcoin import networks

PARENT=networks.nets['mincoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=15 # blocks
IDENTIFIER='6031F5b8c6924210'.decode('hex')
PREFIX='6290192ba6d4729a'.decode('hex')
P2P_PORT=8732
MIN_TARGET=0
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=9773
BOOTSTRAP_ADDRS='fst.cointech.net'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-min'
VERSION_CHECK=lambda v: True
VERSION_WARNING=lambda v: 'Upgrade Mincoin to >= 0.8.5.1!' if v < 70002 else None
