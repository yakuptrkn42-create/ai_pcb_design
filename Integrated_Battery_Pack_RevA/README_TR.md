# Entegre 2S batarya paketi — Rev A / tasarımcıya aktarım

Kullanıcının son yönlendirmesine göre, mevcut BMS PCB'sinden hareketle hazırlanmış **düzenlenebilir ön tasarım ve görsel montaj paketidir**. İki 18650 hücre, üstte BMS ve batarya üzerinde sabit dört kontak tek taşıyıcıda birleştirilmiştir.

- Hedef: 2S1P, nominal 7,4 V / 3500 mAh / yaklaşık 25,9 Wh, yaklaşık 2 A deşarj. Hücre üreticisi/modeli bilinmiyor; 8,4 V tam şarj yalnızca 4,20 V/hücre kimyası doğrulanırsa geçerlidir.
- PCB: 74 × 42 × 1,0 mm, 2 katman; dış montaj zarfı yaklaşık 74 × 42 × 29,2 mm. Kablo/karşı konnektör ve cihaz muhafazası bu zarfa dahil değildir. Hücre/model ölçüleri nominaldir.
- Paket kontak sırası: **1 PACK+ ana / 2 PACK+ yardımcı / 3 NTC / 4 PACK−**. Bu numaralar bu tasarıma aittir; satıcı pin numaraları değildir.
- TH1 BMS için, TH2 host cihaz için ayrı 10 kΩ sensördür. TH2 PACK− referanslı varsayılmıştır; host giriş şeması ve B katsayısı henüz yoktur.

Önce **Tasarimciya_Aktarim_TR.pdf** dosyasına bakın. KiCad 9 ile **Project/BatteryPack_RevA.kicad_pro**, FreeCAD ile **Mechanical/Integrated_Battery_Pack_RevA.FCStd** açılabilir. STEP/WRL montajları ve iki 3D görünüm de teslimdedir. Tüm arşivi çıkarın; yerel kütüphane ve 3D klasörlerini birlikte tutun.

Kaynak arşivdeki şematik ve 11 yedeği boştu. Yeni şematik PCB'deki pad/net bağlantılarından geri kazanıldı. IC sembolleri pasif pad sembolleridir; ERC burada bağlantı/yazım/yapısal kontrolleri gösterir. ERC/DRC sonuçları entegre pin işlevlerinin, BMS eşiklerinin veya medikal cihaz güvenliğinin onayı değildir.

**Üretim, enerji verme ve klinik kullanım onayı yoktur.** Kesin hücre, şarj ve tepe akımı, BMS Data Flash/kalibrasyon, NTC host uyumu, konnektör numunesi, mekanik anahtarlama ve elektriksel/termal/mekanik deneyler tasarımcı tarafından tamamlanmalıdır. Gerber üretim paketi hazırlanmadı.

Dosyalar:
- Views: birleşik ve patlatılmış CAD görünümü, ölçülü plan/pin dizilimi, elektriksel mimari, geri kazanım şematiği PDF ve PCB SVG çıktıları.
- Engineering: elektriksel/mekanik tasarım notları, açık işler, model/yerleşim verileri.
- Verification: ham ERC/DRC, kaynak PCB DRC'si, netlist ve bağımsız bağlantı kontrolleri.
- BOM: aday malzeme listesi ve koordinatlar. Listelenen yeni sigorta/sensörler satın almaya serbest bırakılmamıştır.
- Original ve References: gelen arşivin aynısı ve kullanıcının konnektör çizimi.

Standalone Mechanical/…wrl montajı milimetre birimindedir. Project/3D altındaki footprint WRL dosyaları KiCad için 0,1 inç birimindedir; KiCad referansları STEP modellerini kullanır. Elektronik gövdeler nominal, basitleştirilmiş modeldir.
