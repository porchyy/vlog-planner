# Editing Workflows

ใช้ไฟล์นี้เมื่อเลือกโปรแกรม วางการส่งงานข้ามแอป หรือสร้าง checklist export เลือก workflow ที่สั้นที่สุดซึ่งตอบคุณภาพและเวลาส่งจริง

## เลือกระดับ workflow

| ระดับ | เหมาะกับ | Toolchain | จุดควบคุมหลัก |
|---|---|---|---|
| มือใหม่/เร็วที่สุด | มือถือ, งานวันเดียว, ต้องโพสต์เร็ว | CapCut เท่านั้น | story cut, captions, basic color, sound balance, export |
| ระดับกลาง | มีคลิปยาวและ social versions หรือต้องการ color/sound ดีขึ้น | CapCut -> DaVinci หรือ DaVinci เท่านั้น | ล็อก story ก่อนส่ง, relink media, color, sound, master |
| ระดับจริงจัง | หลายกล้อง, motion graphics, compositing หรือส่งงานหลายเวอร์ชัน | DaVinci -> After Effects -> DaVinci | timecode, frame rate, alpha/intermediate codec, round-trip QC |

อย่าแนะนำ After Effects เพียงเพื่อทำข้อความหรือ counter ธรรมดาที่โปรแกรมหลักทำได้อยู่แล้ว

## Workflow A: CapCut โปรแกรมเดียว

1. สำรองไฟล์และจัดอัลบั้มตามวันหรือ milestone
2. เลือก progressive beats, reaction และ evidence B-roll
3. ทำ story cut โดยยังไม่ใส่ transition/effect
4. ตัด context ซ้ำและวาง re-hook เมื่อเรื่องเปลี่ยน
5. เพิ่ม caption, counter, screen zoom และ sound design เท่าที่จำเป็น
6. ตรวจชื่อบุคคล ตัวเลข caption privacy และระดับเสียงด้วยหูฟัง
7. export master แล้วทำสำเนา 16:9 หรือ 9:16 จาก timeline ที่ duplicate ไว้

## Workflow B: CapCut -> DaVinci Resolve

ใช้เมื่อคัดคลิปหรือทำ captions ใน CapCut ได้เร็ว แต่ต้องการจบ color/sound ใน DaVinci:

1. ล็อก story และความยาวก่อนออกจาก CapCut
2. export clean intermediate ที่ไม่มี captions/effects ถ้าต้องทำ finishing ใหม่
3. ใช้ resolution และ frame rate เดียวกับ master หลีกเลี่ยง variable frame rate เมื่อทำได้
4. ส่งไฟล์คุณภาพสูง เช่น ProRes 422, DNxHR HQ/HQX หรือ H.264/H.265 bitrate สูงเมื่อพื้นที่จำกัด
5. ทำ color, dialogue cleanup, loudness balance และ master export ใน DaVinci
6. กลับ CapCut เฉพาะเมื่อจำเป็นต้องสร้าง social version ที่เร็วกว่า และห้ามบีบอัดวนหลายรอบ

หมายเหตุ: CapCut ไม่มี round-trip timeline ที่เชื่อถือได้กับทุกเวอร์ชัน ให้ถือไฟล์ intermediate เป็นจุดส่งต่องาน ไม่รับประกัน XML/AAF interchange

## Workflow C: DaVinci -> After Effects -> DaVinci

1. ingest, sync, rename และทำ story cut ใน DaVinci
2. ล็อกช็อตที่จะส่ง AE พร้อม handles 12-24 เฟรมเมื่อมี transition
3. ส่งเฉพาะช็อต motion/compositing ด้วย image sequence, ProRes 4444 หรือ codec ที่รองรับ alpha ตามงาน
4. รักษา resolution, frame rate, color space และชื่อช็อตให้ตรงกัน
5. render กลับเป็นไฟล์ intermediate แล้ว replace/relink ใน DaVinci
6. ทำ color, sound mix, caption master และ export final ใน DaVinci

## กติกาส่งงานข้ามโปรแกรม

กำหนดรายการนี้ทุกครั้งที่ใช้มากกว่าหนึ่งแอป:

- master resolution และ orientation
- frame rate และการจัดการคลิป variable frame rate
- color space/gamma
- audio sample rate โดยทั่วไป 48 kHz สำหรับวิดีโอ
- naming เช่น `PROJECT_DATE_SCENE_SHOT_VERSION`
- ตำแหน่ง master, social exports, graphics และ archive
- จุดที่ story lock, picture lock และ final QC

## Export และ QC

- ดู master ตั้งแต่ต้นจนจบอย่างน้อยหนึ่งรอบ
- ตรวจ sync, caption, line break, safe zone, flicker, black frame และเสียง peak
- ตรวจหน้าจอทุกช็อตอีกครั้งเพื่อหา secret หรือข้อมูลส่วนบุคคล
- ทดสอบไฟล์บนโทรศัพท์หนึ่งเครื่องและคอมพิวเตอร์หนึ่งเครื่องเมื่อทำได้
- เก็บ master คุณภาพสูงแยกจากไฟล์ upload และเก็บ project/archive ตามความสำคัญของงาน

