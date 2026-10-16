# STM32F469 / DISEN — Rev I, Layout 1

Mevcut Rev I şematiğinin yalnızca yerleşim ve sunum düzenlemesidir.

## Açılış

KiCad 9 ile `STM32F469_DISEN_RevI.kicad_pro` dosyasını açın, ardından ana şematiği açın. Tüm proje klasörünü birlikte tutun; sembol ve footprint kütüphaneleri proje içindedir.

Şematik üç A3 sayfadan oluşur:

1. **MIPI ve LCD arayüzü:** STM32 CN10 bağlantısı, DSI pin eşleme tablosu, LCD konnektörü, reset pull-up/seri dirençleri ve TE hattı.
2. **Mantık beslemesi ve dokunmatik:** STM32 CN12 ve CN2 bağlantıları, ayrı LCD/touch beslemeleri, hizalı bypass kapasitörleri, DNP I2C pull-up dirençleri ve mantık test noktaları.
3. **Backlight:** harici 5 V girişi, sigorta/ters polarite bloğu, boost güç akışı, LED akım dönüşü, OVP komparatörü, PWM kontrolü ve backlight test noktaları.

## Dosyalar

- `PDF/STM32F469_RevI_Professional.pdf`: üç sayfalı renkli, beyaz zeminli vektör PDF. Hiyerarşik sayfa bağlantıları ve komponent özellikleri PDF içinde korunur.
- `PDF/STM32F469_RevI_Print.pdf`: siyah-beyaz baskı sürümü.
- `SVG/`: her sayfanın ayrı vektör çıktısı.
- `Verification/`: ERC raporları, özgün ve düzenlenmiş netlistler, bağlantı karşılaştırması ve pin/net eşleme dökümü.
- `Kaynak_Notlari/`: arşivdeki özgün mühendislik notları ve BOM. Bu dosyalar kaynak bilgi olarak değiştirilmeden tutulmuştur; eski sayfa numaraları ve dosya atıfları yeni yerleşimi temsil etmez.

## Düzenleme

Fonksiyonel bloklar çerçevelenmiş ve numaralandırılmıştır. Referans/değer alanları yatay ve hizalıdır. Güç girişi ve boost akışı soldan sağa, bypass ve akım dönüşleri yukarıdan aşağı gösterilir. Reset ve güç filtreleme bağlantıları doğrudan kablolanmış, sayfalar arası sinyaller özgün global net adlarıyla korunmuştur. Elektriksel bağlantı uçları KiCad 50 mil ızgarasına hizalanmıştır.

Standart KiCad GND sembolü, projenin taşınabilirliği için mevcut yerel `Adapter_F469` kütüphanesine `GND` adıyla eklenmiştir. Yeni GND sembolleri yalnızca mevcut GND netini gösterir; fiziksel komponent veya yeni elektriksel ağ eklemez.

Elektriksel revizyon **I** olarak kalır. `Layout 1` yalnızca sunum sürümüdür. Kaynak arşiv ve özgün dosyalar değiştirilmemiştir.

## Doğrulama — KiCad CLI 9.0.2

| Kontrol | Sonuç |
| --- | --- |
| Fiziksel/BOM komponentleri | 49 → 49 |
| Referans, değer, footprint, MPN ve diğer alan değerleri | Aynı |
| DNP durumları | R1/R2 aynı |
| Özgün sembol tanımları | Aynı |
| Özgün komponent ve pin UUID'leri | Korundu |
| Özgün power flag sembolleri | 3 adet korundu |
| Sunum için eklenen GND sembolleri | 12; hepsi mevcut GND netinde |
| Global net adları ve bağlı pin kümeleri | 57/57 aynı |
| Gerçek bağlı isimli netler | 32 |
| Bağlantısız pin netleri / NC işaretleri | 25 / 25, aynı |
| Karşılaştırılan pin/net üyeliği | 172, aynı |
| Footprint dosyaları ve proje ayarları | Aynı |
| ERC, kaynak | 0 ihlal |
| ERC, düzenlenmiş proje | 0 hata / 0 uyarı |

Karşılaştırma, her netin adını ve `(referans, pin numarası)` kümesini eşleştirir. Eklenen GND sembollerinin sadece GND'ye bağlı olduğu ayrıca denetlenmiştir. Sayfa yerleşimleri ve hiyerarşi yolları değiştiği için netlistlerin dosya hash'leri karşılaştırılmaz; elektriksel içerikleri karşılaştırılır.

Bu çalışma şematik bağlantı eşdeğerliğini ve belge tutarlılığını doğrular. Kaynak Rev I notlarında bulunan prototip, güç bütçesi, FPC yönü, LED akımı ve OVP ölçüm gereksinimleri aynen geçerlidir; yeni donanım/simülasyon doğrulaması yapılmamıştır.
