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
