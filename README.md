# ร้านขายของชำธัญลักษณ์ช็อป

เว็บแอปพลิเคชันร้านขายของชำ พัฒนาด้วย **Django Framework** ร่วมกับ **SQLite Database** และใช้ **HTML, CSS, JavaScript** ในการออกแบบและตกแต่งหน้าเว็บ

<br>

### ตัวอย่างหน้าจอระบบ

| Home                                                                                                  | Product Detail                                                                                        | Search                                                                                                |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/user-attachments/assets/be84acf4-5296-4b5c-bb42-3b0f2b2954e7" width="300"/> | <img src="https://github.com/user-attachments/assets/6f0b48c3-99d4-4f55-adfc-3410580b026c" width="300"/> | <img src="https://github.com/user-attachments/assets/3bb160b9-e73a-45e0-850e-7b93b62bd857" width="300"/> |

| Dashboard                                                                                             | Product List                                                                                          | Order List                                                                                           |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| <img src="https://github.com/user-attachments/assets/8f283b9d-36c1-4cc1-9d8a-11cc1449deb2" width="300"/> | <img src="https://github.com/user-attachments/assets/c3c76352-e2e4-4258-af9a-a94ea52451c2" width="300"/> | <img src="https://github.com/user-attachments/assets/21f84a56-8923-4c23-b810-72640b444123" width="300"/> |

<br>

### ⚙️ ขั้นตอนการติดตั้ง

#### 1️. Clone โปรเจกต์จาก GitHub

```bash
gh repo clone nantiwan47/ThanyalakShop
```

หรือ

```bash
git clone https://github.com/nantiwan47/ThanyalakShop.git
```

เข้าไปยังโฟลเดอร์โปรเจกต์

```bash
cd ThanyalakShop
```


#### 2️. สร้าง Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```


#### 3️. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```


#### 4️. รัน Django Project

```bash
python manage.py runserver
```

<hr>


### 👤 การเข้าสู่ระบบ

สามารถสร้าง Superuser ของตัวเองได้ด้วยคำสั่ง:

```bash
python manage.py createsuperuser
```

หรือใช้บัญชีที่มีมาให้แล้ว:

| Role     | Username | Password      |
| -------- | -------- | ------------- |
| 🔑 Admin | `admin1` | `admin123`    |
| 🔑 Admin | `admin2` | `admin123`    |
| 👥 User  | `user1`  | `password123` |
| 👥 User  | `user2`  | `password123` |
| 👥 User  | `user3`  | `password123` |
| 👥 User  | `user4`  | `password123` |
| 👥 User  | `user5`  | `password123` |
