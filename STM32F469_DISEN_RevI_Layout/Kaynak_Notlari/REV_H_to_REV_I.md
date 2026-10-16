# STM32F469I-DISCO / DISEN LCD — Rev H → Rev I

15 Ekim 2026 | KiCad 9 projesi | **Laboratuvar prototipi; üretime onay DEĞİL**

## Yapılan gerçek şematik değişiklikleri

1. `Protection.kicad_sch` sayfası ve root hiyerarşideki “Latched backlight safety cutoff” alt sayfası kaldırıldı.
2. Kullanılmayan Q1/Q2/Q3 MOSFET, U3 latch, D4, C14/C15, R21–R25 ile bunların montaj footprint/simge tanımları temizlendi.
3. J5.4 / NRST ve J5.8 / PC7 bağlantıları tekrar NC; host'un iki kullanılmayan pini adapter tarafından sürülmüyor.
4. TPS61165 önündeki R12 0 ohm güç bağlantısı **FIT** (Rev H DNP durumunun tersine). R12 takılmadan booster 5 V almaz.
5. U2 TLV3011B open-drain çıkışı `OVP_OK` yerine doğrudan `BL_CTRL` netine bağlı: eşik aşıldığında CTRL'yi LOW'a çekmek üzere mevcut Rev E yapısı geri getirildi.
6. DSI D0/D1/CLK; LCD RESET/TE; I²C SDA/SCL; touch INT/RESET ve 3.3V hatlarında kablaj değiştirilmedi.
7. Proje, title-block, sayfa dosyası ve instance proje adları Rev I olarak güncellendi.

## Korunan donanım

- 25-pin STM32 CN10, 6-pin STM32 CN2, 2x8 CN12 ve 39-pin DISEN FPC konektörü
- TPS61165DBVR, 22 uH L1, SS16 D1, 10 uF/50 V C3, 5.23 ohm R7 (nominal 38.24 mA)
- Harici +5 V girişi, F2 PTC, ters beslemeye karşı D3, 0R izolasyon R12, 33k çıkış deşarj R18
- TLV3011B (OVP nominal 28.69 V), 221k/10k hassas direnç bölücüsü
- LCD/touch yerel kondansatörleri, seriler, test noktaları ve ihtiyaç olmayan pull-up DNP seçimleri

## Kritik önemli NOT

**Koruma ve 30 V:** TPS61165 internal open-LED protection ~38 V; FH26W-39S-0.3SHW DC voltage rating 30 V. U2'nin nominal 28.69 V'luk düşük-aktif CTRL müdahalesi 30 V tepe limitini garanti etmez. 2.5 ms CTRL low shutdown gecikmesi, bobin ve C3 enerjisi düşünülmelidir. Bu nedenle osiloskop ile ölçüm ve donanım geçerliliği gösterilmeden üretim/PCB release yapılamaz. Uygun donanım clamp/yeniden tasarım gerekebilir.

**Dokunmatik güç:** DISEN çiziminde TP 2.8–3.3 V deniyor; mutlak/sürekli maksimum tolerans açıklığa kavuşturulmalı. ST 3V3 rayı yük/tolerans ve panel akım sınırları belirsiz.

**Konektör mekaniği:** Panelin önerdiği FH26-39S ve projedeki FH26W-39S fiziksel uç genişliği, kontak yönü, pin 1 ve kalınlık ilişkisi üretici çizimleriyle ayrıca doğrulanmalı.

**DSI:** 2 data lane + differential CLK doğrudan bağlı. PCB 100 ohm differential routing, giriş çıkış FPC kablo polaritesi ve host LCD'nin sökülmesi hâlâ zorunlu kontroller.

**KiCad:** Bu çalıştırma ortamında `kicad-cli` kurulu değil. Native KiCad ERC ve native PDF plot **çalıştırılamadı**. Statik denetim raporu ayrıca mevcut; Rev E'ye eşdeğerlik Rev I için native ERC anlamına gelmez.
