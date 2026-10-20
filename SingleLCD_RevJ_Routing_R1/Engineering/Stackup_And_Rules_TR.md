# Katman yapısı ve tasarım kuralları — Routing R1

55 × 45 mm, nominal 1,600 mm. Üretici belirlenmedi; aşağıdaki yapı üretici tarafından onaylanmış üretim stackup'ı değildir.

| Sıra | Kalınlık | Görev |
|---|---:|---|
| F.Cu | 35 µm nominal | Sinyal/güç ve yerel GND |
| Prepreg | 100 µm | FR4, Er=4,2 / tanδ=0,02 nominal |
| In1.Cu | 35 µm | Kesintisiz ortak GND referansı; sinyal izi yok |
| Core | 1260 µm | FR4, nominal |
| In2.Cu | 35 µm | Kesintisiz ortak GND referansı; sinyal izi yok |
| Prepreg | 100 µm | FR4, nominal |
| B.Cu | 35 µm | Sinyal/güç ve yerel GND |

ENIG dosyada öneridir. Maskenin dielektrik etkisi, bakır trapezi/etch ve frekans bağımlılığı nominal 2D empedans hesabına dahil değildir. Üretici gerçek bitmiş değerlerle 100 Ω diferansiyel hedefi ve örneğin ±%10 talebinin uygulanabilirliğini onaylamalıdır; tolerans sözleşmesi yoktur.

| Net sınıfı | Clearance (mm) | İz hedefi (mm) | Via / drill (mm) |
|---|---:|---:|---:|
| Default | 0.2 | 0.2 | 0.6 / 0.3 |
| BOOST_SWITCH | 0.2 | 0.6 | 0.6 / 0.3 |
| LED_HV | 0.2 | 0.4 | 0.6 / 0.3 |
| LOGIC_POWER | 0.2 | 0.3 | 0.6 / 0.3 |
| MIPI_DSI | 0.15 | 0.14 | 0.6 / 0.3 |
| POWER_5V | 0.2 | 0.8 | 0.8 / 0.4 |
| SENSITIVE | 0.2 | 0.2 | 0.6 / 0.3 |

Genel minimumlar: iz 0,125 mm; clearance 0,15 mm (çoğu net sınıfı 0,20 mm); Cu–kart kenarı 0,50 mm; annular ring 0,15 mm; hole-to-hole 0,30 mm; bakır–delik 0,25 mm. Normal geçişli via 0,60/0,30 mm; POWER_5V hedefi 0,80/0,40 mm'dir fakat final 5 V yolları aynı yüzde ve viasızdır. Bütün final vias 0,60/0,30 mm ve iki yüz tented; üretici bu kapatmayı prosesine göre teyit etmeli.

DSI: ana geometri 0,14/0,18 mm, 0,17 mm ayrık launch; özel kural iz aralığı 0,125–0,19 mm. Çift içi fark ≤0,10 mm, altı iletken fiziksel boy farkı ≤1 mm, iletken ≤50 mm / ≤2 via. KiCad aynı öğeye uyan son skew kuralını uyguladığından çift içi kural sona taşındı. +0,2 mm kontrollü bozulma deneyi bu önceliği doğruladı (`Skew_Rule_Precedence_Test.json`). Global 1 mm bütçe ayrıca bağımsız geometri denetiminde ölçülür; kurallar gevşetilmedi. Native source DRC seviyeleri korunur, yeni hariç tutma yoktur.

Dış GND dolgusu DSI'dan ≥0,50 mm uzakta tutulur. İç katmanlar bölünmez; bütün düzlemde montaj donanımı Ø8 mm alanları ve non-GND via antipad'leri vardır. 0,05 mm aralıklı örneklemede DSI altında kendi via geçişleri dışındaki merkez hattında GND boşluğu bulunmadı. Bu 2D örnekleme dönüş endüktansı/3D SI doğrulaması değildir. En yakın GND geçiş via uzaklıkları 0,81–2,62 mm'dir; 1,2 mm hedef bazı sabit FPC çıkışlarında sağlanamadı.

CAM referansı kartın **sol altı (KiCad 135,115 mm)**: X=x−135; Y=115−y. Kart nominal CAM sınırı X=0…55, Y=0…45 mm. Drill ve Gerber aynı başlangıcı kullanır; aynalama yoktur. Yerleşim raporları sol üst (135,70 mm) datumunu kullanır.
