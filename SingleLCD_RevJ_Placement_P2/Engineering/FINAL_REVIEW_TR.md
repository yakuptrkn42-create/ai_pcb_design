# Son mühendislik incelemesi — Rev J / Placement P2

20 Ekim 2026 · Yalnızca ilk LCD: DISEN DS070HSD39T-132. Çift LCD Rev K ve önceki teslimler değiştirilmedi.

## Kaynak ve kapsam

Bu revizyon, kullanıcının yeni Project.zip dosyasını esas alır. Önceki P1 kartı yeniden teslim edilmedi. Yeni kaynakta J4 üç pinli kontrol header'ına, J6 iki pinli JST NV girişine dönüştürülmüş, Ø3,5 mm montaj delikleri şematiğe eklenmiş ve PCB 55 × 45 mm yapılmıştı. Bu tercihler korundu. Önceki sürümdeki 57 net/172 pin yerine kaynakta 44 net/159 pin bulunması, kullanıcının 16 pinli CN12 soketini üç kablolu arayüze çevirmesinden kaynaklanır; P2 bu bağlantıları değiştirmedi.

Kaynak DRC: 3 bulgu (kenara taşan J6 silk'i, J6 kütüphane geometrisi farkı ve L1/R7 silk yakınlığı), parity 0, bağlantısız öğe 115. Ayrıca sınıra göre ayrı mekanik denetim, dokuz test noktası ile J6 courtyard'unun kart dışında kaldığını buldu. Eski alt yüz yazıları da yeni outline dışında kalmıştı. Bu durumlar yalnızca varsayılan DRC'ye güvenilerek görünmeyebilirdi.

## Doğrudan uygulanan değişiklikler

| Konu | Kaynak | P2 sonucu |
|---|---|---|
| J6 güç açıklaması | 1=GND, 2=+5V yazıyor; gerçek netler tersiydi | Netlere dokunulmadı; değer ve şematik not 1=+5V, 2=GND oldu. PCB +/− işaretleri eklendi. |
| J4 kontrol adı | Üç pin olmasına rağmen “CN12 1:1 / 2x08 socket” | 1=PC6 PWM (CN12.6), 2=PB12 TP_RST (CN12.12), 3=GND (CN12.2). |
| Taşınabilirlik | Yeni J4/J6 modelleri sistem klasörüne bağlı; Connector/Mechanical sembol kütüphaneleri proje tablosunda yok | Üç yerel arayüz/montaj sembolü, iki yerel konnektör footprint'i ve iki yerel model eklendi. Sembol pin numarası/tipi değişmedi. |
| J6 footprint | Yerel olarak düzenlenmiş stock gövde çizgileri kütüphaneyle uyuşmuyordu | KiCad stock çizgileri yerel kopyayla eşlendi; pad ölçüsü, delik ve pin–net üyeliği korunuyor. |
| Mekanik | Dört Ø3,5 delik | Delikler korundu; yerel footprint'e Ø8 donanım courtyard'u eklendi. |
| Yerleşim | DSI konnektörleri dik açılı, bazı test noktaları dışarıda | İki DSI FPC üst kenarda, host touch sağ kenarda; bütün courtyard'lar kart içinde. |
| Güç katı | Uzun SW/FB ve çıkış kondansatörü dönüş mesafeleri | L1/U1/D1/C3/C4 yakınlaştırıldı; C2, R7, C9 ve C13 görevlerine göre yerleştirildi. |
| Açıklamalar | Eski kart ölçüsü/revizyon yazıları dışarıda | Üst/alt silk, referanslar, nominal FPC servis alanları ve routing koridoru yenilendi. |

R/C/L değerleri, aktif komponentler, güç netleri, bütün elektriksel pin eşleşmeleri, DNP R1/R2, devre mimarisi ve üç sayfanın fonksiyonel düzeni değişmedi. Şematikte yalnızca hatalı metinler, başlık ve yerel kütüphane metadata'sı değişti. Delik düzenleme sırasında 3,5 mm yapılmış genel pad varsayılanı önceki standart 0,8 mm delik / 2,54 × 1,27 mm boyuta geri alındı; mevcut pad'leri değiştirmez. Net class, routing limitleri ve hata seviyeleri korunmuştur.

## Elektriksel inceleme ve kanıt

| Blok | Kontrol edilen bağlantı/karar | Belge / sınır |
|---|---|---|
| DSI iki veri lane'i + clock | J1.10/8 → J2.16/17 D0; J1.18/16 → J2.20/21 D1; J1.14/12 → J2.24/25 CLK. Polarite aynı, doğrudan DC bağlantı. | DISEN A0 s.7 ve ST UM1932 Rev5 tablo 7 s.21. Haricî 100 Ω terminasyon veya AC kondansatörü eklenmedi. |
| LCD güç/reset/TE | J2.7–10 LCD_VCI; .12 reset; .13 TE; .30/.31 TP_VDD; .32/.33 I²C; .34/.35 touch reset/INT. | DISEN A0 s.7–10 ve touch çizimi. LCD VCI 3,0–3,6 V; touch 3,3 V nominal, üst tolerans/yük bütçesi açık. |
| Host kontrol | PH7 LCD reset, PJ2 TE; J4.1 CN12.6 PC6 PWM, J4.2 CN12.12 PB12 bağımsız touch reset, J4.3 CN12.2 GND. | UM1932 Rev5 tablo 6 s.19, DSI bölüm 4.14. J3 host CN2 girişidir, panelin ayrı touch kuyruğu değildir. CN2 fiziksel sıra teyidi açık. |
| TPS61165 | DBV: 1 VIN / 2 CTRL / 3 SW / 4 GND / 5 COMP / 6 FB. R7=5,23 Ω %1; LEDK, FB/R7 düğümüdür ve GND değildir. | TI SLVS790E pin fonksiyonları ve VFB sınırları: 196/200/204 mV. Nominal 38,24 mA; direnç/VFB toleransı ile 37,10–39,40 mA. |
| Boost elemanları | 22 µH, SS16 60 V/1 A, C1/C2 giriş ve C3/C4 50 V çıkış; C9 220 nF COMP. C3 etkin kapasite ≥4,7 µF koşulu korunur. | TI SLVS790E §9 ve §11.1 s.21: kısa SW alanı, küçük anahtar–diyot–çıkış kapasitörü döngüsü, VIN/GND yakın bypass. Exact kapasitör/indüktör MPN yeterliliği açık. |
| Besleme | J6.1 → F2 → D3 → R12 → BL_POWER; J6.2 ortak GND. Host +5 V ile birleşmez. U1 ve U2/C13 aynı BL_POWER alanında. | Source netlist ve native pad numaraları birebir kontrol edildi. PTC 0,75 A hold; SS14 reverse block. |
| PWM/OVP | PC6 → 2,2 kΩ R13 → CTRL; R6=100 kΩ default LOW. U2 open-drain CTRL'yi LOW yapar. 221 kΩ / 10 kΩ ile nominal 28,69 V. | OVP eşik hesabı hızlı/garantili klemp değildir; TI CTRL filtresi ~180 µs, tam shutdown LOW >2,5 ms. 20 kHz PWM çalışma hedefi uygundur. TLV3011B tam birincil belge/transient yeterliliği açık. |
| Touch | SCL PB8, SDA PB9, INT PJ5; PB12 reset. R1/R2=4,7 kΩ DNP; R3/R15 100 Ω; R14/R17 10 kΩ pull-up. | Resmî ST BSP işlevleri ve source pin–net kontrolü; gerçek host pull-up popülasyonu, ILI2130 adres/reset/INT süreleri teyit edilmelidir. |

Nominal güç hesabı önceki incelemeden korunur: VIN=4,2 V, verim=%75, Lmin=17,6 µH, fsmin=1 MHz, LED Vfmax=27,2 V, IFmax≈39,4 mA varsayımıyla çıkış yaklaşık 1,106 W, ortalama giriş 0,351 A ve tepe akım 0,452 A. Bunlar ölçüm veya arıza akımı kabulü değildir. Panelin iki paralel LED kolu nedeniyle modül akımı 80 mA yapılmadı.

## Yerleşim seçenekleri

Bütün seçeneklerde kart hedefi 55 × 45 mm'dir. Yeni JST gövdesi, Ø8 montaj donanımı, üst FPC erişimi ve routing alanı nedeniyle küçültme seçilmedi. Büyük boş alanın önemli kısmı planlanan DSI geçiş/tuning alanıdır.

| Seçenek | DSI pin mesafesi min / ort / max | Geçiş / mekanik değerlendirme |
|---|---|---|
| A — kullanıcının dik açılı fikri | 22,49 / 24,73 / 26,97 mm | Nominal dışa kablo çıkışı için J1 180°, J2 270°; J6 içeri alınarak ve test noktaları yeniden paketlenerek kavramsal courtyard çakışması 0. 4 mm ana koridor, köşe dönüşü. |
| B — ortak kenar, uygulanan | 16,45 / 17,97 / 19,50 mm | 26,5 × 5 mm ana koridor; dışa ayrık iki FPC servis alanı. Bütün kart için native DRC/parity/model kontrolü yapıldı. |
| C — karşılıklı kenarlar | 47,09 / 48,54 / 49,99 mm | Daha escape/tuning eklenmeden 50 mm başlangıç PCB uzunluk bütçesinin hemen tamamını tüketiyor. Konnektör aşamasında elendi; tam komponent yerleşimi kabulü yapılmadı. |

A/B için non-GND/NC Euclidean MST toplamı 635,83/644,42 mm, farklı net düz çizgi kesişme göstergesi 137/84. B, toplam kablo göstergesini en az yapan seçenek değildir; kritik DSI, erişim ve güç döngülerinin dengesi nedeniyle seçildi. Kaynağın değiştirilmemiş DSI ortalama pin mesafesi 22,91 mm idi; B ile yaklaşık %21,6 azaldı. Bütün sayılar kuş uçuşu göstergedir; gerçek routed uzunluk, KiCad ratsnest topolojisi, via sayısı, EMI veya kanal simülasyonu değildir.

Boost çekirdeği için ağırlıklı kritik pad mesafeleri/courtyard ve hot-loop zarfı üzerinde altı deterministik optimizasyon geçişi (132.000 aday hareket), ardından bütün kart/mekanik incelemesi yapıldı. C1'in yeri JST gövdesi ve VIN besleme yaklaşımı için ayrıca düzeltildi. Son seçimin gerçek mesafeleri aşağıdadır.

| Padlar arası mesafe | Kaynak → P2 |
| C2–U1 VIN | 2.32 → 2.07 mm |
| C2–U1 GND | 6.84 → 3.95 mm |
| L1–U1 SW | 7.39 → 2.41 mm |
| D1–U1 SW | 6.76 → 2.72 mm |
| C4+–D1 katot | 7.98 → 4.14 mm |
| C4 GND–U1 GND | 13.65 → 2.59 mm |
| R7–U1 FB | 10.34 → 2.03 mm |
| C9–U1 COMP | 4.24 → 2.13 mm |
| C3+–D1 katot | 5.82 → 2.82 mm |
| C13–U2 VCC | 3.35 → 2.26 mm |

Bu mesafeler routed döngü alanı değildir. Özellikle C2 GND–U1 GND yaklaşık 3,95 mm kaldığından, ileride yakın GND via'ları ve kesintisiz referansla dönüş kısaltılmalı; “ideal bypass tamamlandı” kabulü verilmez. SW terminal üçgeni ana DSI koridorundan en az 7 mm düşey uzaktadır. Bu geometrik ayırım EMC testinin yerini tutmaz. R7 dönüşü Kelvin olarak sessiz GND'ye, COMP ve OVP referansı SW alanından uzak çizilmelidir.

## DSI routing yapılabilirliği

0,14 mm iz ve 0,18 mm iç aralıkla tek çiftin zarfı 0,46 mm'dir. Üç çift, aralarında iki adet 0,50 mm planlama payı ve dışta iki adet 0,50 mm pay ile toplam 3,38 mm eder. 5 mm ana koridor bu başlangıç zarfına 1,62 mm ilave alan bırakır. Bu pay crosstalk veya meander yeterliliği simülasyonu değildir.

Konnektör pad'leri iki sıraya dağılır; aynı sırada 0,60 mm pitch ve 0,30 mm pad genişliği nedeniyle arada yaklaşık 0,30 mm boşluk bulunur. 0,14 mm iz + iki tarafta 0,15 mm clearance = 0,44 mm gerektiği için karşı sıranın pad'leri arasından basit kaçış varsayılamaz. Yanlardan kaçış ve/veya F.Cu–B.Cu geçişi gerekecektir. Host sırası D0–CLK–D1, panel sırası D0–D1–CLK olduğundan lane kesişmesi vardır. Clock/data sırasını değiştiren anahtar veya net takası yapılmadı.

Bir çiftin katman değiştirmesi ve gerekirse geri dönmesi durumunda 4 via/çift; bir–üç çift için yaklaşık 4–12 DSI via yalnızca planlama zarfıdır. Native PCB'de via yoktur. Her iletkende en fazla iki via bütçesi korunur. DSI via geçişlerine yakın GND dönüş via'ları sonraki aşamada planlanmalı; hiç via gerekmeyeceği veya route'un bu sayıyla kesin biteceği iddia edilmez. İç iki GND katmanı, ileride delik/via antipad kümeleriyle bölünmemelidir.

## Mekanik ve 3D doğrulama

53 footprint'in bütün native courtyard'ları kart içinde ve birbirinden en az 0,15 mm ilave aralıkla ayrıdır. Dört montaj deliği merkezleri sol üst datuma göre (5,5), (50,5), (5,40), (50,40) mm'dir; gerçek delik çapı 3,5 mm. Donanım alanı Ø8 mm varsayımıdır; seçilecek vida/pul bu zarfı aşmamalı. Courtyard bir bakır keepout değildir: vida/pul altındaki copper ve zone açıklıkları routing aşamasında ayrıca tanımlanmalıdır.

49 devre referansının modeli yerel `${KIPRJMOD}/3D` yoluna bağlıdır; 13 kullanılan model tipi, eski kütüphanelerin modelleriyle birlikte 16 dosya vardır. J4 official KiCad STEP modeliyle, J6 footprint XY ölçülerinden üretilen nominal STEP ile gösterildi. JST gövde yüksekliği 8,5 mm varsayımdır ve üretici ölçüsü olarak doğrulanmamıştır. J4/J6 düşey takılır; kablo ve sökme erişimi yukarıda bırakılmalıdır. Alt yüzde çıkıntı yapan header uçları nedeniyle montaj yükselticisi/şase aralığı ayrıca seçilmelidir.

STEP bbox ve WRL vertex'lerinden çıkarılan muhafazakâr XY zarflarda 49 referans için çakışma 0. Ölçekler 1:1, offset/dönüş 0; model konumları native PCB dönüşleriyle kontrol edildi. Bu, exact solid collision veya tolerans analizi değildir. FPC modelleri önceki nominal gövdelerdir: temas yüzü/kalınlık, sipariş eki, latch hareketi, kablo bükülmesi ve gerçek pin-1 sürekliliği fiziksel olarak teyit edilmelidir. R1/R2 DNP olmasına rağmen native 3D çıktısında modelleri görünebilir; assembly çiziminde üzerleri çapraz işaretlidir.

## Nihai kontroller

ERC: **0 hata / 3 uyarı** (BL_SW, BL_COMP, OVP_SENSE tekil global label). Fiziksel DRC **0**, şema–PCB parity **0**. Bağlantısız öğe kayıtları **115** ve hata seviyesinde açık; net sayısı olarak yorumlanmamalı. Kurallar gevşetilmedi; exclusion eklenmedi. Aynı netin pinleri, pad/delik ölçüleri, footprint ve symbol UUID/path'leri, DNP ve sembol pinleri ayrı karşılaştırıldı: 44 net / 159 üyelik aynı. Şema sayfalarının wire/junction/net label yapısı ve sembol konumları korunuyor. Native KiCad dosyaları okunup PDF/SVG/3D çıkarıldı; KiCad parser ve proje bağlantıları çalışıyor.

Orijinal ZIP aynen korunur. Portatif yeniden açma/DRC/ERC, model ve hash kontrolleri `Verification/Portable_Check.json` içinde ayrıca kayıtlıdır. Bu dosya ZIP'in ayrı dizine açıldığı son doğrulamanın sonucudur.

## Routing veya enerji vermeden önce açık kalan teknik koşullar

- Üreticinin gerçek stackup'ı, bitmiş bakır kalınlığı, FR4/mask parametreleri, üretim toleransı ve empedans kuponu. Mevcut boyutlar nominaldir.
- Hirose exact sipariş eki/FPC kontak yüzü ve pin-1 kablo sürekliliği; J3 host CN2 fiziksel pin sırası, host R117/R119 ve I²C pull-up popülasyonu. CN12 üç kablosu 6/12/2 pinlerine göre hazırlanmalıdır.
- Panel/touch yük akımları, touch 3,3 V üst toleransı ve ILI2130 ayrıntıları; C3 DC-bias etkisiyle etkin kapasite ve eski L1 için gerçek tedarik/akım yeterliliği.
- TLV3011B birincil belgesiyle besleme/referans açılışı ve beslemesiz OUT koşulları; açık yük/PWM/güç sıralaması sırasında OVP dalga şekilleri. TI ve JST belge erişimleri bu oturumda proxy 403 verdi; bu veriler doğrulanmış kabul edilmedi.
- Routing sonrasında gerçek hat uzunlukları, empedans, dönüş yolları, boost döngüsü, güç düşümü ve bütün DRC yeniden kontrol edilmelidir.

Bu koşullar kapatılmadan üretim/çalışma garantisi verilmez. **0 iz / 0 via / 0 zone; Gerber, drill, copper pour veya yazılım üretilmedi. Routing ayrı onayınızı bekler.**
