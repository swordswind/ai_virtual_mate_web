import json
from subprocess import Popen
from openai import OpenAI
from ollama import Client as oClient
import requests as rq
from gui import *

with open('data/db/config.db', 'r', encoding='utf-8') as file:
    lines = file.readlines()
prompt = lines[4].strip()
lmstudio_client, ollama_client, custom_client = None, None, None


def chat_llm(message):
    global lmstudio_client, ollama_client, custom_client
    try:
        if api_option_menu.get() == "GLM-4-9B":
            glm_client = OpenAI(base_url="https://api.siliconflow.cn/v1", api_key="您的API KEY")
            completion = glm_client.chat.completions.create(model="THUDM/glm-4-9b-chat",
                                                            messages=[{"role": "system", "content": prompt},
                                                                      {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "通义千问2-72B":
            qwen_client = OpenAI(base_url="https://api.siliconflow.cn/v1", api_key="您的API KEY")
            completion = qwen_client.chat.completions.create(model="Qwen/Qwen2-72B-Instruct",
                                                             messages=[{"role": "system", "content": prompt},
                                                                       {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "星火":
            spark_client = OpenAI(base_url="https://spark-api-open.xf-yun.com/v1", api_key="您的API KEY")
            completion = spark_client.chat.completions.create(model="general",
                                                              messages=[{"role": "system", "content": prompt},
                                                                        {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "Gemini":
            gemini_client = OpenAI(base_url="您的代理网址", api_key="您的API KEY")
            completion = gemini_client.chat.completions.create(model="gemini-pro",
                                                               messages=[{"role": "system", "content": prompt},
                                                                         {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "GPT-4":
            gpt4_client = OpenAI(base_url="您的代理网址", api_key="您的API KEY")
            completion = gpt4_client.chat.completions.create(model="gpt-4",
                                                             messages=[{"role": "system", "content": prompt},
                                                                       {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "GPT-3.5":
            gpt35_client = OpenAI(base_url="您的代理网址", api_key="您的API KEY")
            completion = gpt35_client.chat.completions.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "system", "content": prompt},
                                                                        {"role": "user", "content": message}])
            return completion.choices[0].message.content
        elif api_option_menu.get() == "文心一言":
            return ask_wxyy(message)
        elif api_option_menu.get() == "本地Qwen整合包":
            api = f"http://{local_server_ip}:{qwen_port}/llm/?p={prompt}&q={message}"
            try:
                res = rq.get(api).json()["answer"]
                return res
            except:
                return "本地Qwen大语言模型服务器未开启"
        elif api_option_menu.get() == "本地LM Studio":
            try:
                if not lmstudio_client:
                    lmstudio_client = OpenAI(base_url=f"http://{local_server_ip}:{lmstudio_port}/v1",
                                             api_key="lm-studio")
                completion = lmstudio_client.chat.completions.create(model="",
                                                                     messages=[{"role": "system", "content": prompt},
                                                                               {"role": "user", "content": message}])
                return completion.choices[0].message.content
            except:
                return "本地LM Studio软件未开启"
        elif api_option_menu.get() == "本地Ollama":
            try:
                try:
                    rq.get(f'http://{local_server_ip}:{ollama_port}')
                except:
                    Popen(f"ollama pull {ollama_model_name}", shell=False)
                if not ollama_client:
                    ollama_client = oClient(host=f"http://{local_server_ip}:{ollama_port}")
                response = ollama_client.chat(model=ollama_model_name, messages=[{"role": "system", "content": prompt},
                                                                                 {"role": "user", "content": message}])
                return response['message']['content']
            except:
                return "本地Ollama服务未开启"
        else:
            try:
                if not custom_client:
                    custom_client = OpenAI(base_url=custom_url, api_key=custom_key)
                completion = custom_client.chat.completions.create(model=custom_model,
                                                                   messages=[{"role": "system", "content": prompt},
                                                                             {"role": "user", "content": message}])
                return completion.choices[0].message.content
            except:
                return "自定义API配置错误"
    except:
        return f"{api_option_menu.get()}服务不可用，可更换其他对话模型"


def wxyy_get_access_token():  # 使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=您的API Key&client_secret=您的Secret Key"
    payload = json.dumps("")
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    response = rq.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def ask_wxyy(msg):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token=" + wxyy_get_access_token()
    payload = json.dumps({"messages": [{"role": "user", "content": f"{prompt}。我的问题是：{msg}"}]})
    headers = {'Content-Type': 'application/json'}
    response = rq.request("POST", url, headers=headers, data=payload)
    result = response.json().get("result")
    return result
