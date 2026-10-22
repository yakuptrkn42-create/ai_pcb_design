# STM32F469 / DISEN — J-SR1 / Placement P3

KiCad 9.0 veya üstü ile `Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını açın; ardından PCB Editor'e geçin. Project klasörünü yerel kütüphaneleri ve 3D klasörüyle birlikte taşıyın. Şematik başlığı J-SR1 olarak kalır; PCB revizyonu P3'tür.

**Placement tamamlandı; routing yapılmadı.** 55×45mm / nominal 1,6mm / dört bakır katman; 49 devre elemanı + dört Ø3,5mm montaj deliği. Bütün devre elemanları üst yüzde. Montaj delikleri ve kart sınırı kaynakla aynıdır. J1 soldan, J2/J3 üstten FPC takılacak şekilde yeniden yönlendirildi. J4 kontrol konnektörü ve J6 haricî 5V girişi korunur.

- `Project/`: doğrudan düzenlenebilir PCB, değişmemiş J-SR1 şematikleri, kurallar ve yerel kütüphaneler.
- `PDF/Placement_P3_Review_TR.pdf`: placement gerekçeleri, ölçümler ve sınırlamalar.
- `Views/Routing_Plan.png`: potansiyel routing alanı ve via adayları; bu çizimdeki renkler/via halkaları PCB bakırı değildir.
- `Views/PCB_3D.png`, `Views/PCB_Top.png`, `Views/Assembly.png`: native KiCad çıktıları.
- `Engineering/Component_Placement.csv`: kartın sol üstünden mm; KiCad Y aşağı doğru pozitiftir, rotasyon KiCad derecesidir.
- `Verification/`: fiziksel DRC, ERC, parity, elektriksel kimlik ve mekanik/routing alanı kontrolleri.
- `Original/`: değiştirilmemiş yükleme ve karşılaştırma girdileri. DNM mainboard arşivi bu teslime kopyalanmadı.

Son kontrol: **0 fiziksel DRC ihlali; 0 şema–PCB parity farkı; ERC 0 hata / 0 uyarı.** Routing yapılmadığı için **115 bağlantısız öğe kaydı açıktır**. Kartta **0 iz, 0 via, 0 bakır dolgu** vardır. Dört zone nesnesi, montaj donanımı için bakırsız keepout/rule area'dır; GND dolgusu değildir.

DSI için F.Cu altında In1.Cu, B.Cu altında In2.Cu sürekli GND referansı planlandı. İç katmanlarda henüz GND bakırı yoktur. GND düzlemleri routing aşamasında oluşturulmalıdır. 0,14mm iz / 0,18mm aralık yalnız nominal başlangıçtır; 100Ω empedans üretici stackup'ıyla teyit edilir. Son iz uzunluğu, skew, via sayısı, SI ve güç sıcaklığı routing/ölçümden önce doğrulanmış sayılmaz.

FPC/indüktör STEP modelleri kaynaktan gelen nominal modellerdir. J4'e yerel KiCad WRL modeli eklendi. J6 için uygun 3D gövde modeli yoktur; alanı F.Fab/courtyard üzerinden kontrol edildi, render'da yalnız padları görünür. Exact FPC kontak yüzü, kablo bükülmesi ve kasa/plug yüksekliği için fiziksel teyit gereklidir. Şematik incelemedeki panel akımı/başlatma ve güç geçişi koşulları bu placement ile kapanmış sayılmaz.

Yeniden doğrulama (teslim klasöründe Linux):
```bash
mkdir -p /workspace/.cloud-onboarding/kicad/{config,cache,data}
export XDG_CONFIG_HOME=/workspace/.cloud-onboarding/kicad/config
export XDG_CACHE_HOME=/workspace/.cloud-onboarding/kicad/cache
export XDG_DATA_HOME=/workspace/.cloud-onboarding/kicad/data
kicad-cli pcb drc --schematic-parity --format json -o Verification/DRC_Placement.json Project/STM32F469_DISEN_RevJ_Prep1.kicad_pcb
kicad-cli sch erc --exit-code-violations --format json -o Verification/ERC.json Project/STM32F469_DISEN_RevJ_Prep1.kicad_sch
/usr/bin/python3 Engineering/validate_placement.py
```

Tam DRC'ye `--exit-code-violations` eklenirse bağlantısız öğeler nedeniyle başarısız çıkış beklenir; bu bir route edilmiş kart teslimi değildir. Doğrulama betiği ayrıca fiziksel ihlal/parity olmamasını ve placement-only koşullarını kontrol eder.
