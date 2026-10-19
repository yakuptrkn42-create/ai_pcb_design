# Rev J / PCB Hazırlık 1 — DS070HSD39T-132

19 Ekim 2026 · KiCad 9.0.2 · Bağımsız, kablolu laboratuvar adaptörü.

## Sonuç ve yapılan değişiklikler

Yüklenen Rev J temel alındı; çift LCD Rev K dosyaları değiştirilmedi. 49 devre referansı, 57 net ve 172 numaralı pinin net üyeliği kaynakla aynıdır. Komponent değerleri, footprint kimlikleri, sembol UUID'leri, güç netleri, DNP kararları ve üç sayfanın fonksiyonel yerleşimi korunmuştur. Yeni elektriksel blok veya bağlantı değişikliği yoktur. Başlıklar “J / PCB preparation 1” olarak ayrıldı.

İki FPC footprint'inin sade gövde, silkscreen ve courtyard çizimleri, KiCad 9 FH26 ailesinin 90° dönüştürülmüş çizimleriyle iyileştirildi; bakır pad'ler ve pasta açıklıkları aynen kaldı. J1 için FH26 → FH26W ailesi benzerliği, kesin üretici mekanik onayı değildir. Test pad kütüphanesinin BOM hariç tutma bayrağı, mevcut şematiğin metadata'sıyla eşlendi; BOM'da bunlar satın alınacak parça sayılmaz.

Her referansa yerel model bağlandı: 14 farklı dosya, 9 KiCad WRL ve 5 yeni STEP. Konnektörler ve endüktör nominal gövde/temas modelleridir; üretici tarafından onaylanmış exact MPN CAD'i değildir. Test noktası STEP'i yalnızca 1 mm çaplı, 35 µm nominal bakır disktir; ilave test pini veya komponent öngörmez. Ölçek 1:1, offset ve dönüş 0; model +Y ekseni footprint −Y yönüne karşılık gelir. Kaynaklar, boyutlar ve hash'ler `Project/3D/SOURCES.json` içindedir.

## Elektriksel son kontrol

DISEN'in 20 sayfalık A0 preliminary belgesi ve ayrı touch çizimi; ST UM1932 Rev 5; TI TPS61165 SLVS790E tekrar incelendi. J2'nin 39 kontağı, ST CN10/CN12 kullanılan pinleri ve altı DSI iletkeni netlist/PCB karşılaştırmasıyla kontrol edildi. Ayrıntılı önceki inceleme, belirsizlikleriyle birlikte pakette korunmuştur.

| İşlev | Kontrol / sonuç |
|---|---|
| DSI D0, D1, CLK | J1 +/−: 10/8, 18/16, 14/12 → J2 +/−: 16/17, 20/21, 24/25. İki veri lane'i; polarite değişmedi. Haricî 100 Ω sonlandırma veya anahtar eklenmedi. |
| LCD / touch besleme | J2.7–10 = LCD_VCI; .30/.31 = TP_VDD. Ayrı host girişleri birleştirilmedi. VCI 3,0–3,6 V. Touch çizimi 2,8–3,3 V; garantili üst tolerans ve yük akımları eksik. |
| Touch / kontrol | J2.32 SCL, .33 SDA, .34 reset, .35 INT. J3 host CN2 girişidir; panelin ayrı 6 pin touch kuyruğu buraya takılmaz. J5.6 PC6 PWM; .12 PB12 bağımsız touch reset; .2 GND. PH7 LCD reset ve PJ2 TE korunur. |
| TPS61165 | DBV: 1 VIN, 2 CTRL, 3 SW, 4 GND, 5 COMP, 6 FB. LEDK, GND değildir; FB/R7 dönüşüdür. R7 = 5,23 Ω %1 → 38,24 mA nominal, FB/R toleranslarıyla 37,10–39,40 mA. |
| Güç katı | 22 µH, SS16 / 60 V / 1 A; 10 µF + 100 nF giriş/çıkış; çıkış kapasitörleri 50 V. 0,75 A hold sigorta, SS14 ters blok ve ayrı 5 V girişi korundu. Host +5 V ile birleştirilmedi. |
| OVP / PWM | 221 kΩ / 10 kΩ ile nominal 28,69 V. U2 ve C13, Rev J'deki gibi BL_POWER üzerinde. Open-drain OUT, CTRL'yi LOW'a çeker; hızlı veya garantili voltaj klempi değildir. PWM 20 kHz hedefi, TI 5–100 kHz aralığında. |

40 mA modül akımı ve 21,6–27,2 V LED aralığı esas alındı; iki paralel LED kolu nedeniyle akım 80 mA yapılmadı. VIN=4,2 V, verim=%75, Lmin=17,6 µH ve fsmin=1 MHz varsayımlarıyla en yüksek nominal yükte yaklaşık 1,106 W çıkış, 0,351 A ortalama / 0,452 A tepe giriş akımı hesaplanır. Bu değerler ölçüm veya arıza akımı yeterliliği değildir.

## Native PCB ve kurallar

Şematik gerçek `.kicad_pcb` dosyasına aktarıldı: 49 footprint, 57 net, 172 pin/net eşleşmesi ve 49 model bağı. DNP R1/R2 korunur. Şematik–PCB parity denetimi **0 fark** verdi. **Komponent yerleşimi yapılmadı: bütün footprint merkezleri (0,0) konumunda başlangıç aktarım yığınıdır.** 0 iz, 0 via, 0 zone ve 0 Edge.Cuts; kart boyutu henüz belirlenmedi.

| Sınıf / özellik | Kaydedilen taslak değer |
|---|---|
| Katmanlar | F.Cu sinyal/güç; In1.Cu GND referansı; In2.Cu GND referansı; B.Cu sinyal/güç. İç GND katmanları planlıdır; henüz dolgu yok. |
| Nominal stackup | 35 / 100 / 35 / 1260 / 35 / 100 / 35 µm; toplam 1,60 mm. FR4 Er=4,2 ve tanδ=0,02 varsayım. Maskenin elektriksel modeli yok. |
| Genel imalat tabanı | Min iz 0,125 mm; min clearance 0,15 mm. Default clearance/iz 0,20/0,20 mm. Kenara bakır 0,50 mm; delik–delik 0,30 mm. Üretici teyidi gerekir. |
| Via | Standart geçişli 0,60/0,30 mm çap/delik; alternatif 0,80/0,40 mm. Min annular ring 0,15 mm. Blind/buried veya microvia gerektiren bağlantı yok. |
| MIPI_DSI | 0,14 mm iz / 0,18 mm çift aralığı; clearance 0,15 mm. Launch için 0,125–0,19 mm. Çift içi fark ≤0,10 mm; altı iletkenin PCB fark bütçesi ≤1,0 mm. |
| DSI ek bütçeler | İletken başına PCB uzunluğu ≤50 mm, ≤2 geçişli via; öncelik 0 via. Bunlar başlangıç tasarım bütçeleridir; panelin zorunlu PCB uzunluğu olarak sunulmaz. Dış GND dolgusu için 0,50 mm uzaklık kuralı, kullanılan microstrip modeliyle tutarlıdır. |
| Güç / hassas | POWER_5V ve BOOST_SWITCH hedef 0,60 mm / min 0,30 mm. LED_HV hedef 0,40 / min 0,20 mm. LOGIC_POWER 0,30; SENSITIVE ve kontrol 0,20 mm. PWM/CTRL yanlışlıkla güç sınıfına atanmadı. |

2D quasi-static odd-mode hesapta 0,10 mm dielektrik / 35 µm bakır / Er=4,2 için 0,14/0,18 mm geometrisi yaklaşık **99,3 Ω diferansiyel** verir. 5 ve 2,5 µm ağ adımı karşılaştırması raporlandı. Soldermask, etch/trapez, frekans etkileri, konektör ve FPC dahil değildir. **Üretici ve onaylı stackup yoktur; 100 Ω ±%10 yalnızca teklif hedefidir.** Üretici geometrisi kesinleşince yeniden hesaplanmalıdır.

İnce ağda yayılma yaklaşık 184,8 mm/ns; 0,10 mm çift farkı yaklaşık 0,54 ps, 1 mm PCB farkı yaklaşık 5,4 ps eder. Panelin en yüksek hızdaki UI/50 inter-lane sınırı için host, kablo, PCB ve panel birlikte değerlendirilmelidir; yalnızca PCB bütçesi tam kanal uygunluğunu kanıtlamaz.

35 µm dış bakır için basit IPC-2221 / 10°C tahmini 0,60 mm izde 1,65 A; 0,30 mm daralmada 1,00 A verir. Bu bir IPC-2152/termal analiz değildir. 25 mm / 0,60 mm için 20°C'de yaklaşık 20,5 mΩ ve 0,4 A'da 8,2 mV düşüm hesaplanır; kablo, pad, komponent ve GND dönüşü dahil değildir. Logic yük akımları bilinmediğinden son kapasite kabulü verilmedi.

## Doğrulama ve kalan koşullar

ERC: **0 hata / 3 tekil global label uyarısı** (BL_SW, BL_COMP, OVP_SENSE). Kaynak ERC ayarları aynen korundu; yeni ignore veya exclusion yok. PCB'nin native net class çözümlemesi tüm 57 net için incelendi. Ayrı geçici denemede 0,24 mm DSI ve 0,20 mm güç izlerinin kurallarca reddedildiği görüldü. Bu deneme adaptöre iz eklemedi.

Yerleşimsiz PCB DRC'si 1577 ihlal ve 51 bağlantısız öğe kaydı verir: üst üste aktarımdan kaynaklanan kısa devre/clearance/courtyard/delik/yazı/mask çakışmaları ve henüz kart sınırı bulunmaması. **Bu sonuç üretim DRC geçişi değildir; 51 sayısı unrouted net sayısı değildir.** Hiçbir bulgu gizlenmedi. Yerleşim ve routing tamamlandığında bütün fiziksel DRC yeniden yapılmalıdır.

Aktif PCB, KiCad PCB Editor'da açıldı. 49 modelin ayrı geçici grafik kontrol panosundaki örnekleri gerçek KiCad 3D Viewer ve native raytracer ile görüntülendi. Bu panonun fotoğrafları `Views` içindedir; **adaptör yerleşimi veya kart boyutu değildir**. Aktif projeye kontrol panosu eklenmedi. STEP'ler yeniden içe alınıp solid geçerliliği ve bbox; model dosya yolları/hash/ölçek; sembol pinleri ve pad numaraları; şema–PCB yolları ayrıca denetlendi.

ZIP ayrı bir /tmp klasörüne çıkarılıp boş KiCad ayarlarıyla yeniden kontrol edildi: yerel 49 model yolu, 57 native net class ataması, ERC 0 hata / 3 uyarı ve parity 0 fark. Dosya hash manifesti de eşleşti. Portable_Check.json ayrıntıları içerir.

Yerleşim çalışmasına geçilebilir. Aşağıdaki koşullar üretim/enerji verme kabulünden önce kapanmalıdır:

- TLV3011B tam TI belgesindeki B/DBV çalışma, referans açılış ve beslemesiz OUT limitleri ile OVP transient testleri. TI'nin >2,5 ms CTRL LOW shutdown davranışı nedeniyle nominal eşik hızlı kesme garantisi değildir.
- ST MB1189 üzerinden host CN2 fiziksel sırası; gerçek kartın R117/R119 ve I²C pull-up popülasyonu; tüm kabloların pin-1 ve süreklilik kontrolü. CN10/CN12 kullanılan eşleşmeleri UM1932 ile doğrulandı; CN2 mekanik numaralandırması tam kapanmadı.
- J1/J2/J3 exact sipariş eki, FPC temas yüzü/kalınlığı, mekanik takılma ve latch hareketi. Nominal 3D gövde, gerçek üretici tolerans veya fiziksel fit kabulü değildir.
- Panel LCD/touch yük akımı, touch üst gerilim toleransı, ILI2130 reset/INT/I²C ayrıntıları; C3'ün çalışma geriliminde etkin ≥4,7 µF kapasitesi; eski L1 için stok veya yeterliliği tamamlanmış alternatif. Genel pasiflerin exact MPN seçimleri satın almada tamamlanmalı.
- Üreticinin onaylı 4 katman stackup'ı, bitmiş bakır/maske ve empedans toleransı; sonraki PCB'de kesintisiz GND, kısa boost döngüleri, FB/R7 Kelvin dönüşü ve decoupling yerleşimi.

Üretici sitelerine yeniden erişim denemeleri ağ proxy'sinden 403 aldı; bunlar otomatik onay reddi değildir. Erişilemeyen belgelerin doğrulandığı iddia edilmedi; kaynak Rev J'den açık kalan koşullar varsayımla kapatılmadı. Donanım testi, placement, routing, copper pour, yazılım veya üretim çıktısı yapılmadı. Kesin çalışma garantisi verilmez.
