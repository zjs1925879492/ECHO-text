import keyboard,pyperclip,time
from pynput.keyboard import Controller, Key

keyboards=Controller()

def read():           #全选并剪贴输入框文字，返回剪贴板内的文字的值
    with keyboards.pressed(Key.ctrl_l):
        time.sleep(0.2)
        keyboards.press('a')     #ctrl+按下a全选
        time.sleep(0.2)
        keyboards.release('a')        #ctrl+放开a
        time.sleep(0.2)
        keyboards.press('x')        #ctrl+按下x剪贴
        time.sleep(0.2)
        keyboards.release('x')           #ctrl+放开x
    return pyperclip.paste()      #读取剪贴板内文字并返回

def send(text):         #输入框内输入文字并发送的函数
    keyboards.type(text)
    time.sleep(0.2)
    keyboards.press(Key.enter)
    keyboards.release(Key.enter)
    
def main():        #主程序函数
    text=read()
    text=text.replace('\r\n\r\n', '')      #因PCQQ有shift（ctrl）+enter强制换行机制，遂去除部分多余转义控制字符
    lenth=len(text)
    for i in range(lenth-1):        #循环并切片文字，调用send发送
        time.sleep(0.5)
        text=text[:-1]
        send(text)

if __name__ == '__main__':
    keyboard.add_hotkey('shift+enter',main)          #键盘监听shift+enter键，当按下执行main函数
    keyboard.wait('ctrl+q')
    