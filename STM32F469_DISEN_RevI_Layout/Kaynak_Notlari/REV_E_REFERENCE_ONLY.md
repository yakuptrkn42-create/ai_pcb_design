# STM32F469I-DISCO / DISEN DS070HSD39T-132 — Rev E

25 Eylül 2026 — Revize edilmiş, ERC doğrulaması tamamlanmış prototip şematiği.
**Koşulsuz üretim onayı değildir.** Aşağıdaki açık noktalar nedeniyle hedeflenen “üretime hazır ve çalışması doğrulanmış şematik” aşaması henüz tamamlanmış değildir. PCB ön yerleşimine başlanabilir; konektör/flex, güç ve OVP konuları kapanmadan üretim siparişi verilmemelidir.

## Açılacak dosya

KiCad 9 ile STM32F469_DISEN_RevE.kicad_pro dosyasını açın. Ana şematik, Backlight.kicad_sch ve yerel sembol/footprint kütüphaneleri birlikte kullanılmalıdır. İki sayfalı PDF, güncel netlist, BOM, pin listesi, hesaplar ve kontrol raporu pakettedir. Bu paket PCB/routing içermez.

## Rev D'ye göre gerçekten değiştirilenler

| Nokta | Önce → sonra | Teknik neden |
|---|---|---|
| Touch besleme girişi | R5 girişi CN10/J1 3,3 V → CN2/J3 pin 1 | CN10 LCD besleme kontaklarından touch akımını kaldırır. CN2 zaten touch için 3,3 V sağlar. Ana kart regülatörünün toplam yükü değişmez. |
| J3 pin 1 | NC → HOST_TP_3V3 | Touch beslemesi için yukarıdaki fiziksel yol açıldı; ayrı net adı iki kabloyu adaptör üzerinde paralelleştirmeyi önler. |
| R7 | 4,99 Ω ±%1 → 5,23 Ω ±%1 | Nominal 40,08 mA → 38,24 mA. VFB=204 mV ve direnç -%1 köşesinde 39,40 mA. 40 mA panelde tipik değerdir, mutlak maksimum olarak yorumlanmadı; bu değişiklik temkinli ilk çalıştırma hedefidir. Parlaklık bir miktar azalabilir. |
| C1 | 4,7 µF/16 V → 10 µF/16 V X7R | Kablo ve giriş yolu empedansına karşı daha fazla yerel enerji rezervi. 5 V altında etkin C ≥4,7 µF seçilmeli. Giriş akımı darbesi ve kararlılık yine ölçülmeli. |
| R18 | 100 kΩ → 33 kΩ | Çıkışın daha hızlı boşalması. 10 µF için nominal RC 1 s → 0,33 s; 30 V'ta 27,3 mW kayıp. Giriş bağlıysa diyot üzerinden çıkışta girişe yakın gerilim kalabilir. |
| TP11 / TP12 | Eklendi | Filtre/0 Ω sonrasında gerçek LCD_VCI ve TP_VDD ölçümü. |
| TP13 / TP14 / TP15 | Eklendi | LEDA, LEDK ve yakın GND üzerinden akım/gerilim/OVP ölçümü. LEDK GND değildir. |
| OVP açıklaması | “Korur” → koşullu doğrulama notu | 28,69 V statik eşik tek başına 30 V tepe garantisi sağlamaz; CTRL kapatma gecikmesi ve boost enerjisi dikkate alınmalıdır. |

Mevcut DSI yolları, bağımsız resetler, pull-up yapısı ve LEDK bağlantısı zaten doğru olduğundan korunmuştur. Önceki revizyonda yapılmış değişiklikler bu revizyonun yeni işi olarak sunulmamıştır.

## Pin ve devre denetimi

| İncelenen konu | Sonuç / karar |
|---|---|
| CN10 → J1 | 25 kontak / 0,30 mm. Adaptör konektörü kablo üzerinden bire bir pin eşlemesi içindir. H747 CN15 ile uyumlu değildir. |
| CN2 → J3 | 6 kontak / 0,50 mm. 1=3V3, 2=PJ5 INT, 3=PB8 SCL, 4=PB9 SDA, 5=PH7 reset, 6=GND. Pin 5 kasıtlı boş; touch reset ayrıdır. |
| CN12 → J5 | 2×8 / 2,54 mm. Pin 2 GND, pin 6 PC6 PWM, pin 12 PB12 touch reset; diğerleri boş. Mekanik soket yönü fiziksel kartla doğrulanmalı. |
| DISEN J2 | 39 kontak / 0,30 mm; 1–2 LEDA, 3–4 LEDK, 7–10 VCI, 30–31 touch VDD. 5,6,38,39 NC. Tüm GND pinleri bağlandı. |
| CLK P/N | J1 14/12 → J2 24/25; doğru, doğrudan. |
| D0 P/N | J1 10/8 → J2 16/17; doğru, doğrudan. |
| D1 P/N | J1 18/16 → J2 20/21; doğru, doğrudan. |
| DSI seri elemanlar | AC kuplaj, 100 Ω paralel sonlandırma veya rastgele seri direnç eklenmedi. HS ve LP modları birlikte dikkate alınmalı. |
| LCD RESET | PH7/J1.5 → R15 100 Ω → J2.12; R17 10 kΩ LCD_VCI'ye pull-up. PH7 open-drain kullanılmalı. |
| LCD TE | J2.13 → R16 0 Ω → J1.22/PJ2. MCU giriş olmalı; TE kullanılmazsa R16 takılmayabilir. |
| Touch RESET | PB12/J5.12 → R3 100 Ω → J2.34. R14 10 kΩ TP_VDD'ye pull-up. İlk açılışta yazılımla reset uygulanmalı. |
| Touch INT | J2.35 → J3.2/PJ5. Ana kart R36 4,7 kΩ pull-up bulunduğundan ek pull-up yok. |
| I²C | J3.3/4 → J2.32/33. R1/R2 DNP; ana kart pull-up'larıyla toplam direnç ve kablo kapasitansı ölçülmeli. Başlangıç 100 kHz. |
| Logic seviyeleri | LCD VCI 3,0–3,6 V; 3,3 V sistemle nominal uyumlu. Touch VDD ve giriş üst sınırı için aşağıdaki belirsizlik kritik. |
| Güç ayırma | R4/R5 0 Ω ölçüm ve izolasyon için korunmuştur. Sigorta değildir. R5 artık CN2 beslemesine gider. Besleme linkleri açıkken sinyal sürmekten kaçının. |
| Decoupling | LCD 4,7 µF+100 nF, touch 1 µF+100 nF; konektör pinlerine yakın. Boost C1 büyütüldü, 100 nF paraleli korundu. |
| Ferrit | Otomatik eklenmedi. Kaynak empedansı, DC bias ve LC rezonansı ölçülmeden fayda garanti edilemez. R4/R5 yeri uygun boyutlu aday için değerlendirme noktasıdır. |
| Backlight | TPS61165DBVR SOT23-6: 1 VIN, 2 CTRL, 3 SW, 4 GND, 5 COMP, 6 FB. LEDK → FB/R7 üstü; R7 altı GND. |
| PWM | PC6 → R13 2,2 kΩ → CTRL. R6 100 kΩ başlangıçta düşük tutar. U2 open-drain aynı noktayı düşük çekebilir. PWM hedefi 20 kHz. |
| Harici 5 V | J4.1 GND, J4.2 +5 V. F2 PTC, D3 ters kutup/geri akım engelleme, R12 izolasyon. Regüle 5 V ±%5 / en az 0,5 A; F469 ayrı beslenir. |
| Host backlight | J1.23/24 kullanılmaz. J1.3 GND; R117=0 Ω / R119=DNP şartıyla host sürücüsü kapalı. Fiziksel kartta bu konfigürasyon kontrol edilmeli. |
| ESD / koruma | Mevcut giriş koruması korunmuştur. DSI'ye doğrulanmamış kapasitanslı TVS eklenmedi. Harici/erişilebilir konektör kullanımında ESD koruma seçimi ve IEC testi açık iştir; dahili, enerjisiz bağlanan adaptör varsayımı vardır. |
| Power sequencing | Panelin dış RESET süreleri ve init tablosu dokümandan kesin çıkarılamıyor. İç VDDA/VGH/VGL çizimlerini dışarıya ek besleme gereği olarak yorumlamadım. BL kapalı → logic kararlı → reset/init → görüntü → BL sırası yazılımda uygulanmalı. |

## Kritik açık noktalar

1. **Touch gerilim toleransı:** Mekanik çizimde 2,8–3,3 V, elektriksel tabloda yalnızca 3,3 V tipik var. F469 3,3 V regülatörünün pozitif toleransı, ripple ve 3,3 V pull-up'lar için garanti edilmiş izin alınmalı. CN2'ye taşımak bu tolerans sorununu çözmez. 3,3 V kesin üst sınırsa düşük gerilim regülatörüyle birlikte I²C/INT/RESET seviye dönüşümü yeniden tasarlanmalı; yalnızca VDD'yi düşürmek güvenli çözüm değildir.
2. **Akım bütçesi:** LCD ve touch akımları TBD. LCD açılış/tepe/sürekli akımı; CN10 kontakları, FPC izleri ve F469 regülatörü birlikte değerlendirilmelidir. Touch artık CN2'den beslense de aynı regülatöre yük olur. Ölçüm veya üretici akım verisi olmadan yeterli denemez.
3. **OVP:** TPS61165 kendi açık-LED eşiği 37–39 V iken seçili FH26 ailesi 30 V sınıfındadır. U2 eşiği nominal 28,690 V; offset, referans, histerezis ve direnç toleransları marjı küçültür. CTRL düşük tutulduğunda tam kapanış için 2,5 ms parametresi vardır; bu devre hızlı, sert bir gerilim kelepçesi değildir. Başlangıç, açık yük ve PWM geçişleriyle LEDA tepesinin 30 V altında kaldığı kanıtlanmalı. Aşım görülürse hızlı donanımsal kesme/uygun OVP'li sürücü yeniden tasarlanmalıdır. **Bu revizyon bu riski çözülmüş saymaz.**
4. **Panel yazılımı:** OTA7290B/ILI2130 revizyonu, DSI init komutları, lane hızı, porch/timing, reset süreleri ve I²C adresi üreticiden gerekli. F469'un orijinal ekran BSP'si doğrudan kullanılamaz. ST şemasındaki 0x54 adresi DISEN için kanıt değildir.
5. **FPC/konektör:** Panel belgesi FH26-39S önerir, projede FH26W-39S var. Kontak yüzü, kademeli FPC uç geometrisi, 0,20 mm uç kalınlığı ve pin-1 fiziksel çizimle eşleştirilmeli. Sadece pin sayısı/pitch yeterli değildir. 25 pin kabloda CN10.n→J1.n ve 6 pinde CN2.n→J3.n süreklilik doğrulanmalı. Yerel footprint pad numaraları kontrol edildi; boyutsal/mekanik kabul yapılmadı.
6. **BOM/indüktör:** L1=22 µH SLF7045T-220M1R3-H eski projeden korunmuştur; güncel tedarik ömrü ve onaylı muadil gerekli. Yaklaşık normal akım yeterliliği, 1,44 A'a çıkabilen sürücü akım limiti sırasında doyma/termal davranış garantisi değildir. C3'ün 30 V'ta etkin kapasitesi ve pasiflerin üretici kodları dondurulmalı.

## PCB'ye geçerken

- Başlangıç önerisi 4 katman: üstte bileşen/sinyal, hemen altında kesintisiz GND, üçüncü katmanda güç/yavaş sinyal, altta sinyal/GND. Kesin kalınlıkları üretici stack-up'ına göre seçin.
- DSI için kablo dahil 100 Ω diferansiyel hedef. Yol genişliği/aralığı sabit ezber değerle verilmez. P/N simetrik, kısa, minimum via; GND kesintisi ve test point stub'ı yok.
- Eşleme limitini lane hızı ve panel/MCU D-PHY zaman bütçesi belirler. Sırf tüm hatlar eşit olsun diye gereksiz serpantin eklemeyin.
- Boost SW düğümünü küçük tutun. U1–D1–C3 dönüş döngüsü kısa olsun; U1 giriş bypass ve COMP kapasitörü yakın yerleşsin.
- R7 altını U1 GND'ye Kelvin düşüncesiyle bağlayın. FB hattı SW'den uzak, LEDK güç yolunun düşümü ölçümü bozmayacak şekilde bağlanmalı.
- Analog/dijital toprağı yararak DSI dönüş yolunu bozmayın. Boost yüksek akımını panel/MCU sinyal dönüş yolundan uzak yerleştirin.
- TP13 LEDA ve TP14 LEDK birbirinden ve GND'den prob kısa devresi olmayacak mesafede olsun.
- Konektör kilidinin açılma alanını ve FPC kıvrılma yarıçapını mekanik tasarımla kontrol edin.

## İlk çalıştırma

1. Tüm güçler kapalıyken FPC yönü/süreklilik, polarite ve kısa devre kontrolü.
2. Harici BL beslemesi kapalıyken HOST_3V3, LCD_VCI, TP_VDD ölçümü. TP11/12 kullanın. PWM düşük.
3. PH7 open-drain ve PB12 reset sırasını tedarikçi verilerine göre uygulayın; güç verilmeyen panele sinyal sürmeyin.
4. Panel yerine uygun dummy LED yüküyle akım sınırlı 5 V kaynaktan boost testi; LED akımı = TP14/R7. Açık yükte TP13 tepesini osiloskopla kontrol edin.
5. OVP onaylandıktan sonra panelle görüntü ve touch init testi. U2 beslemesi kararlı olduktan en az 10 ms sonra BL izni; PWM/EasyScale seçim zamanlaması TI belgesine göre.
6. Kapatırken BL önce kapalı; tekrar açma/kapatma, sıcaklık, kablo ve dokunma testleri. Enerjili FPC söküp takmayın.

## Yapılan doğrulama

KiCad 9.0.9 ERC: **0 hata / 0 uyarı**, yeni istisna yok.
Rev D ve Rev E netlistleri yeniden dışa aktarılarak karşılaştırıldı; mevcut pinlerde yalnızca J3.1 ve R5.1 neti değişti. Beş yeni test point eklendi. 172 pin/net kaydı üzerinden kritik eşlemeler ve yerel footprint pad varlığı kontrol edildi; 111 kontrol geçti.
PDF'nin iki sayfası görsel olarak incelendi.
Donanım ölçümü, transient simülasyonu, PCB DRC/empedans ve EMC testi yapılmadı.
