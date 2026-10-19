# STM32F469I-DISCO / iki DISEN LCD — Rev K

**Ortak 39 pinli mimari şematiğe uygulandı; LCD-B'nin tam elektriksel uyumluluğu henüz doğrulanmış değildir.** Kullanıcı, yeni model için yalnızca tek sayfalık mekanik çizimin bulunduğunu bildirdi. Bu nedenle eksik besleme/rating bilgileri varsayımla kapatılmadı.

| Özellik | LCD-A: DS070HSD39T-132 | LCD-B: DS0700BOE1A39CO-0180A |
|---|---|---|
| LCD kontrolcüsü / çözünürlük | OTA7290B / 280×1424 | JD9365DA-H3 / 280×1424 |
| MIPI / 39 pin | 2 data lane + clock | Pin numarası ve polariteler eşleşiyor |
| Touch | ILI2130, I²C | GT911, I²C |
| Backlight çizimi | 8 seri × 2 paralel, 16 LED | 4 seri × 2 paralel, 8 LED |
| LED gerilimi / IF | 21,6–27,2 V / 40 mA | 12 V tipik / 40 mA yazıyor; maksimumlar yok |
| VCI, pin 7–10 | 3,0–3,6 V | Gerilim aralığı verilmemiş |
| VDD, pin 30–31 | 3,3 V touch beslemesi | Sadece VDD yazıyor; işlev/aralık doğrulanmalı |
| Ayrı 6 pin touch flex | GND/SCL/SDA/RST/INT/3V3 | Aynı sıra; adaptörün host J3 girişine takılmaz |

İki çizimde de IF=40 mA yazdığı için **R7=5,23 Ω korundu: nominal 38,24 mA**. Modül toplam akımı yorumu, özellikle B için üretici onayı bekler; 80 mA modu eklenmedi. MIPI üzerinde anahtarlama yoktur. Tek J2 kullanılır; ekran fiziksel olarak, bütün beslemeler kapalıyken değiştirilir.

## Donanım seçimi

| Ayar | LCD-A | LCD-B |
|---|---|---|
| JP1 — yalnızca OVP seçimi | **2–3 HIGH**, nominal 28,690 V | **1–2 LOW**, nominal 14,936 V — geçici aday |
| R7 | 5,23 Ω, aynı kalır | 5,23 Ω, aynı kalır |
| R4 — VCI bağlantısı | Besleme bütçesi kontrolünden sonra 0 Ω takılır | VCI'nin 3,3 V uyumu doğrulanana kadar **DNP** |
| R23 — pin 30/31 bağlantısı | Belgelenmiş 3,3 V touch hattı için 0 Ω takılır | VDD işlevi ve gerilimi doğrulanana kadar **DNP** |

**Varsayılan dosya/BOM, FACTORY HOLD konfigürasyonudur:** R4/R23 DNP, JP1 üzerinde shunt yok. Bu konfigürasyon bir çalıştırma talimatı değildir. R4/R23'ün açık olması, sinyal pinlerini veya LEDA'yı tamamen ayırmaz; panel kabloları bağlanmadan önce gerekli ayarlar/doğrulamalar tamamlanmalıdır. A için onaylı kurulum yapılırken KiCad'de bu iki parçanın DNP işareti de kaldırılmalıdır. B için onay gelmeden değiştirilmemelidir.

JP1, çıkışı sabit 12 V veya 27 V'a ayarlamaz; **koruma eşiğini** seçer. U1 LED akımını regüle eder. Shunt yokken nominal 10,391 V düşük eşikli geri dönüş bulunur; bu bir enable interlock veya sert OFF değildir. Tek shunt kullanılır; üç pinin tamamı köprülenmez. Yeni panelin maksimum Vf ve mutlak sınırları verilmediğinden 14,936 V ayarı güvenli sınır olarak onaylanmış değildir.

## Dosyalar ve kontrol

- `Project/STM32F469_DISEN_RevK.kicad_pro`: KiCad 9 ile açılacak gerçek proje.
- `PDF/STM32F469_DISEN_RevK_DualLCD.pdf`: dört A3 sayfa; son sayfa native konfigürasyon/karşılaştırma tablosudur.
- `PDF/Dual_LCD_Engineering_Review_TR.pdf`: Türkçe kısa mühendislik incelemesi.
- `BOM/BOM_RevK_FACTORY_HOLD.csv` ve `BOM/Assembly_Modes.csv`.
- `Verification/ERC_RevK.txt` ve JSON: **0 hata, 3 korunmuş tekil global etiket uyarısı**.
- `Verification/RevJ_to_RevK_Changes.json`: beş mevcut pin-net değişikliği; diğer mevcut pinler korunur.
- `Verification/Dual_LCD_39_Pin_Audit.csv`: iki belge ile 39 pin karşılaştırması.
- `Verification/OVP_and_Power_Calculations.json`: gerçek netlist üzerinden seçim konumlarının nodal hesabı.
- `Original/Submitted_Schematic_RevJ_Review.zip`: yüklediğiniz arşiv, byte düzeyinde değiştirilmeden korunmuştur.

Yeni parçalar **R21, R22, R23 ve JP1**'dir. Toplam 53 fiziksel sembolün pinleri footprint pad numaralarıyla eşleştirildi. ERC kuralları/exclusion'lar değiştirilmedi. ERC; gerçek besleme gerilimlerini, DNP/jumper montajını veya OVP geçici rejimini doğrulamaz.

**PCB routing ve yazılım geliştirilmedi.** Mevcut PCB, dört yeni footprint ve yeni bağlantılar için ECO gerektirir. Yüklemedeki autosave/PCB/yedekler yalnızca Original arşivinde korunur; eski bir PCB yeni aktif proje içine konmadı. B'nin VCI/VDD bilgileri, maksimum LED değerleri, gerçek FPC eşleşmesi, kontrolcü başlangıç gereksinimleri ve OVP ölçümleri kapanmadan üretim/çalışma onayı verilmez.
