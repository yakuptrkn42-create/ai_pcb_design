# STM32F469I-DISCO / DISEN — J-SR1 elektriksel inceleme
22 Ekim 2026 · Geliştirme/prototip adaptörü · Koşullu tasarım incelemesi

## 1. Karar ve yapılan revizyon

İnceleme 22 Ekim 2026 tarihinde yüklenen Project.zip ve DS070HSD39T-132 A0 PDF üzerinde yapıldı. Amaç, seri üretim dışı bir geliştirme adaptörüdür. İki DSI veri lane’i ve bir saat çifti doğrudan geçer; LCD ve touch hosttan 3,3 V, backlight ayrı regüle 5 V ile beslenir. Çalışmayı sağlayacak temel topoloji mevcut; fiziksel lane/polarite değişikliği gerekmiyor.

J-SR1 native şematik revizyonu tamamlandı. Son KiCad ERC 0 hata / 0 uyarı; 39 LCD pini, 25 CN10 pini ve 53 footprint’in pin üyeliği doğrulandı. Donanım çalışması, nihai PCB dondurma veya üretim kabulü verilmez: touch besleme toleransı, eksik panel akım/reset verileri, fiziksel FPC ve OVP transientleri açıktır.

| Düzeltme | Teknik gerekçe |
| --- | --- |
| J6: 1=+5V, 2=GND | Kaynak değeri ters polarite yazıyordu. Backlight sayfasındaki eski J4 güç açıklaması da J6 olarak düzeltildi. Netler zaten bu sıradaydı. |
| J4: üç telli kontrol konnektörü | 2×8 CN12 soketi olarak yanlış adlandırılmıştı. Yerel 1×3 / 2,54mm header atandı: 1→CN12.6 PC6; 2→CN12.12 PB12; 3→CN12.2 GND. |
| R13: 2,2k → 8,2k / %1 | TI SLVS790E §9.2.1.2.4 önerisi: yanlış EasyScale ACK durumunda sink akımı ≤500µA. Yeni üst hesap 443µA @3,6V. |
| C3: X7R niteliği eklendi | 10µF/50V korunur; 30V DC bias altında etkin kapasite ≥1µF şartı BOM’a yazıldı. |
| Yerel kütüphaneler ve etiket kapsamı | Eksik Connector/Mechanical bağımlılıkları yerelleştirildi. BL_SW/BL_COMP/OVP_SENSE sayfa içi local label yapıldı. ERC kuralları değiştirilmedi. |

49 devre elemanı ve dört montaj deliği korundu; yeni devre bloğu eklenmedi. U2/C13 kaynakta zaten BL_POWER üzerindeydi, bu teslimde yeni bir besleme ECO’su yapılmış gibi gösterilmedi. R7, R19/R20, reset RC’leri ve DNP pull-up kararları korundu. Tüm fiziksel pin-net grupları kaynakla aynıdır; üç düğümün net adı sadece hiyerarşik kapsam kazanır.

## 2. DSI, çözünürlük ve FPC bağlantısı

DISEN s.5: 280(H)×1424(V), 16,7M renk, OTA7290B; s.7: iki data lane. ST MB1189-C01 s.7 ve resmî BSP de iki lane’li arayüzü doğrular. ST BSP’nin 500Mbit/s/lane ayarı panel s.14’teki normal ≤550Mbit/s aralığının içindedir. Panelin speedup seçeneğindeki 1000Mbit/s üst değeri, STM32’nin bu hızda çalışacağı anlamına gelmez.

| Sinyal | Host J1 / CN10 | Panel J2 |
| --- | --- | --- |
| D0+ / D0− | 10 / 8 | 16 / 17 |
| D1+ / D1− | 18 / 16 | 20 / 21 |
| CLK+ / CLK− | 14 / 12 | 24 / 25 |
| LCD RESET / TE | 5 (PH7) / 22 (PJ2) | 12 / 13 |
| VCI / touch VDD | Host 3V3 / CN2.1 | 7–10 / 30–31 |

60Hz RGB888 için yalnız aktif görüntü yükü 287,08Mbit/s/lane’dir; blanking ve paket ek yükü dahil değildir. Tek framebuffer 1.196.160 bayttır. Bu bütçe mimari uygunluk gösterir, çalışma timing’ini kanıtlamaz. OTA7290B init komutları, H/V porch/sync, video/command mode ve gerçek frame rate DISEN’den alınmalı; orijinal 800×480 LCD yazılımının doğrudan çalışması beklenmemelidir. Yazılım geliştirilmedi.

MIPI doğrudan DC bağlantıdır: seri sonlandırma veya AC kuplaj eklenmedi. Panel HS/LP alıcısının düşük gerilimleri haricî 3,3V GPIO seviyesi değildir; s.12’deki 1,5V iç alıcı tablosu adaptöre 1,5V güç ekleme gerekçesi değildir. PCB/kablo için 100Ω diferansiyel hedef, kısa ve sürekli GND dönüşü, lane/polarite sürekliliği gerekir; sayısal göz açıklığı veya SI doğrulanmadı.

Kullanıcının yanıtına göre bağlantı FPC kablo ile yapılacak. CN10/J1: 25 pin 0,3mm; panel J2: 39 pin 0,3mm; host CN2/J3: 6 pin 0,5mm. Hirose FH26 ailesi 0,20±0,03mm altın kaplı uç ve katalogdaki uç geometrisini ister. Yalnız “aynı pitch” eşleşmesi yeterli değildir; kontak yüzü, pin1, kablo uzunluğu ve ekranlama henüz bilinmiyor. Adaptör netlist’i 1→1 bağlantı varsayar; fiziksel kablo ölçülmelidir.

J1.23/.24 host LED çıkışları açık bırakıldı. C01’de R117=0Ω, R119=N/A; J1.3’ün GND’ye bağlanması CABC üzerinden host boost’u kapatır. R118 4,7k pull-up nedeniyle yaklaşık 0,70mA akar. R119 takılı farklı kart konfigürasyonunda PA3 çıkışıyla çakışma olabilir; gerçek kart popülasyonu kontrol edilmelidir.

## 3. Besleme, touch ve kontrol sinyalleri

LCD VCI 3,0–3,6V ister. Host C01 U7=LD1117S33TR; ST datasheet ilgili aralıkta 3,235–3,365V verir: LCD VCI ile nominal/rating uyumu vardır. Ancak aynı aralık, panel çizimi s.6’daki touch 2,8–3,3V üst sınırını aşabilir. Touch tablosu s.9 yalnız tipik 3,3V verir; üst tolerans tanımlamaz. Bu, üretici teyidi olmadan kapatılamayan somut bir tolerans uyuşmazlığıdır.

Bu nedenle R5 üzerinden doğrudan host 3V3 beslemesine kesin uyumluluk onayı verilmedi. Paneli enerjilendirmeden DISEN’den VDD maksimum çalışma/mutlak sınırı ve I/O toleransı alınmalı. Daha düşük VDD için tek başına LDO eklemek, host pull-up ve PB12/INT seviyelerinin panele VDD üstünde uygulanmasını çözmez; gerekirse rail ve I/O birlikte revize edilir. Veri olmadan yeni regülatör/seviye çevirici eklenmedi.

| Host CN2 → J3 | İşlev |
| --- | --- |
| 1 | HOST_TP_3V3 |
| 2 | PJ5 / INT; host R36=4,7k pull-up |
| 3 | PB8 / I2C1 SCL; host R140=1,5k |
| 4 | PB9 / I2C1 SDA; host R142=1,5k |
| 5 | PH7 reset mevcut; adaptörde NC, bağımsız reset PB12’den |
| 6 | GND |

Önemli kablo farkı: panelin ayrı 6-pin touch flex’i s.6’da 1=GND, 2=SCL, 3=SDA, 4=RST, 5=INT, 6=VDD şeklindedir; J3’e takılmaz. Tasarım touch’ı s.7’ye göre panelin 39-pin J2.30–35 bağlantılarından kullanır. Ayrı panel touch flex’i bu adaptörde kullanılmaz.

R1/R2 4,7k DNP kalır: hostta zaten 1,5k pull-up vardır. İlave takılırsa eşdeğer ≈1,14k olur ve sink akımı artar. 1,5k için tr≈0,8473RC; 400kHz/300ns sınırı ideal RC hesabında ≈236pF bus kapasitesine karşılık gelir. FPC ve probe dahil yükselme süresi ölçülmeli; ILI2130 sink/INT tipi/adres/reset ayrıntıları ayrıca temin edilmelidir.

R3/R15=100Ω ve R14/R17=10k reset pull-up’ları korunur; LOW’daki ideal direnç bölücü düşümü ≈33mV’dir. LCD reset PH7 open-drain ile, touch reset PB12 ile bağımsızdır. S.9–11 iç TCON/BIST çizimleri dış RESX darbe süresini doğrulamaz. LCD/touch akımları TBD: 800mA sınıfındaki host regülatörü, kartın diğer yükleri ve termal bütçe düşülmeden panel için 800mA kaynak kabul edilmez.

## 4. TPS61165 ve OVP incelemesi

U1 DBV pinleri TI s.3 ile eşleşir: 1 VIN, 2 CTRL, 3 SW, 4 GND, 5 COMP, 6 FB. LEDK doğrudan GND değildir; J2.3/.4 → FB/R7 üst düğümüdür. LEDA J2.1/.2’dir. R7=%1 5,23Ω: nominal 38,24mA; VFB=196–204mV ile 37,11–39,40mA; sense kaybı en fazla ≈8,04mW. Panelde 40mA tipik değer olup garanti edilmiş mutlak maksimum olarak sunulmaz.

L1=22µH, C9=220nF TI önerileriyle uyumludur. C1=10µF giriş kapasitesi korunur; TI’nin minimum ≥1µF koşulunu karşılar, giriş inrush ölçülmelidir. C3=10µF/50V X7R için etkin kapasite/DC bias eğrisi şarttır. D1 SS16 60V/1A, D3 SS14 40V/1A rating’leri Vishay’dan kontrol edildi. D3 ters akımı/reverse polarity’yi bloklar; F2 PPTC hızlı elektronik akım sınırlayıcı değildir.

İşaretlenmiş mühendislik köşe hesabı: VIN=4,2V, η=%75, etkin L=13,2µH, fSW=1MHz ve LED VF=27,2V kabulüyle yaklaşık giriş 0,351A, ripple 0,270App ve tepe 0,486A çıkar. U1 akım limitinin 0,96A alt sınırına statik marj vardır. Bu varsayımlar giriş kablosu düşümünün, verimin veya açılışın ölçüldüğü anlamına gelmez; soft-start/input dip, gerçek L bias ve termal testler açıktır.

TDK SLF7045T-220M1R3-H referansının tablosu 0,082Ω ±%20 DCR; %10 L düşüm kriterinde 1,3A, %30 için tipik 2,5A, ΔT20°C için tipik 1,25A verir. Mevcut ≈0,49A tepe yükü için makuldür. Ancak TDK belgesi ürünün son sipariş tarihini 31 Mart 2026 olarak verir. Doğrulanmış stok kullanılmalı veya aynı footprint/rating/bias eğrisiyle alternatif kalifiye edilmeli; generic “22µH” tek başına satın alma tanımı değildir.

U2 TLV3011BIDBVR pinleri TI SBOS300C s.3 ile doğrulandı: 1 OUT_OD, 2 GND, 3 IN+, 4 IN−, 5 REF, 6 V+. BL_POWER ile besleme 1,65–5,5V aralığına uygundur. B sürümü fail-safe girişler ve 5,5V’a kadar bağımsız open-drain pull-up destekler; non-B veya TLV3012 sessizce ikame edilemez. İç histerezis 2–8mV olduğundan sırf chatter kaygısıyla yeni feedback dirençleri eklenmedi.

R19/R20=221k/10k ile 1,242V referanstan nominal OVP=28,690V. B sürümünün referansı 1,223–1,260V; offset, histerezis, sıcaklık ve direnç toleransı gerçek eşiği değiştirir. POR sırasında OUT, 1,9ms’ye kadar Hi-Z’dir; “güç gelir gelmez kapatır” iddiası yanlıştır. TPS61165 CTRL’nin 180µs filtresi ve >2,5ms shutdown davranışı nedeniyle devre sert gerilim kıskacı değildir. Dahili 37–39V açık-LED koruması, Hirose aile 30V rating’ini koruma garantisi vermez.

## 5. Kabul koşulları ve ilk çalıştırma

PCB yerleşim çalışmasına native dosyadan başlanabilir; nihai şematik dondurma ve panelle enerji verme aşağıdaki açık koşullar kapanmadan onaylanmaz. Tamamlanmış kontroller ile henüz yapılmamış donanım deneyleri ayrı tutuldu.

| Açık konu | Kapatma kanıtı |
| --- | --- |
| Touch besleme toleransı | DISEN: VDD sürekli/tepe maksimum, 3,365V host toleransı ve I/O injection sınırları. Gerekirse belgeli rail + I/O revizyonu. |
| Akım ve timing | LCD/touch max/başlangıç akımı; OTA7290B gerçek init/timing; dış LCD reset ve ILI2130 reset/INT/I²C bilgisi. |
| Gerçek host ve FPC | Kart revizyonu/popülasyonu, pin1/kontak yüzü, 25/6/39 pin sürekliliği; FH26 legacy/W exact sipariş ve uç uyumu. |
| OVP / açık yük | Dummy LED ile güç sıraları, PWM, open-load ve yeniden yükleme testlerinde tepe <30V. Sağlanmazsa daha hızlı inhibit/clamp revizyonu gerekir. |
| Tedarik ve pasifler | C3 DC-bias eğrisi, L1 stok/alternatif onayı, F2 derating ve exact MPN/rating kontrolleri. |

Önerilen laboratuvar sırası: (1) Güç kapalıyken kabloların bütün pinlerini ve izolasyonu ölçün; orijinal LCD/touch flex’lerini çıkarın. Paneli henüz bağlamayın. (2) Ortak GND ile akım sınırlı 5V kaynağı kullanın; J6.1=+5V, J6.2=GND. Host ve boost rail’lerini, reset seviyelerini ölçün. (3) PWM’yi tüm rail geçişlerinde LOW tutun; rail’ler geçerli olduktan sonra en az 5ms bekleyin. Bu 5ms mühendislik marjıdır, panel reset süresi değildir. (4) Önce uygun seri LED/dummy yükle 20kHz PWM’yi düşük duty’den yükseltin; akım, ripple, açık-yük tepesini ve C3 discharge’ını ölçün. (5) Üretici touch onayı ve önceki testler sonrasında panelle kontrollü başlatma, I²C rise-time, host rail düşümü/ısınma ve görüntü deneyine geçin.

R6=100k varsayılan OFF sağlar; PWM sabit yüksekken boost gücünü açmak POR korumasını aşabilir. Kapatırken önce PWM LOW; tam kapanış için >2,5ms. R18/C3 nominal 33k×10µF hesabıyla 28,69V’tan 5V’a yaklaşık 0,58s verir, fakat gerçek kapasitans/deşarj ölçülmeden sıcak takma/sökme yapılmaz. Rail kapalıyken I²C/reset/INT üzerinden back-power oluşturmayın.

Doğrulama kanıtı: input ERC 0 error / 9 warning; revised ERC 0 error / 0 warning. Dokuz uyarı, altı eksik kütüphane kaydı ve üç tekil global etiketten oluşuyordu. Kontrol kuralları ve exclusion’lar kaynakla aynıdır. XML karşılaştırması tüm komponentleri/fiziksel net bölümlerini korur. 53 footprint için pin-pad varlığı doğrulandı; bu mekanik FPC fit garantisi değildir. Paket farklı dizinden KiCad CLI ile tekrar açılıp ERC/netlist/PDF denemesiyle kontrol edilir. GUI etkileşimli test, gerçek donanım, PCB DRC, routing ve firmware testi yapılmadı.

Teslim: Project/ yerel kütüphanelerle üç sayfalık native proje; PDF/ şematik ve bu rapor; Verification/ ERC/netlist/pin audit/hesaplar; References/ üretici belgeleri; Original/ değişmemiş yükleme. Eski PCB, güncel şematikle aynı teslim gibi görünmemesi için yalnız özgün ZIP içinde korunur. Kaynak depo tarihsel dosyaları değiştirilmedi.
