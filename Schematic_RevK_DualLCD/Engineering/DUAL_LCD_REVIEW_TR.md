# Rev K — Çift LCD uyumluluğu ve şematik ECO

19 Ekim 2026. Uygulanan kapsam: şematik, yerel sembol/footprint tanımları, donanım konfigürasyonu ve doğrulama raporları. PCB routing ve firmware yoktur. **LCD-B, yalnızca mekanik çizimle belgelenmiştir; bu teslim elektriksel uyumluluk/üretim onayı değildir.**

## 1. Uygulanabilirlik kararı

İki panelin ortak adaptör kullanması pin dizilimi açısından mümkündür: tek 39 pin J2, aynı iki DSI veri lane'i ve saat çifti, aynı reset/TE ve touch sinyal konumları kullanılır. Anahtarlı MIPI yolu, ikinci paralel LCD konnektörü ve DSI stub'u eklenmedi. Her defasında yalnızca bir LCD, bütün kaynaklar kapalıyken takılır.

Farklı seri LED sayıları ortak sabit akımlı boost sürücüyle karşılanabilir. İki belgede de IF=40 mA verildiğinden nominal 38,24 mA ayarı korunur. Çıkış gerilimini LED dizisinin gerektirdiği gerilim belirler; seçim eşiği OVP'dir. Yeni panelin VCI/VDD aralıkları ve maksimum LED gerilimi verilmediği için **tam ortak donanım uyumluluğu koşulludur**. Üretici farklı besleme isterse mevcut linkler kapatılmaz; regülatör/besleme ve gerekirse sinyal seviye uyumu yeniden değerlendirilir.

## 2. Belge karşılaştırması

| Özellik | A — DS070HSD39T-132 | B — DS0700BOE1A39CO-0180A |
|---|---|---|
| Kaynak | 20 sayfa A0 preliminary, 10.06.2025; mekanik A00, 17.06.2024 | Tek sayfa mekanik, A01, 14.09.2026 |
| LCD / touch IC | OTA7290B / ILI2130 | JD9365DA-H3 / GT911 |
| Görüntü | 280×1424, 33,60×170,88 mm aktif alan | Aynı çözünürlük ve aktif alan |
| DSI +/− pinleri | D0 16/17; D1 20/21; CLK 24/25 | Aynı numaralar ve polariteler |
| LED çizimi | 8S2P, toplam 16 LED | 4S2P, toplam 8 LED |
| LED VF / IF | 21,6–27,2 V / 40 mA tipik | VF=12 V, IF=40 mA yazıyor; min/max yok |
| VCI, 7–10 | 3,0–3,6 V belgeli | İsim var, gerilim aralığı yok |
| VDD, 30–31 | A elektriksel tablosunda touch VDD | VDD etiketi var; işlev ve aralık belirsiz |
| Touch çalışma gerilimi | Çizimde 2,8–3,3 V | Çizimde 2,8–3,3 V |
| Ayrı touch tail, 1→6 | GND, SCL, SDA, RST, INT, 3V3 | Aynı |
| Lens / toplam kalınlık | 48,25×216,54 / 5,39 mm nominal | 56,95×216,46 / 5,20 mm nominal |

İki panelin ayrı 6 pin touch tail'i aynı sıralıdır. **Host J3 bununla aynı değildir:** J3.1=3V3, J3.6=GND. Panel tail'i buraya doğrudan takılırsa güç pinleri ters eşleşir. J3 host girişidir; panelin touch bağlantıları J2.32–35 üzerinden, modülün iç bağlantısı doğrulandıktan sonra kullanılır. Bu ayrım şematiğe de yazıldı.

FPC uç çizimlerinde 39 kontak, 0,30 mm adım ve yaklaşık 0,20 mm uç kalınlığı gibi nominal ortaklıklar görülür. A belgesi FH26-39S-0.3SHW önerir; B çizimi exact konnektör MPN'si vermez. FH26 footprint'i korunur; bu, B'nin kontak yüzü, kilit geometrisi ve gerçek takılabilirliğinin fiziksel onayı değildir. Lens genişliği farklıdır; ortak adaptör aynı kasa/montaj uyumu anlamına gelmez.

## 3. Ortak backlight ve seçim devresi

U1 TPS61165, 22 µH L1, SS16 D1 ve mevcut giriş/çıkış kondansatörleri korundu. İki panel de 5 V'tan daha yüksek LED gerilimi gerektirdiğinden boost topolojisi uygundur. Sabit R7=5,23 Ω ±%1 ile nominal akım 0,200/5,23=38,241 mA'dır. TI FB=196–204 mV ve R7 toleransıyla yaklaşık 37,10–39,40 mA çıkar. İki paralel kol bulunması toplam hedefi kendiliğinden 80 mA yapmaz. Çizimdeki IF=40 mA modül toplamı olarak yorumlandı; özellikle B için üretici teyidi gerekir. İki kola tam eşit akım dağılımı garanti edilmez.

R19=221 kΩ ±%0,1 üst kol olarak korundu. Alt kola R22=30,0 kΩ kalıcı bağlandı; JP1 iki ek alt dirençten birini GND'ye bağlar:

| JP1 | Gerçek alt kol | Nominal OVP, Vref=1,242 V |
|---|---|---|
| 2–3 HIGH / A | R22 30k ∥ R20 15k = 10k | 28,690 V — Rev J nominal oranıyla aynı |
| 1–2 LOW / B | R22 30k ∥ R21 60,4k = 20,044k | 14,936 V — geçici aday ayar |
| Shunt yok | R22 30k | 10,391 V düşük eşikli geri dönüş |
| Üç pin birlikte kısa devre | Geçersiz | Nominal 33,235 V; izin verilen montaj değildir |

Bir adet iki pinli, 2,54 mm shunt kullanılır. Normal iki seçim fiziksel olarak aynı orta pini paylaşır; aynı anda iki standart shunt takılmaz. Shunt montajı enerjisiz yapılır. Direnç ağı ve fiziksel JP1 pinleri gerçek XML netlist'ten alınarak nodal analizle çözüldü; sadece çizimdeki formül kopyalanmadı.

Kalıcı R22, shunt çıkarıldığında sense girişinin açık kalmasını önler. **Shunt yokluğu bir enable interlock değildir:** sürücü alt eşikte çalışmaya/hiccup yapmaya çalışabilir, çıkış da girişten endüktör/diyot üzerinden beslenebilir. Bu durum tam OFF veya sıfır volt çıkış garantisi sağlamaz.

TPS61165 CTRL'nin filtre ve shutdown gecikmeleri nedeniyle U2 bir sert gerilim kelepçesi değildir. LOW=14,936 V, yalnızca 12 V tipik bilgisine göre seçilmiş laboratuvar aday eşiğidir; bilinmeyen maksimum VF, mutlak LED sınırı, referans/offset/histerezis toleransı ve geçici rejim dahil edilmeden güvenli üst sınır kabul edilmez. Hesap dosyasındaki direnç tolerans sınırları sadece ±%0,1 dirençleri kapsar; tam OVP garantisi değildir. U2 exact TI limitleri/başlangıcı ve gerçek peak ölçümleri Rev J'den taşınan açık maddelerdir.

Yanlışlıkla HIGH seçilen düşük VF panelde U1 normal koşullarda yine aynı akımı regüle eder; HIGH seçimi 27 V çıkış komutu değildir. Bununla birlikte arıza/açık yük için daha yüksek izin seviyesi oluşur. LOW seçilen yüksek VF panelde erken sınırlama/yanmama beklenir. Sade bir manuel seçim devresi panel kimliğini otomatik algılayamaz; yanlış seçimde her arızaya karşı koruma garantisi verilmez.

Güç kontrolü için örnek varsayımlar: boost girişi 4,2 V, verim %75, Lmin=17,6 µH, fsmin=1 MHz. A maksimum VF ile yaklaşık 1,106 W çıkış / 0,351 A giriş / 0,452 A endüktör tepe akımı; B yalnızca 12 V tipik VF ile yaklaşık 0,486 W / 0,154 A / 0,233 A çıkar. Bu hesaplar ideal boost yaklaşımı ve varsayılan verim içerir; ölçülmüş sıcaklık/verim kanıtı değildir. Her ikisi normal yükte TI minimum switch limitinin altında görünür. C3'ün yüksek gerilimde etkin kapasitesi, L1 tedarik/derating'i ve F2 sıcaklık derating'i önceki incelemedeki koşullarla korunur.

## 4. Besleme onayı ve varsayılan montaj

R4 mevcut VCI bağlantısıdır. Varsayılan montajda DNP yapıldı. Yeni R23, J2.30/31 için ayrı `PANEL_VDD_30_31` netini `TP_VDD`'ye bağlayacak 0 Ω onay bağlantısıdır; varsayılan DNP'dir. R5 ve touch kontrol/pull-up alanı ayrı `TP_VDD` adıyla korunur. C7/C8, R23'ün yük tarafındaki panel rayına alındı. Panel gerilimi bu kondansatörlerin pozitif uçlarında ölçülür; TP12 bağlantı öncesindeki kaynak tarafında kalır. J2 pin isimleri belirsizliği göstermek için VDD_CHECK olarak güncellendi; pin numarası değişmedi.

A için belgelenmiş 3,3 V raylar ve host akım bütçesi gözden geçirilerek R4/R23 takılabilir; KiCad DNP işaretleri de bu montaj varyantında kaldırılmalıdır. B'de VCI ve VDD30/31 aralıkları/işlevi üretici tarafından onaylanmadan bu linkler kapatılmaz ve panel bağlanıp enerjilendirilmez. Birbirinden farklı çıkabilecek raylar aynı global güç sembolü altında birleştirilmedi.

**DNP linkler tam izolasyon değildir.** Reset/I²C/DSI/TE/INT ve LEDA bağlantıları kalabilir; beslemesiz panele bu yollardan geri besleme oluşabilir. FACTORY HOLD ile panel kullanımı yapılmaz. Önce montaj koşulları kapatılır, ardından bütün kaynaklar kapalıyken kablolar bağlanır. Bu konfigürasyon bir otomatik yanlış-panel koruma sistemi değildir.

GT911 ile ILI2130'un başlangıç, adres, reset ve INT davranışları aynı kabul edilmedi. Mevcut PB12 reset ve PJ5 INT bağlantıları korundu; GT911 başlangıcında INT'nin host tarafından sürülebilmesi ve ilgili zamanlamalar ayrıca incelenmelidir. I²C pull-up seçenekleri R1/R2 DNP kalır; gerçek host pull-up popülasyonu ve yükselme süreleri kontrol edilir. LCD kontrolcüsü de değişir; model başlatma ayarlarının ayrıca ele alınması gerekir. Bu teslimde yazılım geliştirilmedi.

## 5. Uygulanan ECO ve doğrulama

- 49 mevcut fiziksel komponent korundu; R21/R22/R23/JP1 eklendi: toplam 53. Mevcut footprint atamalarının tamamı korundu; yeni parçalar yerel footprint'lere atanmıştır.
- R20 10k → 15k; R4 0 Ω değeri korunarak DNP yapıldı. R7 ve boost güç katının değerleri değiştirilmedi.
- Beş mevcut pin-net değişikliği: R20.2 GND → OVP_SEL_HIGH; J2.30/.31 ve C7.1/C8.1 TP_VDD → PANEL_VDD_30_31. Diğer mevcut fiziksel pinler korunur; altı MIPI yolu ve J1/J3/J5 bağlantıları değişmez.
- 39 panel kontağı iki belgeyle karşılaştırıldı. Bu kontrol pin isim/numarası kontrolüdür; eksik elektriksel gerilim/timing onayı değildir.
- 53 sembolün pin numaraları yerel footprint pad numaralarıyla eşleşti.
- KiCad 9.0.2 ile dört native sayfa yüklenerek netlist/PDF üretildi. PDF sayfaları görsel olarak incelendi. GUI üzerinden etkileşimli açma testi yapılmadı.
- ERC: 0 hata / 3 uyarı. Uyarılar, önceki sürümde de bulunan tekil global BL_SW, BL_COMP, OVP_SENSE etiketleridir. Kural veya exclusion değişikliği yoktur. ERC, shunt/DNP montajını ve gerçek analog davranışı doğrulamaz; PWR_FLAG bildirimleri ilgili güç bağlantıları takılı çalışma durumuna aittir.
- Mevcut PCB düzenlenmedi. R20 bağlantısı, panel VDD ayırımı ve dört yeni footprint için PCB ECO gerekir. Kullanıcı yüklemesindeki autosave PCB ve yedekler Original arşivinde aynen korunur; yeni aktif projeye taşınmadı.

## 6. Kapatılacak kritik bilgiler

1. B'nin VCI7–10 ve VDD30/31 işlevi, min/nom/max gerilimleri, açılış/çalışma akımları ve sıralaması.
2. B LED maksimum VF, mutlak sınırlar ve IF=40 mA toplam modül akımı yorumu. LOW OVP eşiği bundan sonra yeniden kabul edilir/ayarlanır.
3. Her iki panelin gerçek FPC kontak yüzü, mekanik kilit/kalınlık uyumu ve 39 pin touch sinyallerinin iç bağlantısı.
4. LCD/touch kontrolcüleri için reset/başlatma, I²C/INT ve DSI timing bilgileri; B için tam elektriksel doküman.
5. U2 exact birincil veri sayfası kontrolü ve her modda açık yük, yeniden bağlama, güç sırası ve PWM durumlarında OVP tepe ölçümleri. Önce panel yerine uygun dummy LED yüküyle denenmelidir.

Yeni panel için bu bilgiler olmadan PCB tasarımı/üretimi nihai hale getirilmemelidir. Kullanıcıya teslim edilen Rev K, uygulanmış ve denetlenebilir ortak şematik ile açık kalan koşulları birlikte içerir.
