# STM32F469 / DISEN — PCB Yerleşim İncelemesi P1

**Yerleşim tamamlandı; routing yapılmadı.** Onaylı Rev I şematiği ve özgün footprint kütüphanesi değiştirilmeden gerçek KiCad 9 PCB dosyası oluşturulmuştur. Kullanıcının seçimi doğrultusunda kart, **bağımsız ve kablolu adaptör** olarak tasarlanmıştır; DISCO üzerine mekanik olarak takılan bir daughterboard değildir.

## Açılış ve inceleme

`Project/STM32F469_DISEN_RevI.kicad_pro` dosyasını **KiCad 9** ile açın. Aynı klasördeki `.kicad_pcb` gerçek PCB yerleşimidir; `.kicad_sch` dosyaları onaylı şematiğin birebir kopyalarıdır. Kütüphaneleri ve `3D/` klasörünü birlikte tutun.

- `Placement_Review.pdf`: kısa değerlendirme, üst/alt ve 3D görünümler, montaj ve mekanik çizimler.
- `Views/01_PCB_Top.png`: üst görünüm.
- `Views/02_PCB_Bottom.png`: alt görünüm; altta SMD komponent yoktur.
- `Views/03_PCB_3D_Isometric.png`: gerçek PCB dosyasının KiCad 3D render'ı.
- `Views/04_Assembly_Top.svg`, `05_Assembly_Bottom.svg`, `06_Mechanical_Placement.svg`: vektör çizimler.
- `Verification/`: DRC/ERC ve pin/net karşılaştırması.
- `placement_coordinates.json`: sol üst nominal kart köşesine göre yerleşim koordinatları, mm/derece.

## Kart ve mekanik

| Özellik | Seçim |
| --- | --- |
| Nominal ölçü | **46 × 40 mm** |
| Köşe yarıçapı | 2 mm |
| Nominal kalınlık | 1,6 mm |
| Katman | 4 bakır katman |
| Montaj | Üst yüzde 49 devre footprint'i; R1/R2 DNP |
| Delikler | 4 × Ø2,7 mm NPTH, M2.5 için |
| Delik merkezleri | (3,5;3,5), (42,5;3,5), (42,5;36,5), (3,5;36,5) mm |
| Donanım zarfı | Her delik çevresinde Ø5,9 mm courtyard; nominal vida başı Ø5 mm |
| Yüzey | ENIG önerisi |

J1 ve J2 aynı üst kenarda yan yanadır; J3 sol kenara, harici 5 V girişi J4 sağ kenara, CN12 kablo soketi J5 alt kenara konmuştur. FPC servis/çıkış alanları `Dwgs.User` katmanında gösterilir. J4'te kare pad **pin 1 = GND**, diğer pad **pin 2 = +5 V** olarak korunmuştur. PCB üzerinde `G` ve `+` işaretleri vardır. Dört delik ve komponent courtyard'ları arasında çakışma yoktur. Konnektörler board üzerine sabitlenmiş host geometrisine göre değil, kablo erişimine göre yerleştirilmiştir.

## Alternatiflerin değerlendirilmesi

Aynı pad numaraları korunarak üç geometri incelenmiştir. Aşağıdaki sayılar pad merkezleri arasındaki düz çizgi mesafesidir; route edilmiş hat uzunluğu değildir.

| Alternatif | Ortalama DSI mesafesi | En büyük DSI mesafesi | Değerlendirme |
| --- | --- | --- | --- |
| Karşılıklı kenarlar | 36,53 mm | 38,00 mm | Doğrudan görünen fakat uzun bağlantı alanı |
| **Aynı kenarda paralel — seçilen** | **14,99 mm** | **16,50 mm** | Kısa DSI alanı, ortak FPC servis kenarı |
| Komşu kenarlarda 90° | 18,76 mm | 19,76 mm | Daha fazla yön değişimi ve geniş escape alanı |

Seçilen düzende 20 × 4 mm komponentten arındırılmış bir MIPI geçiş koridoru ayrılmıştır: x=14–34 mm, y=7–11 mm. Pin dizilimi J1'de D0/CLK/D1, J2'de D0/D1/CLK olduğundan sıralama değişimini ve çiftlerin karşılıklı pad sıralarını routing sırasında çözmek gerekir. Netler veya P/N eşlemeleri değiştirilmemiştir. Clock/data çiftlerinin katman geçişi gerekebilir; bu aşamada **hiç via eklenmemiştir**.

## Katman yapısı ve sinyal bütünlüğü

| Katman / dielektrik | Nominal kalınlık | Amaç |
| --- | --- | --- |
| F.Cu | 35 µm | Üst komponentler ve sinyaller |
| FR4 prepreg | 0,10 mm | Yakın GND referansı |
| In1.Cu | 35 µm | İleride kesintisiz GND referansı için ayrıldı |
| FR4 core | 1,26 mm | Çekirdek |
| In2.Cu | 35 µm | İleride alt sinyallerin GND referansı için ayrıldı |
| FR4 prepreg | 0,10 mm | Yakın GND referansı |
| B.Cu | 35 µm | Alt escape/kontrol bağlantılarına ayrıldı |

Bu yapı PCB dosyasına kaydedilmiştir. **GND plane veya başka copper pour yoktur.** DSI için 100 Ω diferansiyel empedans hedeflenir; 0,15/0,15 mm genişlik/aralık netclass değerleri yalnızca başlangıç yer tutucusudur. Üreticinin gerçek stackup, bakır ve dielektrik bilgisiyle hesaplanmadan empedans doğrulanmış sayılmaz. Pair içi skew, dönüş yolu, via geçişleri ve toplam flex+PCB uzunluğu routing aşamasının kontrolleridir.

## Backlight ve analog bölüm

Boost bölümü kartın alt/sağ kısmında, MIPI koridorundan ayrı tutulmuştur. U1-SW → D1 → C4 → U1-GND yüksek frekans döngüsü kompakt tutulmuş; L1'in SW ucu U1'e, C2 VIN pinine, R7 FB pinine yakın yerleştirilmiştir. C3 çıkış bulk kondansatörü D1 çıkış tarafındadır. C9 ve R7 quiet uçları SW düğümünden ayrı tarafta, U2 ve R19/R20 bölücü grubu switcher'ın solunda bulunur. R19/R20 paralel ve hizalıdır. F2/D3/R12 güç girişi grubunu oluşturur.

| Kritik iki pad arası mesafe | Kuş uçuşu |
| --- | --- |
| C2 besleme → U1 VIN | 1,96 mm |
| C4 GND → U1 GND | 1,96 mm |
| R7 sense → U1 FB | 2,51 mm |
| D1 anot → U1 SW | 3,57 mm |
| L1 SW → U1 SW | 4,34 mm |

Bu mesafeler yerleşim ölçütüdür; bakır bağlantı direnci, loop inductance veya termal doğrulama yerine geçmez. Routing sırasında SW alanı küçük, C4 dönüşü kısa, R7/FB bağlantısı Kelvin yaklaşımıyla ve kontrol hatları SW'den ayrı tutulmalıdır. Yeni routing için kullanıcı onayı beklenir.

## Yapılan kontroller

- 49 devre footprint'i, referans/değer ve DNP durumu onaylı şematikle eşleşiyor.
- **57 net / 172 pin-net üyeliği** birebir korundu; pad numaraları yeniden eşlenmedi.
- Onaylı üç şematik dosya, sembol kütüphanesi ve özgün footprint dosyaları byte düzeyinde aynı.
- KiCad 9.0.2 DRC: **0 yerleşim ihlali, 0 schematic parity sorunu**. Courtyard, mask/silk, pad clearance, kart kenarı, delik ve outline kontrolleri etkin.
- Şematik ERC: **0 ihlal**.
- **115 açık bağlantı bulgusu bekleniyor:** dosyada 0 iz, 0 via, 0 zone vardır. Açık bağlantı kontrolü kapatılmadı ve hiçbir DRC bulgusu exclusion ile gizlenmedi. Bu sonuç, tüm devrenin routing DRC'sinden geçtiği anlamına gelmez.
- 35 monte edilen gövdenin 3D dosyası proje içinden çözülür; DNP R1/R2 gövdesi çizilmez, test noktaları çıplak pad olarak görünür.

## Doğrulama sınırları

**FPC ve sistem mekanikleri:** Orijinal Hirose land pattern çizimleri, panelin mekanik CAD'i, seçilecek flex ve kasa geometrisi verilmedi. Mevcut footprint'teki lokal +Y yönü kablo ağzı olarak kabul edilerek J1/J2 çıkışı yukarı, J3 çıkışı sola planlandı. Pin numaraları, PCB üzerindeki geometri, boşluk ve çakışmalar denetlendi; gerçek kontakt yüzü, aktüatörün açık hali, flex kalınlığı/tipi, kablo bükülme yarıçapı ve karşı konnektörle süreklilik henüz fiziksel olarak teyit edilmiş değildir. Hirose ve TI resmi PDF uçlarına bu ortamdan erişim 403 ile engellendi; erişilmemiş üretici çizimleri doğrulanmış gibi raporlanmamıştır. Kaynak şematikteki FPC teyit gereksinimi geçerlidir.

**3D model doğruluğu:** J1/J2/J3 ve L1 için nominal mekanik hacim modelleri oluşturuldu; bunlar üretici STEP modelleri değildir. Diğer gövdeler KiCad'in paket modelleridir. 3D görüntü üretici onaylı mekanik uyum simülasyonu değildir.

Bu teslim **yerleşim incelemesi P1** içindir. İmalat dosyaları veya tamamlanmış routing sunulmamıştır. Yerleşim onayından ve yukarıdaki mekanik/stackup teyitlerinden sonra routing aşamasına geçilebilir.

## Teknik kaynaklar

- [TI TPS61165 datasheet](https://www.ti.com/lit/ds/symlink/tps61165.pdf) — SW döngüsü, VIN bypass ve feedback ayrımı için esas alınan cihaz.
- [TI TLV3011B](https://www.ti.com/product/TLV3011B).
- [Hirose FH26W-39S](https://www.hirose.com/en/product/p/CL0580-2412-8-60).
- Sağlanan Rev I şematiği ve `Adapter_F469.pretty` kütüphanesi.
- [KiCad packages3D](https://github.com/KiCad/kicad-packages3D) — gövde model kaynakları ve hash'leri `Project/3D/SOURCES.json` içinde.
