# silab_wifi — PCB Bağlantı Kurtarma ve Donanım İncelemesi
23 Ekim 2026 · KiCad 9.0.2 · R1 · **Bağlantı kurtarma doğrulandı; üretim / RF kabulü verilmedi.**

## 1. Sonuç ve güven sınırı
Kaynak şematik 229 baytlık boş bir KiCad dosyasıdır. PCB üzerinden 20 komponent, 126 numaralı ped ve 20 adlandırılmış net çıkarıldı. Yeniden kurulan beş sayfalık şematiğin tüm 126 ped üyeliği kaynakla eşleşir; 88 adlandırılmış üyelik ve 38 netsiz ped ayrı korunur. Kaynak PCB dosyası byte düzeyinde değiştirilmedi. Kaynak `REF**0`, yalnızca yeni şematikte U2 olarak adlandırıldı.

**Bu sonuç elektriksel işlev onayı değildir.** 453-00221R tam üretici/varyant kimliği ve SiT1532 pin işlevleri resmi datasheet ile bağımsız doğrulanamadı. Üretici siteleri çalışma ortamında proxy 403 verdi. Gerekli alan adları ortam taslağına eklendi; bu kayıt canlı erişimi kendiliğinden açmaz. Bilinmeyen pin işlevleri tahminle adlandırılmadı; PADn ve pasif elektrik tipiyle açıkça işaretlendi. Özellikle modül güç, RF, reset/boot ve IO gerilim uyumu henüz teyit bekler.

| Kontrol | Sonuç | Yorum |
|---|---:|---|
| Komponent / değer / footprint eşleşmesi | 20 / 20 | Footprint geometrileri yerel kütüphaneye aktarıldı. |
| Numaralı ped–net kimliği | 126 / 126 | Tekil unconnected netler kaynak boş nete normalize edildi. |
| Native şematik–PCB parity | 0 fark | Yalnız metadata hizalanmış inceleme kopyasında; bakır değişmedi. |
| Kaynak PCB DRC | 26 hata + 12 uyarı | 0 atanmış-net açık bağlantısı; 38 netsiz ped ayrı incelendi. |
| Yeniden dolumlu kopya DRC | 38 bulgu | Dolgu yenilemesi bulgu sayısını değiştirmedi. |
| Şematik ERC | 37 açık-pin hatası | U2:36 + C3:1. Gizlenmedi; bilinmeyenler NC yapılmadı. |
| Üretici pinout / RF / fiziksel test | Tamamlanmadı | Erişim ve kesin modül dokümanı gerekiyor. |

## 2. Dosyalar ve izlenebilirlik
- `Project/Recovered_Wifi.kicad_pro`: düzenlenebilir beş sayfalık proje.
- `Recovered_Schematic.pdf`: şematik PDF.
- `Original/`: kaynak PCB, boş şematik ve kaynak kurallarının aynısı.
- `Verification/`: ham DRC/ERC, native netlist, 126 satırlık ped karşılaştırması, sayısal geometri ve fiziksel kopya denetimleri.
- `Engineering/`: BOM, bulgular ve yeniden üretme betikleri.
- `References/SOURCE_STATUS.json`: okunan ve okunamayan kaynakların dürüst kaydı.

`Project/Recovered_Wifi.kicad_pcb` bir **inceleme eşlik kopyasıdır**, yeniden tasarlanmış/üretime hazırlanmış PCB değildir. Yalnız U2 referansı, yerel footprint kütüphane öneki, şematik UUID yolları ve önceden netsiz pedlere tekil unconnected net adları eklenmiştir. Hiçbir adlandırılmış net birleştirilmedi; iz/via/ped bakır koordinat ve boyut imzaları aynı kaldı. Kaynak `Original/silab_wifi.kicad_pcb` değişmedi.

## 3. Fiziksel yapı ve envanter
Kart Edge.Cuts **merkez çizgilerine göre 34,00 × 34,00 mm**, 1,6 mm nominal kalınlık ve iki bakır katmandır. 34,12 × 34,12 mm değeri çizgi kalınlığını içeren görüntü sınır kutusudur; üretim boyutu olarak kullanılmadı. Dört düz kenar vardır; ayrı montaj deliği footprinti yoktur. 235 iz parçası ve 230 through-via bulunur. Via boyutları 220 adet 0,6/0,3 mm ve 10 adet 0,508/0,254 mm (çap/delik). 209 via GND netindedir.

F.Cu GND dolgu alanı yaklaşık 701,75 mm²; B.Cu 810,91 mm². Her katmanda 9 geometrik dolgu bölgesi vardır. Bunlar otomatik olarak 9 yüzen ada demek değildir; aralarında via/iz bağlantıları olabilir. Her iki dolgunun clearance değeri 0,33 mm, minimum dolgu kalınlığı 0,3175 mm. Rule-area / anten keepout kaydı yoktur. 20 footprintte de courtyard ve 3D model bulunmadı.

![PCB işlevsel yolları](Views/PCB_Annotated.png)

| Ref | PCB değeri | Görev / durum |
|---|---|---|
| C1 | 10nF | Net_553–GND, 10nF |
| C193 | 1uF /50V | Untitled–GND besleme grubu kondansatörü |
| C200 | 18pF /50V | Untitled–GND besleme grubu kondansatörü |
| C201 | 1uF /50V | Untitled–GND besleme grubu kondansatörü |
| C202 | 100nF/50V | Untitled–GND besleme grubu kondansatörü |
| C3 | 1nF | POC_IN kondansatörü; 2. ped açık |
| C67 | 1uF /50V | Net_14–GND, 1uF |
| C79 | 1uF /50V | Untitled–GND besleme grubu kondansatörü |
| C80 | 1uF /50V | Untitled–GND besleme grubu kondansatörü |
| G1 | SIT1532AI-J4-DCC-32.768D | 32,768 kHz adlı MEMS osilatör; pinout bekler |
| J2 | FTSH-107-01-L-D-RA | 14 pinli host arayüzü; altta, sağ açılı |
| L11 | IND_0805_N | Seri besleme elemanı; gerçek değer/MPN bilinmiyor |
| R207 | 0R | U2.1 için 0R GND bağlantısı; işlev teyidi yok |
| R211 | 100k | Net_553 için Untitled railine 100k bağlantı |
| R213 | 33R | G1.2 ile U2.29 arasında 33R |
| R3 | 100k | WIFI_PWR_EN için 100k GND pull-down |
| R4 | 10k | POC_IN ile U2.32 arasında 10k |
| R53 | 0R | U2.61 için 0R GND bağlantısı; işlev teyidi yok |
| REF**0 | 453-00221R | U2 olarak kurtarılan 71 pedli modül; üretici pinout teyidi bekler |
| U1 | MAX40200AUK+T | Enable kontrollü ideal diyot; regülatör değildir |

## 4. Fonksiyonel mimari
### 4.1 Güç ve enable
J2.1 `LT8609_REG_3V3` → U1.1 VDD; U1.5 OUT → `Net_548` → L11 → `Untitled`. Bu isim, taşıyıcı kart üzerinde LT8609 bulunduğunu göstermez: kartta böyle bir regülatör yoktur. 3,3 V adı hosttan gelen hattın CAD etiketidir; gerçek gerilim ölçülmedi. U1 MAX40200AUK pin tablosu, kurulu KiCad kütüphanesinden 1=VDD, 2=GND, 3=EN, 4=NC, 5=OUT olarak kontrol edildi; doğrudan üretici PDF incelemesi tamamlanmadı. J2.12 EN hattını getirir; R3 100k ile varsayılan kapalı duruma yardımcı olur.

`Untitled`, L11.2, U2.26/34/50/52, G1.3, R211.1 ve altı kondansatörün ortak netidir. `Net_14` yalnız U2.36/54 ve C67.1 ile bağlıdır. Bu ikinci railin bir modül regülatör çıkışı mı, giriş mi veya özel domain mi olduğu bilinmeden gerilim adı verilmedi.

Untitled üzerindeki nominal kapasite 4,100018 µF; Net_14 üzerinde ayrıca 1 µF vardır. DC bias, tolerans, sıcaklık, ESR/ESL ve gerçek MPN bilinmez. C200 18 pF güç railine paraleldir; yalnız değerine bakarak RF matching elemanı diye sınıflandırılamaz.

35 µm bakır ve 20 °C **örnek varsayımıyla**, J2.1–U1 giriş railindeki 19,026 mm / 0,508 mm iz toplamı yaklaşık 18,45 mΩ, U1–L11 arası 2,214 mm / 0,508 mm yaklaşık 2,15 mΩ verir. Untitled dallarının toplu bakır hesabı 73,66 mΩ olsa da bu bir tek seri akım yolu değildir. Via, lehim, konektör, U1, L11 DCR ve GND dönüşü bu hesapta yoktur; akım kapasitesi veya kesin droop sonucu sayılamaz.

Örnek duyarlılık: hostun anlık akımı karşılamadığı varsayılan 200 mA / 10 µs yük adımında ΔV=IΔt/C, yalnız 4,1 µF için yaklaşık 0,49 V verir. **200 mA modül datasheet akımı değildir; bir senaryodur.** Bu değer tasarımın başarısızlığını kanıtlamaz, güç bütünlüğünün ölçülmesi gerektiğini gösterir. Yeni bulk kapasitör eklemek de inrush, host kararlılığı ve L11 rezonansıyla birlikte değerlendirilmelidir.

### 4.2 Host haberleşmesi ve kontrol
| J2 pin | PCB neti | Modül pedi / diğer bağlantı |
|---:|---|---|
| 1 | LT8609_REG_3V3 | U1.1 |
| 2 | GND | U2.2,3,9,11,57,60,62,63,64,65,66,67,68,69,70,71 |
| 3 | WIFI_UART_RX | U2.20 |
| 4 | WIFI_UART_TX | U2.22 |
| 5 | GND | U2.2,3,9,11,57,60,62,63,64,65,66,67,68,69,70,71 |
| 6 | WIFI_UART_CTS | U2.59 |
| 7 | WIFI_UART_RTS | U2.56 |
| 8 | GND | U2.2,3,9,11,57,60,62,63,64,65,66,67,68,69,70,71 |
| 9 | HOST_BYP_ULP_WAKEUP | U2.30 |
| 10 | WIFI_WAKE_FROM_DEV | U2.58 |
| 11 | WIFI_HOST_WAKE_IND | U2.55 |
| 12 | WIFI_PWR_EN | U1.3 + R3.1 |
| 13 | GND | U2.2,3,9,11,57,60,62,63,64,65,66,67,68,69,70,71 |
| 14 | POC_IN | U2.31 |

Bu tablo pad bağlantısını doğrular; UART RX/TX isimlerinin hosta mı modüle mi göre seçildiğini doğrulamaz. Firmware modu, baud, IO domaini, wake zamanlaması ve konektör mating görünümü host/üretici dokümanıyla kontrol edilmelidir. USB/SPI/SDIO adlı ayrı bir carrier arayüz devresi gözlenmedi; bu, modülün bu arayüzleri desteklemediği anlamına gelmez.

| Net | Toplam planar iz (mm) | Via | Genişlikler (mm) |
|---|---:|---:|---|
| HOST_BYP_ULP_WAKEUP | 16.723 | 1 | 0.2032, 0.329933 |
| WIFI_HOST_WAKE_IND | 42.988 | 2 | 0.2032 |
| WIFI_UART_CTS | 45.864 | 3 | 0.1524, 0.2032 |
| WIFI_UART_RTS | 44.501 | 2 | 0.2032 |
| WIFI_UART_RX | 26.535 | 0 | 0.2032 |
| WIFI_UART_TX | 23.042 | 0 | 0.2032 |
| WIFI_WAKE_FROM_DEV | 36.442 | 3 | 0.1524, 0.2032 |

### 4.3 Saat, reset/strap ve POC
G1 pad 2 → Net_193 → R213 (33R) → Net_554 → U2.29. G1 pad 3 Untitled, 1 ve 4 GND. Osilatör parça adında 32.768 kHz belirtilmiştir; üretici pin sırası, çıkış tipi, yük ve besleme aralığı doğrulanmadı. Şematikte bu nedenle PAD1..PAD4 gösterilir.

R211 (100k) Untitled–Net_553; C1 (10nF) Net_553–GND; U2.33 aynı node. Basit nominal RC sabiti 1 ms. Bu topoloji reset/strap benzeri olabilir; modül pin işlevi, eşikler ve dahili pull yapılarını görmeden reset davranışı diye kesinleştirilmedi.

POC_IN, J2.14 → U2.31 ve C3.1 bağlantısıdır. R4 10k, POC_IN ile Net_0/U2.32 arasında. **Net_0 gerçek bir isimdir; boş net değildir.** C3.2 ise gerçekten boştur. Bu yüzden R4/C3 için çalışan 10 µs RC filtresi varsayımı yapılmadı. R207 ve R53, U2.1 ve U2.61 pedlerini 0R üzerinden GND’ye bağlar; datasheet olmadan RF portunu kısa devre ettiği veya doğru strap olduğu söylenemez.

## 5. Elektriksel ve RF inceleme
### 5.1 RF topolojisi ve 50 Ω sınırı
Kaynak dosya, modülün iç RF şemasını ve anten geometrisini içermez. Carrier üzerinde doğrulanmış RF feed, anten konektörü veya kontrollü 50 Ω matching ağı tespit edilmedi. Parça kodu/varyant teyidi olmadan modülün entegre antenli mi, harici antenli mi olduğu kesinleştirilmedi. Bu nedenle herhangi bir dijital hattın 50 Ω olmaması bir RF tasarım hatası diye raporlanmadı.

RF padleri ve anten bölgesi üretici tarafından belirlendikten sonra gereken 50 Ω hat; gerçek dielectric yüksekliği, bitmiş bakır, maske, komşu GND açıklığı ve connector launch ile çözülmelidir. Anten keepout yalnız F.Cu ile sınırlı olmayabilir; B.Cu, komponent, kasa ve ana kart metali de dahil olabilir. Kaynakta keepout rule area yoktur; bu yalnız entegre antenli varyantta koşullu risk olarak değerlendirilir.

Aşağıdaki hesap **yalnız ölçek kontrolü**: izole, sıfır bakır kalınlıklı microstrip, h=1,6 mm ve Er=4,2; coplanar GND, maske ve modül/anten hariç. Bu h/Er kartın doğrulanmış stackup’ı değildir.

| Örnek genişlik (mm) | Model Z0 (Ω) |
|---:|---:|
| 0.1524 | 159.0 |
| 0.2032 | 148.2 |
| 0.3810 | 124.7 |
| 0.5080 | 114.1 |
| 3.1924 | 50.0 |

Modelde 50 Ω genişliği yaklaşık 3.19 mm. Bu sonuç carrier’ın gerçek bir RF hattının yanlış olduğunu kanıtlamaz; çünkü böyle bir hat ve gerçek kesit henüz doğrulanmadı. VNA/TDR, S11, kazanç/etkinlik, çıkış gücü, PER/RSSI ve kasa içi anten performansı fiziksel ölçüm gerektirir.

### 5.2 GND ve dijital dönüş yolları
209 GND via ve çift yüz dolgu, düşük empedanslı bağlantı kurmak için olumlu bir başlangıçtır. Ancak via sayısı tek başına iyi RF/topraklama kanıtı değildir. 0,1 mm aralıklı merkez çizgisi örneklemesinde karşı katman GND kapsaması RX/TX için yaklaşık %84,8/%66,8, CTS/RTS için %47,3/%47,4 ve HOST_WAKE_IND için %24,4 çıktı. Aynı net via/THT geçişlerinin yakınları dışlandı. Bu oranlar bakır örneklemesidir; aynı-katman coplanar dönüşleri, 3B alanları ve devrenin gerçek dönüş akımını kapsamaz. EMI/SI geçme-kalma ölçütü olarak kullanılmamalıdır.

### 5.3 Koruma ve termal davranış
Ayrı TVS, sigorta, ters-polarite giriş devresi veya IO seviye dönüştürücü gözlenmedi. U1 ideal-diyot işlevi, her negatif giriş veya sistem ESD durumunda tam koruma garantisi sayılmaz. Gerçek maksimumlar ve güç sıralaması datasheet ile kontrol edilmeli. Host sinyalleri modül beslemesi kapalıyken sürülürse geri besleme riski değerlendirilmelidir.

U1/L11 termal yükselmesi, modül güç tüketimi ve muhafaza koşulu bilinmeden hesaplanamaz. Genel kontrol P≈I×Vdrop (U1), P≈I²×DCR (L11) üzerinden gerçek veriyle yapılır. Via merkezleri modülün pad sınır kutuları içinde bulunmadı; yalnız yüksek via sayısından via-in-pad lehim emme hatası çıkarılmadı.

## 6. Bulgular ve uygulanabilir düzeltmeler
### K1 — 453-00221R modül kimliği ve pinout teyidi yok

**Sınıf:** Üretime çıkışı engelleyen doğrulama açığı.

**Kanıt:** PCB değer alanı 453-00221R, footprint adı SiLabs,_SL917; 71 numaralı pad var. Tam üretici/varyant dokümanı okunamadı.

**Etki:** Yanlış pin işlevi/voltaj/boot varsayımı, tasarımın çalışmamasına kadar gidebilir; şu an bir pinin kesin yanlış bağlı olduğu iddia edilmiyor.

**Çözüm:** Tam sipariş kodunu ve üretici pin tablosunu doğrula. Özellikle 1/61 GND strapları, 26/34/50/52 ortak rail, 36/54 ortak rail, 29 saat ve 31/32/33 kontrol bağlantılarını üretici şemasıyla karşılaştır.

### K2 — C3.2 açık

**Sınıf:** Doğrulanan eksik bağlantı; işlevsel önem teyit bekliyor.

**Kanıt:** C3.1=POC_IN; C3.2 boş net. Native bağlantı listesinde pad/iz teması yok; GND dolgusunun içinde değil.

**Etki:** C3 şu haliyle tanımlı iki terminalli bir bypass/filtre yolu sağlamaz. Bunun kartın çalışmasını engellediği, amaç bilinmeden söylenemez.

**Çözüm:** Orijinal devre niyetini doğrula. GND dönüşü amaçlanıyorsa ayrı ECO ile bağla; amaçlanmıyorsa DNP veya BOM düzeltmesini açıkça belgele. Bu incelemede bağlantı eklenmedi.

### K3 — 26 fiziksel DRC hatası

**Sınıf:** Doğrulanan tasarım kuralı hatası.

**Kanıt:** 25 clearance + 1 hole_clearance. Mevcut min clearance 0,2032 mm; en kötü ölçülen clearance 0,1107 mm.

**Etki:** Kaynak kurallara göre tasarım temiz değil. Bu, 26 kısa devre veya her üreticide kesin imalat hatası anlamına gelmez.

**Çözüm:** Gerçek imalatçının kurallarını seç; yerleşim/iz/via konumlarını düzelt. Kuralları yalnızca raporu sıfırlamak için düşürme. 0,2377 mm delik–bakır açıklığını 0,25 mm hedefle ayrıca çöz.

### K4 — L11 yalnızca IND_0805_N

**Sınıf:** BOM ve güç doğrulama açığı.

**Kanıt:** Değer ve footprint alanı fiziksel sınıf adı; L/empedans, MPN, DCR, akım, doygunluk tanımsız.

**Etki:** Yanlış eleman seçimi DC düşüm, ısınma veya besleme rezonansı oluşturabilir. Akım kapasitesi hesaplanamaz.

**Çözüm:** Gerçek MPN ve ferrit/indüktör türünü belirle; DC bias, DCR ve akım değerini Wi-Fi yük profiline göre doğrula.

### G1 — Besleme transientleri ve giriş kapasitesi teyit edilmemiş

**Sınıf:** Güvenilirlik / güç bütünlüğü riski.

**Kanıt:** Untitled üzerinde 4×1 µF + 100 nF + 18 pF = 4,100018 µF nominal; U1 giriş railinde yerel kondansatör yok.

**Etki:** Host kablosu ve aç/kapa anahtarlaması sırasında droop/overshoot oluşabilir; gözlenen nominal kapasite tek başına yeterlilik kararı verdirmez.

**Çözüm:** Modül maksimum akım ve inrush şartını öğren; U1 öncesi/sonrası ve modül padlerinde yük adımı ölç. Kapasiteyi host kararlılığı ve L11 ile rezonans dahil değerlendir.

### G2 — Güç kapalıyken GPIO üzerinden geri besleme olasılığı

**Sınıf:** Güvenilirlik / arayüz riski.

**Kanıt:** U1 EN ile besleme kesilebilir; UART/CTS/RTS/wake/POC hatları modüle doğrudan bağlı.

**Etki:** Host hatları HIGH kalırsa koruma yapıları üzerinden kapalı modül raili yükselebilir; gerçek Ioff/absolute max verisi olmadan kesinleşmez.

**Çözüm:** Host pinlerini tri-state etme sırasını ve modül Ioff şartlarını doğrula; gerekirse kapalı güçte izolasyon sağlayan uygun tampon kullan.

### G3 — Kesintisiz referans düzlemi gösterilemedi

**Sınıf:** Güvenilirlik / EMI riski.

**Kanıt:** İki katmanda GND dolgusu var; her birinde 9 geometrik bölge. Seçilmiş sinyal merkez çizgilerinin karşı katman GND örneklemesinde boşluklar var.

**Etki:** Dönüş akımı dolaşabilir ve emisyon/bağışıklık kötüleşebilir; bu örnekleme elektromanyetik kabul testi değildir.

**Çözüm:** Sinyallerin altındaki dönüş yolunu sürekli tut; katman değişimlerine uygun GND dönüş via yerleştir; gerçek kenar hızında ölç.

### G4 — 20 footprintte de courtyard yok; kontrol ignore

**Sınıf:** Montaj / üretilebilirlik riski.

**Kanıt:** Kaynak ayarı missing_courtyard=ignore; yerel kütüphane özgün geometrileri aynen taşır.

**Etki:** DRC montaj gövdesi/servis alanı ve tolerans çakışmalarını bu veriyle yakalayamaz.

**Çözüm:** Üretici mekanik çizimine dayalı courtyard/Fab katmanlarını ekle; J2 sağ açılı gövde ve modül yüksekliklerini kontrol et.

### G5 — 10 tek katmanda bağlı / boşta via uyarısı

**Sınıf:** Doğrulanan uyarılar.

**Kanıt:** Via_dangling: 5 GND + 5 sinyal via; toplam 230 via içinde.

**Etki:** Bazı via yerel olarak amaçlanan katman geçişini veya stitching işlevini yapmıyor olabilir. Her uyarı açık net anlamına gelmez.

**Çözüm:** Her via çevresini doldurulmuş iki katmanda kontrol et; gerçekten gereksizleri ayrı düzeltmede kaldır, gerekli olanları bakıra bağla.

### G6 — Anten/keepout ve RF portu doğrulanamadı

**Sınıf:** Koşullu RF riski.

**Kanıt:** Carrier üzerinde rule-area keepout yok; doğrulanmış 50 Ω RF feed neti veya ayrı anten konnektörü tespit edilmedi. Modül içi RF PCB dosyasında yok.

**Etki:** Entegre antenli varyantta uygunsuz carrier GND/metal anteni bozabilir; harici antenli varyantta farklı koşullar geçerlidir.

**Çözüm:** Tam varyantın anten bölgesini, taşıyıcı keepout ve approved antenna şartlarını üretici dokümanından belirle; kasa/host ile RF ölçümü yap.

### G7 — Bağımsız TVS/sigorta ve sistem ESD hedefi yok

**Sınıf:** Koruma / dış arayüz riski.

**Kanıt:** 20 bileşende tanımlı koruma dizisi/sigorta yok. Modül içi korumalar bu taşıyıcıdan görülemez. MAX40200 ideal diyot olması tam ters-polarite garantisi değildir.

**Etki:** Dış kablo ESD/EFT veya yanlış besleme etkisi sistem koşullarına bağlıdır; mevcut tasarımın ESD testi geçtiği söylenemez.

**Çözüm:** Host/kablo koşuluna göre düşük kapasiteli ESD korumasını ve besleme korumasını seç; U1 giriş limitini ve hedef sistem testlerini doğrula.

### O1 — İz ve katman geçişlerini sadeleştirme

**Sınıf:** İsteğe bağlı optimizasyon.

**Kanıt:** UART RX/TX 26,535/23,042 mm; CTS/RTS 45,864/44,501 mm. CTS 3, RTS 2 via.

**Etki:** Bu uzunluklar tek başına UART hatası değildir; kenar hızı ve dönüş yolu belirleyicidir.

**Çözüm:** Host konnektörü/yerleşim uygunken yolları sadeleştir; gerekiyorsa ölçüme dayalı kaynak sonlandırma değerlendir.

### O2 — Test erişimi ve net adlandırması

**Sınıf:** İsteğe bağlı optimizasyon.

**Kanıt:** Untitled, Net_14, Net_0 vb. gerçek netlerdir; fonksiyonel isim eksik.

**Etki:** Üretim testi ve bakım hata riski artar.

**Çözüm:** Pinout doğrulandıktan sonra anlamlı adlandırma; güç, reset, saat, UART ve EN için kontrollü test noktaları ekle.

### O3 — 4 katman değerlendirmesi

**Sınıf:** İsteğe bağlı optimizasyon.

**Kanıt:** Kaynak 2 katman, 1,6 mm nominal.

**Etki:** Sürekli GND referansı ve güç dağıtımı kolaylaşabilir; maliyet artar.

**Çözüm:** RF/montaj verileri ve gerçek EMI/PI sonucu gerekiyorsa 4 katmanı değerlendir; sırf Wi-Fi olduğu için zorunlu ilan etme.

## 7. DRC / ERC sonuçlarının anlamı
Kaynak PCB kuralları korundu. Min clearance 0,2032 mm; min hole clearance 0,25 mm; min copper-edge clearance 0,06 mm; min_track_width 0 mm ve missing_courtyard ignore. Kontrolleri geçirtmek için kurallar değiştirilmedi. Solder mask ve delik toleransları, seçilmiş imalatçı ve gerçek proses verisi olmadan üretim onayı değildir.

| DRC türü | Adet | Seviye |
|---|---:|---|
| Clearance | 25 | Hata |
| Hole clearance | 1 | Hata |
| Via dangling | 10 | Uyarı |
| Silk edge clearance | 2 | Uyarı |

En dar clearance 0,1107 mm, WIFI_WAKE_FROM_DEV via ile U2.56/RTS pedi arasındadır; delik–bakır açıklığı 0,2377 mm aynı bölgede 0,25 mm kuralının altındadır. J2 alt silk çizgileri kart kenarında kesilir; sağ açılı konektörün gövde taşması elektriksel hata sayılmaz ama mekanik çizim teyidi gerekir. Tam koordinat listesi DRC_Findings.csv ve JSON içindedir.

ERC’deki 37 açık-pin hatası veriyle eşleşir: modülün 36 netsiz pedi ve C3.2. U1.4, KiCad pin tablosunda NC olarak tanımlandığı için yalnız burada NC işareti kullanıldı. Diğer açık padleri kasıtlı NC diye sınıflandıracak veri yoktur. Modül ve G1 bilinmeyen pin tipleri pasif tutulduğundan ERC’nin güç domaini / çıkış çatışması / reset / RF işlevi kontrol kapsamı sınırlıdır. Bu sebeple ERC sonucu bir elektriksel doğruluk sertifikası değildir.

## 8. Güçlü taraflar
- Kaynak adlandırılmış netlerde DRC açık bağlantısı veya raporlanan kısa devre yok.
- Besleme enable hattında 100k GND pull-down var; güç kesme davranışı niyeti açık.
- Ana giriş ve anahtar sonrası kısa güç kesiti 0,508 mm genişlikte.
- Modül çevresinde çok sayıda GND stitching via ve iki yüz dolgu var.
- Tek header üzerinden güç/host akış kontrolü/wake sinyalleri ayrıştırılmış.
- Şematik kurtarması orijinal belirsizlikleri saklamadan tüm 126 ped üyeliğini korur.

## 9. Kapatılması gereken doğrulamalar ve tezgah planı
1. Tam modül MPN/varyant, pin tablosu, referans şema, anten tipi/keepout, güç ve IO limitlerini üreticiden al. SiT1532 ve MAX40200 tam sipariş kodlarını kontrol et; L11 gerçek BOM’unu belirle.
2. Kaynak 1/61 GND straplarını ve 26/34/50/52 ile 36/54 rail birleşmelerini pin tablosuyla kontrol et. C3.2’nin amaçlanan dönüşünü teyit et.
3. Gerilim limitleri doğrulandıktan sonra akım sınırlı ve doğru gerilimli kaynakla host/power-enable sırasını test et; U1 giriş/çıkış, L11 sonrası ve modül güç padlerini yük altında kaydet.
4. Maksimum beklenen Wi-Fi TX/yük senaryosunda droop/overshoot, inrush ve U1/L11 sıcaklığını ölç. 32,768 kHz olduğu doğrulanan çıkışı uygun düşük kapasitanslı probla test et; reset/boot eşiğini ölç.
5. Host IO yönü ve gerilimleri doğrulandığında UART veri/akış kontrolü ve wake/uyku geçişlerini test et. Besleme kapalıyken geri beslemeyi ölç.
6. Tam anten varyantı ve kasa/ana kart geometrisiyle RF performansını ve uygun hedeflerde EMC/ESD davranışını değerlendir; yalnız carrier çiziminden anten kazancı veya 50 Ω kabulü verme.
7. Üretici stackup/DFM, gerçek footprint/courtyard ve komponent rating’leriyle ayrı düzeltme çalışması yap; ERC/DRC’yi tekrar çalıştır.

## 10. Kaynak durumu ve devam için gerekenler
- **S1** — User-uploaded silab_wifi.zip: Read; original board and blank schematic preserved
- **S2** — Native KiCad 9.0.2 PCB API, netlist export, DRC/ERC: Executed; reports bundled
- **S3** — /usr/share/kicad/symbols/Analog_Switch.kicad_sym:MAX40200AUK: Read; confirms 1=VDD, 2=GND, 3=EN, 4=NC, 5=OUT. Secondary curated source, NOT a direct manufacturer datasheet read.
- **S4** — https://www.analog.com/media/en/technical-documentation/data-sheets/MAX40200.pdf: HTTP proxy 403; NOT READ
- **S5** — https://www.sitime.com/datasheet/SiT1532: HTTP proxy 403; NOT READ
- **S6** — https://www.ezurio.com/wireless-modules/wifi-modules-bluetooth/sona-si917: Candidate vendor/product lookup only; HTTP proxy 403. Exact identity of 453-00221R NOT VERIFIED.
- **S7** — https://www.silabs.com/documents/public/data-sheets/siwg917y-datasheet.pdf: Candidate related-family lookup only; HTTP proxy 403. Relevance to exact module NOT VERIFIED.
- **S8** — First-order isolated microstrip equations in Engineering/plots.py: Illustrative computation only; assumptions and JSON results included. Not stackup or RF acceptance.

Üretici siteleri için ortam taslağına `www.ezurio.com`, `ezurio.com`, `www.silabs.com`, `www.analog.com`, `www.sitime.com`, `datasheets.maximintegrated.com` eklendi; paket yöneticisi izinleri korundu. Taslak kaydı canlı ağ erişimi veya yayın anlamına gelmez. Ortam ayarlarında gözden geçirip kaydetmek ve ortamı yayımlamak gerekir. Erişim açılırsa üretici belgeleri okunarak fonksiyonel pin tipleri ve bu rapordaki koşullu RF/güç bulguları tamamlanmalıdır.

**Teslim durumu:** Açılabilir ve tüm pedleri PCB’ye eşleşen şematik, sayısal PCB incelemesi ve açık bulgu listesi hazırdır. Tam datasheet doğrulaması, fiziksel ölçüm ve üretim kabulü açık kalır.
