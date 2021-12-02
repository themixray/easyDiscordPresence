# Easy Discord Presence
[Original](https://github.com/LennyPhoenix/py-discord-sdk)
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
Source of [rpc.activity](https://github.com/LennyPhoenix/py-discord-sdk/blob/master/discordsdk/model.py)
