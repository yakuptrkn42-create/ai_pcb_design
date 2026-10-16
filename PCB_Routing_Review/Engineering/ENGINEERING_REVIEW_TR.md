# Rev I · Routing R1 — Mühendislik değerlendirmesi

16.10.2026 — Bağımsız, kablolu DISEN LCD adaptörü. Routing gerçek KiCad 9 PCB dosyasında tamamlandı; komponent konumları ve yönleri onaylanan yerleşimle aynıdır. Üç şematik dosyası byte düzeyinde korunmuştur. 49 devre footprint'i, dört kart montaj deliği, 57 net ve 172 pin-net üyeliği doğrulandı. R1/R2 DNP kaldı.

## Sonuç ve doğrulama

| Kontrol | Sonuç |
|---|---:|
| Doldurulmuş PCB DRC ihlali / açık bağlantı | 0 / 0 |
| Şematik–PCB parity / ERC ihlali | 0 / 0 |
| DRC hariç tutması | 0 |
| Sinyal izi bulunan iç katman | 0 |
| Bakır dolgu / montaj donanımı keepout | 4 / 4 |
| Toplam through via / GND via | 110 / 63 |
| Bağımsız ayrıştırılan Gerber dosyası | 11 |
| Native kartla eşleşen PTH / NPTH delik | 128 / 4 |

DRC önem seviyeleri önceki projeyle aynı tutuldu; kontrol kapatılmadı. Test edilen sonuç son doldurulmuş karttır. DRC üreticiye özgü proses yeterliliği, sinyal bütünlüğü ölçümü veya fonksiyon testi değildir. Ayrıntılar `Verification/` altındadır.

## Katman yapısı — nominal, üretici tarafından onaylanmadı

| Sıra | Yapı | Kalınlık |
|---|---|---:|
| L1 | F.Cu — komponentler, sinyal, güç, GND dolgu | 0,035 mm |
| Dielektrik | FR4 prepreg, nominal εr 4,2 | 0,100 mm |
| L2 | In1.Cu — GND referans | 0,035 mm |
| Dielektrik | FR4 core, nominal εr 4,2 | 1,260 mm |
| L3 | In2.Cu — GND referans | 0,035 mm |
| Dielektrik | FR4 prepreg, nominal εr 4,2 | 0,100 mm |
| L4 | B.Cu — sinyal, güç, GND dolgu | 0,035 mm |

Toplam nominal kalınlık 1,600 mm; soldermask bu toplama ve empedans modeline dahil değildir. İki iç GND dolgusu ayrı ayrı tek, kesintisiz bağlı poligondur. Montaj delikleri etrafında tüm bakır katmanlarda 3 mm yarıçaplı donanım rezervi bulunur. Dış GND dolgularında kopuk adalar kaldırılmış, padlerde termal bağlantı kullanılmıştır.

## Tasarım kuralları

| Özellik | Projeye uygulanan değer |
|---|---|
| Minimum bakır açıklık | 0,15 mm; normal/güç sınıfları 0,20 mm |
| Minimum iz / kart kenarı açıklığı | 0,14 mm / 0,50 mm |
| Through via | 0,50/0,25 mm; güç düğümlerinde 0,60/0,30 mm |
| Minimum annular ring / hole-to-hole | 0,10 mm / 0,30 mm |
| MIPI çift | 0,14 mm iz; 0,18 mm kenardan kenara çift aralığı |
| MIPI kısa tekil kaçışlar | 0,17 mm; ince pad çıkışları 0,14 mm |
| MIPI CAD kuralları | Çift içi skew ≤0,10 mm, iletken ≤35 mm, en fazla iki via |
| MIPI dış GND dolgu uzaklığı | En az 0,50 mm |
| Güç yolları | 5 V omurga 0,60 mm; boost 0,30–0,60 mm; mantık 0,20–0,30 mm |

0,25 mm delik ve 1,6 mm kart için nominal aspect ratio 6,4:1'dir. Bu değer seçilen proses hedefidir; üreticinin delme/kaplama yeterliliği henüz onaylanmış değildir.

## MIPI DSI

| Çift | P bakır merkez çizgisi | N bakır merkez çizgisi | CAD çift içi fark | Via / iletken |
|---|---:|---:|---:|---:|
| CLK | 22,297 mm | 22,297 mm | <0,001 mm | 2 |
| D0 | 26,984 mm | 26,984 mm | <0,001 mm | 2 |
| D1 | 27,008 mm | 27,008 mm | <0,001 mm | 2 |

Tablo via barrel uzunluğunu içermez; tüm iletkenlerde aynı iki through geçiş vardır. En büyük lane–clock bakır uzunluk farkı 4,711 mm'dir; uygulanan 5 mm inceleme bütçesinin içindedir. Bunlar CAD geometrisi değerleridir; üretim veya gerçek yayılma gecikmesi ölçümü değildir. Host kart, LCD, flex ve konnektör gecikmeleri dahil değildir.

Staggered FPC padlerinin gerektirdiği kaçışlar için CLK/D1 ağırlıklı B.Cu, D0 ağırlıklı F.Cu üzerinde düzenlendi. Geçiş sayısı dengelendi. Uzun eşlenmiş kısımlar paralel tutuldu; tekil kaçışlar ayrı genişlikle oluşturuldu. Kritik izler kilitlidir.

Nominal stackup ile iki boyutlu yarıstatik sonlu hacim odd-mode hesabı, 0,14/0,18 mm geometri için **99,3 Ω diferansiyel** verdi. 5 µm ağda 98,75 Ω, 2,5 µm ağda 99,14 Ω; daha geniş hesap bölgesinde 99,32 Ω bulundu. Ayrık 0,17 mm iz için nominal tekil değer yaklaşık 49,3 Ω'dur. Ham girişler ve sonuçlar `nominal_impedance.json` dosyasındadır. Soldermask, gerçek cam örgüsü/εr toleransı, pad/konnektör/via 3D alanları bu modele dahil değildir; üreticiye doğrulanmış 100 Ω garantisi verilmemektedir.

GND dönüş viasları geçişlerin yakınına eklendi; sinyal viasına en yakın GND via mesafeleri 0,70–1,61 mm aralığındadır. Doldurulmuş iç katmana geometrik izdüşüm kontrolünde uzun 0,14 mm izlerin **doğrudan altında eksik GND alanı bulunmadı**. Bu test geçişlerin 0,75 mm çevresini hariç tutar. Üç kontrol/güç viasının kaydırılmasıyla yan alan açıklıkları azaltıldı. İki komşu signal viasının antipadı, ilave 0,10 mm yan referans marjında toplam yaklaşık 0,109 mm² yerel boşluk bırakır. Bu geçiş/fringing bölgeleri, konnektörler ve son stackup için 3D SI/TDR değerlendirmesi hâlâ gereklidir. Ayrıntı `Verification/MIPI_reference_plane.json` içindedir.

## Backlight, güç ve optimizasyon

TPS61165 SW–D1 yolu, L1 dalı, C2–VIN bypass ve C4–GND dönüşü elle oluşturuldu. SW ağında via yoktur; SW bakırı izlerle sınırlıdır. D1/C4/U1 dönüş çevrimi kısa tutuldu ve yerel GND inişleri eklendi. LEDK akımı R7 tarafına gelir; IC FB ucu ayrı kısa Kelvin dalıyla bağlanır. COMP yerel tutulur; kontrol ve OVP bölümü SW bakırından ayrıdır.

Kalan ağlarda yerel Freerouting ve geometri tabanlı yardımcı yönlendirme kullanıldı. Sonuç KiCad'de tekrar doldurulup denetlendi. Kontrol güzergâhlarında **413 gereksiz segment ve yaklaşık 9,8 mm bakır uzunluğu** kaldırıldı; kullanılmayan iki via ve uçları temizlendi. Uygun 77 güç segmenti 0,20'den 0,30 mm'ye genişletildi. Daha sonra referans düzlemi marjı için üç via kaydırıldı. Son kontrol bu işlemlerin tamamından sonradır.

35 µm dış bakır ve 10 °C sıcaklık artışı için yaklaşık IPC-2221 hesabı, 0,20 / 0,40 / 0,60 mm izlerde sırasıyla 0,75 / 1,23 / 1,65 A verir. Bu, IPC-2152 veya termal ölçüm yerine geçmez. 5 V giriş inceleme zarfı 0,75 A; mantık/LCD 0,30 A ve dokunmatik 0,10 A alındı; bunlar panelin doğrulanmış tüketim değerleri değildir. F2'nin hold değeri sert akım sınırı değildir.

R7=5,23 Ω ve nominal FB=0,20 V ile LED akımı yaklaşık 38,2 mA'dır. OVP bölücüsü ve 1,242 V referans varsayımıyla eşik yaklaşık 28,69 V olur. 4,5 V giriş / %80 verim inceleme örneği, yaklaşık 0,305 A ortalama boost giriş akımı verir. Giriş bakır yollarının tüm dalları seri kabul edildiğinde 0,75 A'da toplam bakır/via düşümü üst sınırı yaklaşık 56 mV'dir; diyot, sigorta, 0 Ω bağlantı, konnektör, flex ve GND dönüşü buna dahil değildir. Mantık/LCD ağlarında aynı muhafazakâr yöntemle 0,30 A'da ağ başına 45 / 31 mV üst sınır hesaplandı. Via direnci hesabında henüz doğrulanmamış 20 µm kaplama kabul edilmiştir. Ham hesap `power_estimates.json` içindedir.

## Üretim öncesi açık bilgiler

1. Üreticinin bitmiş stackup'ı, gerçek εr/soldermask, empedans toleransı ve kupon/TDR yaklaşımı kesinleştirilmeli; gerekirse iz genişliği/aralığı yeniden hesaplanmalıdır. Mevcut Gerberler nominal inceleme çıktılarıdır.
2. Verilen FPC footprint'lerinin numaralandırması ve pad geometrisi korunmuştur; W serisi üretici çizimi, kontakt yüzü, flex kalınlığı/pin sırası, aktüatörün açık hali ve LCD/kasa geometrisi fiziksel parçalarla eşleştirilmemiştir. Dört montaj deliği ve kart içi mekanik açıklıklar denetlenmiştir. J1/J2/J3/L1 3D gövdeleri nominaldir; gerçek üretici STEP'i değildir.
3. L1'in kesin MPN'i, Isat/Irms/DCR'si; C3'ün DC bias altında etkin kapasitesi ve kesin BOM parçaları teyit edilmelidir. İlk prototipte kontrollü güç verme, çıkış/OVP/PWM, termal davranış, DSI ve dokunmatik testleri yapılmalıdır. EMI/EMC testi yapılmamıştır.

Onaylanan şematikte değişiklik yapılmadı. Bu paket tamamlanmış routing'in son mühendislik incelemesine sunulmasıdır; üretici/mekanik onayı yerine geçmez.

`BOM_REV_I.*`, `PIN_MAPPING_REV_I.md` ve `SOURCE_REFERENCES_REV_I.md` önceki Rev I tesliminden aynen alınan kaynak kayıtlardır; yeni üretici doğrulaması veya bu çalışmada tüm bağlantılı veri sayfalarının yeniden incelendiği anlamına gelmez.
