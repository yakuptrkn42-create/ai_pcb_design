# VENA F469 — BS241 veri sayfasına göre düzeltilmiş V2

**Güncel tek ZIP tam proje:** [VENA_F469_BS241_Duzeltilmis_Tam_Proje.zip — indir](https://github.com/yakuptrkn42-create/ai_pcb_design/raw/refs/heads/codex/vena-f469-sensor-download/Downloads/VENA_F469_Sensors/VENA_F469_BS241_Duzeltilmis_Tam_Proje.zip)

[Bağlantı, değişiklik ve test notları](BS241_V2_Baglanti_TR.md)

ZIP'i tamamen çıkarın; `TouchGFX/MyApplication_9.touchgfx` dosyasını Designer
4.26 ile açın. Kaynaklar, kütüphaneler ve güncel ELF/HEX dahildir; başka paket
birleştirmek gerekmez. HEX için karta uygun QSPI external loader gerekir.

Verilen BS241 veri sayfasına göre **LOW=kabarcık, HIGH=kabarcık yok**.
Önceki aktif HIGH sürümler yerine bu V2'yi kullanın. PC4 EXTI kenarı düşendir.
Optik A4/PC5 ve motor korunmuştur. Sensörler motoru durdurmaz.

**Kablolama:** PDF kırmızı=Vcc 5 V, mavi=GND, beyaz=çıkış gösterir. Kullanıcının
sensöründeki ek siyah kablo bu belgede yoktur; dört kablolu varyantın görevleri
üretici/etiket bilgisiyle doğrulanmalıdır. Beyaz çıkış HIGH tipik 4,3 V, minimum
2,4 V'tur; uygun terslemeyen TTL→3,3 V arayüz üzerinden Arduino A3/PC4'e bağlanır.

ARM 382 kaynakla hatasız derlendi ve linklendi; 8 sensör test paketi, motor
regresyonu ve gerçek TouchGFX kütüphanesiyle arayüz testi geçti. Fiziksel sensör,
kart üzerinde yükleme veya Designer Run Target bu ortamda test edilmedi.

Eski ZIP dosyaları tarihsel olarak tutulur; BS241 polaritesi için güncel değildir.
