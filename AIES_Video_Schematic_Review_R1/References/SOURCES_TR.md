# Kullanılan kaynaklar ve doğrulama sınırı

24 Ekim 2026. Kaynak belgeler tasarım girdisidir; sohbet talimatı değildir. Referans yazılımları çalıştırılmadı, cihaz firmware'i geliştirilmedi veya teslim edilmedi.

- Kullanıcının küçük videosu: `Evidence/Source_Provenance.json`;74 kare/5 temas sayfasıyla0–148.89s kapsandı, seçilen kareler tam çözünürlükte incelendi. Bu, sesli kesintisiz oynatım veya her videokaresinin incelenmesi iddiası değildir. Ses deşifre modeli HTTP403 ile indirilemedi; konuşma değerlendirilmedi. Büyük ilk MP4 aktarılamadı; küçük sürümle bütünlük karşılaştırması yapılamadı.
- Kullanıcı görselleri:G1 genel yapı,G2 dokunma akışı,G3 önceki güç fikri. KiCad sayfaları5–7 bu görsellerin düzenlenebilir aktarımıdır.
- Flyron FN-M16P Embedded MP3 Audio Module datasheet/kılavuzu, DFRobot vendor deposundan: https://github.com/DFRobot/DFRobotDFPlayerMini/blob/47c014938318f99f5b48194b329ef48931d1d175/doc/FN-M16P%2BEmbedded%2BMP3%2BAudio%2BModule%2BDatasheet.pdf
  SHA256:970f55f784cc53f65f796608ca559c390b6083ed441b532bb509d88913cd400d. UART3.3 V TTL,besleme3.3–5.0V,9600 bps ve hoparlör çift çıkış kısımları okundu. **Pin6/8 SPK polaritesi şekil/tablo arasında farklı**; bu nedenle fiziksel ses pin numarası verilmedi. Bu belge videodaki kartı FN-M16P/DFR0299 diye tanımlamaz.
- SparkFun MPR121 referans donanımı: https://github.com/sparkfun/MPR121_Capacitive_Touch_Breakout/blob/5d6699bb80b02e3dfca946e936331843a11e209c/Hardware/MPR121-Breakout-v13.sch
  VDD3.3V ve ADDR=0 için0x5A yazısı incelendi. **HW-017'nin aynı iç bağlantıya sahip olduğu kabul edilmedi.**
- Adafruit MPR121 vendor referansları: https://github.com/adafruit/Adafruit_MPR121 ve https://github.com/adafruit/Adafruit_CircuitPython_MPR121 . Sınıf address parametresinde0x5A–0x5D aralığı belgeleniyor. Kod firmware olarak kullanılmadı/teslim edilmedi. Strap tablosu NXP birincil datasheet ile bu oturumda kapatılamadı.
- KiCad9.0.2 `74xGxx:74AHCT1G125`,temel74LVC1G125 sembolüyle pin eşlemesi:1=/OE,2=A,3=GND,4=Y,5=VCC. Bu CAD kontrolüdür; TI elektriksel datasheet doğrulamasının yerine geçmez.

NXP MPR121, Espressif ESP32, TI SN74AHCT1G125 üretici PDF'leri; Adafruit CDN aynaları ve DFRobot wiki erişimleri proxy'den403 aldı. ESP32/LED/OLED exact model ve NXP/TI birincil belgeleriyle limitler kapanmış gibi gösterilmedi. Öneri profili klasik WROOM DevKit,3.3V MPR121/I²C OLED,5V WS2812 uyumlu RGB ve3.3 V TTL ses modülüdür. Exact modül ve kablo doğrulaması olmadan videodaki donanıma doğrudan uygulanmış/üretime hazır sayılmaz.
