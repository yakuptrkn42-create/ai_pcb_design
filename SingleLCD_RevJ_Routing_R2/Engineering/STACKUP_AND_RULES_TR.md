# R2 nominal kesit ve imalat şartnamesi

**Üretici/sipariş kodu doğrulanmış değildir.** Aşağıdaki kesit üreticiye onaylatılacak tasarım şartıdır; herhangi bir üreticinin standart kesiti diye sunulmaz.

| Sıra | Nominal kalınlık | Görev |
|---|---:|---|
| F.Cu | 35 µm | D0 ana bölümü, güç ve düşük hızlı sinyaller |
| Prepreg | 0,100 mm | Er=4,2; tanδ=0,02 varsayımı |
| In1.Cu | 35 µm | F.Cu altında GND referansı |
| Core | 1,260 mm | FR4 nominal |
| In2.Cu | 35 µm | B.Cu altında GND referansı |
| Prepreg | 0,100 mm | Aynı nominal model |
| B.Cu | 35 µm | CLK/D1 ana bölümleri, yardımcı yollar |

Nominal toplam 1,600 mm; maske ve bitmiş yüzey üretici tarafından belirlenir. İki iç katmanda GND dolgusu oluşturuldu; güç için referans düzlemi bölünmedi. DSI'nın kendi signal-via antipad'leri ve montaj keepout'ları bu düzlemlerde açıklık oluşturur.

Hedef 100 Ω diferansiyel. Ana hat 0,14 mm; çift açıklığı 0,18 mm. Ayrık launch 0,17 mm. STM32F469 DS11189 Rev8 s.124 Table45, D-PHY tek uç çıkış empedansı için 50 Ω tipik verir; TI SPRAAR7J Appendix A-7, aynı D-PHY'yi kullanan CSI için 100 Ω tipik diferansiyel / 50 Ω tek uç örneği verir. TI'nin başka cihazına ait tolerans/uzunluk kuralları bu panel için sertifikasyon değildir. DISEN PDF'sinde PCB için açık bir diferansiyel empedans toleransı belirtilmemiştir; 100 Ω tasarım hedefidir.

2D finite-volume çözüm: ε dağılımında ∇·(ε∇V)=0; odd mode ±1 V; Codd=Q(+)/1 V, vakum çözümü C0; Zdiff=2/(c√(Codd·C0)). Metal sınırı yarım hücre mesafesiyle ele alınır. 2 × 0,7 mm çözüm alanı; dikdörtgen bakır; maskesiz hava/FR4. Mesh 5 → 2,5 µm için 99,26 → 99,40 Ω; bu yalnız nümerik yakınsamadır, proses doğrulaması değildir. Ayrık 0,17 mm launch tek uç tahmini 49,13 Ω. H=90/110 µm için yaklaşık 94,7/103,3 Ω; Er=3,9/4,5 için 102,2/96,5 Ω (5 µm mesh). Maske, trapez etch, dispersiyon, örgü, via, FPC ve konnektör modeli yoktur.

Gerçek kesit/bitmiş bakır/maske ve 100 Ω ±%10 talebinin uygulanabilirliği üreticiye teyit ettirilmelidir; bu tolerans henüz bir üretim sözleşmesi değildir. Empedans kuponu/TDR ve örnek kart kontrolü istenmelidir. İç katman routing seçilmedi: iki sürekli GND referansı korundu ve kısa dış yollar çözüldü.

Kaynak minimumlar ve DRC seviyeleri korunur: iz 0,125 mm; genel clearance 0,15 mm; çoğu net sınıfı 0,20 mm; bakır–kenar 0,50 mm; annular 0,15 mm; delik–delik 0,30 mm. Normal via Ø0,60 / delik Ø0,30 mm. DSI ≤50 mm planar / ≤2 via; çift içi ≤0,10 mm; tüm iletkenler arası hedef ≤1 mm. Bunlar PCB bütçeleridir; host ve FPC dahil değildir. Son skew kuralı 0,10 mm çift içi kuraldır; geçici +0,217 mm bozma deneyi bu kuralın ihlali yakaladığını doğruladı.
