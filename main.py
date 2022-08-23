from enum import auto
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import winsound
from idlelib.tooltip import Hovertip


class Tomato(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("400x300")
        self.title("طماطم")
        self.iconbitmap(r"tomatoF/tomatoIcon.ico")
        # Restricting root window to change
        # it's size according to user's need
        self.resizable(0, 0)#this make the surface dimention of app not able to change
        self.configure(background="darkred")
        self.imageStudy=PhotoImage(file='tomatoF/tomatoStudy.png')
        self.imageSleep = PhotoImage(file='tomatoF/tomatosleeping.png')
        self.frame1=tk.Frame(self, borderwidth=5, relief="groove",bg="lightgreen")
        self.frame1.place(relx=0.5, rely=0.03, relwidth=0.9, relheight=0.9, anchor='n')
        self.frame0=tk.Label(self.frame1,text="استعداد",compound = TOP,image=self.imageStudy,font=("Dubai Medium",20),
                             fg="darkred",bg="white",relief="groove",borderwidth=5)
        self.frame0.place(relx=0.03, rely=0.25, relwidth=0.5, relheight=0.56)
        self.remaining = 0
        self.sec = 0
        self.secConstant=0
        self.breaksec = 0
        self.voice = True
        self.fillVar()
        self.count = 0
        self.countrun = 0
        self.studyTime = 0
        self.totalStudy = 0
        self.countbreaks = 0
        self.totalbreak=0.0
        self.gostatics = True
        self.breaky = True
        self.stop = True
        self.lab1=tk.Label(self.frame1,text= " ♡ تركيز لدقائق ثم استراحة",font=("Dubai Medium",20),bg="darkred",fg="white",relief="sunken",width=20)
        self.lab1.place(relx=0.05, rely=0.03)
        self.lblmin = tk.Label(self.frame1, text=str(int(self.sec/60)).zfill(2), font=("Dubai Medium",15,'bold'),bg="darkred",fg="white",relief="sunken")
        self.lblmin.place(relx=0.67, rely=0.53)
        self.lblsec = tk.Label(self.frame1, text='00', font=("Dubai Medium",15,'bold'),bg="darkred",fg="white",relief="sunken")
        self.lblsec.place(relx=0.78, rely=0.53)
        self.butt_study = tk.Button(self.frame1, text="ابدأ الدراسة", width=14, font=("Dubai Medium", 10),command=self.click)
        self.butt_study.place(relx=0.60, rely=0.29)
        self.image3=tk.PhotoImage(file = "tomatoF/finish.png")
        self.butt_finish = tk.Button(self.frame1,text="إنهاء جلسة الدراسة  ", image= self.image3 ,compound = RIGHT, font=("Dubai Medium", 10),height=30, command=self.done)
        self.butt_finish.place(relx=0.57, rely=0.76)
        self.image1=tk.PhotoImage(file = "tomatoF/stat-small.png")
        self.image2=tk.PhotoImage(file = "tomatoF/setting-small.png")
        self.image4=tk.PhotoImage(file = "tomatoF/info-small.png")
        self.butt_static = tk.Button(self.frame1, image= self.image1,  font=("Dubai Medium", 10),command=self.statics)
        self.butt_info = tk.Button(self.frame1, image=self.image4 , font=("Dubai Medium", 10),command=self.info)
        self.butt_setting = tk.Button(self.frame1, image=self.image2 , font=("Dubai Medium", 10),command=self.setting)
        self.butt_static.place(relx=0.36, rely=0.85)
        self.butt_setting.place(relx=0.24, rely=0.85)
        self.butt_info.place(relx=0.12, rely=0.85)
        tip1 = Hovertip(self.butt_setting,'  إعدادات  ')
        tip2 = Hovertip(self.butt_static,'  إحصائيات الدراسة  ')
        tip2 = Hovertip(self.butt_info,'  عن طماطم  ')
        #self.butt_study = tk.Button(self.frame1, text="قف/أكمل", width=15, font=("Dubai Medium", 10))
        #self.butt_study.place(relx=0.58, rely=0.70)
        
        



    def fillVar(self):
        file = open("tomatoF/setting.txt", "r")
        line = 0
        for i in file:
            if line == 1:
                self.secConstant = int(i) * 60
                self.sec = self.secConstant
            elif line == 2:
                self.breaksec = int(i) * 60
            elif line == 0:
                if i.strip() == "True":
                    self.voice = True
                elif i.strip() == "False":
                    self.voice = False
            self.remaining=self.secConstant
            line += 1

    def click(self):
        if self.stop:
            self.stop = False
            self.butt_study.config(text="||",font=("Dubai Medium", 13,"bold"),width=4)
            self.butt_study.place(relx=0.68, rely=0.29)
        else:
            self.stop =True
            self.butt_study.config( text="أكمل الدراسة", width=14, font=("Dubai Medium", 10))
            self.butt_study.place(relx=0.60, rely=0.29)
        
        self.run()



    def run(self):
        if self.breaky:
            self.frame0.config( text="دراسة", compound=TOP, image=self.imageStudy)
        #else:
           # self.frame0.config( text="استراحة", compound=TOP, image=self.imageSleep)
        if self.remaining < 0:
            self.playSound()
            if self.breaky:
                self.attributes("-topmost", True)
                ask = messagebox.askyesno("!!!وقت الاستراحة", "هل ستبدأ الاستراحة الآن؟")
                if ask:
                    self.breakSet()
                else:
                    self.attributes("-topmost", True)
                    conf = messagebox.askokcancel("تحذير خطر على الصحة", "عيونك وجسمك بحاجة الى استراحة قصيرة، هل أنت متأكد!؟ ")
                    if conf:
                        self.breakStudy()
                    else:
                        self.breakSet()

            else:
                self.attributes("-topmost", True)
                confstr = messagebox.showinfo("وقت الدراسة", "سيبدأ عداد الدراسة الآن")
                self.breakStudy()
        if self.stop:
            pass
        else:

            self.m, self.s = divmod(self.remaining, 60)
            self.lblmin.config(text=str(self.m).zfill(2))
            self.lblsec.config(text=str(self.s).zfill(2))
            self.remaining = self.remaining - 1
            self.after(1000, self.run)


    def breakSet(self):
        self.breaky = False
        self.gostatics=False
        self.remaining = self.breaksec
        self.countbreaks += 1
        self.totalbreak += self.breaksec / 60
        self.frame0.config(text="استراحة",compound = TOP,image=self.imageSleep)

    def breakStudy(self):
        self.breaky = True
        self.gostatics = True
        self.remaining = self.sec
        self.studyTime += 1
        self.totalStudy +=  self.sec
        self.frame0.config( text="دراسة", compound=TOP, image=self.imageStudy)

    def done(self):
        if self.gostatics:
            self.destroy()
            self.statics()
        else:
            self.destroy()

    def playSound(self):
        if self.voice==True:
            winsound.PlaySound('tomatoF/finish.wav',winsound.SND_ASYNC)

    def statics(self):
        global top2
        if self.gostatics:
            top2 = tk.Tk()
            top2.geometry("400x460")
            top2.title("Setting")
            top2.configure(background="darkred")
            top2.resizable(0, 0)
            #top2.wm_protocol("WM_DELETE_WINDOW", lambda: self.on_exit)  # window cant be close from x botton
            frame = Frame(top2, borderwidth=5, relief="groove", bg="white")
            frame.place(relx=0.5, rely=0.03, relwidth=0.9, relheight=0.9, anchor='n')
            btn = Button(frame, text="تم", width=15, font=("Dubai Medium", 13), command=self.cancelTop2)
            top2.attributes("-topmost", True)
            totalSecond= int( (self.sec-self.remaining)+self.totalStudy)
            m, s = divmod(totalSecond, 60)
            h, m = divmod(m, 60)
            str1 = " تم قضاء " + str(self.studyTime) + """ فترة دراسة 
__________________________
أي:{} ساعات و {} دقائق و {} ثواني
__________________________
فترات الاستراحة: {} مرات 
الوقت الكلي للاستراحات:{} من الدقائق
__________________________
أعانك الله ووفقك؛ اللهم آمين
""".format(h, m, s, self.countbreaks, self.totalbreak)
            lblls = Label(frame, text=str1, font=("Dubai Medium", 16), bg="white", fg="darkred")
            lblls.pack()
            btn.pack()
        else:
            messagebox.showwarning("تحذير", "يفترض بك أن لا تنظر للشاشة خلال وقت الاستراحة")

    def setting(self):
        global top
        global var
        global var2
        global var1
        top = tk.Tk()
        top.geometry("400x300")
        top.title("Setting")
        top.configure(background="darkred")
        top.resizable(0, 0)
        top.attributes("-topmost", True)
        frame = Frame(top, borderwidth=5, relief="groove", bg="lightgreen")
        frame.place(relx=0.5, rely=0.03, relwidth=0.9, relheight=0.9, anchor='n')
        lblmin1 = Label(frame, text="مقدار وقت الدراسة (دقائق)", font=("Dubai Medium", 15), bg="darkred", fg="lightgreen",
                        relief="sunken")
        lblmin2 = Label(frame, text="مقدار وقت الاستراحة (دقائق)", font=("Dubai Medium", 15), bg="darkred", fg="lightgreen",
                        relief="sunken")
        var = StringVar(top)
        var.set(self.sec / 60)
        var1 = StringVar(top)
        var1.set(self.breaksec/60)
        ent1 = Spinbox(frame, from_=1, to=60, font=("Dubai Medium", 15), textvariable=var, width=6)
        ent2 = Spinbox(frame, from_=1, to=60, font=("Dubai Medium", 15), textvariable=var1, width=6)
        lblmin1.grid(row=1, column=2, padx=5, pady=3)
        ent1.grid(row=1, column=1, padx=10, pady=18)
        lblmin2.grid(row=3, column=2, padx=10, pady=18)
        ent2.grid(row=3, column=1, padx=5, pady=18)
        var2 = BooleanVar(top)
        check = Checkbutton(frame, text="تنبيه صوتي", font=("Dubai Medium", 15), bg="darkred", fg="lightgreen", activeforeground="red3",
                    highlightcolor="lightgreen",
                    disabledforeground="red3", relief="sunken", width=10, variable=var2).grid(row=5, column=2)
        var2.set(self.voice)
        button = Button(frame, text="حفظ",font=("Dubai Medium", 10,"bold"), bd=2, command=self.save)
        button1 = Button(frame, text="إلغاء",font=("Dubai Medium", 10,"bold"), bd=2, command=self.cancelTop1)
        button.place(relx=0.03, rely=0.82, width=80)
        button1.place(relx=0.33, rely=0.82, width=80)
        top.wm_protocol("WM_DELETE_WINDOW", lambda: self.on_exit)  # window cant be close from x botton

    def save(self):
        conf = messagebox.askokcancel("تنويه", "سيتم تصفير العداد والاحصائيات والبدء من جديد")
        if conf:

            file = open("tomatoF/setting.txt", 'w')
            if var2.get():
                str = "True"
            else:
                str = "False"
            file.write(str + '\n' + var.get() + '\n' + var1.get())
            file.close()
            top.destroy()
            self.setUp()
        else:
            top.destroy()
        #we will not use this but this is good sourse for restart app:
        #self.destroy()
        #self.__init__()

    def cancelTop1(self):
        top.destroy()

    def cancelTop2(self):
        top2.destroy()

    def on_exit():
        pass
    def setUp(self):
        self.fillVar()
        self.stop=True
        self.butt_study.config( text="أكمل الدراسة", width=14, font=("Dubai Medium", 10))
        self.butt_study.place(relx=0.60, rely=0.29)
        self.m, self.s = divmod(self.remaining, 60)
        self.lblmin.config(text=str(self.m).zfill(2))
        self.lblsec.config(text=str(self.s).zfill(2))


    def info(self):
        global top3
        top3 = tk.Tk()
        top3.geometry("600x430")
        top3.title("about Tomato")
        top3.configure(background="darkred")
        top3.resizable(0, 0)
        top3.attributes("-topmost", True)
        frame = Frame(top3, borderwidth=5, relief="groove", bg="white")
        frame.place(relx=0.5, rely=0.03, relwidth=0.9, relheight=0.9, anchor='n')
        btn = Button(frame, text="تم", width=15, font=("Dubai Medium", 13), command=self.cancelTop2)
        top3.attributes("-topmost", True)
        about ="""،حطَّابٌ كان في عجلةٍ واضطرابٍ من أمره      
،يريد قطع أكبر قدر من الأشجار قبل غروب الشمس
كان يعمل بلا توقف    
مر عليه ناصحٌ فقال: ألا تأخذ دقيقة لتشحذ هذا المنشار 
!وتسرّع عملك، فإنه لا يكاد يعمل 
"!!رد عليه الحطاب مستعجلاً: "لا وقت لدي


بذكاء_وليس_بجهد#



         """
        lblls = Label(frame, text=about, font=("Dubai Medium bold", 16), bg="white", fg="darkred")
        cpyright = Label(frame, text= "MALAK SABOUNI @2022", font=(" ITC Franklin Gothic",11),bg="white", fg="darkred")
        lblls.place(relx=0.17, rely=0.1)
        cpyright.place(relx=0.34, rely=0.9)

           

    



if __name__ == "__main__":
    app = Tomato()
    app.mainloop()


