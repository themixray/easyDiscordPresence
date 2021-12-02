import threading
import time
import os
try:
    import discordsdk as dsdk
except OSError:
    import urllib.request
    import win32api
    import pathlib
    url = 'http://main.trackly.site/discord_game_sdk.dll'
    src = win32api.GetFullPathName(__file__)
    src = str(pathlib.Path(src).parent)+'\\'
    try:
        os.mkdir(src+'lib')
    except: pass
    with open(src+'lib\\discord_game_sdk.dll','wb') as f:
        f.write(urllib.request.urlopen(url).read())
        f.close()
    while 1:
        try:
            import discordsdk as dsdk
            break
        except: pass

class presence:
    def __init__(self, client_id):
        self._started = False
        self.client_id = client_id
    def connect(self):
        if not self._started:
            self.app = dsdk.Discord(self.client_id, dsdk.CreateFlags.default)
            self.activity_manager = self.app.get_activity_manager()
            self.activity = dsdk.Activity()
            self.update()
            self._started = True
            def cb(self):
                while self._started:
                    time.sleep(1/10)
                    self.app.run_callbacks()
            threading.Thread(target=lambda: cb(self), daemon=True).start()
    def disconnect(self):
        if self._started:
            self._started = False
            del self.app
    def update(self):
        if self._started:
            def callback(result):
                if result != dsdk.Result.ok:
                    print(result)
            self.activity_manager.update_activity(self.activity, callback)
d = presence(772915052969197619)
d.connect()

d.activity.state = '123'
d.update()

input()
d.disconnect()
# import requests
#
# print(requests.get('https://gist.githubusercontent.com/themixray/d5b5f4b69f08b16fa1a0dc5f281444b3/raw/9e16e1e251d0b9667377c4a2d7b9e8bdf3b36ee0/discord_game_sdk.dll').content)
