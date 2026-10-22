# İmalat aktarımı — R2 / üretici onayı bekleyen paket

Gerber/drill son R2 PCB'den native KiCad 9 ile üretildi. 55 × 45 mm, nominal 1,6 mm, 4 bakır katman. Sıra: F.Cu / In1.Cu GND / In2.Cu GND / B.Cu. İki iç düzlemi güç için bölmeyin.

İmalata serbest bırakmadan önce: 100 µm dış dielektrik / 35 µm bakır / nominal Er4,2 ve 0,14 mm iz / 0,18 mm gap için 100 Ω hedefini gerçek malzeme, bitmiş bakır/etch ve maskeyle onaylayın. Bu dosyalar üretici stack-up'ı doğrulanmış kabul edilmemelidir. Kesit farklıysa routing genişliği/aralığı/CAM yeniden değerlendirilir. ENIG proje içindeki öneridir; üreticiyle teyit edilir. Empedans kuponu/TDR talebi ve tolerans anlaşması ayrıca yapılmalıdır.

- Gerber: 4 copper + 2 mask + 2 silk + 2 paste + outline; X2 job beraber verildi.
- Drill: ayrı PTH/NPTH, mm/absolute/decimal; Gerber ile aynı PCB datum'u. Dosyaları ayrı origin'e taşımayın veya aynalamayın.
- PCB koordinatlarında outline X115,5…170,5 / Y70…115 mm'dir. Gerber/Excellon'da Y işareti kart koordinatına göre terstir; bu iki CAM formatında tutarlıdır.
- 91 PTH (86 via + 5 konnektör deliği) ve dört Ø3,5 mm NPTH. Excellon XY 0,001 mm seri hale getirilir; denetimde en fazla 0,0005 mm yuvarlama farkı vardır.
- Minimum iz 0,125 mm; minimum clearance 0,15 mm; çoğu net 0,20 mm; Cu–kenar 0,50 mm; via Ø0,60/0,30 mm; annular ≥0,15 mm. Üretici yeteneği bu kuralları karşılamalıdır.
- FPC altında via proses/tenting ve lehim maskesiyle gerçek konnektör gövdesi teyit edilmeli. Nominal modeller exact parça/flex montaj onayı değildir.
- Dört montaj deliği çevresinde nominal Ø8 mm bakır keepout vardır; kesin vida/pul/kasa ölçüsü müşteri montajında teyit edilir.

R1/R2 DNP; montaj listesinde generic parça değerlerinin kesin MPN/rating/DC-bias/doyma kontrolü gerekir. Assembly veya panelizasyon üretici tarafından ayrıca değerlendirilir. Gerber/drill hazırlanmış olması fonksiyon, EMI, ısıl test veya donanım çalışma garantisi vermez.
