# BS241 veri sayfasına göre düzeltilmiş tam proje — V2

Bu sürüm, kullanıcının sağladığı **BS241_supplied_datasheet.pdf** belgesini
esas alır. Önceki aktif HIGH varsayımı düzeltildi. Optik sensör ve motor sürücüsü
korundu; sensörler motoru durdurmaz veya hızını sınırlamaz.

## Önceki bağlantı neden kontrol edilmeli?

Kullanıcı: 5 V besleme, kırmızı +, siyah -, beyaz A3.
PDF sayfa 2: **kırmızı Vcc, mavi GND, beyaz çıkış**.
PDF'de üç kablo gösterilir; kullanıcının bildirdiği dördüncü **siyah kablonun
işlevi belirtilmez**. Siyahı GND kabul etmek bu belgeyle doğrulanamaz. Dört
kablolu varyantın etiketini/bağlantı şemasını doğrulamadan siyaha veya maviye
rastgele görev atamayın. Besleme kapalıyken bağlantıyı kontrol edin.

PDF sayfa 1:

| Özellik | Belgedeki değer |
|---|---|
| Besleme | 4,5–5,5 V, tipik 5 V |
| Akım | tipik 10 mA, en fazla 30 mA |
| **Hava/kabarcık var** | **LOW: 0,2–0,5 V** |
| **Hava/kabarcık yok** | **HIGH: en az 2,4 V, tipik 4,3 V** |
| Tipik yanıt süresi | 50 µs |
| Önerilen hortum | dış çap 3,5–4,0 mm, yumuşak hortum |

Yazılımın ters polaritesi tek başına çalışmama nedenini kanıtlamaz; kablo
referansı, besleme ve çıkış seviyesi de ölçülmelidir. Karta fiziksel test yapılmadı.

## Bağlantı — yalnızca PDF ile aynı kablo düzeni doğrulandığında

| Sensör/kart sinyali | Bağlantı |
|---|---|
| BS241 kırmızı (Vcc) | Regüle +5 V |
| BS241 mavi (GND) | 5 V kaynağı GND ve STM32 GND ortak |
| BS241 beyaz (Output) | Uygun **terslemeyen TTL→3,3 V tamponun girişine** |
| Tamponun 3,3 V çıkışı | **Arduino A3 / PC4** |
| Siyah | PDF'de tanımsız; dört kablolu varyant için üretici/etiket bilgisi gerekli |
| Optik dijital çıkışı | **Arduino A4 / PC5**, 0–3,3 V sinyal; çalışan bağlantı korunur |

Beyaz çıkışı, gerilim uyumluluğu doğrulanmadan PC4'e doğrudan bağlamayın.
Bu proje için 0–3,3 V dijital sinyal kullanın. Seviye dönüştürücü **girişte 5 V
TTL sinyali kabul etmeli**, en az 2,4 V HIGH değerini güvenilir algılamalı,
0,5 V LOW değerini LOW kabul etmeli ve çıkışta 3,3 V vermelidir.

Uygun bir terslemeyen tampon sınıfına örnek: **SN74LVC1G125**. Kullanacağınız
üretici/ürün varyantının veri sayfasında 5 V toleranslı giriş ve 3,3 V beslemede
uygun TTL eşiklerini kontrol edin. Mantıksal bağlantı: VCC=3,3 V, GND=ortak GND,
/OE=GND, A=beyaz çıkış, Y=PC4; VCC–GND arasına parçanın yanında 100 nF bypass
kondansatörü. Fiziksel bacak numaralarını satın alınan paketin çiziminden alın.
Bu tampon **sinyali terslememeli**; yazılım LOW=kabarcık varsayar.

Basit bir direnç bölücüyle yalnızca tipik 4,3 V değerini esas almak doğru değildir:
BS241'in garanti edilen HIGH alt sınırı 2,4 V'tur; bölünmüş seviye STM32'nin
HIGH eşiğinin altına düşebilir. Donanım arayüzü fiziksel ölçümle doğrulanmalıdır.

## Yazılım davranışı

- **PC4 LOW → HAVA KABARCIĞI + kartın kırmızı LED3'ü (PD5).**
- **PC4 HIGH → hava sinyali yok.** Son algılamadan sonra uyarı yaklaşık 2 sn tutulur.
- PC4 kesmesi **düşen kenar** kullanır. Örneklemeler arasında biten kısa LOW
  darbesi hatırlanır. Ayrı bir darbe sayacı veya kabarcık hacmi ölçümü değildir.
- PC5 LOW → optik hedef var + yeşil LED1 (PG6). PC5 HIGH → hedef yok.
  Optik giriş 20 ms kararlılık filtresi kullanır. Çalışan optik bağlantıyı değiştirmeyin.
- Sensör görevi 1 ms RTOS tick aralıkla örnekler; kesme motorun önüne geçmez
  (motor öncelik 6; BS241 EXTI4 öncelik 7). GUI yaklaşık 100 ms aralıkla güncellenir.
- Sensör yolu motor alarm/durdurma fonksiyonlarını çağırmaz. Motorun PH6 STEP,
  PG10 DIR pinleri ve motor kaynak dosyaları değişmedi.
- Boşta kalan giriş pull-up nedeniyle HIGH okunabilir. **Bu bağlantı varlığı
  veya kablo kopması teşhisi değildir; bağlı olmayan BS241 hava yok gibi okunabilir.**
- Görev verisi 100 ms'den eskiyse arayüz okuma bekliyor gösterir. Bu da sensörün
  fiziksel olarak bağlı/sağlam olduğunu doğrulamaz.

Varsayılan ayar `Core/Inc/sensor_config.h`:

```c
#define SENSOR_AIR_ACTIVE_LEVEL 0U
#define SENSOR_AIR_POLARITY_CONFIRMED 1U
#define SENSOR_AIR_HOLD_MS 2000U
```

`.ioc` içindeki PC4 kenarı da `GPIO_MODE_IT_FALLING` olarak düzeltildi.

## Açma ve yükleme

1. Tam proje ZIP'ini tamamen çıkarın; önceki dosyalarla birleştirmek gerekmez.
2. `TouchGFX/MyApplication_9.touchgfx` dosyasını TouchGFX Designer 4.26 ile açın.
3. Bilgisayarınızdaki çalışan Run Target / ST-LINK / QSPI ayarlarıyla yükleyin.
   Bu ortamda Designer Generate Code / Run Target ve fiziksel yükleme test edilmedi.
4. Hazır dosyalar `Firmware/VENA_F469_Sensors.elf` ve `.hex` içindedir. HEX dahili
   Flash + harici QSPI içerir; uygun QSPI external loader gerekir.

Runtime ekranları ortak `VenaPanel` / `VenaScene.cpp` üzerinden çizilir. Designer
referans yerleşimleri canlı sensör yerleşimi değildir. Mevcut projenin yapısı
korundu. STM32CubeIDE `.project` linked resource'ları ve tüm kütüphaneler dahildir.

## Doğrulama

```sh
python3 Validation/run_sensor_tests.py
python3 Validation/build_host.py
(cd Validation/host_build/runtime && ../vena_headless test ../click.raw)
python3 Validation/build_arm.py /path/to/arm-toolchain/bin
```

Varsayılan BS241 polaritesini sabit LOW bekleyen regresyon, HIGH/LOW alternatif
ayarlar, ham mod, optik titreşim, kısa darbe, 2 sn tutma, stale veri ve tick taşması
kontrol edildi. Sensörlerin start/run/pause/resume/bolus/stop/KVO durumlarında
motor komutunu değiştirmemesi test edildi. ASan/UBSan açık; bu ortamın ptrace
sınırlaması nedeniyle test komutunda `ASAN_OPTIONS=detect_leaks=0` kullanıldı.
Gerçek TouchGFX kütüphanesiyle tıklama testi ve ARM derleme/link tekrar çalıştırıldı.

Gerçek sensörde, doğru kablo eşlemesi ve besleme doğrulandıktan sonra beyaz
çıkışı sensör GND'sine göre ölçün: sıvı dolu uygun hortumda HIGH; aynı hortumda
hava olduğunda LOW beklenir. Tampon çıkışında PC4'e ulaşan seviyeler 0/3,3 V
olmalıdır. Yazılım sensörü fiziksel olarak çalışır hale getirmez; kablo/sinyal
kontrolü ve kart üzerindeki motor zamanlaması ölçümü ayrıca yapılmalıdır.
