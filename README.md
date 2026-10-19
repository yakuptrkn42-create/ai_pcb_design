# STM32F469I-DISCO / DISEN — Tek LCD PCB hazırlığı

**Güncel çalışma: DS070HSD39T-132 için Rev J / PCB Hazırlık 1.** Yüklenen eski Rev J esas alındı; çift LCD Rev K ayrı korunuyor.

- [Tek LCD hazırlık teslimatı — ZIP](STM32F469_DISEN_RevJ_PCBPrep1.zip)
- [KiCad proje ve kütüphaneleri](SingleLCD_RevJ_PCBPrep/Project/)
- [Doğrulama raporu — PDF](SingleLCD_RevJ_PCBPrep/PDF/Validation_RevJ_Prep1_TR.pdf)
- [Şematik — PDF](SingleLCD_RevJ_PCBPrep/PDF/STM32F469_DISEN_RevJ_Prep1.pdf)
- [Açılış ve kapsam](SingleLCD_RevJ_PCBPrep/README_TR.md)

49 footprint, 57 net ve 49 model bağı; 172 pin/net kontrolü; şema–PCB parity **0 fark**, ERC **0 hata / 3 açıklanmış uyarı**. Elektriksel bağlantılar ve değerler Rev J ile aynıdır. 4 katmanlı nominal stackup ve routing kuralları kaydedildi.

**Yerleşim henüz yapılmadı:** komponentler başlangıç aktarımı olarak (0,0)'da üst üste durur. Kart sınırı, iz, via ve dolgu yoktur. Bu aşamanın DRC çakışmaları gizlenmeden paketlendi; üretim kabulü verilmedi. FPC ve endüktör modelleri nominaldir; exact mekanik/panel/OVP ve üretici stackup koşulları raporda açıktır. Model kontrol panosu görüntüleri adaptör yerleşimi değildir.

ZIP'i tamamen çıkarıp `SingleLCD_RevJ_PCBPrep/Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını KiCad 9 ile açın. GitHub ZIP sayfasındaki **Download raw file** düğmesiyle indirebilirsiniz.

# Korunan çift LCD çalışması — Rev K

**Güncel teslim: ortak 39 pinli donanım ve seçilebilir backlight OVP şematiği.** LCD-A: DS070HSD39T-132; LCD-B: DS0700BOE1A39CO-0180A.

- [Tüm Rev K dosyaları — ZIP](STM32F469_DISEN_RevK_DualLCD_Review.zip)
- [Gerçek şematik, 4 sayfa — PDF](Schematic_RevK_DualLCD/PDF/STM32F469_DISEN_RevK_DualLCD.pdf)
- [Türkçe mühendislik incelemesi — PDF](Schematic_RevK_DualLCD/PDF/Dual_LCD_Engineering_Review_TR.pdf)
- [Açılış, karşılaştırma ve montaj tablosu](Schematic_RevK_DualLCD/README_TR.md)
- [Native KiCad projesi](Schematic_RevK_DualLCD/Project/) · [BOM](Schematic_RevK_DualLCD/BOM/BOM_RevK_FACTORY_HOLD.csv) · [ERC](Schematic_RevK_DualLCD/Verification/ERC_RevK.txt)

**Yeni LCD için yalnızca mekanik çizim mevcut; tam elektriksel uyumluluk onayı verilmedi.** VCI/VDD gerilim aralıkları ve maksimum LED değerleri eksiktir. Varsayılan R4/R23 DNP montajı bir onay bekletme durumudur; tam izolasyon değildir. Panel-B, eksik veriler kapanmadan bağlanıp enerjilendirilmemelidir.

R7 her iki panel için 5,23 Ω / nominal 38,24 mA kaldı. JP1 yalnızca OVP eşiğini seçer: A 2–3 HIGH ≈28,69 V; B 1–2 LOW ≈14,94 V (geçici aday). MIPI yollarına anahtar eklenmedi. ERC: **0 hata / 3 açıklanmış uyarı**; kurallar değiştirilmedi. PCB ve yazılım bu aşamada değiştirilmedi. Eski PCB'ler yeni dört footprint ve bağlantılar için ECO gerektirir.

ZIP'i tamamen çıkarıp `Schematic_RevK_DualLCD/Project/STM32F469_DISEN_RevK.kicad_pro` dosyasını KiCad 9 ile açın. GitHub ZIP sayfasındaki **Download raw file** düğmesi dosyayı indirir. Yüklenen Rev J arşivi teslimin Original klasöründe aynen korunmuştur.

![Native konfigürasyon ve koşullar sayfası](Schematic_RevK_DualLCD/Views/04_RevK_Schematic.png)

## Korunan önceki teslimler

- [Rev J şematik ZIP](STM32F469_DISEN_RevJ_Schematic_Review.zip) · [Rev J incelemesi](Schematic_RevJ_Review/README_TR.md)
- [Rev I routing ZIP](STM32F469_RevI_Routed_Review.zip) · [Routing incelemesi](PCB_Routing_Review/Routing_Review_TR.pdf)
- [Rev I placement](PCB_Placement_Review/Placement_Review.pdf) · [Placement ZIP](STM32F469_RevI_Placement_Review.zip)
- [Rev I şematik PDF](STM32F469_RevI_Professional.pdf) · [Şematik KiCad arşivi](STM32F469_RevI_Professional_KiCad.zip)

Tarihsel dosyalar değiştirilmedi; Rev K'nin yeni devresini içermezler. Önceki Gerber'ler Rev K üretim çıktısı değildir.
