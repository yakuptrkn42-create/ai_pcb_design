# VENA F469 — optik ve BS241 sensör güncellemesi

**Tek ZIP tam proje:** [VENA_F469_Sensor_Tam_Proje.zip — indir](https://github.com/yakuptrkn42-create/ai_pcb_design/raw/refs/heads/codex/vena-f469-sensor-download/Downloads/VENA_F469_Sensors/VENA_F469_Sensor_Tam_Proje.zip)

Bu tam arşiv kaynakları, kütüphaneleri, sensör değişikliklerini ve hazır firmware'i
birlikte içerir. ZIP'i tamamen çıkarın; `TouchGFX/MyApplication_9.touchgfx`
dosyasını TouchGFX Designer 4.26 ile açın. Başka paket birleştirmeniz gerekmez.
Karta yükleme için bilgisayardaki mevcut Run Target / ST-LINK / QSPI ayarları
gereklidir; fiziksel karta yükleme bu ortamda test edilmedi.

Aşağıdaki küçük paketler yalnızca mevcut projesine güncelleme uygulamak isteyenler içindir:

- [Kod + hazır ELF/HEX firmware — indir](https://github.com/yakuptrkn42-create/ai_pcb_design/raw/refs/heads/codex/vena-f469-sensor-download/Downloads/VENA_F469_Sensors/VENA_F469_Sensor_Guncelleme.zip)
- [Yalnız kaynak güncellemesi — indir](https://github.com/yakuptrkn42-create/ai_pcb_design/raw/refs/heads/codex/vena-f469-sensor-download/Downloads/VENA_F469_Sensors/VENA_F469_Sensor_Kod.zip)
- [Bağlantı, kurulum ve test notları](SENSOR_ENTEGRASYONU_TR.md)

Bunlar güncelleme paketleridir; kullanıcının sağladığı iki orijinal arşivden
birleştirilen `VENA_F469_TouchGFX_3` klasörünün üzerine uygulanır.
Tam pakette `Firmware/VENA_F469_Sensors.elf` ve birleşik HEX bulunur.
HEX dahili Flash ve harici QSPI içerir; karta uygun QSPI external loader kullanın.

Optik: Arduino A4/PC5; 0 = hedef var, yeşil LED1 yanar.
BS241: Arduino A3/PC4; kullanıcı bilgisine göre 1 = hava, kırmızı LED3 yanar.
Sensörler motoru durdurmaz veya hızını değiştirmez. Hava uyarısı 2 saniye tutulur.

ARM derlemesi, sensör testleri, motor regresyonu ve gerçek TouchGFX kütüphanesiyle
arayüz testleri geçti. Fiziksel kart ve sensörle test yapılmadı. BS241'in
mavi/kırmızı/siyah/beyaz kablo görevleri ve elektriksel çıkış seviyesi henüz
doğrulanmadı; renge göre bağlantı yapmayın. MCU girişine 0–3,3 V uygulanmalıdır.

Bu dal yalnızca indirme paketlerini ekler; deponun PCB dosyalarını değiştirmez.
