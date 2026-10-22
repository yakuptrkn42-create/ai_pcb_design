# STM32F469I-DISCO / DISEN — Rev J Routing R2

**Routing tamamlandı: 0 DRC ihlali / 0 bağlantısız öğe / 0 şematik–PCB farkı / ERC 0 hata ve 0 uyarı.**

22 Ekim 2026 tarihinde yüklediğiniz güncel Project.zip temel alınmıştır. Önceki P3 placement bu dosyanın yerine geçirilmedi. Kart 55 × 45 mm / nominal 1,6 mm / 4 katmandır. J1/J2/J3 konum ve yönleri, kart sınırı ve dört Ø3,5 mm montaj deliği korundu. Uygun mevcut touch yolları korundu; güç çekirdeği ve onunla çakışan yollar yeniden düzenlendi.

ZIP'i tamamen çıkarıp **Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro** dosyasını KiCad 9.0 veya üstüyle açın. Yerel sembol/footprint/3D klasörlerini Project ile birlikte taşıyın. Original klasörü çalışma projesi değildir.

- `Project/`: düzenlenebilir son şematik/PCB, kurallar ve yerel kütüphaneler.
- `PDF/Routing_R2_Review_TR.pdf`: teknik inceleme, empedans modeli ve açık koşullar.
- `PDF/Schematic_R2.pdf`: son şematik.
- `Manufacturing/Gerber/`: dört bakır, iki mask, iki silk, iki paste, outline ve X2 job.
- `Manufacturing/Drill/`: ayrı PTH/NPTH Excellon ve PDF delik haritaları.
- `Manufacturing/Fabrication_Readme_TR.md`: üreticiye aktarım koşulları.
- `Engineering/`: komponent koordinatları/BOM, stack-up ve güç devir notları; yeniden çalıştırılabilir denetimler.
- `Verification/`: native DRC/ERC, elektriksel kimlik, DSI ölçümleri, referans GND örneklemesi, Gerber/drill ve taşınabilirlik kontrolleri.
- `Views/`: gerçek KiCad SVG/PNG/3D ve ölçülmüş routing detayları.
- `Original/`: değişmemiş yükleme ve karşılaştırma için kaynak dosyalar.

**Üretim kabulü koşulludur.** Gerçek üretici stack-up'ı sağlanmadı; erişilebilen kaynaklarda üreticiye ait doğrulanmış bir sipariş kesiti elde edilmedi. Bu teslimde 100 µm dış dielektrik / 35 µm bakır / Er=4,2 nominal şartnamesi korunur. 0,14 mm / 0,18 mm diferansiyel geometri için maskesiz 2D tahmin 99,4 Ω'dur; üretici onaylı sonuç veya ölçülmüş TDR değildir. Üretici bu kesiti, bitmiş hat geometrisini ve 100 Ω hedefini onaylamadan CAM dosyalarını imalata serbest bırakmayın. Kesit farklıysa genişlik/aralık yeniden hesaplanmalı ve routing/CAM tekrar üretilmelidir.

FPC kontak yüzü/kablo yönü/bükülme ve takılı konnektör yüksekliği numune üzerinde doğrulanmalıdır. FPC ve L1 modelleri nominaldir; J4 modeli 2,54 mm pin aralığına hizalandı; J6 gövdesinin 3D modeli yoktur, 2D Fab/courtyard kontrolü yapıldı. Bu görsel tam mekanik montaj onayı değildir.

Önceki elektriksel incelemede açık kalan touch gerilim toleransı, panel akımları/timing ve OVP açılış/açık yük transient koşulları bu routing ile kapanmaz. R5 üzerinden doğrudan host touch beslemesi, host toleransı ile DISEN sınırının teyidini gerektirir. C3 gerçek parçasının 30 V DC bias altında ≥1 µF etkin kapasitesi ve L1 stok/akım rating'i BOM seçimiyle doğrulanmalıdır. R1/R2 DNP kalır. Yazılım ve fiziksel fonksiyon testleri yapılmadı.

Linux yeniden doğrulama:
```bash
kicad-cli pcb drc --schematic-parity --exit-code-violations --format json -o Verification/DRC_Final.json Project/STM32F469_DISEN_RevJ_Prep1.kicad_pcb
kicad-cli sch erc --exit-code-violations --format json -o Verification/ERC_Final.json Project/STM32F469_DISEN_RevJ_Prep1.kicad_sch
/usr/bin/python3 Engineering/validate_routing.py
/usr/bin/python3 Engineering/verify_manufacturing.py
```
Salt okunur ev dizini bulunan bulut ortamında XDG_CONFIG_HOME, XDG_CACHE_HOME ve XDG_DATA_HOME'u yazılabilir dizinlere yönlendirin. Empedans betiği NumPy/SciPy ister ve nominal hesap dosyasını yeniden üretir. `export_deliverables.py` mevcut üretim/görsel çıktılarını son PCB'den yeniden üretir; KiCad CLI ve Inkscape ister.
