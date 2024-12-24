# * author: 黎愔

import os
import webbrowser
import ttkbootstrap
import json

# local
import core

afdian_liyin_link = 'https://afdian.com/a/ticca'
content = f"如果黎愔的插件对你有所帮助，欢迎在前往黎愔的爱发电 https://afdian.com/ticca 支持一下哦~ "
tip = f"如果黎愔的插件对你有所帮助，\n可以在'关于'界面中点击'黎愔的爱发电'\n前往黎愔的爱发电赞助支持一下哦~ "

def bin_open_afdian_liyin(*args):
    webbrowser.open(afdian_liyin_link)


def afdian_liyin(*args):
    self = core.window.interface.about

    if getattr(self, 'afdian_liyin', None) != 'afdian_liyin':        
        self.afdian_liyin = 'afdian_liyin'
        self.label_afdian_liyin = ttkbootstrap.Label(self.frame_afdian, text=">> 黎愔的爱发电 >>>", font=("黑体", 16), foreground="medium purple", cursor="hand2")
        self.label_afdian_liyin.pack(side="left", padx=(50, 0))

        self.label_afdian_liyin.bind("<Button-1>", bin_open_afdian_liyin)


def creat_afdian_liyin(name, version):
    try:
        self = core.window.interface.about

        afdian_liyin()

        path = os.path.join(core.env.directory.resources.cache, 'afdian_liyin.txt')
        json_path = os.path.join(core.env.directory.resources.cache, 'plugins_liyin.json')
        plugins = {}
        if not os.path.isdir(core.env.directory.resources.cache): os.mkdir(core.env.directory.resources.cache) 

        if os.path.isfile(json_path):
            with open(json_path, "r", encoding="utf-8") as file_object:
                file_content = file_object.read()

            plugins = json.loads(file_content)

        if not os.path.isfile(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)

        if plugins.get(name, None) != version:
            plugins[name] = version
            with open(json_path, 'w', encoding='utf-8') as f:  
                json.dump(plugins, f, ensure_ascii=False, indent=4)

            if getattr(self, 'has_showinfo', False) == False:   
                core.window.messagebox.showinfo(title='afdian_liyin', message=f'{tip}')
                self.has_showinfo = True
    except Exception as e:
        core.window.messagebox.showinfo(title=name, message=f' {e.__class__} {e}')
