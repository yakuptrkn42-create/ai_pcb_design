# İlk DISEN LCD — Rev J / PCB Hazırlık 1

Yalnızca **DS070HSD39T-132** için, yüklediğiniz Rev J'den ayrı kaydedilen KiCad 9 projesi. Çift LCD Rev K korunmuştur.

ZIP'i tamamen çıkarın; `Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını açın. Şematik üç sayfadır. Aynı adlı PCB dosyasında 49 footprint / 57 net aktarılmıştır. Şematikle pin–net veya değer farkı yoktur. Kütüphane ve 3D dosyaları proje içindedir; dış model kurulumu gerekmez.

**Henüz yerleşim yapılmadı.** PCB'yi açtığınızda bütün komponentlerin (0,0) noktasında üst üste görünmesi başlangıç aktarımıdır. Kart sınırı ve boyutu belirlenmedi; iz, via ve dolgu yoktur. Yerleşim aşamasında kart sınırını belirleyip komponentleri dağıtın. Görsel kontrol panosu görüntülerini adaptör yerleşimi olarak kullanmayın.

- `PDF/STM32F469_DISEN_RevJ_Prep1.pdf`: gerçek şematik çıktısı.
- `PDF/Validation_RevJ_Prep1_TR.pdf`: kontrol sonucu, kurallar ve açık doğrulama koşulları.
- `Engineering/VALIDATION_TR.md`: aynı raporun okunabilir kaynağı.
- `BOM/BOM_RevJ_Prep1.csv`: 49 referans, DNP R1/R2, modeller ve satın alınmayacak çıplak test pad'leri.
- `Verification`: ERC, ham yerleşimsiz DRC, 0 fark parity, 172 pin/net, footprint/model/net class ve elektriksel eşdeğerlik kontrolleri; nominal empedans ve akım hesapları.
- `Project/3D/SOURCES.json`: nominal modellerin kaynak/ölçü/sınırları. Konnektör ve endüktör STEP'leri üretici CAD'i değildir.
- `Views/3D_Model_Library_Validation_ONLY.png` ve `KiCad_3D_Viewer_ModelAudit.png`: ayrı geçici model kontrol panosu. **Adaptör placement tasarımı değildir.**
- `Original/Submitted_Schematic_RevJ_Review.zip`: yüklediğiniz orijinal ZIP, byte düzeyinde korunur. İçindeki eski autosave PCB aktif projenin parçası değildir.

ERC **0 hata / 3 açıklanmış uyarı**; şema–PCB native parity **0 fark**. Başlangıç yığınının fiziksel DRC çakışmaları beklenir ve raporda gizlenmeden bulunur; bu aşama üretim kabulü değildir. Nominal 4 katman / 1,6 mm stackup ve 100 Ω hedefi üretici onayı bekler. Host CN2/FPC fiziksel eşleşmesi, OVP, panel akım/gerilim ayrıntıları ve parça tedarik koşulları raporda açıktır. Laboratuvar donanım testi yapılmadı.
