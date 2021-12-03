# Easy Discord Presence
[Original](https://github.com/LennyPhoenix/py-discord-sdk)

**Requires:**
* pywin32
* discordsdk
## Quick Start
```python
from edp import presence

rpc = presence(clientID)
rpc.connect()

rpc.activity.state = 'Example'
rpc.update()

input('Close ')
rpc.disconnect()
```
Source of [rpc.activity](https://github.com/LennyPhoenix/py-discord-sdk/blob/963fd0b137fccbf64c53665130168dcbdfd86cae/discordsdk/sdk.py#L113)
