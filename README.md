- อ่านไฟล์ test_emails.txt 
- Run Code ตามตัวอย่างเพื่อ 1. รับ Address กับ Name / 2. Recipient Name

ที่เพิ่มเข้ามาจะเป็น ส่วนที่ Comment ไว้ 
- ตั้งเงื่อนไข if-else ถ้ามี ตาม Pattern ที่วางไว้ ให้เก็บไว้ใน ro_status 
- ตั้งอีก 1 เงื่อนไขว่า ถ้า ข้อมูลใน ro_status != None ให้เก็บไว้ใน read_open_status 
- เก็บไว้ใน dictionary email 
- จัดการข้อมูลโดยใช้ pandas (email.append)
- ใช้ key + value ในการแสดงผล
- บอกค่า Status ว่า Email ถูกเปิดอ่านแล้วหรือยัง