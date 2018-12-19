# StackBehavior
โครงงานวิเคราะห์ข้อมูลเว็บไซต์ Stack Overflow ผ่านคำถาม, คำตอบ, ความคิดเห็น และพฤติกรรมโดยรวมของผู้ใช้บนเว็บไซต์

* โครงงานนี้เป็นส่วนหนึ่งของรายวิชาการแก้ปัญหาทางด้านเทคโนโลยีสารสนเทศ (06016314) สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง

## Topics
> หัวข้อในการวิเคราะห์

### ความนิยมของห้วข้อต่างๆในปีที่ผ่านมา
วิเคราะห์ความนิยมจากแท็กที่ผู้ใช้ใส่ไว้กับคำถามในแต่ละตัว

### พฤติกรรมของผู้ใช้ผ่านบริบทของความคิดเห็นที่แสดง
วิเคราะห์พฤติกรรมของผู้ใช้ผ่านบริบทเชิงบวกและเชิงลบ ของความคิดเห็นที่แสดงลงบนคำถามและคำตอบ

### กิจกรรมของผู้ใช้โดยเฉลี่ยต่อปี
วิเคราะห์ว่าช่วงเวลาในแต่ละปีนั้นส่งผลกระทบต่อกิจกรรมของผู้ใช้อย่างไร

## Results
> ผลการวิเคราะห์

* [ดูผ่านเว็บไซต์](https://phwt.github.io/StackBehavior/)
* [ดูผ่าน YouTube](https://www.youtube.com/watch?v=0eT0Aw0En2s)

## Data Sources
> แหล่งที่มาของข้อมูล
#### [ข้อมูลสาธารณะเว็บไซต์เครือ StackExchange - StackOverflow](https://archive.org/download/stackexchange)
* `badges` - เหรียญตราที่ได้รับ  - 1.19 GB
* `comments` - ความคิดเห็นที่แสดง - 12.01 GB
* `post_questions` - คำถามที่ถูกถาม - 25.10 GB
* `post_answers` - คำตอบที่ตอบ - 20.17 GB
* `tags` - แท็กที่ใส่ลงในคำถาม - 2.08 MB
* `users` - ข้อมูลผู้ใช้ - 1.4 GB

**ช่วงเวลาของข้อมูล** - 2008 - 2018

**ขนาดโดยรวม** - 59.87 GB (โดยประมาณ)

## Built-With
> เครื่องมือที่ใช้

* Python `3.7.0`
    * pygal `2.4.0`
* Google Cloud Platform
    * BigQuery
    
## Development Setup
> การตั้งค่าเพื่อการพัฒนา

ลงไลบราลีที่จำเป็น

    pip install pygal
    
### Directory Structure
> โครงสร้างไดเรกทอรี
* `dataset`
  * `data` - ข้อมูลดิบและข้อมูลที่ประมวลผลแล้ว
  * `query` - กระบวนการ Query ข้อมูลผ่าน BigQuery
* `convert` - ไฟล์สำหรับแปลงข้อมูลดิบเป็นข้อมูลสำหรับการการแปลงเป็นกราฟ
* `visualize` - ไฟล์สำหรับแปลงข้อมูลเป็นกราฟ
* `docs` - เว็บไซต์ของโครงงาน

**หมายเหตุ** - ที่อยู่ของไฟล์ทั้งหมดนั้นตั้งไว้ตรงกับรูทไดเรกทอรีของโครงงานทั้งหมด (`./StackBehavior/...`)

## Authors
> ผู้จัดทำ

* นายภูวทิตต์ สัมมาวิวัฒน์ - 61070173 - [phwt](https://github.com/phwt)
* นายวีรพงศ์ ทันจันทึก - 61070213 - [veerapong76](https://github.com/veerapong76)
* นายณภัทร พรบุญเรือง - 61070044 - [61070044](https://github.com/61070044)
* นายสหัสวรรษ หิรัญเพชร - 61070239 - [maizerocom](https://github.com/maizerocom)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
