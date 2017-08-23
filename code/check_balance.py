from electrum import Network
from electrum.util import json_encode, print_msg
import json


n = Network()
n.start()

addr = '1ByMK9Q5HnLmoewQ5ji8wjrJgdkanBngSL'

h = n.synchronous_get(('blockchain.address.get_balance', [addr]))
print(h)
print h.get('confirmed')
