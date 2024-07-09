import signal
import pyaudio
import vosk
from main_sub import *
import keyboard as kb

say_text = ""


def refresh_preference():
    global voice_switch, prefer_llm, prefer_tts
    while True:
        try:
            voice_switch = voice_option_menu.get()
            prefer_llm = api_option_menu.get()
            prefer_tts = tts_option_menu.get()
        except:
            pass
        time.sleep(0.1)


def run_chatweb():
    try:
        ft.app(target=main, assets_dir="data", view=ft.WEB_BROWSER, port=chatweb_port)
    except:
        pass


def voice_chat(msg2):
    voice_output_label.config(text="")
    voice_input_label.config(text=f"{username}: {msg2}")
    bot_response = chat_llm(msg2)
    voice_output_label.config(text=f"{mate_name}: {bot_response}")
    get_tts_play_live2d(bot_response)


def voice_th():
    global say_text
    model = vosk.Model("data/vosk-model-small-cn-0.22")
    rec = vosk.KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = None
    while True:
        try:
            if voice_option_menu.get() == "开启":
                try:
                    if not stream:
                        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,
                                        frames_per_buffer=8000)
                    data = stream.read(4000, exception_on_overflow=False)
                    if rec.AcceptWaveform(data):
                        say_text = rec.Result()[14:-3].replace(" ", "")
                        if len(say_text) > 1:
                            pg.init()
                            if pg.mixer.music.get_busy():
                                pass
                            else:
                                voice_chat(say_text)
                except:
                    time.sleep(0.01)
            else:
                time.sleep(0.01)
        except:
            pass


def switch_voice(event=None):
    if voice_switch == "开启":
        voice_variable.set("关闭")
    elif voice_switch == "关闭":
        voice_variable.set("开启")


Thread(target=run_live2d).start()
Thread(target=run_chatweb).start()
Thread(target=voice_th).start()
Thread(target=refresh_preference).start()
try:
    kb.add_hotkey(f'alt+{voice_key}', switch_voice)
except:
    pass
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
with open('data/db/preference.db', 'w', encoding='utf-8') as file2:
    file2.write(f'[实时语音交互]\n{voice_switch}\n\n')
    file2.write(f'[对话语言模型]\n{prefer_llm}\n\n')
    file2.write(f'[语音合成引擎]\n{prefer_tts}')
os.kill(os.getpid(), signal.SIGTERM)
