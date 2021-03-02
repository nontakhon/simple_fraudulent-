# simple_fraudulent-

1. บรรทัดที่1 คือการอ่านไฟล์ที่ชื่อ test_emails.txt
2. บรรทัดที่5 คือการเก็บค่าที่ขึ้นต้นด้วย From: จากตัวแปร fh ใส่ใน ตัวแปร address
3. บรรทัดที่6 คือรับค่าจากตัวแปร address ไปในตัวแปร item
4. บรรทัดที่7 คือรับค่าที่เป็น character, space, @, character จากตัวแปร item ใส่ใน ตัวแปร line
5. บรรทัดที่8 คือการแยกค่าจากตัวแปร line เป็น usernameและ domain_name
6. บรรทัดที่9 คือการprintค่า usernameและdomain_nameออกมา