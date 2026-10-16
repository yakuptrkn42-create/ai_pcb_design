# Rev J — Elektriksel tasarım incelemesi

Tarih: 16 Ekim 2026. Amaç: STM32F469I-DISCO ile DS070HSD39T-132 ekranın GUI/dokunmatik denemeleri için bağımsız, kablolu laboratuvar adaptörü. İnceleme ve şematik ECO tamamlandı; üretim kabulü verilmedi. Yeni koruma, regülatör veya işlev bloğu eklenmedi.

## 1. Sonuç ve revizyon sınırı

Kaynak projenin ana mimarisi korunmuştur: iki DSI veri çifti ve bir saat çifti doğrudan geçer; LCD ve touch, ayrı isimli host 3,3 V girişlerinden beslenir; LED boost için haricî regüle 5 V kullanılır. Orijinal host LED çıkışları bağlı değildir. LCD ve touch resetleri bağımsız tutulur.

Yalnızca iki fiziksel pinin neti değişti: **U2.6 ve C13.1, HOST_3V3 → BL_POWER**. OVP algılayıcısının beslemesi artık host 3,3 V'un gelmesine bağlı değildir. Bu, karşılaştırıcının açılışta hazır olduğunu veya çıkışı sert sınırladığını garanti etmez. **TLV3011B'nin tam SBOS300 belgesindeki çalışma aralığı, referans açılışı ve beslemesiz OUT davranışı bu oturumda birincil kaynaktan yeniden doğrulanamadı. Bu ECO'nun üretim öncesi kabulü bu kontrol ve ölçümlere bağlıdır.**

J2 temel MPN/değer/footprint adı, DISEN'in önerdiği FH26-39S-0.3SHW olarak düzeltildi. Eski FH26W adı üzerinden farklı seri bir konnektör sipariş edilmesi önlendi. Pad geometrisi aynen korundu ve KiCad 9 standart FH26 footprint'inin tüm 39 kontağı ve iki montaj pad'iyle 90° dönüş altında eşleştirildi. Bu CAD kontrolü gerçek flex takma deneyi veya Hirose sipariş eki doğrulaması yerine geçmez.

49 fiziksel komponent, 57 net ve 172 fiziksel pin üyeliği korunur. Diğer tüm bağlantılar, değerler ve DNP kararları önceki XML netlist ile eşleştirilmiştir. Şematik root/sheet ve fiziksel komponent UUID'leri korunmuştur.

## 2. Kaynaklar ve doğrulama düzeyi

- Kullanıcının DISEN 20 sayfalık PDF'i: A0, revizyon tarihi 2025-06-10, **Preliminary Specification**. Pin tablosu s.7; VCI/LED s.8; touch s.9; MIPI elektriksel tabloları s.12–14.
- Kullanıcının tek sayfalık touch/mekanik çizimi: A00, 2024-06-17. ILI2130, 2,8–3,3 V çalışma aralığı, 6 pin touch flex'i. Ana PDF s.6 da bu mekanik tarihi kullanır. Tarih farkı not edilmiştir; belgeye nihai onay statüsü atanmamıştır.
- ST üretici belgesi UM1932 Rev 5, GitHub'da saklanan PDF kopyası: CN12 tablo 6, CN10 tablo 7 ve CABC/R117/R119 açıklaması kontrol edildi. Resmî ST BSP'de PH7 LCD reset, PJ5 INT, PB8/PB9 I²C işlevleri de kontrol edildi.
- TI üretici belgesi TPS61165, SLVS790E, Nisan 2019, GitHub'da saklanan PDF kopyası: DBV pinleri, FB toleransı, PWM/shutdown, L/C seçimi, akım limiti ve OVP kontrol edildi.
- ST MB1189-C01 tam şematik paketi, TI TLV3011B tam veri sayfası ve Hirose tam mekanik kataloğu bu ortamda ilgili üretici sitelerinin erişim engeli nedeniyle alınamadı. İkincil proje yorumları üretici doğrulaması sayılmadı. CN2 fiziksel numaralandırması, host pull-up direnç popülasyonu ve U2 ayrıntıları açık tutuldu.

Paketlenen PDF'lerin kaynağı ve SHA-256 değerleri `References/SOURCES_TR.md` ve `MANIFEST_SHA256.json` içindedir. Belge içindeki kullanım/bakım notları tasarım girdisi olarak değerlendirildi; görev talimatı olarak uygulanmadı.

## 3. MIPI, LCD ve host bağlantıları

J2'nin **39 kontağının tamamı** DISEN s.7 tablosuyla karşılaştırıldı; altı DSI iletkeninde lane veya polarite değişikliği gerekmedi:

| Çift | Host J1 (+ / −) | LCD J2 (+ / −) |
|---|---|---|
| D0 | 10 / 8 | 16 / 17 |
| D1 | 18 / 16 | 20 / 21 |
| CLK | 14 / 12 | 24 / 25 |

J2.1/2 LEDA; .3/4 LEDK; .7–10 VCI; .12 RESX; .13 TE; .30/31 touch VDD; .32 SCL; .33 SDA; .34 touch reset; .35 INT'tir. .5/.6/.38/.39 NC olarak kalır. GND kontakları panel tablosuyla eşleşir. **LEDK, GND değildir:** U1.FB ve R7 üst düğümüne bağlı akım dönüşüdür.

UM1932 tablo 7, J1'in 25 pinini doğrular. J1.5=PH7 reset; .22=PJ2 TE; .6/.21=3,3 V. J1.23/.24 host LEDK/LEDA bilinçli NC'dir. J1.3 CABC'nin GND'ye alınması, UM1932'de belirtilen varsayılan R117 takılı/R119 takılı değil durumu için host boost'u kapatır. Gerçek kart popülasyonu kontrol edilmelidir; farklı konfigürasyon varsayılan kabul edilmez.

UM1932 tablo 6, CN12.2 GND, .6 PC6 PWM ve .12 PB12 touch reset eşleşmelerini doğrular. J3'teki PB8/PB9/PJ5 MCU işlevleri resmî BSP ile doğrulanmıştır; **CN2'nin fiziksel altı pin sırası bu oturumda MB1189 şemasıyla yeniden doğrulanamadı**. Mevcut eşleşme korunur; enerji vermeden kablo sürekliliği kontrolü gerekir.

DSI hatlarına AC coupling, genel amaçlı TVS, seri direnç veya haricî 100 Ω sonlandırma eklenmedi. Panelin s.12 tablosu nominal 100 Ω dahili sonlandırma gösterir. D-PHY LP durumlarını da kullandığı için doğrudan DC bağlantı uygundur. Bu inceleme kablo/PCB empedans ölçümü veya eye diyagramı doğrulaması değildir.

S.14, 80–1000 Mbit/s aralığına karşılık gelen 1–12,5 ns UI ve register'a bağlı hız sınırları verir; data-clock skew ±0,15 UI, inter-lane statik skew UI/50 yazılıdır. Bunlar sonraki PCB/flex incelemesinde gerçek çalışma hızına göre ele alınmalıdır. Örnek olarak 280×1424 RGB888 / 60 Hz aktif veri, iki lane için yaklaşık 287,1 Mbit/s/lane gerektirir; blanking/protokol payı hariçtir ve desteklenen mod garantisi değildir. OTA7290B başlatma komutları, piksel yönü ve gerçek timing bilgisi panel üreticisinden alınmalıdır; yazılım geliştirilmedi.

## 4. Backlight ve güç hesabı

DISEN, IF=40 mA tipik ve VF=21,6–27,2 V verir. 30 V LED mutlak maksimumu veya garanti edilen güvenli OVP tavanı verilmez. Önceki “30 V altında” hedefi üretici sınırı olarak kabul edilmedi.

R7=5,23 Ω ±%1 ve TI FB=196/200/204 mV:

- Nominal ILED = 0,200 / 5,23 = **38,24 mA**.
- Alt/üst tolerans = 0,196/(5,23×1,01) … 0,204/(5,23×0,99) = **37,10–39,40 mA**.
- R7 kaybı yaklaşık 8,2 mW altındadır; standart 0805 güç kapasitesine göre düşüktür. PCB'de FB/R7 Kelvin dönüşü gerekir; bu aşamada routing yapılmadı.

L1=22 µH, TI'nin 10–22 µH önerisindedir. Hesap örneği: LED 39,4 mA, VOUT=27,404 V; R18 ve bölücü akımları dahil POUT yaklaşık 1,106 W. **Varsayılan** VIN=4,2 V, verim=%75, Lmin=17,6 µH, fsmin=1 MHz için IIN≈0,351 A; ideal boost ripple≈0,202 App ve tepe≈0,452 A. Bunlar ölçülmüş verim/gerilim değildir; kayıplar ve sıcaklıkla doğrulanacak boyutlandırma örneğidir. Normal yükte 1,3 A L1 doyma referansı ve TI minimum 0,96 A switch limiti altında kalır. L1'in eski/tedarik dışı MPN'si ve arıza durumundaki doyma davranışı ayrıca yeterlilik bekler; doğrudan eşdeğer MPN uydurulmadı.

D1 SS16 60 V/1 A, normal 27,4 V çıkış için makul gerilim/akım payı sağlar. D3 SS14 ters besleme bloklaması korundu. F2 0,75 A hold/6 V, örnek nominal giriş akımının üstündedir; sıcaklık derating'i ve açma süresi garanti edilmedi. R12=0 Ω boost izolasyon noktası korundu. Haricî 5 V, host +5 V'a bağlanmaz.

C1=10 µF/16 V + C2=100 nF giriş; C3=10 µF/50 V + C4=100 nF/50 V çıkış; C9=220 nF COMP korundu. TI giriş için en az 1 µF, çıkış için 1–10 µF aralığı ve tipik 220 nF COMP gösterir. **C3'ün tam MPN'si/DC bias eğrisi yoktur:** 27–30 V'ta hedef etkin ≥4,7 µF koşulu satın almada kanıtlanmalıdır. Etiketteki 10 µF'nin çalışma geriliminde aynen kaldığı varsayılmadı.

R18=33 kΩ, 27,4 V'ta yaklaşık 22,8 mW ve 0,83 mA tüketir. Boşalma yolu sağlar; anında dokunma güvenliği veya hızlı deşarj garantisi değildir. U1 DBV pin sırası TI ile eşleşir: 1 VIN, 2 CTRL, 3 SW, 4 GND, 5 COMP, 6 FB. SOT-23-6 pad konumları KiCad standart footprint'iyle eşleşir.

### OVP ve PWM sınırları

R19/R20=221 kΩ/10 kΩ ±%0,1, nominal 1,242 V referansla **28,690 V** eşik oluşturur. Bu nominal hesap tolerans/offset/histerezis, sıcaklık, referans başlangıcı ve gecikmeleri içermez. Kesin minimum/maksimum eşik veya “<30 V garanti” verilmez.

U2 open-drain OUT, R13=2,2 kΩ üzerinden gelen 3,3 V PWM'i LOW'a çekebilir; 5 V pull-up eklenmedi. R6=100 kΩ varsayılan kapalı durumu korur. TI TPS61165 PWM aralığı 5–100 kHz'dir; önceki 20 kHz hedefi bu aralıktadır. CTRL'nin 180 µs filtresi ve >2,5 ms LOW ile tam shutdown davranışı nedeniyle karşılaştırıcı çıkışı doğrudan hızlı güç kesicisi değildir. Panel sökülmesi/açık yükte yükselme ve hiccup ölçülmelidir. U1'in yaklaşık 38 V iç açık-LED koruması panel için yeterli bir voltaj sınırı olarak kabul edilmez.

Rev J, U2 ve C13'ü BL_POWER'a taşır; ek devre kurmadan host-besleme bağımlılığı kaldırılır. Buna rağmen U2 için birincil TI belge kontrolü ve iki beslemenin tüm açılış/kapanış sıralarında PWM/OVP ölçümü yapılmadan koruma kabulü verilmez. PWM, güç geçişleri boyunca LOW tutulmalıdır; sabit ve doğrulanmamış bir bekleme süresi üretici gereği gibi sunulmaz.

## 5. Logic, touch ve yardımcı komponentler

| Komponentler | Değerlendirme / karar |
|---|---|
| R4, C5, C6 | LCD 3,3 V giriş izolasyonu ve 4,7 µF + 100 nF decoupling korundu. LCD VCI 3,0–3,6 V aralığıyla uyumlu nominal besleme. Akım/başlangıç düşümü ölçülecek. |
| R5, C7, C8 | Ayrı host touch girişinden TP_VDD; 1 µF + 100 nF korundu. PDF s.9 nominal 3,3 V, mekanik çizim 2,8–3,3 V der; maksimum tolerans belirsizdir. Veri olmadan regülatör eklenmedi. |
| R3, R14; R15, R17 | Bağımsız touch/LCD reset: 100 Ω seri + 10 kΩ pull-up korundu. LOW durumda yaklaşık 0,033 V seri direnç düşümü oluşur. Darbe süreleri/başlatma koşulları üretici verisi bekler. |
| R16 | TE hattı 0 Ω bağlantısı korundu; yeni yük veya sonlandırma eklenmedi. |
| R1, R2 | I²C 4,7 kΩ opsiyonları DNP kaldı. Host pull-up varlığı ve toplam bus kapasitesi ölçülmeden takılmamalı. Host R140/R142/R36 popülasyonu bu oturumda doğrulanmış sayılmaz. |
| C13, U2 | Boost ile birlikte besleme ECO'su; açık OVP doğrulama koşulları yukarıdadır. |
| J1, J2, J3, J5 | Pin kontrolleri ve doğrulama sınırları bölüm 3'te. Bağımsız kablolu kullanım korunur; socket/FFC ön-arka görünüşleri karıştırılmamalı. |
| J4, F2, D3, R12 | Ayrı regüle 5 V girişi, ters blok ve servis izolasyonu korundu. |
| U1, L1, D1, C1–C4, C9, R7, R18–R20, R6, R13 | Hesap/driver değerlendirmesi bölüm 4'te; değer değişikliği gerekmedi. |
| TP1/3/4/5/6/9/10/11/12/13/14/15 | 12 mevcut test noktası korundu. DSI üzerine test stub'u eklenmedi. TP14 LEDK'dır; GND test noktası gibi kullanılmamalı. |

LCD ve touch akımları panel PDF'inde **TBD** olduğundan host regülatörü, FPC kontakları ve besleme izolasyon dirençleri için toplam yük kapasitesi sayısal olarak kapatılamadı. R4/R5 test sırasında ayrılabilir; beslemesiz panele I²C/reset/TE sürerek back-power oluşturulmamalı. Host gücü kapalıyken logic hatları aktif tutulmamalı; bağımsız 5 V, yalnızca boost bölümünü besler.

ILI2130 I²C adresi, maksimum sink akımı, interrupt çıkış tipi, reset ve başlatma ayrıntıları verilmemiştir. Orijinal Discovery BSP'sindeki FT6x06/FT6206 dokunmatik desteği ILI2130 için doğrulama değildir. Bu fark yalnızca arayüz değerlendirmesi olarak kaydedildi; firmware yazılmadı.

## 6. Güç sembolleri, ERC ve görsel kalite

52 güç global portu, KiCad standart ok/GND grafikleriyle değiştirildi. GND standart `power:GND`'dir. Farklı güç netleri için aynı `+3V3` veya `+5V` global sembolü kullanmak devreleri birleştireceğinden özel, sabit net isimli `Adapter_F469_Power` sembolleri oluşturuldu. Net isimleri değiştirilmedi. `BL_LEDK`, `BL_SW`, COMP ve sense sinyalleri güç/GND sembolü yapılmadı.

Eksik gerçek besleme bildirimleri PWR_FLAG ile tamamlandı. Flag'ler yalnızca haricî girişler/pasif elemanlardan sonra oluşan besleme düğümlerini ERC'ye tanımlar; fiziksel komponent veya yeni besleme kaynağı değildir. IC pin tipleri pasife çevrilmedi. Kütüphaneler projeye göreceli tanımlıdır; standart GND/PWR_FLAG kullanılan kopyaları paketlendi.

Kaynak ERC: **6 error + 126 warning** (güç sürücüsü ve ızgara). Rev J ERC: **0 error + 3 warning**. Kalanlar `BL_COMP`, `BL_SW`, `OVP_SENSE` isimli tekil global etiketlerdir. İsimlerini ve net bağlantı kimliğini korumak için bırakılmıştır. Bu etiketler sayfa içinde anlamlı düğüm adlarıdır; birer açık elektriksel bağlantı değildir. Denetim kaynak projede ignore iken warning seviyesine yükseltildi. Footprint-filter ve dört yönlü junction denetimleri de warning yapıldı. Yeni ignore veya ERC exclusion yoktur; orijinal/son JSON raporları paket içindedir.

Üç A3 sayfanın genel fonksiyonel yerleşimi korundu. Bağlantı ızgarası 50 mil, döndürülmüş güç sembollerinin yazıları yatay ve tutarlı, güç bildirimleri ayrık ve okunabilir tutuldu. PDF doğrudan düzenlenen native dosyalardan üretildi ve üç sayfa görsel olarak incelendi.

## 7. PCB uyumluluğu ve açılabilirlik

Yüklenen PCB'de 49 devre footprint'i + 4 montaj deliği, sıfır track/via/zone bulunur. Depodaki önceki route edilmiş Rev I PCB'de 53 footprint, 517 iz segmenti + 110 via, 8 zone bulunur. Her iki dosya yalnızca okundu.

İki PCB ile de pin-net karşılaştırması **yalnızca U2.6 ve C13.1 için eski HOST_3V3 → yeni BL_POWER farkını** gösterir. J2'nin footprint kimliği/değeri güncellenmelidir; elektriksel pad geometrisi aynıdır. PCB ECO yapılmadan eski dosyalar Rev J ile eşleşmez. Bu aşamada yerleşim, iz, via, bakır dolgu ve Gerber değiştirilmedi/üretilmedi.

Native projenin üç sayfası KiCad CLI 9.0.2 ile yüklenerek XML netlist ve PDF üretildi; ERC çalıştı. 49 sembolün pin numaraları yerel footprint pad numaralarıyla eşleşir; eksik footprint yoktur. Bu kontrol gerçek komponent gövdesinin, flex yüzünün veya üretici toleranslarının fiziksel kabulü değildir. GUI üzerinden etkileşimli açma testi yapılmadı; native parser/export/ERC ile dosya açılabilirliği doğrulandı. Özgün ZIP üyelerinin SHA-256 karşılaştırması değişiklik göstermedi.

## 8. Üretim öncesi kapatılacak konular

1. **U2:** Tam TI SBOS300 dokümanından exact B/DBV parçasının besleme/OUT/power-off limitleri, referans başlangıcı ve toleransları. OVP açılış, açık yük ve yeniden yükleme tepe gerilimleri; panelin gerçek mutlak LED limiti.
2. **Panel verisi:** LCD/touch tepe ve sürekli akımı, touch 3,3 V toleransı, RESX ve ILI2130 reset/INT/I²C ayrıntıları. S.9–11 iç TCON/BIST çizimleri, haricî RESX darbe süresi yerine kullanılmamalı.
3. **FPC ve host:** Exact host board revizyonu, CN2 fiziksel pin sırası, R117/R119 ve pull-up popülasyonu; 1:1 kablo sürekliliği; J2 sipariş eki, kontak yüzü, flex kalınlığı/şekli ve pin 1.
4. **Tedarik:** C3 etkin kapasite eğrisi; L1 mevcut stok veya yeterliliği tamamlanmış alternatif; generic BOM kalemlerinin tam MPN/rating seçimi.
5. **Laboratuvar:** Güç kapalı süreklilik; PWM LOW ile rail ölçümleri; dummy LED yüküyle akım ve OVP deneyleri; sonra panel ile kontrollü güç verme, host akım/ısı ve I²C yükselme süresi ölçümü. Ölçümler bu ortamda yapılmadı.

Bu maddeler kapanmadan üretime hazır/çalışması kesin ifadesi kullanılmaz. Ek devre ekleyerek doküman eksikleri varsayımla kapatılmadı; mevcut sade prototip mimarisi korunarak incelenebilir Rev J teslim edildi.
