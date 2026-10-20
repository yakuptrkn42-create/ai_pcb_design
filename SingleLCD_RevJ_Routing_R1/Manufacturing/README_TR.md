# CAM teslimi — Rev J / Routing R1

11 adet Gerber X2 + `.gbrjob`; dört bakır, iki mask, iki silk, iki paste ve Edge.Cuts. Excellon PTH/NPTH ayrı; PDF delik haritaları dahildir. **84 via + 5 konnektör PTH = 89 PTH**, ayrıca 4 × Ø3,5 mm NPTH. Bütün drill konum/çapları native PCB ile ±0,0005 mm yuvarlama içinde eşleşti. CAM ve drill ortak sol-alt orijin kullanır; dosyalar aynalanmadı.

Katmanlar sırasıyla F.Cu / In1.Cu GND / In2.Cu GND / B.Cu. Nominal kalınlık 1,6 mm ve nominal bakır 35 µm. Gerber silk, standart mask subtraction ile plotlandı; PCB DRC kontrolleri ve hata seviyeleri korunur. R1/R2 DNP; stencil/paste açıklıkları montajcının DNP tercihiyle değerlendirilmelidir.

Gerber ve drill üretici incelemesi için hazırdır; **stackup, bitmiş geometriler, empedans toleransı ve FPC mekanik/elektrik doğrulamaları kapanmadan kesin üretim kabulü değildir**. İstenen 100 Ω diferansiyel hedefi, nominal 0,14 mm iz / 0,18 mm aralığa dayanır; üretici gerçek stackup ve maske ile doğrulamalı, gerekli geometri değişirse routing/DRC yeniden değerlendirilmelidir. Üretici verisi raporda kesinleştirilmiş gösterilmemiştir.

`Verification/Manufacturing_Audit.json` bütün 11 Gerber'i geri okuyup 93 deliği native PCB ile karşılaştırır. gerbonara'nın KiCad G90 ve fazladan kullanılmayan RoundRect makro parametresi bildirimleri raporda açıkça kaydedilmiştir; dosyalar bu bildirimleri gizlemek için düzenlenmedi.

Native `.gbrjob` içindeki `ImpedanceControlled=true` tasarım talebidir; üretici empedans doğrulaması değildir. Job `Size=55,05 × 45,05 mm` değeri 0,05 mm Edge.Cuts çizgisinin dış zarfını içerir; profil merkez hattı ölçüsü **55 × 45 mm** esas alınır.
