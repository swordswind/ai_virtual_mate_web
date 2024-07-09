import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from PIL import Image, ImageTk
from gui_sub import *


def on_closing():
    if messagebox.askokcancel("确认退出", "您确定要退出AI虚拟伙伴Web版吗？"):
        root.destroy()


def open_setting_w():
    def save_and_close():
        with open('data/db/config.db', 'w', encoding='utf-8') as file:
            file.write(f'[虚拟伙伴名称]\n{mate_name_entry.get()}\n\n')
            file.write(f'[虚拟伙伴人设]\n{prompt_text.get("1.0", tk.END).strip()}\n\n')
            file.write(f'[用户名]\n{username_entry.get()}\n\n')
            file.write(f'[密码]\n{password_entry.get()}\n\n')
            file.write(f'[edge-tts音色]\n{speaker_menu.get()}\n\n')
            file.write(f'[edge-tts语速]\n{rate_entry.get()}\n\n')
            file.write(f'[edge-tts音高]\n{pitch_entry.get()}\n\n')
            file.write(f'[对话网页端口]\n{chatweb_port_entry.get()}\n\n')
            file.write(f'[角色网页端口]\n{live2d_port_entry.get()}\n\n')
            file.write(f'[本地AI引擎服务器IP]\n{server_ip_entry.get()}\n\n')
            file.write(f'[千问LLM服务端口]\n{qwen_port_entry.get()}\n\n')
            file.write(f'[LM Studio服务端口]\n{lmstudio_port_entry.get()}\n\n')
            file.write(f'[Ollama服务端口]\n{ollama_port_entry.get()}\n\n')
            file.write(f'[Ollama模型名称]\n{ollama_model_name_entry.get()}\n\n')
            file.write(f'[GPT-SoVITS端口]\n{gsv_port_entry.get()}\n\n')
            file.write(f'[自定义API-base_url]\n{custom_url_entry.get()}\n\n')
            file.write(f'[自定义API-api_key]\n{custom_key_entry.get()}\n\n')
            file.write(f'[自定义API-model]\n{custom_model_entry.get()}\n\n')
            file.write(f'[实时语音开关键]\n{voice_key_entry.get()}')
        messagebox.showinfo("保存成功", "保存成功！重启软件生效")
        setting_w.destroy()

    def restore_set():
        if messagebox.askokcancel("恢复默认设置", "您确定要重置AI虚拟伙伴Web吗？"):
            with open('data/db/config.db', 'w', encoding='utf-8') as file:
                file.write('[虚拟伙伴名称]\n三月七\n\n')
                file.write(f'[虚拟伙伴人设]\n你的名字是三月七。现在请你扮演[崩坏:星穹铁道]游戏中的[三月七]和我对话，[三月七]是一个活泼可爱的的少女，乐观好奇，随身携带相机记录冒险，与星穹列车同行。你的回答尽量不要超过30个字\n\n')
                file.write('[用户名]\n开拓者\n\n')
                file.write('[密码]\n12345678\n\n')
                file.write('[edge-tts音色]\n晓伊-年轻女声\n\n')
                file.write('[edge-tts语速]\n+0\n\n')
                file.write('[edge-tts音高]\n+10\n\n')
                file.write('[对话网页端口]\n5260\n\n')
                file.write('[角色网页端口]\n5261\n\n')
                file.write('[本地AI引擎服务器IP]\n127.0.0.1\n\n')
                file.write('[千问LLM服务端口]\n8088\n\n')
                file.write('[LM Studio端口]\n1234\n\n')
                file.write('[Ollama服务端口]\n11434\n\n')
                file.write('[Ollama模型名称]\nqwen2:0.5b\n\n')
                file.write('[GPT-SoVITS端口]\n9880\n\n')
                file.write('[自定义API-base_url]\n填入服务提供方地址，例如 https://api.siliconflow.cn/v1\n\n')
                file.write('[自定义API-api_key]\n填入从服务提供方控制台获取的密钥，例如 sk-xxxxxxxxxx\n\n')
                file.write('[自定义API-model]\n填入服务提供方支持的模型名称，例如 Qwen/Qwen2-7B-Instruct\n\n')
                file.write('[实时语音开关键]\nx')
            messagebox.showinfo("恢复默认设置成功", "恢复默认设置成功！重启软件生效")
            setting_w.destroy()

    setting_w = tk.Toplevel(root)
    setting_w.title("AI虚拟伙伴Web版软件设置")
    setting_w.minsize(810, 450)
    setting_w.maxsize(810, 450)
    setting_w.iconbitmap("data/image/logo.ico")
    logo_label2 = tk.Label(setting_w, image=logo_photo)
    logo_label2.place(x=10, y=10)
    tk.Label(setting_w, text="软件设置", font=("宋体", 18, "bold"), fg="#587EF4").place(x=45, y=11)
    tk.Label(setting_w, text="AI Virtual Mate Web", fg="#587EF4").place(x=155, y=13)
    tk.Label(setting_w, text='用户名:').place(x=75, y=50)
    username_entry = tk.Entry(setting_w, width=10, justify='center')
    username_entry.insert(tk.END, username)
    username_entry.place(x=50, y=75)
    tk.Label(setting_w, text='密码:').place(x=80, y=100)
    password_entry = tk.Entry(setting_w, width=10, justify='center')
    password_entry.insert(tk.END, password)
    password_entry.place(x=50, y=125)
    tk.Label(setting_w, text='虚拟伙伴名称:').place(x=50, y=150)
    mate_name_entry = tk.Entry(setting_w, width=10, justify='center')
    mate_name_entry.insert(tk.END, mate_name)
    mate_name_entry.place(x=50, y=175)
    tk.Label(setting_w, text='虚拟伙伴人设:').place(x=250, y=50)
    prompt_text = scrolledtext.ScrolledText(setting_w, width=13, height=9)
    prompt_text.insert(tk.END, prompt)
    prompt_text.place(x=250, y=75)
    tk.Label(setting_w, text='edge-tts音色:').place(x=50, y=200)
    speaker_list = ["晓伊-年轻女声", "晓晓-成稳女声", "云健-大型纪录片男声", "云希-短视频热门男声", "云夏-年轻男声",
                    "云扬-成稳男声", "晓北-辽宁话女声", "晓妮-陕西话女声", "晓佳-粤语成稳女声", "晓满-粤语年轻女声",
                    "云龙-粤语男声", "晓辰-台湾话年轻女声", "晓宇-台湾话成稳女声", "云哲-台湾话男声", "佳太-日语男声",
                    "七海-日语女声"]
    speaker_variable = tk.StringVar(setting_w)
    speaker_variable.set(speaker)
    speaker_menu = ttk.Combobox(setting_w, textvariable=speaker_variable, values=speaker_list, height=12, width=20,
                                state="readonly", justify='center', font=("宋体", 11))
    speaker_menu.place(x=25, y=225)
    tk.Label(setting_w, text='edge-tts语速:').place(x=50, y=250)
    rate_entry = tk.Entry(setting_w, width=4, justify='center')
    rate_entry.insert(tk.END, rate)
    rate_entry.place(x=85, y=275)
    tk.Label(setting_w, text='edge-tts音高:').place(x=50, y=300)
    pitch_entry = tk.Entry(setting_w, width=4, justify='center')
    pitch_entry.insert(tk.END, pitch)
    pitch_entry.place(x=85, y=325)
    tk.Label(setting_w, text="对话网页端口:").place(x=450, y=50)
    chatweb_port_entry = tk.Entry(setting_w, width=5, justify='center')
    chatweb_port_entry.insert(tk.END, chatweb_port)
    chatweb_port_entry.place(x=485, y=75)
    tk.Label(setting_w, text="角色网页端口:").place(x=450, y=100)
    live2d_port_entry = tk.Entry(setting_w, width=5, justify='center')
    live2d_port_entry.insert(tk.END, live2d_port)
    live2d_port_entry.place(x=485, y=125)
    tk.Label(setting_w, text="本地AI引擎服务器IP:").place(x=615, y=50)
    server_ip_entry = tk.Entry(setting_w, width=15, justify='center')
    server_ip_entry.insert(tk.END, local_server_ip)
    server_ip_entry.place(x=625, y=75)
    tk.Label(setting_w, text="千问LLM服务端口:").place(x=625, y=100)
    qwen_port_entry = tk.Entry(setting_w, width=5, justify='center')
    qwen_port_entry.insert(tk.END, qwen_port)
    qwen_port_entry.place(x=675, y=125)
    tk.Label(setting_w, text="LM Studio端口:").place(x=625, y=150)
    lmstudio_port_entry = tk.Entry(setting_w, width=5, justify='center')
    lmstudio_port_entry.insert(tk.END, lmstudio_port)
    lmstudio_port_entry.place(x=675, y=175)
    tk.Label(setting_w, text="Ollama服务端口:").place(x=625, y=200)
    ollama_port_entry = tk.Entry(setting_w, width=5, justify='center')
    ollama_port_entry.insert(tk.END, ollama_port)
    ollama_port_entry.place(x=675, y=225)
    tk.Label(setting_w, text="Ollama模型名称:").place(x=625, y=250)
    ollama_model_name_entry = tk.Entry(setting_w, width=15, justify='center')
    ollama_model_name_entry.insert(tk.END, ollama_model_name)
    ollama_model_name_entry.place(x=625, y=275)
    tk.Label(setting_w, text="GPT-SoVITS端口:").place(x=625, y=300)
    gsv_port_entry = tk.Entry(setting_w, width=5, justify='center')
    gsv_port_entry.insert(tk.END, gsv_port)
    gsv_port_entry.place(x=675, y=325)
    tk.Label(setting_w, text="实时语音开关键:").place(x=625, y=350)
    tk.Label(setting_w, text="Alt+").place(x=650, y=375)
    voice_key_entry = tk.Entry(setting_w, width=4, justify='center')
    voice_key_entry.insert(tk.END, voice_key)
    voice_key_entry.place(x=700, y=375)
    tk.Label(setting_w, text="自定义API-base_url:").place(x=5, y=350)
    custom_url_entry = tk.Entry(setting_w, width=60, justify='center', font=("宋体", 10))
    custom_url_entry.insert(tk.END, custom_url)
    custom_url_entry.place(x=200, y=355)
    tk.Label(setting_w, text="自定义API-api_key:").place(x=5, y=375)
    custom_key_entry = tk.Entry(setting_w, width=60, justify='center', font=("宋体", 10))
    custom_key_entry.insert(tk.END, custom_key)
    custom_key_entry.place(x=200, y=380)
    tk.Label(setting_w, text="自定义API-model:").place(x=5, y=400)
    custom_model_entry = tk.Entry(setting_w, width=60, justify='center', font=("宋体", 10))
    custom_model_entry.insert(tk.END, custom_model)
    custom_model_entry.place(x=200, y=405)
    tk.Label(setting_w, text="Honorably created\nby MVCH-AI Team", fg="green").place(x=225, y=265)
    tk.Label(setting_w, text="*本软件为开源免费的数字人聊天工具,\n仅供个人娱乐,严禁用于商业用途", fg="green",
             font=("宋体", 10)).place(x=190, y=315)
    tk.Label(setting_w,
             text="The flower of technology\nshould blossom freely,\npaving the stage for\nthe progress of civilization.",
             fg="green", font=("宋体", 10)).place(x=415, y=290)
    tk.Label(setting_w, text="版本信息:\nv1.0").place(x=465, y=150)
    tk.Button(setting_w, text="下载本地AI引擎",
              command=lambda: open_browser("https://swordswind.github.io/2024/03/13/engine"), bg="#3E92ED",
              fg="white").place(x=440, y=200)
    tk.Button(setting_w, text=" 恢复默认设置 ", command=restore_set, bg="#FF7700", fg="white").place(x=440, y=250)
    cancel_btn = tk.Button(setting_w, text="取消", command=setting_w.destroy)
    cancel_btn.place(x=650, y=405)
    save_btn = tk.Button(setting_w, text="保存", command=save_and_close, bg="#2A6EE9", fg="white")
    save_btn.place(x=725, y=405)
    tk.Label(setting_w, text="GitHub开源地址:https://github.com/swordswind/ai_virtual_mate_web", font=("宋体", 10),
             fg="green").place(x=0, y=430)
    setting_w.mainloop()


root = tk.Tk()
root.title("AI Virtual Mate Web v1.0 - AI虚拟伙伴Web版启动器")
root.minsize(810, 540)
root.maxsize(810, 540)
root.configure(bg="#FFFFFF")
root.option_add("*Background", "#FFFFFF")  # 设置所有组件底色
root.option_add("*Foreground", "black")  # 设置所有组件字体颜色
root.option_add('*Font', '宋体 15')
root.iconbitmap("data/image/logo.ico")
logo_img = Image.open("data/image/logo.png")
logo_img = logo_img.resize((25, 25), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_img)
logo_label = tk.Label(root, image=logo_photo)
logo_label.place(x=10, y=10)
tk.Label(root, text="AI虚拟伙伴Web", font=("宋体", 18, "bold"), fg="#587EF4").place(x=50, y=11)
tk.Label(root, text=f"欢迎,\n{username}").place(x=725, y=5)
tk.Label(root, text="多设备全平台通过浏览器，与虚拟伙伴同享美好时光").place(x=100, y=75)
tk.Label(root,
         text=f"此电脑访问:\n对话网址: http://127.0.0.1:{chatweb_port}\n角色网址: http://127.0.0.1:{live2d_port}").place(
    x=100, y=150)
tk.Button(root, text="打开对话", font=("宋体", 11),
          command=lambda: open_browser(f"http://127.0.0.1:{chatweb_port}")).place(x=425, y=165)
tk.Button(root, text="打开角色", font=("宋体", 11),
          command=lambda: open_browser(f"http://127.0.0.1:{live2d_port}")).place(x=425, y=195)
tk.Label(root,
         text=f"同一WiFi/局域网访问:\n对话网址: http://{server_ip}:{chatweb_port}\n角色网址: http://{server_ip}:{live2d_port}").place(
    x=100, y=250)
tk.Button(root, text="打开对话", font=("宋体", 11),
          command=lambda: open_browser(f"http://{server_ip}:{chatweb_port}")).place(x=485, y=265)
tk.Button(root, text="打开角色", font=("宋体", 11),
          command=lambda: open_browser(f"http://{server_ip}:{live2d_port}")).place(x=485, y=295)
tk.Label(root, text="实时语音交互:").place(x=50, y=350)
voice_options = ["开启", "关闭"]
voice_variable = tk.StringVar(root)
voice_variable.set(voice_switch)
voice_option_menu = ttk.Combobox(root, textvariable=voice_variable, values=voice_options, height=12, width=13,
                                 state="readonly", justify='center')
voice_option_menu.place(x=50, y=375)
tk.Label(root, text="对话语言模型:").place(x=300, y=350)
api_options = ["GLM-4-9B", "通义千问2-72B", "星火", "Gemini", "GPT-4", "GPT-3.5", "文心一言", "本地Qwen整合包",
               "本地LM Studio", "本地Ollama", "自定义API"]
api_variable = tk.StringVar(root)
api_variable.set(prefer_llm)  # 设置默认选中的 API 接口
api_option_menu = ttk.Combobox(root, textvariable=api_variable, values=api_options, height=12, width=13,
                               state="readonly", justify='center')
api_option_menu.place(x=300, y=375)
tk.Label(root, text="语音合成引擎:").place(x=550, y=350)
tts_options = ["微软云edge-tts", "VITS云服务1", "VITS云服务2", "VITS云服务3", "本地pyttsx3", "本地GPT-SoVITS", "关闭语音"]
tts_variable = tk.StringVar(root)
tts_variable.set(prefer_tts)  # 设置默认选中的语音合成引擎
tts_option_menu = ttk.Combobox(root, textvariable=tts_variable, values=tts_options, width=14, state="readonly",
                               justify='center', font=("宋体", 13))
tts_option_menu.place(x=550, y=375)
voice_input_label = tk.Label(root, text="", font=("宋体", 11))
voice_input_label.place(x=50, y=425)
voice_output_label = tk.Label(root, text="", font=("宋体", 11))
voice_output_label.place(x=50, y=475)
tk.Button(root, text="软件设置", command=open_setting_w, bg="#3E92ED", fg="white").place(x=700, y=495)
