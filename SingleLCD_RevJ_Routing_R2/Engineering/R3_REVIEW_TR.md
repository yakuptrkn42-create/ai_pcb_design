# STM32F469I-DISCO → DISEN / Rev J R3 — kontrollü layout revizyonu
22 Ekim 2026

## Amaç ve kapsam
R2 yerleşimi, şematik topolojisi, J1/J2/J3 konnektörleri, dört montaj deliği, kart dış sınırı (55 × 45 mm), katman sırası ve güç netleri korunmuştur. Bu dalda yalnız PCB güzergâh geometrisinin hedefli iyileştirmeleri yapılmıştır; **R2 üretim dosyaları R3 için geçerli değildir**.

## Gerçek PCB değişiklikleri
- DSI_D0_N: F.Cu üzerinde 9 segmentlik U biçimli uzunluk döngüsü, 0,14 mm düz segmentle değiştirildi. Eski yerel uzunluk 6,985244 mm; yeni 5,366274 mm; kısalma 1,618970 mm.
- DSI_D0_P: eşleşen 9 segmentlik döngü, 0,14 mm düz segmentle değiştirildi. Eski yerel uzunluk 6,852697 mm; yeni 5,233726 mm; kısalma 1,618971 mm.
- Eş doğrultudaki 7 bölünmüş bakır izi geometriyi değiştirmeksizin birleştirildi.
- Toplam routing segmenti 435 → 412. Via adedi 86 olarak kalır.
- D0 çifti arası iz açıklığı 0,18 mm; her iki hat aynı miktarda kısaltıldığı için çift içi planar uzunluk farkı yaklaşık 0,001 mm altında kaldı.
- D0 hatlarının yeni yaklaşık uzunluğu 28,074657 mm; CLK ve D1 hatları yaklaşık 29,693628 mm. Saat/veri hatları arasındaki azami planar fark artık yaklaşık 1,619 mm'dir. Bu değişiklik, önceki taslakta kullanılan 1 mm hatlar arası hedefi aştığı için gerçek panel/host zamanlama bütçesi onaylanmadan nihai kabul edilemez.
- Değişen D0 ana yolunun mevcut diğer F.Cu izlerine en yakın hesaplanan bakır açıklığı yaklaşık 0,165 mm (geometrik segment incelemesi); resmî üretim kuralı 0,15 mm, ancak pad/via/zone ve tam 3D geometrisi KiCad DRC ile tekrar denetlenmelidir.

## Değişmeyen teknik belirsizlikler
- 100 Ω diferansiyel empedans yalnız nominal model varsayımıdır; üretici stack-up/etched width/gap/mask/TDR teyidi alınmamıştır.
- D-PHY dönüş via uzaklıkları, FPC launch discontinuity ve uçtan uca kanal modeli doğrulanmadı.
- Host touch 3,3 V toleransı; LED sürücü OVP/açık yük; PCB gerçek termal/EMI/fonksiyon testleri bekliyor.
- R2 Gerber/Excellon/PDF ve Validation_Summary.json önceki revizyona aittir; üretime kesinlikle verilmemelidir.

## Kontrol geçiş kapısı
1. KiCad 9 DRC **--schematic-parity**, ERC, fiziksel net bağlantısı sıfır açık.
2. DSI çift içi ≤0,10 mm; her hat ≤50 mm; çift başına ≤2 via; 0,18 mm diferansiyel aralık korunacak.
3. Saat/veri grupları arasındaki 1,619 mm fark için datasheet/PHY zamanlama analizi ve D-PHY kanal SI incelemesi yapılmadan bu R3 nihai routing değildir.
4. Güncellenen PCB'den Gerber/Drill yeniden üretilecek ve CNC/FPC/test koşullarıyla üretici kontrolüne gönderilecek.
5. Bu kontrollerin raporları oluşmadıkça '0 DRC' veya 'üretime hazır' beyanı verilmemelidir.

R2 ana dalda değiştirilmedi. Revizyon karşılaştırması: `git diff main...revJ-routing-R3-improvement -- SingleLCD_RevJ_Routing_R2/Project/STM32F469_DISEN_RevJ_Prep1.kicad_pcb`.
