import os
import flet as ft
from flet_core import Image as ImageW
from flet_core import Row
from llm import *
from tts import *
from live2d import *
import datetime as dt


def get_head(head_name):
    head_path = f"data/image/ch/{head_name}.png"
    if os.path.exists(head_path):
        return head_path
    else:
        return "data/image/logo.png"


class Message:
    def __init__(self, user_name2: str, text: str, message_type: str):
        self.user_name2 = user_name2
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(content=ImageW(get_head(message.user_name2), width=50, height=50)),
            ft.Column([ft.Text(message.user_name2, weight="bold"), ft.Text(message.text, selectable=True)],
                      tight=True, spacing=5)]


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "对话 - AI虚拟伙伴"
    logo_image = ImageW("data/image/logo.png", width=25, height=25)
    title_label = ft.Text(value="AI虚拟伙伴", size=22, color="#587EF4")
    ip_label1 = ft.Text(value=f"对话网址: http://{server_ip}:{chatweb_port}", size=16)
    ip_label2 = ft.Text(value=f"角色网址: http://{server_ip}:{live2d_port}", size=16)
    open_ch_bt = ft.ElevatedButton(text="打开角色(主机)", on_click=open_ch)
    row1 = Row([logo_image, title_label])
    page.add(row1)
    row2 = Row([ip_label1])
    page.add(row2)
    row3 = Row([ip_label2, open_ch_bt])
    page.add(row3)

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "名称不能为空!"
            join_user_name.update()
        elif join_password.value != password:
            join_password.error_text = "密码错误"
            join_password.update()
        else:
            page.session.set("user_name2", join_user_name.value)
            page.dialog.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(user_name2=join_user_name.value, text=f"{join_user_name.value} 加入了聊天",
                        message_type="login_message"))
            page.update()

    def send_message_click(e):
        state.value = f"消息已发送，等待{mate_name}回复..."
        user_name2 = page.session.get("user_name2")
        user_message = new_message.value.strip()  # 获取用户输入的消息并去除两端空白字符
        page.pubsub.send_all(Message(user_name2=user_name2, text=user_message, message_type="chat_message"))
        new_message.value = ""  # 清空输入框
        new_message.focus()  # 将焦点重新放在输入框上
        bot_response = chat_llm(user_message)
        state.value = f"收到{mate_name}回复"
        page.pubsub.send_all(Message(user_name2=mate_name, text=bot_response, message_type="chat_message"))
        get_tts_play_live2d(bot_response)

    def export_chat(e):
        messages = []  # 存储聊天记录的列表
        timestamp = dt.datetime.now().strftime("%Y%m%d%H%M%S")
        ch = [username, mate_name]  # 说话者标识列表
        for control in chat.controls:
            if isinstance(control, ChatMessage):  # 确保是 ChatMessage 类型的控件
                messages.append(ch[0] + ":\n" + control.controls[1].controls[1].value)  # 第一条消息总是用户
                ch.reverse()  # 切换下一个说话者为虚拟伙伴
        file_path = f'data/history/AI虚拟伙伴Web版{mate_name}对话记录{timestamp}.txt'
        with open(file_path, 'w', encoding='utf-8') as file3:
            for message in messages:
                file3.write(message + '\n\n')  # 写入每条消息，并添加换行符
        state.value = f"对话已成功导出至data/history/AI虚拟伙伴Web版{mate_name}对话记录{timestamp}.txt"
        page.update()

    def clean_chat(e):
        chat.controls.clear()
        state.value = "记录已清空"
        page.update()

    def on_message(message: Message):
        m = None
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.colors.GREEN, size=12)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)  # 一个请求用户显示名称的对话框
    join_user_name = ft.TextField(label="用户名", value=username, autofocus=True, on_submit=join_chat_click)
    join_password = ft.TextField(label="密码", value=password, autofocus=True, password=True)
    page.dialog = ft.AlertDialog(open=True, modal=True, title=ft.Text("AI虚拟伙伴"),
                                 content=ft.Column([join_user_name, join_password], width=300, height=120, tight=True),
                                 actions=[ft.ElevatedButton(text="登录", on_click=join_chat_click)],
                                 actions_alignment=ft.MainAxisAlignment.END)
    chat = ft.ListView(expand=True, spacing=10, auto_scroll=True)  # 聊天信息
    # 一个新消息输入表单
    new_message = ft.TextField(hint_text="请输入消息...", autofocus=True, shift_enter=True, min_lines=1,
                               max_lines=5, filled=True, expand=True, on_submit=send_message_click)
    page.add(ft.Container(  # 将所有内容添加到页面上
        content=chat, border=ft.border.all(1, ft.colors.OUTLINE), border_radius=5, padding=10, expand=True),
        ft.Row([ft.IconButton(icon=ft.icons.DOWNLOAD_ROUNDED, tooltip="导出记录", on_click=export_chat),
                ft.IconButton(icon=ft.icons.ADD_ROUNDED, tooltip="开启新对话", on_click=clean_chat), new_message,
                ft.IconButton(icon=ft.icons.SEND_ROUNDED, tooltip="发送消息", on_click=send_message_click)]))
    state = ft.Text("欢迎使用AI虚拟伙伴Web版")
    page.add(state)
