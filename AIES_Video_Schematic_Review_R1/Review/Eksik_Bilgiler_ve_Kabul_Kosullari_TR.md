# Kapanmamış konular

Kod olmadığı belirtildi; tasarım seçimleri kullanıcı yetkisiyle **öneri P1** olarak yapıldı. Yeni bir yazılım/kod talebi işi durdurmuyor. Öneri ile mevcut kayıt ayrı tutuldu.

1. **ESP32 exact kart/yonga:** GPIO21/22/18/17/16/27/26/25 klasik WROOM profili için seçildi. S3/C3 veya WROVER/PSRAM kartına aynen uygulanmaz. USB/VIN/5V/3V3 iç güç şeması ve regülatör kapasitesi görülmeli.
2. **Dokunma modülleri:** PCBHW-017 okunur; IC üst kodu ve ADDR default bağları/pull-up değerleri okunamadı. Önerilen adres bağlantıları exact MPR121 dokümanı ve modül kartıyla teyit edilmeli; sabit GND köprüsü varsa doğrudan3.3V/SDA'ya bağlanmaz. Gerçek elektrot/kalp bölgesi sayısı ve dağılımı bilinmiyor.36 kanal yalnız kapasitedir.
3. **Ekran:** model,gerilim toleransı,I²C veya başka arayüz ve adres bilinmiyor. P1 yalnız3.3V uyumlu I²C ekran profili içindir;0x3C öneridir. Kablonun header sırası pin isimlerinden kontrol edilmeli; footprint verilmedi.
4. **LED:**24 görünür paket sayıldı; gerçek IC/RGB/RGBW,gerilim sınırı,DIN/DOUT yönleri,besleme polaritesi ve seri sıra tespit edilemedi. U401→U402→U403 yeni öneridir.24×60mA hesabı model doğrulaması değil bütçe varsayımıdır.
5. **Ses ve yük:**microSD kart yuvası görülür; DFPlayer/FN-M16P exact varyantı ve hoparlörΩ/W bilinmiyor. P1 3.3 V TTL hedefi kullanır. Kılavuzdaki SPK şekil/tablo çelişkisi yüzünden pad6/8 polaritesi atanmadı. SPK A/B hiçbir şekildeGND değildir.8 Ω / 3 W yalnız yeni yük önerisidir.
6. **Güç/USB:**4.8–5.0V,≥4A ön bütçe ve3.15 A fuse seçimi gerçek etiket/akım ölçümüne dayanmıyor. USB + harici kaynak işletimi **teyitsizdir**; JP101 ayırması, farklı GPIO hatlarından geri beslemeyi veya güç sırası sorunlarını tek başına çözmez. Exact devboard şeması/geri besleme testi kapanana kadar **USB + harici eşzamanlı kullanım onayı verilmez**. P1 servis modu bu koşula bağlıdır; yalnızUSB modu tasarlanmadı. Enerji varken jumper konumu değiştirilmez.
7. **Pull-up/akım/termal:**modül/OLED pull-up eşdeğeri ve bağlı rail ölçülmeli; R201/R202 DNP olup gerekirse4.7k takılır.100 kHz başlangıç hedefi, trise ve sink akımı doğrulanınca kullanılmalı. DevKit3.3V ek yükü, regülatör ısısı, LED/ses ani akımı ve kablo düşümü ölçülmeli. LED güç akımı breadboard/ESP32 üzerinden geçirilmemeli.
8. **Belgeler/test:**NXP,Espressif,TI birincil PDF limitleri bu oturumda kapanmadı; ses konuşması dinlenmedi/deşifre edilmedi. AİES Rev A dosyaları gelmedi. PCB,simülasyon,fiziksel test veya firmware yok; üretime hazır onayı yok.

Bu bilgileri kapatmak için gereken asgari fiziksel kayıt: kartın iki yüzünü ve pin yazılarını gösteren bir ESP32 fotoğrafı; HW-017 ADDR/pull-up ve terminal yakın fotoğrafı; OLED/ses/LED üzerindeki model/pin yazıları; güç ve hoparlör etiketi. Video mevcut kablo uçlarını gizlediği için istenenler yalnız okunmayan noktalardır.

## Mevcut yazılım uyumu

P1 yeni GPIO/adres/LED sırası/BLE seçimidir. Kartta yüklü yazılımın bunlarla uyumu bilinmiyor. Öneri uygulanacaksa firmware atamaları buna uyarlanmalı veya gerçek mevcut atamalar bulunmalıdır. Bu teslimatta firmware okunmadı, değiştirilmedi ve geliştirilmedi.
