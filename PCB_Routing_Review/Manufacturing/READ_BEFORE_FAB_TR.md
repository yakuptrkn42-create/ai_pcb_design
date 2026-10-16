# Üretim dosyaları — Rev I / Routing R1

Bu dosyalar paketteki son doldurulmuş PCB'den üretilmiştir. Native DRC 0, açık bağlantı 0, parity 0'dır. Dört bakır katman sırası: F.Cu → In1.Cu (GND) → In2.Cu (GND) → B.Cu. Kart 46 × 40 mm, R2 köşe, nominal 1,6 mm; bakır nominal 35 µm'dir.

Gerber X2: dört bakır, iki soldermask, iki silkscreen, iki paste ve tek kapalı profil. Alt yüzde SMD bulunmadığından B.Paste boş bir geçerli katmandır. R1/R2 DNP'dir; montaj/stencil varyantı tedarikçiyle ele alınmalıdır.

Excellon ayrı dosyalar: 128 PTH delik (100 × 0,25; 10 × 0,30; 18 × 1,00 mm), 4 × 2,70 mm NPTH. Tüm delikler through'dur. Gerber ve drill aynı yardımcı orijini kullanır. Gerber koordinatında profil merkezi çizgisi X=0…46, Y=-40…0 mm'dir. Görünümü elle aynalamayın veya drill orijinini değiştirmeyin. Üretici CAM'inde dört montaj deliği profil ile üst üste kontrol edilmelidir.

11 Gerber ayrı bir parser ile açılmış, 132 drill konumu native kartla eşleşmiştir. Bağımsız SVG önizlemeler `../Views/10_Gerber_Top.svg` ve `11_Gerber_Bottom.svg` dosyalarıdır. Gerbonara, KiCad'in G90 yerleşimi ve RoundRect makrosundaki kullanılmayan parametre için sözdizimi uyarısı üretmiştir; native DRC ihlali değildir. Ayrıntı `../Verification/manufacturing_audit.json` içindedir.

**Üretici ve onaylı stackup henüz belirlenmedi.** 100 Ω diferansiyel hedefine ait 0,14/0,18 mm geometri nominal 0,10 mm FR4 / εr 4,2 hesabına dayanır. Soldermask ve proses toleransı doğrulanmadı. Gerçek stackup ve empedans kuponu üzerinde anlaşılmadan bu dosyalar kontrollü empedans garantisi olarak kullanılmamalıdır. FPC/flex mekanik eşleşmesi ve kesin BOM teyitleri de mühendislik raporunda açıktır.
