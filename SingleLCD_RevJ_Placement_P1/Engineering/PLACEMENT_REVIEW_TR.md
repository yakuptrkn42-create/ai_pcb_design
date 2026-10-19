# Rev J / Placement P1 — Tek DISEN LCD

19 Ekim 2026 · DS070HSD39T-132 · Bağımsız, kablolu adaptör · Yerleşim incelemesi.

## Sonuç ve dosya kapsamı

Onaylı SingleLCD_RevJ_PCBPrep projesinin gerçek KiCad PCB dosyasındaki 49 devre referansı yerleştirildi. Şematik, sembol kütüphaneleri, mevcut footprint kütüphaneleri, 3D model dosyaları ve tasarım kuralları kaynakla byte düzeyinde aynıdır. 57 net / 172 numaralı pin–net üyeliği, değerler, footprint kimlikleri, PCB–sembol yolları ve UUID'ler korunur. R1/R2 DNP kalır. Çift LCD Rev K değiştirilmedi.

Kart **50 × 42 mm**, köşeler **R2**, nominal **1,6 mm / 4 katman**. Bütün devre referansları üst yüzde. Laboratuvar sabitlemesi ve kablo takma kuvvetleri için dört adet Ø2,7 mm M2.5 NPTH mekanik delik eklendi; bunlar board-only, BOM dışı ve elektriksel bağlantısızdır. Yeni elektriksel komponent/blok eklenmedi. Montaj merkezleri kart sol üstünden (3,5;3,5), (46,5;3,5), (46,5;38,5), (3,5;38,5) mm; baş/washer için Ø6 mm alan ayrıldı.

**0 track, 0 via, 0 zone** — keepout zone dahil. PCB üzerinde kart sınırı, footprint'ler, yazılar ve bakır olmayan açıklama çizgileri bulunur. Referans/origin (100;80) mm'ye, kartın sol üst köşesine ayarlandı. Yerleşim onayı gelmeden routing yapılmayacaktır. Gerber, drill veya üretim çıktısı oluşturulmadı.

## Üç alternatif ve seçim

Üç yaklaşım, aynı footprint/pin geometrileriyle koordinat konsepti olarak değerlendirildi. GND ve tek başına NC netleri hariç Euclidean minimum yayılım ağacı (MST) toplamı/kesişimi, ratsnest yoğunluğu karşılaştırmasında kullanıldı. Bu metrikler gerçek iz uzunluğu, via adedi veya KiCad'in bire bir ratsnest ağacı değildir. Alternatiflerin native courtyard poligonlarında çakışma yoktur; tam parity/DRC/3D son kabul yalnızca seçilen B projesine uygulanmıştır.

| Konsept | Boyut / alan | DSI pad mesafesi min–maks. | DSI koridoru | GND/NC hariç MST toplam / kesişim |
|---|---|---|---|---|
| A — kompakt | 44 × 38 mm / 1672 mm² | 14,3–17,3 mm | 22 × 3 mm / 66 mm² | 588,4 mm / 68 |
| B — routing / SI, seçilen | 50 × 42 mm / 2100 mm² | 16,9–20,0 mm | 25,2 × 4 mm / 100,8 mm² | 638,2 mm / 68 |
| C — mekanik erişim | 56 × 46 mm / 2576 mm² | 47,1–50,05 mm | 38 × 6 mm / 228 mm² | 927,1 mm / 134 |

Tablodaki DSI sayıları **pad merkezi kuş uçuşu mesafeleridir**, route edilmiş hat uzunluğu değildir. Yuvarlanmamış değerler Alternative_Comparison.json içindedir.

A fiziksel olarak sığar, ancak iki üst FPC gövdesi arasındaki nominal boşluk 4,7 mm'ye iner; son tuning/escape alanı ve alt güç/soket erişimi daha sıkışıktır. 0,14 mm iz / 0,18 mm çift aralığında bir çift 0,46 mm kaplar. Üç çift, çiftler arası 0,50 mm planlama payı ve iki kenarda 0,50'şer mm ile 3,38 mm alan ister; A'nın 3 mm koridoru tek yüz için bu bütçeyi karşılamaz. Bu 0,50 mm aralık bir SI tasarım rezervidir; hesapla doğrulanmış crosstalk sınırı değildir.

B'de 4 mm koridor, 3,38 mm bütçeyi karşılar; FPC gövdeleri arasındaki nominal boşluk 7,4 mm'dir. A'ya göre 428 mm² alan artışı, daha rahat fanout, length tuning, besleme ve servis erişimi için kullanıldı. C'nin karşı kenarlı FPC çıkışları bağımsız erişim sağlar; ancak daha fazla ratsnest kesişimi ve 50 mm PCB iletken bütçesine yaklaşan/aşan alt sınır, bu adaptörde gereksiz kanal uzaması getirir. 50 mm kuralı tasarım bütçesidir; panelin mutlak fiziksel uzunluk sınırı değildir.

İlk B taslağında J1 x=35 mm idi. Konnektör 2,5 mm J2'ye yaklaştırıldı; TE direnci ve touch bulk kondansatörü yeniden hizalandı. DSI ortalama pad mesafesi **20,951 → 18,465 mm**, yaklaşık **%11,9** azaldı. Genel MST toplamı **656,8 → 638,2 mm** oldu. Sonrasında J4/L1 ve giriş diyodu çevresindeki mekanik açıklıklar iyileştirildi. Boost grubu için beş deterministik arama geçişinde 90.000 aday hareket değerlendirildi; son konumlar PCB'nin tamamı görülerek ayrıca düzeltildi. Optimizasyon skoru elektriksel çalışma garantisi değildir.

## DSI, güç ve kontrol yerleşim mantığı

J2 LCD, üst solda; J1 host DSI, üst sağda. İki nominal FPC ağzı kartın üst kenarına yönlendirilmiştir. J3 host touch girişi sağ kenarda, J5 CN12 kablo soketi alt sağda, J4 haricî 5 V girişi sol alttadır. J5, Discovery üzerine doğrudan oturacak konumda kabul edilmedi; mevcut karar olan kablolu kullanım esas alındı.

DSI ana koridoru kart sol üstünden x=11,8…37 / y=12…16 mm arasında komponentsizdir. LCD ve host launch yaklaşımları için sırasıyla x≈11,8…16 ve x≈30,5…34,2 mm bölgeleri açık tutuldu. SW terminal üçgeninin koridora en yakın mesafesi **8,5 mm**. L1/güç anahtarlama grubu alt solda; FB/COMP ve OVP, SW düğümünün sağındaki daha sakin tarafta; touch/reset/PWM bağlantıları sağ/alt bölgede toplanır.

FPC sıra/pin düzeni önemli bir darboğazdır: aynı pad sırasındaki komşu kontaklar 0,60 mm aralıklı, pad genişliği 0,30 mm'dir; arada yaklaşık 0,30 mm kalır. 0,14 mm iz + iki tarafta 0,15 mm clearance toplam 0,44 mm gerektirir. Bu nedenle iç sıra fanout'u doğrudan diğer sıradaki pad'lerin arasından geçirilemez. Konnektör yanından çıkış veya standart geçişli via ile karşı dış kata geçiş gerekir. Saat ve D1 lane sıraları iki konnektörde farklı fiziksel sıralandığından crossover da planlanmalıdır; pin/net değişimi yapılmadı.

Bu aşamada **4–12 DSI via** yalnızca bir planlama aralığıdır: bir çiftin katman değiştirmesi dört via, üç çiftin tamamı on iki via gerektirebilir. Yan escape ile bazıları azaltılabilir; kesin sayı routing ile bulunur. Mevcut iletken başına en çok iki via kuralı korundu. Viasız routing garantisi verilmez ve hiçbir via konulmadı. Sonraki aşamada MIPI önce route edilmeli; çiftlerin geçişleri simetrik, GND dönüşleri yakın olmalı; kontrollü empedans ve eşleşme gerçek bakır üzerinde tekrar denetlenmelidir.

TPS61165 yerleşimi TI SLVS790E §11.1, s.21'deki SW yollarını ve switch–Schottky–çıkış kapasitörü döngüsünü küçültme; giriş kapasitörünü VIN/GND'ye yakın tutma yaklaşımına dayanır. L1.2/U1.3/D1.2 üçgeni kısa tutuldu. C4 yüksek frekanslı çıkış döngüsüne, C3 bulk olarak diyot çıkışına, R7 FB tarafına, C9 COMP tarafına yerleşti. C2 ve C13 ilgili IC beslemelerine yakındır.

| Kritik bağlantı | Pad merkezi mesafesi |
|---|---|
| C2 → U1 VIN | 1,90 mm |
| L1 SW → U1 SW | 2,41 mm |
| D1 anodu → U1 SW | 2,72 mm |
| C4 GND → U1 GND | 2,74 mm |
| C4 çıkış → D1 katodu | 4,01 mm |
| C3 çıkış → D1 katodu | 3,54 mm |
| R7 → U1 FB | 1,97 mm |
| C9 → U1 COMP | 2,26 mm |
| C13 → U2 VCC | 1,90 mm |

Bu sayılar bakır uzunluğu veya döngü endüktansı değildir. C2/C13 GND dönüşleri, R7 Kelvin dönüşü ve C9 sessiz GND bağlantısı routing sırasında kısa ve doğrudan kurulmalıdır. Özellikle C2'nin GND pini ile U1 GND arasındaki merkez mesafesi yaklaşık 6,1 mm'dir; yalnızca kısa VIN bağlantısı tam decoupling başarısı sayılmaz. İç GND'ye yakın dönüş bağlantıları sonraki aşamanın görevidir.

Giriş sigortası, ters blok diyodu ve izolasyon linki sol altta gruplanır. Çıkış deşarj direnci R18, bulk kapasitör yakınındadır. VCI/touch decoupling elemanları J2 yakınında, R15 host reset tarafında, R16 host TE tarafındadır. Opsiyonel I²C pull-up'ları sağdaki touch grubunda DNP korunur. On iki mevcut test pad'i erişilebilir boşluklara yerleşti; DSI üzerine yeni test stub'u eklenmedi.

## Mekanik ve 3D doğrulama sınırları

49 referansın 3D yolları ve hash'leri doğrulandı. 13 farklı model kullanılır; kaynak paketindeki 14 dosya korunur. Bütün nominal model AABB izdüşümleri karşılaştırıldı, komponentler arasında izdüşüm çakışması yok. Bu, muhafazakâr nominal hacim kontrolüdür; gerçek solid/latch hareketi veya kasa tolerans analizi değildir. Dört delikte Ø6 mm donanım zarfı için native courtyard ayrıldı. Tüm courtyard'lar arasında en az 0,15 mm ek açıklık doğrulandı. Montaj zarfı bu aşamada courtyard rezervidir; sonraki routing/zone aşamasında vida/washer altı bakır boşlukları ayrıca tanımlanmalıdır.

J1/J2/J3 pin-1 konumları native pad numarasıyla kaydedildi; numara/net/polarite ve CAD yönleri korunur. Library içindeki alt kontak/FPC 0,20 mm açıklamaları tasarım girdisidir; yeni fiziksel doğrulama olarak sunulmaz. Hirose exact sipariş varyantları, gerçek FPC kontak yüzü, kablo pin-1 yönü ve aktüatörün açık konumu önceki çalışmada da tam doğrulanamamıştı. Nominal 3D modeller bu eksikleri kapatmaz. Kart dışındaki FPC açıklama kutuları servis rezervidir; gerçek flex bükülme yarıçapı veya minimum bend-radius onayı değildir. Kasa/LCD mekanik CAD'i ve kablo boyları verilmedi; physical fit kabulü açık kalır.

3D görseller opsiyonel R1/R2 modellerini de gösterebilir; BOM ve native DNP bayrakları esas alınır. Altta SMD komponent yoktur; J4/J5'in lehim bacakları ve NPTH delikler alt görünümde bulunur. Üstten lehimleme/rework ve prob erişimi dikkate alındı; uzun soket/indüktör yüksekliği için gerçek karşı fiş/kasa ölçüleri ayrıca gerekir.

## Kontroller ve sonraki aşama

Yerleşim DRC: **0 fiziksel ihlal**. Schematic parity: **0 sorun**. ERC: **0 hata / 3 mevcut tekil global-label uyarısı**. Routing yapılmadığı için **115 bağlantısız öğe kaydı** vardır; bu sayı unrouted net sayısı değildir. Unconnected denetimi error düzeyinde açıktır; ignore, rule gevşetme veya exclusion eklenmedi. Ham JSON/metin raporları pakettedir.

Kaynak stackup/rule dosyaları aynen korundu: F.Cu / In1 GND / In2 GND / B.Cu; 1,6 mm; nominal dış dielektrik 0,10 mm, 35 µm bakır ve Er=4,2. İç GND katmanları henüz dolu değildir. 0,14/0,18 mm DSI geometrisinin yaklaşık 99,3 Ω sonucu önceki nominal hesaptır; üretici/stackup/empedans toleransı onayı yoktur. Bu yerleşim çalışması sinyal bütünlüğü simülasyonu veya donanım ölçümü değildir.

Onay sonrası routing öncelikleri: DSI fanout/crossover ve GND dönüşleri; küçük boost komütasyon döngüsü; C2/C13 yerel GND ve R7 Kelvin/COMP bağlantıları; 0,60 mm sınıfındaki ana 5 V yolları ve yeterli GND; touch/reset/PWM. Mevcut şematik incelemesinde açık kalan CN2 fiziksel eşleşmesi, panel akım/tolerans verisi, OVP transient ve parça tedarik koşulları Source_Review_TR.md içinde korunur. Bu teslim placement onayı içindir; üretim serbest bırakması veya kesin çalışma garantisi değildir.

ZIP temiz KiCad ayarlarıyla ayrı klasörde yeniden açılıp kontrol edildi: 49 model yolu ve 57 net class çözüldü; DRC/parity 0, ERC 0 hata / 3 uyarı, 115 beklenen bağlantısız kayıt korundu.
