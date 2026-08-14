# Changelog

การเปลี่ยนแปลงสำคัญของโปรเจกต์บันทึกตามรูปแบบ [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) และใช้ [Semantic Versioning](https://semver.org/)

## [2.1.0] - 2026-08-14

### Added

- Shot Priority แบบ P1 ต้องมี, P2 ควรมี และ P3 ถ้ามีเวลา
- Minimum viable coverage สำหรับสถานการณ์เวลาน้อย
- Emergency checklist สำหรับแบต พื้นที่ เสียง ความร้อน อินเทอร์เน็ต และไฟล์สูญหาย
- Privacy checklist สำหรับ consent, venue rules, API key, token, repository และข้อมูลส่วนบุคคล
- แนวทางแบ่งบทบาทสำหรับผู้ถ่ายคนเดียว ทีม 2 คน และทีม 3 คนขึ้นไป
- Editing workflows สามระดับ: CapCut only, CapCut/DaVinci และ DaVinci/After Effects
- ชุด eval 3 สถานการณ์และสคริปต์ `scripts/run_evals.py`
- Source register พร้อมลิงก์และวันที่ตรวจล่าสุด
- ภาพตัวอย่างและเอกสาร GitHub ฉบับปรับปรุง

### Changed

- เพิ่ม Emergency/Privacy และ Workflow level ในรูปแบบคำตอบหลัก
- จำกัด P1 ให้ถ่ายได้จริงและให้กิจกรรมหลักสำคัญกว่าช็อตเสริม
- ระบุข้อจำกัดของการส่ง timeline จาก CapCut และลดการ render ซ้ำ

## [2.0.0] - 2026-08-14

### Added

- Packaging ก่อนถ่าย: viewer promise, title options และ thumbnail moment
- Progressive beats, evidence B-roll และ human track
- Retention map, short-form story arc และ post-publish loop
- Creator pattern library พร้อมแหล่งอ้างอิง

## [1.0.0] - 2026-08-14

### Added

- Story arc แบบ Before / During / After
- ไทม์ไลน์ถ่ายทำและแผนตัดต่อสำหรับวล็อกแข่งขัน
- แนวทาง CapCut, DaVinci Resolve, After Effects และมายด์แมพ

