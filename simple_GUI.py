"""
轻量版本GUI
用于指示动作
"""

import tkinter
import tkinter.filedialog
import time
import datetime
from tkinter.font import NORMAL, Font
from tkinter import DISABLED, ttk
import utils_sound


# original version motion guide app
class MotionGuideGUI():
    def __init__(self, init_window_obj, active_duration = 6000, relax_duration = 6000):
        self.init_window_name = init_window_obj
        # 控制小程序的运行和停止
        self.is_suspend = False
        # 用于循环的动作序列
        self.motion_sequence = ["收缩\n", "舒张\n"]
        self.instruction_sound = ["wav_files\sound_contract.wav", "wav_files\sound_relax.wav"]
        self.motion_seq_len = len(self.motion_sequence)
        self.motion_index = 0
        # 倒计时
        self.count_down_sequence = ["3\n", "2\n", "1\n"]
        self.count_down_sound = [r"wav_files\3.wav", r"wav_files\2.wav", r"wav_files\1.wav"]
        self.count_down_sequence_len = len(self.count_down_sequence)
        self.count_down_flag = False
        self.count_down_index = 0
        # 设置字体等其他参数
        self.my_font = Font(family="Arial", size=12)
        self.motion_duration = active_duration
        self.relax_duration = relax_duration
        # 动作次数统计
        self.action_counter = 0
        pass

    def set_init_window(self):
        # 窗口名和尺寸设置
        self.init_window_name.title("Motion Guide GUI")#窗口名
        self.init_window_name.geometry('600x500+300+500')#窗口尺寸和位置
        self.init_window_name.attributes("-alpha", 0.9)
        # label文字
        self.init_data_label = tkinter.Label(self.init_window_name, font=('Arial', 20), text="Follow The Instructions Bellow")
        self.init_data_label.grid(row=0, column=0)
        self.action_counter_label = tkinter.Label(self.init_window_name, font=self.my_font, text="动作完成次数统计")
        self.action_counter_label.grid(row=2, column=0)
        self.log_label = tkinter.Label(self.init_window_name, font=('Arial', 10), text="Log Message")
        self.log_label.grid(row=4, column=0)
        # 文本框
        self.init_data_Text = tkinter.Text(self.init_window_name, font=('Arial', 20), width=25, height=2)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=1, columnspan=1)
        self.action_counter_text = tkinter.Text(self.init_window_name, font=self.my_font, width=50, height=2)
        self.action_counter_text.grid(row=3, column=0)
        self.log_data_Text = tkinter.Text(self.init_window_name, width=50, height=20)  # 日志框
        self.log_data_Text.grid(row=5, column=0, rowspan=3, columnspan=1)
        # 按键，控制开始和停止等功能
        self.start_button = tkinter.Button(self.init_window_name, text = "START", bg = "lightblue", width = 10, command = self.start)#调用内部方法，加()为直接调用
        self.start_button.grid(row=0, column=1, columnspan=2)
        self.stop_button = tkinter.Button(self.init_window_name, text = "STOP", bg = "lightgreen", width = 10, command = self.stop)
        self.stop_button.grid(row=1, column=1, columnspan=2)

        pass

    def start(self):
        # start 后重新建立新文件
        self.f_name = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + ".txt"
        # 开始进入loop循环
        self.is_suspend = True
        # 开始新一轮倒计时
        self.count_down_flag = True
        self.count_down_index = 0
        # 动作index重置为0，倒计时结束后从收缩开始新一轮
        self.motion_index = 0
        # 清空上一轮log
        self.log_data_Text.delete(1.0, tkinter.END)
        # 显示动作计数
        self.action_counter = 0
        self.action_counter_text.delete(1.0, tkinter.END)
        self.action_counter_text.insert(1.0, self.action_counter)
        pass

    def stop(self):
        self.is_suspend = False
        pass


    def get_channel_num(self):
        """
        get channel NO. 
        get channel NO. 
        list insex 0-3: agonist 1-4; index 4-7: antagonist 1-4
        [7,8,0,0,1,2,0,0]
        """
        channel_onoff = list(i.get() for i in self.channel_var_list)
        # get index
        # channel_num = tuple(i for i, e in enumerate(channel_onoff) if e != 0)
        # print("channel ", channel_onoff)
        # print(channel_num)
        return channel_onoff

    def gui_loop(self):
        self.init_window_name.update()

        if self.is_suspend: # 程序开始
            if self.count_down_flag:    # 判断是否进入倒计时
                # 进入倒计时
                if self.count_down_index <= self.count_down_sequence_len - 1:
                    # 打印倒计时序列
                    self.init_data_Text.delete(1.0, tkinter.END)
                    self.init_data_Text.insert(1.0, self.count_down_sequence[self.count_down_index])
                    # 播放倒计时声音
                    utils_sound.play_wav(self.count_down_sound[self.count_down_index])
                    self.count_down_index += 1
                    self.init_window_name.after(1000, self.gui_loop)
                else:
                    # 倒计时完成一次后，flag改为false，进入动作循环
                    self.count_down_flag = False
                    # 设置1000倒计时结束后2s后开始动作循环
                    self.init_window_name.after(1000, self.gui_loop)
            else:
                # 不进入倒计时，打印动作提示信息
                if self.motion_index <= self.motion_seq_len-1:
                    # 打印动作完成次数
                    self.action_counter_text.delete(1.0, tkinter.END)
                    self.action_counter_text.insert(1.0, self.action_counter)
                    # 打印动作提示
                    self.init_data_Text.delete(1.0, tkinter.END)
                    self.init_data_Text.insert(1.0, self.motion_sequence[self.motion_index])
                    # 播放语音提示
                    utils_sound.play_wav(self.instruction_sound[self.motion_index])
                    # 
                    self.write_log_to_Text(self.motion_sequence[self.motion_index])
                    if self.motion_index == 0:
                        self.init_window_name.after(self.motion_duration, self.gui_loop)
                    else:
                        self.init_window_name.after(self.relax_duration, self.gui_loop)
                    self.motion_index += 1
                else:
                    self.motion_index = 0
                    self.action_counter += 1
                    self.init_window_name.after(0, self.gui_loop)
                    
        else:   # 程序未开始运行
            self.init_window_name.after(0, self.gui_loop)
        pass
        
    def write_log_to_Text(self, logmsg):
        # dt_s = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logmsg_in = str(dt_ms) +" " + str(logmsg) + "\n"      #换行
        self.log_data_Text.insert(tkinter.END, logmsg_in)
        with open(self.f_name, "a") as f:
            f.write(logmsg_in)
        pass
    # end class
    pass


def gui_start():
    # 实例化父窗口
    init_window = tkinter.Tk()
    # 创建motion guide GUI类，设置窗口组间和属性
    win_a = MotionGuideGUI(init_window, active_duration=6000, relax_duration=6000)
    win_a.set_init_window()
    # 运行gui_loop方法
    init_window.after(2000, win_a.gui_loop)
    # 父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
    init_window.mainloop()
    pass


if __name__ == '__main__':
    gui_start()

