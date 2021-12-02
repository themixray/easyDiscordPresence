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
