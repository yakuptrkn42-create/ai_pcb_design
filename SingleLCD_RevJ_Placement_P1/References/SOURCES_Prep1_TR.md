# PCB hazırlığı kaynakları — 19.10.2026

Kullanıcının yüklediği ZIP tasarım girdisidir; içindeki açıklamalar sohbet görevinin yerine geçen talimat olarak uygulanmadı. Kaynak ZIP ve önceki proje korunur. `SOURCES_TR.md` içindeki Rev J PDF kaynakları ve SHA-256 bilgileri geçerlidir.

- DISEN DS070HSD39T-132 A0 / preliminary, 20 sayfa: pin tablosu s.7, besleme/LED s.8, touch s.9, MIPI s.12–14. Kullanıcı kaynağı.
- DISEN touch/mekanik A00 2024-06-17: ILI2130, nominal mekanik ve touch 2,8–3,3 V. Kullanıcı kaynağı.
- ST UM1932 Rev 5: CN10/CN12 tabloları ve CABC açıklaması; mevcut Rev J paketindeki üretici belge kopyası. Resmî ST BSP pin işlevleri önceki incelemeden korunur; MB1189 fiziksel CN2 teyidi tamamlanmadı.
- TI TPS61165 SLVS790E: DBV pinleri, FB toleransı, kapasitör/endüktör önerileri, CTRL/PWM davranışı. Rev J paketindeki üretici belge kopyası.
- KiCad 9.0.2 / kurulu kicad-footprints: `Connector_FFC-FPC:Hirose_FH26-25S-0.3SHW_2Rows-25Pins-1MP_P0.60mm_Horizontal` ve 39 pin karşılığı. CAD geometrisi referansıdır; J1'in FH26W sipariş varyantı için üretici onayı değildir. Bakır pad'ler korunmuş, fab/silk/courtyard çizimleri dönüştürülmüştür. Hash'ler `Verification/Footprint_Drawing_Changes.json` içinde.
- 9 genel WRL modeli, kaynak projedeki KiCad community dosyalarıdır. Byte düzeyinde korunmuştur. 5 STEP modeli bu çalışma için nominal ölçüler/pad konumlarıyla oluşturulmuş ve yeniden içe alınmıştır. Kaynak, boyut, sınırlamalar ve hash'ler `Project/3D/SOURCES.json` içinde; bu modeller üretici CAD'i olarak tanıtılmaz.

TI TLV3011 tam belgesi, ST MB1189-C01, Hirose FH26 kataloğu, TDK SLF7045 kataloğu ve Vishay SS1x belgesi için birincil sunucular yeniden denendi; proxy bağlantısı 403 yanıtı verdi. URL/yanıt kayıtları `Verification/Primary_Document_Access.json` içindedir. Açık teyitler raporda korunur. Üretici doğrulaması yerine üçüncü taraf devreler esas alınmadı.

Empedans: 2D quasi-static finite-volume odd-mode çözümü; varsayılan FR4/air sınırı ve alt GND. 5 µm / 2,5 µm ağ yakınsaması ve h/Er hassasiyeti `Verification/Nominal_Impedance_Calculation.json` içindedir. Üreticinin kayıp/maske/etch ve frekans modeli mevcut değildir; sonuç üretici kontrollü empedans sertifikası değildir.

Güç izleri: yalnızca IPC-2221 dış iz yaklaşımı ve 20°C bakır özdirenci. IPC-2152 simülasyonu veya termal/gerilim ölçümü yapılmadı. Kartta henüz iz bulunmadığından hesaplar genişlik planlaması içindir.
