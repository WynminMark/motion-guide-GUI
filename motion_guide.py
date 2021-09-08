import tkinter
import time
import datetime
from tkinter.font import Font


class motion_guide_GUI():
    def __init__(self, init_window_obj):
        self.init_window_name = init_window_obj
        self.progress_bar_len = 500
        self.is_suspend = False
        self.motion_sequence = ["收缩\n", "舒张\n"]
        self.motion_seq_len = len(self.motion_sequence)
        self.motion_index = 0
        self.myFont = Font(family="Times New Roman", size=12)
        self.motion_duration = 2000
        self.relax_duration = 1000
        self.f_name = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) + ".txt"


    def set_init_window(self):
        self.init_window_name.title("motion guide GUI")           #窗口名
        self.init_window_name.geometry('938x681+10+10')
        self.init_data_label = tkinter.Label(self.init_window_name, text="follow the instructions bellow")
        self.init_data_label.grid(row=0, column=0)
        self.log_label = tkinter.Label(self.init_window_name, text="log message")
        self.log_label.grid(row=0, column=15)

        self.init_data_Text = tkinter.Text(self.init_window_name, width=60, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.log_data_Text = tkinter.Text(self.init_window_name, width=60, height=35)  # 日志框
        self.log_data_Text.grid(row=1, column=12, rowspan=10, columnspan=10)

        self.progress_bar = tkinter.Canvas(self.init_window_name, width = self.progress_bar_len, height = 22, bg = "white")
        self.progress_bar.place(x=200, y=500)

        self.start_button = tkinter.Button(self.init_window_name, text = "START", bg = "lightblue", width = 10, command = self.start)  # 调用内部方法  加()为直接调用
        self.start_button.grid(row = 1, column = 11)
        self.stop_button = tkinter.Button(self.init_window_name, text = "STOP", bg = "lightgreen", width = 10, command = self.stop)
        self.stop_button.grid(row = 2, column = 11)

    
    def start(self):
        self.is_suspend = True


    def stop(self):
        self.is_suspend = False
        # self.log_data_Text.insert(tkinter.END, "stop function here\r\n")


    def gui_loop(self):
        self.init_window_name.update()

        if self.is_suspend:
            if self.motion_index <= self.motion_seq_len-1:
                self.init_data_Text.delete(1.0, tkinter.END)
                self.init_data_Text.insert(1.0, self.motion_sequence[self.motion_index])
                self.write_log_to_Text(self.motion_sequence[self.motion_index])
                self.motion_index += 1
                self.init_window_name.after(self.motion_duration, self.gui_loop)
            else:
                self.motion_index = 0
                self.init_window_name.after(self.relax_duration, self.gui_loop)

        #self.init_window_name.after(2000, self.gui_loop)


    def write_log_to_Text(self,logmsg):
        dt_s = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logmsg_in = str(dt_ms) +" " + str(logmsg) + "\n"      #换行
        self.log_data_Text.insert(tkinter.END, logmsg_in)
        f = open(self.f_name, "a")
        f.write(logmsg_in)
        f.close()



def gui_start():
    init_window = tkinter.Tk()              #实例化出一个父窗口
    win_a = motion_guide_GUI(init_window)
    # 设置根窗口默认属性
    win_a.set_init_window()
    init_window.after(2000, win_a.gui_loop)
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()

