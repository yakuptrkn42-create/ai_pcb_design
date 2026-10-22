# Nominal dört katman ve routing kuralları

55×45mm; nominal 1,600mm. Üreticiye onaylatılmış stackup değildir.

| Katman | Nominal değer / görev |
|---|---|
| F.Cu | 35µm; komponentler ve ana sinyal/güç |
| Prepreg | 0,100mm FR4; Er=4,2 / tanδ=0,02 varsayımı |
| In1.Cu | 35µm; F.Cu DSI altında GND referansı |
| Core | 1,260mm FR4 |
| In2.Cu | 35µm; B.Cu DSI altında GND referansı |
| Prepreg | 0,100mm FR4 |
| B.Cu | 35µm; ikinci DSI güzergâhı ve yardımcı routing |

Her iki iç katman şu anda boş. Maske ve nihai yüzey prosesini üretici belirler. 100Ω diferansiyel hedefi nominal 0,14mm iz / 0,18mm aralıkla başlatıldı; gerçek Dk, bakır ve maske için üretici yeniden hesaplamalıdır. Garantili empedans iddiası yoktur.

Genel minimumlar korunur: iz 0,125mm, clearance 0,15mm, Cu–kenar 0,50mm, delik–delik 0,30mm, annular 0,15mm. Çoğu net sınıfında clearance 0,20mm. Normal via 0,60/0,30mm; güç seçeneği 0,80/0,40mm. Mikrovia veya blind/buried via gerektiren bir çözüm hedeflenmedi.

Net class hedefleri: MIPI 0,14/0,18; POWER_5V 0,8mm; BOOST_SWITCH 0,6mm; LED_HV 0,4mm; LOGIC_POWER 0,3mm; SENSITIVE/Default 0,2mm. Üç yerel şematik net adı için netclass atamaları güncellendi. ERC ve fiziksel minimum kuralları gevşetilmedi. Intra-pair skew kuralı, genel skew kuralının ardından gelecek şekilde sıralandı.
