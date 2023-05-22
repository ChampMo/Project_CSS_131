import requests
from pprint import pprint
from songline import Sendline
import tkinter.messagebox
from tkinter import *
import tkinter as tk
from tkinter import ttk

def main():
    token = 'q1kMJN5qnrWglFhOZBjVITYOrfT1bkUGNSMtPjiPMim'
    messenger = Sendline(token)
    city = ["bangkok","rayong","chiang mai","chiang rai"]
    tags = ["@5773","@5774","@5775","@5776"]
    def PM2_5():
        api_key = "e458a579eef36fd1a856d0f48764fa8ce2f849a5"
        findcity =  choice.get() #txt.get() or
        inputcity = findcity.lower()

        found_match = False
        for i in range(len(city)):
            if inputcity == "":
                text2 = ("  ")
                text3 = ("  ")
                text4 = ("  ")
                text5 = ("กรุณาใส่ข้อมูล")
                text6 = ("  ")
                text7 = ("  ")
                v2_result.set(text2)
                v3_result.set(text3)
                v4_result.set(text4)
                v5_result.set(text5)
                v6_result.set(text6)
                v7_result.set(text7)

            if inputcity == city[i]:
                tag = tags[i]
                found_match = True
                url = 'https://api.waqi.info/feed/'+tag+'/?token='+ api_key
                response = requests.get(url).json()
                aqi = response['data']['aqi']
                city_name = response['data']['city']['name']
                dominent_pollutant = response['data']['dominentpol']
                pm25_avg = response['data']['iaqi']['pm25']['v']
                o3_avg = response['data']['iaqi']['o3']['v']
                pm10_avg = response['data']['iaqi']['pm10']['v']

                text2 = ("City : %s"%city_name)
                text3 = ("\nAir Quality Index (AQI) : %d" %aqi)
                text4 = ("\nDominant Pollutant : %s" %dominent_pollutant)
                text5 = ("\nAverage PM2.5 Level : %d " %pm25_avg)
                text6 = ("\nAverage Ozone Level (O3) : %d" %o3_avg)
                text7 = ("\nAverage PM10 Level : %d" %pm10_avg)
                v2_result.set(text2)
                v3_result.set(text3)
                v4_result.set(text4)
                v5_result.set(text5)
                v6_result.set(text6)
                v7_result.set(text7)

        if not found_match:
            text2 = ("  ")
            text3 = ("  ")
            text4 = ("  ")
            text5 = ("ไม่พบผลลัพธ์")
            text6 = ("  ")
            text7 = ("  ")
            v2_result.set(text2)
            v3_result.set(text3)
            v4_result.set(text4)
            v5_result.set(text5)
            v6_result.set(text6)
            v7_result.set(text7)
            
    #Sendline#
    def SendLine():
        api_key = "e458a579eef36fd1a856d0f48764fa8ce2f849a5"
        findcity =  choice.get() #txt.get() or
        inputcity = findcity.lower()

        found_match = False
        for i in range(len(city)):
            if inputcity == "":
                text5 = ("ไม่พบผลลัพธ์")
                messenger.sendtext(text5)

            if inputcity == city[i]:
                tag = tags[i]
                found_match = True

                url = 'https://api.waqi.info/feed/'+tag+'/?token='+ api_key
                response = requests.get(url).json()
                aqi = response['data']['aqi']
                city_name = response['data']['city']['name']
                dominent_pollutant = response['data']['dominentpol']
                pm25_avg = response['data']['iaqi']['pm25']['v']
                o3_avg = response['data']['iaqi']['o3']['v']
                pm10_avg = response['data']['iaqi']['pm10']['v']
                text2 = ("\nCity : %s"%city_name)
                text3 = ("\nAir Quality Index (AQI) : %d" %aqi)
                text4 = ("\nDominant Pollutant : %s" %dominent_pollutant)
                text5 = ("\nAverage PM2.5 Level : %d " %pm25_avg)
                text6 = ("\nAverage Ozone Level (O3) : %d" %o3_avg)
                text7 = ("\nAverage PM10 Level : %d" %pm10_avg)
                messenger.sendtext(text2+text3+text4+text5+text6+text7)

        if not found_match:
            if choice.get() != "กรอกข้อมูลหรือเลือกหา":
                text5 = ("ค้นหาสภาพอากาศที่ : "+choice.get()+"\n---ไม่พบผลลัพธ์---")
                messenger.sendtext(text5)
            else:
                text5 = ("ไม่พบผลลัพธ์")
                messenger.sendtext(text5)

    #GUI#

    FONT1 = ('Tahoma' ,20,'bold')
    FONT2 = ('Tahoma' ,15)
    FONT3 = ('' ,15)
    FONT4 = ('' ,5)
    FONT5 = ('' ,10)
    FONT6 = ('Tahoma' ,25,'bold')

    GUI = Tk()
    GUI.geometry('600x900')
    GUI.title('AIR QUALITY CHECK')

    #Air quality#
    L = Label(GUI,text ='',font = FONT3).pack()
    L2 = Label(GUI,text ='Air quality', fg="gray17",font = FONT6).pack()
    L1 = Label(GUI,text ='ค้นหาสภาพอากาศ\n', fg="gray17",font = FONT6).pack()

    #txt = StringVar()
    #Entry(GUI,textvariable=txt, fg="gray",font = FONT3).pack(ipadx=60,ipady=4)
    
    choice = StringVar(value = "กรอกข้อมูลหรือเลือกหา")
    combo = ttk.Combobox(textvariable=choice)
    combo["values"]=('Bangkok','Rayong','Chiang Mai','Chiang Rai')
    #combo.place(x=150, y=115,width=250, height=37)
    combo.pack(ipadx=78,ipady=8)
    L = Label(GUI,text ='',font = FONT1).pack()
    def Select():
        if choice.get() != "กรอกข้อมูลหรือเลือกหา":
            Label(GUI,text =choice.get(), fg="steel blue",font = FONT6).place(x=200, y=220,width=200, height=50)

    B = Button(GUI,text = "แสดง", fg="white",bg = "gray",font = FONT5,command = Select).place(x=450, y=160,width=60, relheight=0.042)
    L = Label(GUI,text ='\n',font = FONT1).pack()
    B = Button(GUI,text = "ค้นหา", fg="white",bg = "gray",font = FONT5,command = PM2_5).pack(ipadx=78,ipady=5)

    L = Label(GUI,text ='\n',font = FONT1).pack()
    v2_result = StringVar()
    R2 = Label(GUI,textvariable = v2_result, fg="gray20",font = FONT1).pack()
    v3_result = StringVar()
    R3 = Label(GUI,textvariable = v3_result, fg="gray35",font = FONT1).pack()
    v4_result = StringVar()
    R4 = Label(GUI,textvariable = v4_result, fg="gray35",font = FONT1).pack()
    v5_result = StringVar()
    v5_result.set('     ')
    R5 = Label(GUI,textvariable = v5_result, fg="gray35",font = FONT1).pack()
    v6_result = StringVar()
    R6 = Label(GUI,textvariable = v6_result, fg="gray35",font = FONT1).pack()
    v7_result = StringVar()
    R7 = Label(GUI,textvariable = v7_result, fg="gray35",font = FONT1).pack()

    def help():
        GUI = tk.Tk()
        GUI.geometry('1340x900')
        GUI.title('คู่มือรายระเอียดข้อมูล')
        canvas = tk.Canvas(GUI)

        # สร้างเฟรมสำหรับใส่เนื้อหา
        content_frame = tk.Frame(canvas)
        # สร้างแถบสกอลล์บาร์แนวแกน Y
        scrollbar = ttk.Scrollbar(GUI, orient="vertical", command=canvas.yview)
        # กำหนดให้ Canvas เลื่อนเนื้อหาผ่านแถบสกอลล์บาร์
        canvas.configure(yscrollcommand=scrollbar.set)
        # ใส่เฟรมใน Canvas
        canvas.create_window((0, 0), window=content_frame, anchor="nw")
        

        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L1 = Label(content_frame,text ='Air Quality Index (AQI) : เกณฑ์ของดัชนีคุณภาพอากาศของประเทศไทย ', fg="gray5",font = FONT1).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L2 = Label(content_frame,text ='ค่า AQI  คือ ข้อมูลการวัดคุณภาพอากาศในภาพรวมที่ประกอบด้วยมลพิษทางอากาศ 6 ชนิด ได้แก่ \n', fg="gray20",font = FONT2).pack()
        L3 = Label(content_frame,text ='PM2.5 , PM10 , โอโซน (O3) , (CO) , (NO2) , (SO2)', fg="gray20",font = ('Tahoma' ,15,'bold')).pack()
        L4 = Label(content_frame,text ='สามารถวัดออกมาเป็นค่าได้ตามตารางดังนี้', fg="gray20",font = FONT2).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()
        #L = Label(GUI,text =' : ', fg="gray35",font = FONT2).grid(row=2,column=2)
        #L2 = Label(GUI,text ='เกณฑ์ของดัชนีคุณภาพอากาศของประเทศไทย ', fg="gray35",font = FONT2).grid(row=2,column=3)
        table = ttk.Treeview(content_frame)
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Tahoma", 12))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview"
        table.tag_configure("Custom.Treeview", font=("Tahoma", 12))
        style.configure("Space", font=("Arial", 1))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview"
        table.tag_configure("Space", font=("Arial", 1))
        table.tag_configure('sky blue', background='sky blue')
        table.tag_configure('seaGreen1', background='seaGreen1')
        table.tag_configure('khaki1', background='khaki1')
        table.tag_configure('tan1', background='tan1')
        table.tag_configure('coral1', background='coral1')
        #style.configure("Custom.Treeview.Heading", font=("Arial", 50, "bold"))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview.Heading"
        #table.configure(style="Custom.Treeview.Heading")
        
        table['columns'] = ( 'ความหมาย', 'สี','คำอธิบาย')
        table.heading('#0', text='AQI', anchor="center")
        table.heading('ความหมาย', text='ความหมาย', anchor="center")
        table.heading('สี', text='สี', anchor="center")
        table.heading('คำอธิบาย', text='คำอธิบาย', anchor="center")
        table.column('#0', width=120)
        table.column('ความหมาย', width=200)
        table.column('สี', width=80)
        table.column('คำอธิบาย', width=820)
        table.configure(height=22)
        table.pack()
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","sky blue"))
        table.insert('', 'end', text='    0 - 25', values=('      คุณภาพอากาศดีมาก', '     ฟ้า', '  คุณภาพอากาศดีมาก เหมาะสำหรับกิจกรรมกลางแจ้งและการท่องเที่ยว'), tags=("Custom.Treeview","sky blue"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","sky blue"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","seaGreen1"))
        table.insert('', 'end', text='   26 - 50', values=('        คุณภาพอากาศดี', '    เขียว', '  คุณภาพอากาศดี สามารถทำกิจกรรมกลางแจ้งและการท่องเที่ยวได้ตามปกติ'), tags=("Custom.Treeview","seaGreen1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","seaGreen1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","khaki1"))
        table.insert('', 'end', text='  51 - 100', values=('             ปานกลาง', '   เหลือง', '  ประชาชนทั่วไป : สามารถทำกิจกรรมกลางแจ้งได้ตามปกติ'), tags=("Custom.Treeview","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  ผู้ที่ต้องดูแลสุขภาพเป็นพิเศษ : หากมีอาการเบื้องต้น เช่น ไอ หายใจลำบาก ระคายเคืองตา ควรลดระยะเวลาการทำ'), tags=("Custom.Treeview","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  กิจกรรมกลางแจ้ง'), tags=("Custom.Treeview","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","tan1"))
        table.insert('', 'end', text=' 101 - 200', values=('    เริ่มมีผลกระทบต่อสุขภาพ', '     ส้ม', '  ประชาชนทั่วไป : ควรเฝ้าระวังสุขภาพ ถ้ามีอาการเบื้องต้น เช่น ไอ หายใจลำบาก ระคายเคืองตา ควรลดระยะเวลาการทำ'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  กิจกรรมกลางแจ้ง หรือใช้อุปกรณ์ป้องกันตนเองหากมีความจำเป็น'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  ผู้ที่ต้องดูแลสุขภาพเป็นพิเศษ : ควรลดระยะเวลาการทำกิจกรรมกลางแจ้ง หรือใช้อุปกรณ์ป้องกันตนเองหากมีความจำเป็น'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  ถ้ามีอาการทางสุขภาพ เช่น ไอ หายใจลำบาก ตาอักเสบ แน่นหน้าอก ปวดศีรษะ หัวใจเต้นไม่เป็นปกติ คลื่นไส้ อ่อนเพลีย'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  ควรปรึกษาแพทย์'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","coral1"))
        table.insert('', 'end', text=' 201 ขึ้นไป', values=('     มีผลกระทบต่อสุขภาพ', '    แดง', '  ทุกคนควรหลีกเลี่ยงกิจกรรมกลางแจ้งหลีกเลี่ยงพื้นที่ที่มีมลพิษทางอากาศสูง หรือใช้อุปกรณ์ป้องกันตนเองหากมี'), tags=("Custom.Treeview","coral1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', '  ความจำเป็นหากมีอาการทางสุขภาพควรปรึกษาแพทย์'), tags=("Custom.Treeview","coral1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","coral1"))

        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L1 = Label(content_frame,text ='\nDominant Pollutant ', fg="gray5",font = FONT1).pack()
        L2 = Label(content_frame,text ='สารมลพิษหลัก เป็นชนิดของมลพิษหลักๆที่วัดค่าได้ในอากาศ', fg="gray20",font = FONT2).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()

        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L1 = Label(content_frame,text ='Average PM2.5 Level ', fg="gray5",font = FONT1).pack()
        L2 = Label(content_frame,text ='ค่ามาตรฐาน PM 2.5 ในบรรยากาศทั่วไป หรือเรียกง่าย ๆ ว่าค่าฝุ่น PM2.5 \nคือ การกำหนดขึ้นเพื่อบ่งชี้ความเข้มข้นของการปล่อยฝุ่นละอองขนาดเล็กไม่เกิน 2.5 \nไมครอนในบรรยากาศ มีหน่วยเป็น ไมโครกรัมต่อลูกบาศก์เมตร โดยคิดค่าเฉลี่ยราย 24 ชั่วโมง และรายปี  \n', fg="gray20",font = FONT2).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()

        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L1 = Label(content_frame,text ='Average Ozone Level (O3) ', fg="gray5",font = FONT1).pack()
        L2 = Label(content_frame,text ='เป็นก๊าซอันตรายที่ปัจจุบันมีการเพิ่มขึ้นสูง และส่งผบกระทบต่อระบบเดินหายใจป้องกันยากกว่าฝุ่น PM 2.5 เพราะเป็นก๊าซ ไม่มีสี ไม่มีกลิ่น', fg="gray20",font = FONT2).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()

        L = Label(content_frame,text ='        ',font = FONT3).pack()
        L1 = Label(content_frame,text ='Average PM10 Level', fg="gray5",font = FONT1).pack()
        L2 = Label(content_frame,text ='PM 10 หรือเรียกว่า ฝุ่นหยาบ(Course Particles) \nคือ อนุภาคฝุ่นละอองในอากาศที่มีเส้นผ่าศูนย์กลางขนาด 2.5 - 10 ไมครอน ฝุ่นประเภทนี้เมื่อรวมกันเป็นจำนวนมากแล้วมักจะสังเกตเห็นได้ง่าย \nเช่น ฝุ่นที่เกาะอยู่ตามข้าวของเครื่องใช้ เกสรดอกไม้ หรือฝุ่นละอองจากงานก่อสร้าง ', fg="gray20",font = FONT2).pack()
        L = Label(content_frame,text ='        ',font = FONT3).pack()

        # ปรับขนาด Canvas เมื่อมีการเพิ่มหรือลดเนื้อหา
        def on_content_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        content_frame.bind("<Configure>", on_content_frame_configure)
        # แสดง Canvas และแถบสกอลล์บาร์
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def table():
        GUI = tk.Tk()
        GUI.geometry('1200x550')
        GUI.title('คู่มือรายระเอียดข้อมูล')

        L = Label(GUI,text ='        ',font = FONT3).pack()
        L1 = Label(GUI,text ='ตารางค่าความเข็มข้นของสารมลพิษทางอากาศที่เทียบเท่ากับค่าดัชนีคุณภาพอากาศ', fg="gray5",font = FONT1).pack()
        L = Label(GUI,text ='        ',font = FONT3).pack()

        table = ttk.Treeview(GUI)
        style = ttk.Style()
        style.configure("Custom.Treeview", font=("Tahoma", 12))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview"
        table.tag_configure("Custom.Treeview", font=("Tahoma", 12))
        style.configure("head", font=("Arial", 10))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview"
        table.tag_configure("head", font=("Arial", 10))
        style.configure("Space", font=("Arial", 1))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview"
        table.tag_configure("Space", font=("Arial", 1))
        table.tag_configure('sky blue', background='sky blue')
        table.tag_configure('seaGreen1', background='seaGreen1')
        table.tag_configure('khaki1', background='khaki1')
        table.tag_configure('tan1', background='tan1')
        table.tag_configure('coral1', background='coral1')
        #style.configure("Custom.Treeview.Heading", font=("Arial", 50, "bold"))  # กำหนดฟอนต์ให้กับสไตล์ "Custom.Treeview.Heading"
        #table.configure(style="Custom.Treeview.Heading")
        
        table['columns'] = ( 'PM25', 'PM10','O3','CO','NO2','SO2')
        table.heading('#0', text='AQI', anchor="center")
        table.heading('PM25', text='PM25(มคก./ลบ.ม)', anchor="center")
        table.heading('PM10', text='PM10(มคก./ลบ.ม)', anchor="center")
        table.heading('O3', text='O3(ppb)', anchor="center")
        table.heading('CO', text='CO(ppm)', anchor="center")
        table.heading('NO2', text='NO2(ppb)', anchor="center")
        table.heading('SO2', text='SO2(ppb)', anchor="center")
        table.column('#0', width=150)
        table.column('PM25', width=150)
        table.column('PM10', width=150)
        table.column('O3', width=150)
        table.column('CO', width=150)
        table.column('NO2', width=150)
        table.column('SO2', width=150)
        table.configure(height=16)
        table.pack()
        table.insert('', 'end', text=' ', values=('           เฉลี่ย 24 ชม.', '           เฉลี่ย 24 ชม.', '           เฉลี่ย 8 ชม.', '           เฉลี่ย 8 ชม.', '           เฉลี่ย 1 ชม.', '           เฉลี่ย 1 ชม.'), tags=("head"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","sky blue"))
        table.insert('', 'end', text='      0 - 25', values=('           0-25' ,'           0-50' ,'           0-35','           0-4.4','           0-60','          0-100'), tags=("Custom.Treeview","sky blue"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","sky blue"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","seaGreen1"))
        table.insert('', 'end', text='     26 - 50', values=('          26-37' ,'          51-80' ,'          36-50','          4.5-6.4','         61-106','        101-200'), tags=("Custom.Treeview","seaGreen1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","seaGreen1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","khaki1"))
        table.insert('', 'end', text='    51 - 100', values=('          38-50' ,'         81-120' ,'          51-70','          6.5-9.0','        107-170','        201-300'), tags=("Custom.Treeview","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","khaki1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","tan1"))
        table.insert('', 'end', text='   101 - 200', values=('          51-90' ,'        121-180' ,'         71-120','         9.1-30.0','        171-340','        301-400'), tags=("Custom.Treeview","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","tan1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","coral1"))
        table.insert('', 'end', text='   201 ขึ้นไป', values=('          91 up' ,'         181 up' ,'         121 up','         30.1 up','         341 up','          401 up'), tags=("Custom.Treeview","coral1"))
        table.insert('', 'end', text=' ', values=(' ', ' ', ' '), tags=("Space","coral1"))
        L = Label(GUI,text ='        ',font = FONT3).pack()
        L = Label(GUI,text ='อ้างอิง : https://www.gistda.or.th/news_view.php?n_id=6728&lang=TH', fg="gray20",font = ('Tahoma' ,12)).pack()

    #Climate#

    def Climate():
        def inclimate():
            api_key = "35d8f84f39ff2c037f1f51dfb84cb4b7"
            Tcity = choice.get()
            city = Tcity.lower()
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(url).json()
            
            if response["cod"] == "404":
                text4 = ("ไม่พบข้อมูลสภาพอากาศสำหรับเมืองนี้")
                v4_result.set(text4)
            else:
                weather_description = response["weather"][0]["description"]
                temperature = (response["main"]["temp"])-272.15
                humidity = response["main"]["humidity"]

                text2 = (f"สภาพอากาศในเมือง : {Tcity}")
                text3 = (f"สถานะ : {weather_description}")
                text4 = ( "อุณหภูมิ : %.2f  เซลเซียส"%temperature)
                text5 = (f"ความชื้น : {humidity}%")
                v2_result.set(text2)
                v3_result.set(text3)
                v4_result.set(text4)
                v5_result.set(text5)

        #Sendline#
        def SendLine():
            api_key = "35d8f84f39ff2c037f1f51dfb84cb4b7"
            Tcity = choice.get()
            city = Tcity.lower()
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
            response = requests.get(url).json()

            if response["cod"] == "404":
                text4 = ("ไม่พบข้อมูลสภาพอากาศสำหรับเมืองนี้")
                messenger.sendtext(text4)
            else:
                weather_description = response["weather"][0]["description"]
                temperature = (response["main"]["temp"])-272.15
                humidity = response["main"]["humidity"]

                text2 = (f"\nสภาพอากาศในเมือง : {Tcity}")
                text3 = (f"\nสถานะ : {weather_description}")
                text4 = ( "\nอุณหภูมิ : %.2f  เซลเซียส"%temperature)
                text5 = (f"\nความชื้น : {humidity}%")
                messenger.sendtext(text2+text3+text4+text5)

        GUI = Tk()
        GUI.geometry('600x900')
        GUI.title('CLIMATE CHECK')

        
        L = Label(GUI,text ='',font = FONT3).pack()
        L2 = Label(GUI,text ='Climate', fg="gray17",font = FONT6).pack()
        L1 = Label(GUI,text ='ค้นหาสภาพภูมิอากาศ\n', fg="gray17",font = FONT6).pack()

        #txt = StringVar()
        #Entry(GUI,textvariable=txt, fg="gray",font = FONT3).pack(ipadx=60,ipady=4)
        choice = StringVar(value = "กรอกข้อมูลหรือเลือกหา")
        combo = ttk.Combobox(textvariable=choice)
        combo["values"]=('Bangkok','Kamphaeng Phet','Chai Nat','Nakhon Nayok','Nakhon Pathom','Nakhon Sawan','Nonthaburi','Pathum Thani','Phra Nakhon Si Ayutthaya','Phichit','Phitsanulok','Phetchabun','Lop Buri','Samut Prakan','Samut Songkhram','Samut Sakhon','Saraburi','Sing Buri','Sukhothai','Suphan Buri','Ang Thong','Uthai Thani')
        #combo.place(x=150, y=115,width=250, height=37)
        combo.pack(ipadx=78,ipady=8)
        L = Label(GUI,text ='',font = FONT1).pack()
        def Select():
            if choice.get() != "กรอกข้อมูลหรือเลือกหา":
                Label(GUI,text =choice.get(), fg="steel blue",font = FONT6).place(x=70, y=220,width=500, height=50)

        B = Button(GUI,text = "แสดง", fg="white",bg = "gray",font = FONT5,command = Select).place(x=450, y=160,width=60, relheight=0.042)
        L = Label(GUI,text ='\n',font = FONT1).pack()
        B = Button(GUI,text = "ค้นหา", fg="white",bg = "gray",font = FONT5,command = inclimate).pack(ipadx=78,ipady=5)

        def About():
            tkinter.messagebox.showinfo("ผู้พัฒนา","\t65090500452\t\t\n\tMonthol Sukjinda\t\t\n\tนายมณฑล สุขจินดา\t\t")
        def Exit():
            confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่!!!")
            if confirm == "yes" :
                GUI.destroy()

        L = Label(GUI,text ='\n',font = FONT1).pack()
        v2_result = StringVar()
        R2 = Label(GUI,textvariable = v2_result, fg="gray20",font = FONT1).pack()
        v3_result = StringVar()
        R3 = Label(GUI,textvariable = v3_result, fg="gray35",font = FONT1).pack()
        v4_result = StringVar()
        R4 = Label(GUI,textvariable = v4_result, fg="gray35",font = FONT1).pack()
        v5_result = StringVar()
        v5_result.set('     ')
        R5 = Label(GUI,textvariable = v5_result, fg="gray35",font = FONT1).pack()

        def ref():
            GUI.destroy()
            main()
        def Climate1():
            GUI.destroy()
            Climate()
        def Coming_soon():
            tkinter.messagebox.showinfo("coming soon","     coming soon\t")
        mMenu = Menu()
        mMenu.add_command(label="คู่มือรายระเอียดข้อมูล",command=help)
        mMenu.add_command(label="ตารางสรุปรวมสารมลพิษ",command=table)
        mMenu.add_command(label="Export Climate to line",command=SendLine)
        mMenu.add_cascade(label="-------------------")
        mMenu.add_cascade(label="Exit Program",command=Exit)
        m2Menu = Menu()
        m2Menu.add_command(label="-  ผู้พัฒนา  -",command=About)

        myMenu = Menu()
        GUI.config(menu = myMenu)
        myMenu.add_cascade(label="Air quality",command=ref)
        myMenu.add_cascade(label="Climate",command=Climate1)
        myMenu.add_cascade(label="About",menu=m2Menu)
        myMenu.add_cascade(label="Menu",menu=mMenu)

    def About():
        tkinter.messagebox.showinfo("ผู้พัฒนา","\t65090500452\t\t\n\tMonthol Sukjinda\t\t\n\tนายมณฑล สุขจินดา\t\t")
    def Exit():
        confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่!!!")
        if confirm == "yes" :
            GUI.destroy()
    def ref():
        GUI.destroy()
        main()
    def Climate1():
        GUI.destroy()
        Climate()

    mMenu = Menu()
    mMenu.add_command(label="คู่มือรายระเอียดข้อมูล",command=help)
    mMenu.add_command(label="ตารางสรุปรวมสารมลพิษ",command=table)
    mMenu.add_command(label="Export Air quality to line",command=SendLine)
    mMenu.add_cascade(label="-------------------")
    mMenu.add_cascade(label="Exit Program",command=Exit)
    m2Menu = Menu()
    m2Menu.add_command(label="-  ผู้พัฒนา  -",command=About)

    myMenu = Menu()
    GUI.config(menu = myMenu)
    myMenu.add_cascade(label="Air quality",command=ref)
    myMenu.add_cascade(label="Climate",command=Climate1)
    myMenu.add_cascade(label="About",menu=m2Menu)
    myMenu.add_cascade(label="Menu",menu=mMenu)
    
    GUI.mainloop()
main()

