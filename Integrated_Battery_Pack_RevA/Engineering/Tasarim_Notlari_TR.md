# Tasarım açıklaması ve tasarımcıya açık maddeler

## Elektriksel yapı

Mevcut BQ28Z610DRZR-R1, BQ294502DRVR, CSD16412Q5A MOSFET'ler, 1 mΩ şönt ve SCF4030-12-02 tetiklemeli sigorta korunmuştur. Bunların değerleri kaynak PCB'den okunmuştur; tedarikçi veri sayfaları ve gerçek malzemeyle yeniden nitelendirme yapılmadı. TI veri sayfasını doğrudan edinme girişimi ortam ağından HTTP 403 aldı; üretici pin/limit teyidi tamamlanmış sayılmamalıdır. Boş kaynak şematik nedeniyle işlevsel şema doğrulaması ayrıca gereklidir.

Hücre uçları: PAD7 = CELL_PLUS (B+), PAD1 = CELL_MID (B1), PAD8 = CELL_MINUS (B−). Seri köprü birinci hücrenin artısını ikinci hücrenin eksisine bağlar. Hücreler ters yönlerde, uzun eksenleri X yönünde durur. CELL_PLUS şarj/deşarj MOSFET'leri ve mevcut sigorta zinciri üzerinden PROTECTED_PLUS'a gider. Yeni F1 (2,5 A aday DC sigorta) PROTECTED_PLUS ile dock ana PACK_PLUS arasındadır. PACK_MINUS, mevcut şöntün paket tarafıdır; CELL_MINUS'a doğrudan yeni dönüş yolu eklenmemiştir.

J1: 1=PACK_PLUS, 2=PACK_PLUS_AUX, 3=HOST_NTC, 4=PACK_MINUS. R40=0,1 Ω / %1 / en az 0,25 W yardımcı pozitif kolu dengeler; F2=0,5 A hızlı DC sigorta adayı küçük kontağın ana pozitif kontak kesildiğinde sürekli 2 A taşımasını önlemeyi amaçlar. F1/F2 kesin MPN, DC kesme kapasitesi ve zaman-akım/I²t eğrileri seçilmemiştir. Sigortalar BMS akım limitinin yerine geçmez. Ana temasın kesilmesinde pompanın enerji kaybı ve alarm davranışı cihaz seviyesinde ele alınmalıdır.

TH1: BMS_TS–CELL_MINUS arası 10 kΩ sensör. TH2: HOST_NTC–PACK_MINUS arası ayrı 10 kΩ sensör. Aynı NTC iki ölçüm girişine bağlanmadı. NTC'lerin B sabiti, toleransı ve host ADC/bias yapısı bilinmiyor. Sensörler hücre kılıfına elektriksel olarak izole, termal olarak temas eden boncuk biçiminde modellenmiştir; kısa izole iç bağlantılar gerekir. PCB'deki TH1/TH2 delikleri lehimli sensör ucu bağlantısıdır. BMS sense toprağı ile harici NTC dönüşü arasında şöntü köprüleyen yeni bağlantı yoktur.

Mevcut SCL/SDA servis noktaları korunmuştur. Dört kontaklı dock'ta haberleşme yoktur. BQ28Z610 programlama, kimya eşlemesi, kapasite/şönt kalibrasyonu, şarj/deşarj/UV/OV/OC/SC/sıcaklık eşikleri, uyandırma ve depolama akımı hazırlanmadı. 3500 mAh etiketi hücrenin güvenli akımını veya şarj gerilimini tek başına belirlemez. BMS, 2S CC/CV şarj cihazının yerine geçmez.

## Kaynak PCB düzeltmeleri

Kaynağın KiCad 9.0.2 DRC sonucu 143 ihlal ve 16 açık bağlantıydı. R1/R2/R11/R12/R28/R29/C2/C17'nin alt yüz yönleri pad/net–mevcut iz eşleşmesini bozuyordu; 180° düzeltildi. Atanmamış bakır terminal poligonları net taşıyan gerçek pad'lere dönüştürüldü. U2'nin ithal yinelenmiş termal pad adları aynı EP pad numarasına birleştirildi; hücre/gauge GND ve SIGNAL_GND aynı CELL_MINUS netine alındı. Kaynaktaki boş netli termal PAD19, fiziksel olarak içinde bulunduğu U1 termal toprağına bağlandı; bu seçimin IC land-pattern teyidi tasarımcıya aittir. Yakın delikler/vialar, iki clearance noktası, boştaki vialar ve mask/silk çizimleri düzeltildi; bölgeler yeniden dolduruldu. Şöntün iki tarafı birleştirilmedi.

Genel clearance 0,15 mm, delik aralığı 0,25 mm ve bakır–kenar 0,5 mm üretim hedefidir. İnce aralıklı mevcut QFN/SON geometrisi nedeniyle 0,15 mm proses hedefi seçilmiştir; fabrika kabiliyeti ve orijinal IC footprint'leri ayrıca onaylanacaktır. Yeni ana güç izleri 1,5 mm, kısa paralel via köprüleri 0,7 mm ve sinyal izleri 0,25–0,3 mm'dir. Modelde PCB 1,0 mm'dir; 1,8 mm konnektör kuyrukları için nominal 0,8 mm lehim çıkıntısı sağlar. En az 35 µm dış bakır hedeflenmiştir; mask/paste/stackup üreticiye teyit ettirilmelidir.

35 µm bakır ve 1,5 mm iz için 20 °C'de R ≈ 0,328 mΩ/mm. 100 mm toplam gidiş+dönüş yolu 32,8 mΩ ve 2 A'de yaklaşık 0,131 W verir; bu, mevcut çekirdeğin dar boğazları, MOSFET, kontak, sigorta ve via dirençlerini içermez. Bu bir termal simülasyon değildir. Tam yol ölçümü ve sıcaklık artışı testi gerekir. Via çiftleri yeni ana güç katman geçişlerinde kullanılmıştır.

## Dock konnektörü

Kullanıcı çizimi: CZX-4B2-2.54-e; dış ölçü 27,62 × 5,1 mm, kulak merkezi 23,98 mm, kulak deliği 1,9 mm, kontak adımı 2,54 mm. Bataryada sabit taraf kullanılır. Büyük/küçük kuyruklar için aday bitmiş delikler 1,5/0,9 mm, kulaklarda 2,0 mm NPTH seçildi. Delik toleransı, pin kesiti/konumu, yükseklik, lehim kuyruk boyu ve karşı yüz numuneyle onaylanmalıdır. 3D gövde yüksekliği nominal zarftır; üretici STEP modeli değildir.

Çizimde 36 V DC, 30 mΩ maks kontak direnci, 5 A / 1 A, 20.000 çevrim, 1,0 mm çalışma stroku, tam strokta 60 g ±20% yay kuvveti, PA46 gövde ve N52 mıknatıs bilgileri vardır. 5 A büyük dış, 1 A küçük iç kontak yorumunun satıcıdan yazılı teyidi gereklidir. Bataryanın sabit kontakları yaylı değildir; kuvvet ve strok cihazdaki yaylı karşılık içindir. Dört yay için nominal toplam kuvvet yaklaşık 2,35 N (toleransla yaklaşık 1,88–2,82 N); mıknatıs tutma kuvveti bu çizimde verilmemiştir. Bu hesap tam strok verisidir; seçilecek çalışma sıkışmasındaki kuvvet doğrulanmamıştır.

Ana ve yardımcı kontağın her biri 30 mΩ kabul edilirse, R40 ile pozitif kollarda yaklaşık 1,625 A / 0,375 A paylaşım oluşur (F2 ve PCB direnci hariç). Negatif tek kontak tüm 2 A'i taşır. Kontaklar+R40 üzerinde yaklaşık 0,218 W/0,109 V hesaplanır. Bunlar numune ölçümü değildir. İki pozitif, 10 A paket anlamına gelmez. F2'nin açma süresindeki geçici küçük-kontak yükü, eşzamanlı temas, ilk-son temas, bounce ve ESD ayrıca denenmelidir.

## Mekanik ve montaj

Referans eksenler: PCB alt-sol köşe X=0/Y=0, X=74 uzunluk, Y=42 genişlik, Z yukarı. Hücreler X=4,4…69,6; merkezler Y=11 ve 31, Z=10,7; nominal Ø18,6 ×65,2 mm. Hücreler arası yüzey boşluğu 1,4 mm; hücre tepesi Z=20,0; PCB altı Z=23,0. Ölçüler bilinmeyen hücreye göre varsayımdır. Korumalı/uzun 18650 hücreye uygunluk iddia edilmez.

Taşıyıcı alt taban 1,2 mm, yan/end destekleri, uç havalandırma açıklıkları ve orta ayırıcı içerir. İki yalıtkan bant ve uyumlu ped hücreleri tutar; dört M2 PCB desteği ve konnektör altında iki ek yük köprüsü vardır. Dock kulakları aday M1.6 vidalarla yükü taşıyıcıya iletir; lehim bağlantıları yapısal tutucu değildir. Sıkma torku, insert/vida boyu ve polimer sürünmesi hesaplanıp numunede doğrulanacaktır. PA66-GF bir malzeme adayıdır; alev, sterilizasyon/temizlik ve uzun dönem koşulları için ürün şartnamesi gerekir.

0,4 mm yalıtım bariyeri, hücre pozitif uç halkaları, nikel kaplamaları, sensör izolasyonu ve tüm keskin kenarlar için koruma gerekir. Bariyerde tab geçiş boşlukları nominal modellenmiştir; boşluklar montajda yalıtkan manşon/üst filmle kapatılacaktır. Hücre emniyet ventleri kapatılmaz; bantlar hücre kılıfını ezmez. Kablo/nikel mekanik yükü taşıyıcıdaki tutucularla alınır. Nikel yolları ve lehim tabları şekillendirilmiş nominal geometridir; tam büküm/kalıp ve üretim tolerans çizimi değildir.

Hücreye saf nikel şerit punta kaynak yapılır. PCB'ye punta kaynak yapılmaz. PCB terminalinde fabrikada ön kalaylanmış, daraltılmış 2,5 mm dil içeren şekillendirilmiş tab ve mevcut 3 mm PTH lehim bağlantısı aday yöntemdir. B+ ve B− karşı uçlardan, B1 seri köprüden ilgili pad'e gider. Ön kalaylama ısısı hücreden uzakta uygulanır; nihai kaynak/lehim sırası, ısı emici, ıslatma, yalıtım ve gerilim alma proses kuponlarıyla doğrulanmalıdır. Kaynak sırasında hücre kısa devresi ve canlı pakette ardışık bağlantı riski için üretim fikstürü gerekir. Nikel saf/kaplı çelik ayrımı, punta parametreleri ve çekme mukavemeti tedarikçiye bağlıdır.

Cihazdaki yaylı karşılığın CAD'i ve muhafaza ölçüleri verilmedi. Gömülme/sıkışma, kılavuz boşlukları ve mekanik polarizasyon kesinleştirilmemiştir. N/S mıknatıs yönü tek başına ters takmayı güvenli biçimde önleyen mekanik anahtar sayılmamalıdır. Asimetrik kılavuz, kısa devre yapmayan karşı kontak yüzeyi ve parmak/metal parça erişimi cihaz tasarımına eklenecektir.

## Tasarımcı için öncelikli kapatma listesi

1. Dolu orijinal şema veya bu bağlantı geri kazanımının IC veri sayfalarıyla pin pin teyidi; U1/U2/MOSFET/fuse land-pattern'leri ve EP ağları.
2. Kesin hücre modeli, 2 A sürekli ve motor tepe/stall akımı, şarj akımı/algoritması, kullanım sıcaklığı ve ömür/kapasite koşulları.
3. BQ28Z610 Data Flash/kimya/kalibrasyon/koruma eşikleri; hücre dengesinin izlenmesi, ikincil koruma ve tetiklemeli sigorta fonksiyonu.
4. Host NTC topolojisi ve sensör B/toleransı; konnektör kesin pin/akım/kuvvet/ölçü ve numune teyidi; F1/F2 tam parça ve DC kesme/I²t seçimi.
5. Tolerans zinciri, ters takmayı önleyen mekanik anahtar, nikel/termistör izolasyonu, tab manşonları, vidalama, şok/titreşim, vent ve taşıyıcı yükleri.
6. Akım sınırlı ilk devreye alma; hücre bazlı gerilim, şarj/deşarj, OV/UV/OC/SC ve sıcaklık kesmeleri, 2 A ve tepe akımda termal ölçüm, temas direnci/çevrim, tek kontak açık/kısa arızası ve bağlantı sırası deneyleri.
7. İnfüzyon pompasında düşük pil/kontak kaybı alarmı, güç geçişi, tedavi sırasında kesintinin cihaz seviyesindeki güvenli davranışı ve medikal ürün doğrulama kapsamı. Bu ön tasarım hasta kullanımına serbest bırakılmaz.
