import tkinter
import time
from tkinter.constants import X

class motion_guide_GUI():
    def __init__(self, init_window_obj):
        self.init_window_name = init_window_obj

    def set_init_window(self):
        self.init_window_name.title("motion guide GUI")           #窗口名
        self.init_window_name.geometry('1068x681+10+10')
        self.init_data_label = tkinter.Label(self.init_window_name, text="follow the instructions bellow")
        self.init_data_label.grid(row=0, column=0)
        self.log_label = tkinter.Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)

        self.init_data_Text = tkinter.Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.log_data_Text = tkinter.Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)

        self.progress_bar = tkinter.Canvas(self.init_window_name, width = 465, height = 22, bg = "white")
        self.progress_bar.place(x=110, y=60)

        self.start_button = tkinter.Button(self.init_window_name, text = "START", bg = "lightblue", width = 10, command = self.start)  # 调用内部方法  加()为直接调用
        self.start_button.grid(row = 1, column = 11)
        self.stop_button = tkinter.Button(self.init_window_name, text = "STOP", bg = "lightgreen", width = 10, command = self.stop)
        self.stop_button.grid(row = 2, column = 11)
    
    def start(self):
        fill_line = self.progress_bar.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
        x = 5
        n = 465/x
        for i in range(x):
            n = n + 465/x
            self.init_data_Text.insert(tkinter.END, "sunshine\n")
            self.progress_bar.coords(fill_line, (0, 0, n, 60))
            self.init_window_name.update()
            time.sleep(2)

        fill_line = self.progress_bar.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="white")
        x = 500
        n = 465/x
        for t in range(x):
            n = n + 465/x
            self.progress_bar.coords(fill_line, (0, 0, n, 60))
            self.init_window_name.update()
            time.sleep(0)

    def stop(self):
        self.log_data_Text.insert(tkinter.END, "哈哈，这个stop不好使，妹想到吧\r\n")


    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行



def gui_start():
    init_window = tkinter.Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = motion_guide_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()