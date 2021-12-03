import threading
import time
try:
    import discordsdk as dsdk
except OSError:
    import requests,win32api,zipfile,\
           pathlib,randstr,struct,shutil,os
    src = pathlib.Path(win32api.GetFullPathName(__file__)).parent
    ap = lambda x: f'{src}\\{x}'
    try: os.mkdir(ap('lib'))
    except: pass
    tp = f'temp_{randstr.randstr(15)}.zip'
    with open(ap(tp),'wb') as f:
        url = 'https://dl-game-sdk.discordapp' \
              '.net/2.5.8/discord_game_sdk.zip'
        f.write(requests.get(url).content)
        f.close()
    with zipfile.ZipFile(ap(tp),'r') as z:
        t = "_64"if(struct.calcsize("P")*8==64)else""
        z.extract(f'lib/x86{t}/discord_game_sdk.dll')
        shutil.move(f'lib/x86{t}/discord_game_sdk.dll',
        ap('lib/discord_game_sdk.dll'))
    os.remove(tp)
    def tryingToRemove():
        while 1:
            try:os.remove(f'lib/x86{t}');break
            except:pass
    threading.Thread(
    target=tryingToRemove,
    daemon=True).start()
    import discordsdk as dsdk
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
            self.activity_manager.update_activity(self.activity,lambda x:None)
