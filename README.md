# Project_CSS_131

Air quality & Climate

-เป็นโปรแกรมเช็คค่าสภาพอากาศ ทั้งในเรื่องค่าฝุ่นในอากาศ และสภาพอากาศต่างๆ และยังมีคำอธิบายสำหรับค่าสภาพอากาศต่างๆที่น่ารู้-

## คำอธิบายการ Run Program

1. ดาวน์โหลดโปรเจกต์จากไฟล์  Python_project_131.py

2. เนื่องจากมีการใช้งาน Library จากภายนอก จึงต้องทำการ Install Library เหล่านี้ก่อน

      **pip install requests**
   
   (ใช้สำหรับเรียกข้อมูล)

      **pip install songline**
      
   (ใช้สำหรับฟังก์ชั่นส่งค่าสภาพอากาศเข้าไลน์)

3. วิธีการรับแจ้งเตือนในฟังก์ชั่นส่งไลน์

   3.1) เข้ากลุ่มไลน์ [https://line.me/ti/g/DhVUP_slbD] (มี Qr code อยู่ในไฟล์นำเสนอ)

   ***หรือ***

   3.2) ทำการเปลี่ยน token ให้เป็นของผู้ใช้งาน ในโค้ดบรรทัดที่ 10 (token ที่มีอยู่เป็นของผู้พัฒนาที่ใช้กับกลุ่มที่กล่าวมาข้างต้น ถ้าไม่เปลี่ยน token โปรแกรมจะรันได้ตามปกติแต่จะไม่แจ้งเตือนในไลน์ของผู้ใช้) 



## วิธีการเปลี่ยน token (*** ทางเลือกแบบ private***)

      (***

1. ทำการสร้าง [กลุ่มไลน์] ขึ้นมา 1 กลุ่ม

2. เข้าไปที่ Line notify หรือ [https://notify-bot.line.me/th/] และทำการล็อกอิน

3. เข้าไปที่ตั้งค่าด้านขวาบน คลิก [My page]

4. กด Generate token ใส่ชื่อ Bot และเลือกกลุ่มที่สร้างไว้ กด Generate token

5. Copy token มาใส่แทน token เดิม

6. เข้าไปที่กลุ่มไลน์ที่สร้างขึ้น และกดเชิญ Bot ที่ชื่อ Line Notify

   ***)

## ผู้พัฒนา

65090500452 นายมณฑล สุขจินดา
