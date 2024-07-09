import socket
import webbrowser as wb

with open('data/db/config.db', 'r', encoding='utf-8') as file:
    lines = file.readlines()
mate_name = lines[1].strip()
prompt = lines[4].strip()
username = lines[7].strip()
password = lines[10].strip()
speaker = lines[13].strip()
rate = lines[16].strip()
pitch = lines[19].strip()
chatweb_port = lines[22].strip()
live2d_port = lines[25].strip()
local_server_ip = lines[28].strip()
qwen_port = lines[31].strip()
lmstudio_port = lines[34].strip()
ollama_port = lines[37].strip()
ollama_model_name = lines[40].strip()
gsv_port = lines[43].strip()
custom_url = lines[46].strip()
custom_key = lines[49].strip()
custom_model = lines[52].strip()
voice_key = lines[55].strip()
with open('data/db/preference.db', 'r', encoding='utf-8') as file2:
    lines2 = file2.readlines()
voice_switch = lines2[1].strip()
prefer_llm = lines2[4].strip()
prefer_tts = lines2[7].strip()


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('223.5.5.5', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    return ip


def open_ch(e):
    wb.open(f"http://{server_ip}:{live2d_port}")


def open_browser(url):
    wb.open(url)


server_ip = get_local_ip()
