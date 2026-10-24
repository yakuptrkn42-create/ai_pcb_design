# AİES kalp anatomi eğitim cihazı — video kaydı ve bağlantı önerisi

**İki ayrı, düzenlenebilir KiCad projesi teslim edildi.** Videodaki gözlemler ile mühendislik seçimleri ayrıdır. Kod olmadığı ve seçim yapmama izin verildiği için, eksik GPIO/adres/LED sırası için ayrıca **P1 bağlantı önerisi** hazırlandı.

## Hangi projeyi açmalıyım?

ZIP'in tamamını çıkarıp KiCad 9 ile aç:

- **Bağlantı önerisi:** `Proposal/Project/AIES_Oneri_P1.kicad_pro`. Kullanabileceğin bağlantı planı burada. ERC **0 hata / 0 uyarı**; 157 pin–net eşlemesi ve 12 kritik yol kontrol edildi. Exact modül ve güç doğrulamaları açık olduğu için üretime hazır değildir.
- **Videodan mevcut kayıt:** `Project/AIES_Video_Review_R1.kicad_pro`. 14 gözlem referansı, 68 ayrı belirsiz terminal neti ve 76 açık ERC bulgusu var. Kablo uçları/GPIO görünmediği için mevcut devre tamamen çözülemedi; belirsizlikler saklanmadı. Bu projede No Connect kullanılmadı.

Her proje 7 sayfadır: sistem genel görünümü; güç/ESP32; dokunma/elektrot; ekran/LED/ses; paylaştığın üç görselin düzenlenebilir KiCad blok karşılıkları. Son üç sayfadaki kutu/ok/yazılar resim olarak gömülü değildir.

**G3 güç sayfası önceki görsel fikridir.** Oradaki ayrı 3.3 V regülatör P1 devresine eklenmedi; P1'de DevKit'in regülatörü kullanıldı. Bu fark sayfa üzerinde de yazılıdır.

## P1'de seçilen bağlantılar

GPIO21=SDA, GPIO22=SCL, GPIO18=LED verisi, GPIO17=ses TX, GPIO16=ses RX; GPIO27/26/25 üç ayrı dokunma IRQ hattıdır. MPR121 adresleri 0x5A/0x5B/0x5C, LED sırası 1→2→3 olarak önerildi. Bunlar videodaki gerçek kablolama diye sunulmadı. **Yeni GPIO/adres/LED sırası ve BLE seçimi için firmware uyarlaması gerekir; kartta yüklü mevcut yazılımın bu seçimlerle uyumu bilinmiyor.** Bu teslimatta firmware geliştirilmedi.

Hedef profil klasik ESP32-WROOM DevKit, 3.3 V dokunma/I²C OLED, 5 V WS2812 uyumlu RGB ve 3.3 V TTL seri ses modülüdür. S3/C3/WROVER veya başka modüllere aynı pin tablosu doğrudan uygulanmaz. Modüllerin fiziksel header numaraları ve footprint'leri uydurulmadı; pin kimlikleri işlevseldir. Seçilen AHCT entegresinde 5 pinli DBV haritası ayrıca CAD kaynağıyla kontrol edildi.

Özel semboller proje klasöründe `${KIPRJMOD}` yolu ile bulunur, şematiklere de gömülüdür. Başka bilgisayarda kişisel kütüphane gerekmez. İki proje temiz KiCad ayarlarıyla başka klasöre kopyalanıp kontrol edildi. PCB, simülasyon veya firmware oluşturulmadı.

## Dosyalar

- `PDF/AIES_Oneri_P1.pdf`: 7 sayfalı bağlantı önerisi.
- `PDF/AIES_Video_Review_R1.pdf`: 7 sayfalı gözlem kaydı.
- `PDF/Inceleme_Raporu_TR.pdf`: bulgular, sınırlar ve yakın görüntüler.
- `Review/`: zaman/kesinlik tablosu, iki parça listesi, iki GPIO tablosu, elektrot/LED öneri haritaları ve açık koşullar.
- `Evidence/`: 74 karenin zaman indeksi, 5 temas sayfası, seçili orijinal kareler/kırpmalar. Büyütmede eksik detay üretilmedi. MP4/WAV pakete eklenmedi; kaynak SHA kaydedildi.
- `References/`: üretici ses kılavuzu, kaynaklar ve erişim sınırları.
- `Verification/`: native ERC/netlist ve taşınabilir açılış sonuçları.

## İnceleme sınırı

Küçük videonun 148.89 saniyesi 2 saniye aralıklı karelerle tarandı; seçili yakın kareler incelendi. 480×848 görüntüde örtülü kablo/GPIO uçları okunamadı. Ses izi çıkarıldı ama yerel deşifre modeli indirilemedi; konuşma değerlendirilmedi. Büyük ilk video 32 MiB aktarım sınırını aştı. AİES Rev A dosyaları gelmedi.

LED'lerde **24 görünür gövde** sayıldı; IC tipi/azami akımı, kaynak kapasitesi ve hoparlör Ω/W değeri bilinmiyor. Önerideki 4 A bütçesi koşulludur. USB + harici kaynak birlikte kullanımında JP101 tek başına bütün geri besleme sorunlarını çözmez; exact DevKit güç şeması ve test kapanmadan bu kullanım onaylanmadı. Ayrıntılar `Review/Eksik_Bilgiler_ve_Kabul_Kosullari_TR.md` içindedir.

## Sade çalışma mantığı

**Dokununca ne oluyor?** Dokunma modülü elektrottaki kapasitans değişimini algılar. ESP32 hangi kanala dokunulduğunu okur, çalışma moduna göre karşılığını seçer.

**ESP32 ne söylüyor?** LED'lere renk bilgisini, ses modülüne kayıt numarasını, ekrana da gösterilecek bilgiyi gönderir. Telefon mod seçimi içindir; P1'de BLE önerildi, yazılım yazılmadı. Videodaki telefon protokolü belirlenemedi.

**Güç nereden gidiyor?** P1'de harici 4.8–5.0 V, LED/ses tarafını ve JP101 üzerinden DevKit'i besler. DevKit'in 3.3 V çıkışı dokunma/OLED tarafına gider. Bütün GND'ler öneride ortak referanstır; bu, videonun görünmeyen GND kablolarının doğrulandığı anlamına gelmez.
