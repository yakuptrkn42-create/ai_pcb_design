# Dört katmanlı mimari ve kayıtlı kurallar

P2, kaynak projenin uygun nominal stackup/net class/routing bütçelerini korur. Üretici seçilmediği için onaylı üretici stackup'ı veya garantili empedans değildir. DRC sonucu temiz görünsün diye minimumlar değiştirilmedi.

| Sıra | Katman | Nominal kalınlık / görev |
|---|---|---|
| 1 | F.Cu | 35 µm; ana DSI, boost/güç, kontrol |
| — | Prepreg | 100 µm FR4; Er 4,2 / tanδ 0,02 varsayım |
| 2 | In1.Cu | 35 µm; kesintisiz GND referansı planı |
| — | Core | 1260 µm FR4 |
| 3 | In2.Cu | 35 µm; kesintisiz GND referansı planı |
| — | Prepreg | 100 µm FR4; aynı nominal varsayım |
| 4 | B.Cu | 35 µm; gerekli DSI çapraz geçişleri ve ikincil routing |

Toplam 1,600 mm (nominal bakır+dielektrik). Soldermask ve nihai yüzey kalınlığı bu toplam/modelde hesaba katılmadı. ENIG önerisi üretici seçimi değildir. İç katmanlar şu anda dolgu içermez; katman adının GND olması bir bağlantı kurmaz. F.Cu altında In1; B.Cu altında In2 sürekli referans olarak doldurulmalıdır. DSI altına bölünmüş güç adası yerleştirilmemeli.

| Sınıf/limit | Projede kayıtlı değer |
|---|---|
| Global min | İz 0,125 mm; clearance 0,15 mm; kart kenarı 0,50 mm; delik–delik 0,30 mm |
| Default | İz 0,20 mm / clearance 0,20 mm |
| Geçişli via | 0,60 mm çap / 0,30 mm delik; min annular 0,15 mm. Alternatif 0,80/0,40 mm. Microvia/blind/buried gerekmiyor. |
| MIPI_DSI | Hedef 0,14 mm iz / 0,18 mm çift aralığı / 0,15 mm clearance |
| DSI launch | İz min 0,125 / opt 0,14 / max 0,19 mm |
| DSI uzunluk | Çift içi fark ≤0,10 mm; altı PCB iletkeni fark bütçesi ≤1,0 mm; iletken uzunluğu ≤50 mm |
| DSI via bütçesi | Her iletkende ≤2 geçişli via; 0 via tercihi, garanti değil |
| DSI dış GND | Dış katman GND dolgusu ile en az 0,50 mm uzaklık; kullanılan microstrip yaklaşımına uygunluk için |
| POWER_5V / BOOST_SWITCH | Hedef 0,60 mm / min 0,30 mm iz; 0,20 mm clearance |
| LED_HV | Hedef 0,40 / min 0,20 mm iz; 0,20 mm clearance |
| LOGIC_POWER | 0,30 mm iz / 0,20 mm clearance |
| SENSITIVE / kontrol | 0,20 mm iz / 0,20 mm clearance |

BL_CTRL ve BL_PWM_RAW güç sınıfına sokulmadı. Bütün 44 netin gerçek KiCad netclass çözümlemesi `Verification/Native_Netclasses.json` içinde. Custom kurallar proje ile aynı kökte `.kicad_dru` içinde; sayısal imalat minimumları `.kicad_pro` içinde. DSI gap opt=0,18 mm'dir; nihai geometrinin sabit ve eşleşmiş kalması manuel routing incelemesinde de kontrol edilmelidir. Güç daralmasının ≤1 mm olması bir yorum/hedeftir; KiCad bunu uzunluk olarak otomatik uygulamıyor.

Hedef diferansiyel empedans 100 Ω, üreticiye önerilecek tolerans ±%10. Önceki 2D quasi-static odd-mode hesap, maskesiz Er=4,2 / h=0,100 / Cu=0,035 mm nominal kesitte 0,14/0,18 mm için yaklaşık 99,3 Ω vermişti; bu P2'de yeniden çözülmüş veya üretici tarafından doğrulanmış sonuç değildir. Önceki hesap kanıtı eklenmiştir. Maske, gerçek Dk/frekans, etch/trapez, FPC ve konnektörler dahil değildir. Fab stackup kesinleşince iz/ara açıklığı yeniden hesaplanmalı ve üreticiyle onaylanmalıdır; katalog dışı kesinlik iddia edilmez.

0,60 mm dış iz / 35 µm bakır için eski IPC-2221 yaklaşımıyla 10°C artışta ~1,65 A, 0,30 mm için ~1,00 A hesaplanmıştı. Bunlar IPC-2152, gerçek termal ölçüm veya arıza kabulü değildir. 25 mm / 0,60 mm izde 20°C için yaklaşık 20,5 mΩ ve 0,4 A'da 8,2 mV düşüm; konektör, kablo, diyot ve GND dönüşü hariç. İz henüz çizilmediğinden gerçek güç kapasitesi veya gerilim düşümü onayı verilmez.
