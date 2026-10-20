# Rev J / Placement P2 — DS070HSD39T-132

20 Ekim 2026 · Bağımsız, kablolu laboratuvar adaptörü · KiCad 9.0.2.

ZIP'i tamamen çıkarıp `Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını açın. Dosya kökü, mevcut üç sayfalı projenin hiyerarşi/PCB yollarını korumak için değiştirilmedi; başlıklar **J / Placement P2** oldu.

**55 × 45 mm, R2 köşeler, nominal 1,6 mm / 4 bakır katman.** Kullanıcının eklediği dört Ø3,5 mm NPTH delik korundu; her biri için Ø8 mm montaj donanımı alanı ayrıldı. 49 devre referansı üst yüzde. Üç yerleşim yaklaşımı incelendi; iki DSI konnektörünün ortak kenarda olduğu seçenek uygulandı.

**0 iz / 0 via / 0 zone.** ERC 0 hata / 3 mevcut tekil global label uyarısı; fiziksel DRC 0 ihlal; şema–PCB karşılaştırması 0 fark. Routing yapılmadığından 115 bağlantısız öğe kaydı açık ve hata seviyesindedir; bu sayı bağlantısız net sayısı değildir. Kural veya uyarı gizlenmedi.

Yüklenen Project.zip temel alındı; elektriksel bağlantılar, 44 net ve 159 numaralı pin–net üyeliği aynen korundu. J4'ün üç pinli kontrol bağlantısı ve J6'nın JST güç girişi kaynakta zaten vardı. Hatalı J6 polarite açıklaması **1=+5V / 2=GND** olarak düzeltildi. J4'ün eski 2×8 soket adı gerçek **1=PC6 PWM / 2=PB12 touch reset / 3=GND** bağlantısını anlatacak şekilde düzeltildi. CN12 tarafı sırasıyla 6/12/2 pinleridir; J4, CN12'ye 1:1 takılan bir soket değildir.

- `PDF/Placement_P2_Review_TR.pdf`: kısa değerlendirme ve PCB görselleri.
- `PDF/STM32F469_DISEN_RevJ_Placement_P2.pdf`: güncel üç sayfalı şematik.
- `Views`: üst/alt 2D, gerçek KiCad 3D çıktıları, mekanik koridorlar ve alternatif karşılaştırması.
- `Engineering`: değişiklikler, kritik bağlantı tablosu, stackup/kurallar ve açık doğrulama koşulları.
- `Verification`: ERC/DRC, pin–net karşılaştırması, 3D model ve taşınabilirlik kontrolleri.
- `BOM/BOM_P2.csv`: güncel referans listesi; R1/R2 DNP. Test noktaları çıplak bakırdır, satın alınacak parça değildir.
- `Original/Submitted_Project.zip`: yüklenen orijinal dosyanın aynısı; yedekleriyle korunmuştur.

Üretici stackup'ı, exact FPC temas/latch/kablo uyumu ve bazı komponent/panel verileri henüz kesinleşmedi. GND referans katmanları planlandı; henüz GND dolgusu yok. Native 3D çıktısı R1/R2'nin DNP modellerini de gösterebilir; montaj kararı şematik/BOM ve DNP işaretli assembly çizimidir. FPC ve JST modeliyle fiziksel uyum garantisi verilmez. Bu paket üretim dosyası değildir. **Routing yalnızca ayrı onayınızdan sonra başlayabilir.**
