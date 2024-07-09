import asyncio
import shutil
import time
import edge_tts
import librosa
import numpy as np
import pygame as pg
import pyttsx3
import requests as rq
from gradio_client import Client
from threading import Thread
from gui import *

voice_path = 'data/cache/cache_voice'
try:
    engine = pyttsx3.init()
except:
    pass


def play_voice():
    def play_mp3_th():
        pg.init()
        pg.mixer.music.load(voice_path)
        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            pg.time.Clock().tick(1)
        pg.mixer.music.stop()
        pg.quit()

    Thread(target=play_mp3_th).start()


def get_tts_play_live2d(text):
    speaker_mapping = {"晓伊-年轻女声": "zh-CN-XiaoyiNeural", "晓晓-成稳女声": "zh-CN-XiaoxiaoNeural",
                       "云健-大型纪录片男声": "zh-CN-YunjianNeural", "云希-短视频热门男声": "zh-CN-YunxiNeural",
                       "云夏-年轻男声": "zh-CN-YunxiaNeural", "云扬-成稳男声": "zh-CN-YunyangNeural",
                       "晓北-辽宁话女声": "zh-CN-liaoning-XiaobeiNeural",
                       "晓妮-陕西话女声": "zh-CN-shaanxi-XiaoniNeural", "晓佳-粤语成稳女声": "zh-HK-HiuGaaiNeural",
                       "晓满-粤语年轻女声": "zh-HK-HiuMaanNeural", "云龙-粤语男声": "zh-HK-WanLungNeural",
                       "晓辰-台湾话年轻女声": "zh-TW-HsiaoChenNeural", "晓宇-台湾话成稳女声": "zh-TW-HsiaoYuNeural",
                       "云哲-台湾话男声": "zh-TW-YunJheNeural", "佳太-日语男声": "ja-JP-KeitaNeural"}
    select_speaker = speaker_mapping.get(speaker, "ja-JP-NanamiNeural")

    async def ms_edge_tts():  # 使用edge_tts进行文本到语音的转换并保存到文件
        communicate = edge_tts.Communicate(text, select_speaker, rate=f"{rate}%", pitch=f"{pitch}Hz")
        await communicate.save(voice_path)

    try:
        if tts_option_menu.get() == "微软云edge-tts":
            asyncio.run(ms_edge_tts())
            play_voice()
        elif tts_option_menu.get() == "VITS云服务1":
            client = Client("https://example.com/api/VITS-1")
            result = client.predict(text, "人物名", 0.2, 0.6, 0.8, 1, api_name="/predict")
            shutil.move(result, voice_path)
            play_voice()
        elif tts_option_menu.get() == "VITS云服务2":
            client = Client("https://example.com/api/VITS-2")
            result = client.predict(text, "人物名", 0.2, 0.6, 0.8, 1, api_name="/predict")
            shutil.move(result, voice_path)
            play_voice()
        elif tts_option_menu.get() == "VITS云服务3":
            client = Client("https://example.com/api/VITS-3")
            result = client.predict(text, "人物名", 0.2, 0.6, 0.8, 1, api_name="/predict")
            shutil.move(result, voice_path)
            play_voice()
        elif tts_option_menu.get() == "本地pyttsx3":
            engine.save_to_file(text, voice_path)
            engine.runAndWait()
            play_voice()
        elif tts_option_menu.get() == "本地GPT-SoVITS":
            url = f'http://{local_server_ip}:{gsv_port}/?text={text}&text_language=中文'
            response = rq.get(url)
            wav_data = response.content
            with open(voice_path, 'wb') as f:
                f.write(wav_data)
            play_voice()
    except:
        pass

    def play_live2d():
        try:
            x, sr = librosa.load(voice_path, sr=8000)
            x = x - min(x)
            x = x / max(x)
            x = np.log(x) + 1
            x = x / max(x) * 1.2
            s_time = time.time()
            for _ in range(int(len(x) / 800)):
                it = x[int((time.time() - s_time) * 8000) + 1]
                if it < 0:
                    it = 0
                with open("data/cache/cache.txt", "w") as cache_file:
                    cache_file.write(str(float(it)))
                time.sleep(0.1)
        except:
            pass
        time.sleep(0.1)
        with open("data/cache/cache.txt", "w") as cache_file:
            cache_file.write("0")

    Thread(target=play_live2d).start()
