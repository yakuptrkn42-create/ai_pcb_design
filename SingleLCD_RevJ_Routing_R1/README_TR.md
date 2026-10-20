# STM32F469 / DISEN — Rev J / Routing R1

**Dört katman routing tamamlandı: 0 DRC ihlali, 0 bağlantısız öğe, 0 şematik–PCB parity farkı.**

Yalnızca ilk LCD, **DS070HSD39T-132**, için hazırlanmıştır. Çift LCD Rev K ayrı tutuldu. En son yüklenen `Project.zip` temel alındı; orijinali `Original/Submitted_Project.zip` içinde byte düzeyinde korunuyor. Önceki routing girdisi de `Original/Prior_Submitted_Project.zip` olarak saklandı.

## Açılış

ZIP'in **tamamını çıkarın** ve KiCad **9.0 veya daha yeni sürümle** `Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını açın. Kaynak basename bağlantı yollarını korumak için değiştirilmedi; PCB başlığı **Routing R1**'dir. `.kicad_pro`, `.kicad_dru`, tüm şematikler, kütüphaneler ve `3D/` aynı dizinde kalmalıdır. Modeller `${KIPRJMOD}` üzerinden yereldir. KiCad 9.0.2 ile başka dizine kopyalanarak açılış/DRC/ERC kontrolü yapıldı.

## Sonuç

- **55 × 45 mm**, nominal **1,6 mm / dört bakır katman**; 49 devre referansı ve 4 adet Ø3,5 mm NPTH.
- 44 net / 159 numaralı pad–net üyeliği, elektriksel değerler ve R1/R2 DNP durumu kaynakla aynı.
- 466 track/arc öğesi; **84 via: 12 DSI, 18 diğer sinyal, 54 GND**. Dört GND dolgusu ve dört montaj donanımı keepout alanı.
- J1/J2 ana konnektörleri **aynı konum ve yönde**. J3/J4 ve L1 de korundu. J6 +3 mm içeri alındı; 12 güç/test referansı yerel güç çekirdeği için yeniden düzenlendi. Bazı kaymalar ~15 mm'dir; hepsi küçük kozmetik hareketler değildir. Tam liste `Engineering/Placement_Changes.json` ve rapordadır.
- Bütün 5 V yolları **0,8 mm**; SW **0,6 mm**, LED ana yolları **0,4 mm**, FPC LED yaklaşımları **0,3 mm**. 0,2 mm LED sense/Kelvin dalları yük akımı için ana yol değildir. Dokunmatik 3V3 konnektöründe 0,9 mm uzunlukta 0,2 mm çıkış bulunur; sonrası 0,3 mm'dir.
- DSI çiftlerinde ana geometri **0,14 mm iz / 0,18 mm aralık**, kısa ayrık çıkışlarda 0,17 mm. İletken başına iki via. Bakır orta düzlemleri arasındaki via boyu dahil **32,824 mm**; çift içi fark **<0,01 mm**. Bu fiziksel uzunluk eşlemesidir; tam kanal gecikmesi veya empedans sertifikası değildir.
- ERC **0 hata / 3 mevcut tekil global etiket uyarısı**: BL_COMP, BL_SW, OVP_SENSE. Uyarılar gizlenmedi.

## Dosyalar

- `Project/`: düzenlenebilir KiCad projesi, şematikler, kurallar, yerel footprint/sembol/3D kütüphaneleri.
- `PDF/Routing_R1_Review_TR.pdf`: kısa mühendislik raporu ve görseller; `PDF/Schematic_RevJ_Routing_R1.pdf`: güncel şematik.
- `Views/`: gerçek KiCad 2D/3D çıktıları, iç GND katmanları ve Gerber'den geri okunmuş önizlemeler. Alt yüz görselleri alttan bakış için aynalı; CAM dosyaları aynalanmadı.
- `Manufacturing/`: 11 Gerber + job, ayrı PTH/NPTH Excellon ve PDF delik haritaları. Dosyalar son mühendislik/üretici incelemesi içindir.
- `Engineering/`: stackup/kurallar, güç hesapları, final bakır geometrisi, BOM ve konum değişiklikleri.
- `Verification/`: son DRC/ERC, net/pad/kimlik/model karşılaştırması, DSI/GND örneklemesi ve CAM denetimleri. `Base_`, `Prior_`, `Initial_` dosyaları önceki aşama kanıtlarıdır; son kabul için `DRC_Final`, `ERC_Final`, `Final_Independent_Audit`, `Manufacturing_Audit` kullanın.
- `Original/` ve `References/`: korunan girdiler, kullanıcı talebi ve kullanılan kaynak belgeler.

## Üretimden önce açık kalan koşullar

Üretici **henüz seçilmedi**. 100 Ω diferansiyel hedef için kullanılan stackup nominaldir; üretici bitmiş bakır/dielektrik/maskeyi ve empedans toleransını onaylamalıdır. Yaklaşık 99,3 Ω maskesiz 2D hesabı üretici kabulü değildir. FPC konnektörü/sipariş eki/kontak yönü ve gerçek kablo sürekliliği; host CN2/R117-R119 ve pull-up popülasyonu; LCD/touch TBD akımları/3V3 toleransı; C3 DC-bias, L1 ve U2 OVP davranışı doğrulanmalıdır. Nominal 3D model çakışması yok; exact mating/latch/FPC bükülme zarfı doğrulanmadı. DSI GND dönüş via mesafeleri 0,81–2,62 mm; bütün geçişler 1,2 mm hedefe sığmadığından tam kanal SI kontrolü açık kalır.

Şematik topolojisi değişmedi. J6'nın kaynakta ters yazılmış polarite açıklaması **1=+5V / 2=GND** olarak düzeltildi; J4 gerçek üç kablo olarak adlandırıldı: **1=PC6 PWM (CN12.6), 2=PB12 touch RESET (CN12.12), 3=GND (CN12.2)**. Bunlar net değişikliği değildir. R1/R2 **DNP**; 3D görüntü modellerini gösterebilir. BOM/assembly montaj için esastır. Bu pakette yazılım geliştirilmedi; fiziksel çalışma garantisi verilmez.
