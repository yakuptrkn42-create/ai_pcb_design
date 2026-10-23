# Optik + BS241 sensör güncellemesi

Bu sürüm sensörleri **yalnızca izleme ve gösterim** için kullanır. Sensör değeri
START, STOP, PAUSE, RESUME, bolus, KVO veya motor frekans komutunu değiştirmez.
Mevcut motor limitleri ve heartbeat koruması korunur. `motor_control.c/.h`
dosyaları alınan projeyle aynıdır.

## Bağlantılar

| İşlev | STM32F469I-DISCO bağlantısı | Gösterim |
|---|---|---|
| Optik sensörün **3,3 V seviyesine uyarlanmış** dijital çıkışı | Arduino **A4 / PC5** | 0 = hedef var; 1 = hedef yok |
| BS241'in **3,3 V seviyesine uyarlanmış** dijital çıkışı | Arduino **A3 / PC4** | Kullanıcının bilgisine göre 1 = hava, 0 = hava sinyali yok |
| Optik LED | Kart üzerindeki **LED1 / PG6 / yeşil** | Hedef varken yanar |
| Hava LED | Kart üzerindeki **LED3 / PD5 / kırmızı** | Hava sinyalinde yanar, sinyal bitince 2 sn tutulur |
| Referans | STM32 GND ile arayüzün ortak GND'si | İzole arayüz kullanılıyorsa kart tarafındaki referans |

Motor pinleri **PH6 (STEP)** ve **PG10 (DIR)** aynıdır. Ekran, dokunmatik,
SDRAM, QSPI ve projenin SD kart pinleriyle çakışma yoktur. Optik giriş polling
kullanır; PC5 için EXTI açılmaz ve PJ5 dokunmatik kesmesiyle çakışmaz.
Arduino eşlemesi için kaynak:
https://github.com/ARMmbed/mbed-os/blob/master/targets/TARGET_STM/TARGET_STM32F4/TARGET_STM32F469xI/TARGET_DISCO_F469NI/PinNames.h
Kartınızın sürümündeki A3/A4 işaretlerini bağlantıdan önce kontrol edin.

**Elektriksel bilgi henüz doğrulanmadı:** BS241 besleme gerilimi, kablo renkleri,
pin sırası ve çıkışın push-pull / açık kolektör / başka tip oluşu için belge
verilmedi; üretici sayfasına bu ortamdan erişilemedi. Bu nedenle sensör besleme
ve kablo rengi bağlantısı tahmin edilmedi. 1= hava bilgisi kullanıcı beyanıdır.

Kullanıcının bildirdiği BS241 kablo renkleri: **mavi, kırmızı, siyah, beyaz**.
Renklerin besleme/GND/çıkış görevleri henüz doğrulanmadı; renklerden bağlantı
ataması yapılmamalıdır. Etiket veya üretici bağlantı çizimi gereklidir.


- STM32 girişinde LOW yaklaşık 0 V, HIGH yaklaşık 3,3 V olacak şekilde bağlantı
  hazırlayın. Sensör beslemesini STM32 sinyal pini üzerinden vermeyin.
- 5/12/24 V çıkışı doğrudan bağlamayın; çıkış tipine uygun seviye dönüştürücü veya
  izole giriş kullanın. Açık kolektör çıkış ancak üretici şartları uygunsa kart
  tarafında 3,3 V pull-up ile kullanılabilir. Dahili pull-up kablo gürültüsü ve
  bilinmeyen çıkış tipinin yerini tutmaz; harici arayüz donanımı doğrulanmalıdır.
- Kart LED'leri kullanılır; bu sürüm için harici LED bağlamak gerekmez.
- Girişlerde pull-up vardır. **Boşta kalan giriş HIGH okunabilir.** İki telli
  dijital okumadan kablo kopması, sensör arızası veya fiziksel bağlantı varlığı
  ayırt edilemez. Bağlanmamış BS241 girişinin uyarı vermesi bu nedenle mümkündür;
  hiçbir durumda bu uyarı motoru durdurmaz.

## Yazılım davranışı

- `Sensor_Init()` GPIO ve EXTI4'ü başlatır. Girişler ilk 20 ms yerleşirken arayüz
  “okuma bekleniyor” gösterir; bu süre motoru kilitlemez.
- Mevcut defaultTask, 1 RTOS tick aralıkla `Sensor_Poll()` çağırır. Projede tick
  1 ms'dir. Optik sinyalin değişmesi için yeni seviyenin 20 ms kararlı kalması
  gerekir. Filtre süresince önceki kararlı seviye gösterilir.
- BS241'de optik filtre kullanılmaz: aktif HIGH kenarı EXTI4 ile yakalanır.
  Darbe iki görev örneklemesi arasında bitse bile kesme bayrağı hatırlanır.
  Bu bir darbe sayacı değildir; yakın darbeler tek uyarıda birleşir. Fiziksel en
  kısa algılanabilir darbe ve gürültü dayanımı kart üstünde ölçülmelidir.
- Hava HIGH kaldıkça uyarı/LED devam eder. Son algılamadan sonra 2 saniye tutulur.
  Dokunmatik Model güncellemesi yaklaşık 100 ms'de durumu ekrana taşır.
- Sensör kesmesi önceliği 7'dir; motor TIM12 kesmesi önceliği 6 ile daha öndedir.
  Kesmede yalnızca bir atomik bayrak yazılır. Dokunmatik için mevcut HAL EXTI
  callback'i korunur ve PC4 olayını bu bayrağa yönlendirir.
- GPIO okuma ve LED yazma görevde yapılır. Yeni sensör yolunda `HAL_Delay`,
  dosya erişimi, motor komutu, GUI çağrısı veya bekleme döngüsü yoktur.
- GUI'ye seviyeler ve uyarı tek atomik durum kelimesiyle yayımlanır. Son görev
  örneklemesi 100 ms'den eskiyse ekranda eski değer normal gibi gösterilmez.
  Bu, kablo teşhisi değildir; LED'ler görevin son yazdığı fiziksel durumda kalır.
- Uyarı ana sayfada, diğer sayfaların başlığında ve kilitli ekranda görünür.
  “Hava Algılama” ve “Sensör Durumu” sayfaları ham seviyeyi de gösterir.
- Dijital BS241 değerinden µL hacim çıkarılmadığı için önceki hava hacmi ayarları
  bu sayfada gösterilmez. Sensörle motor durduran `raiseAlarm()` çağrısı yapılmaz.

## Ayarlar

`Core/Inc/sensor_config.h` tek sensör ayar dosyasıdır:

```c
#define SENSOR_AIR_ACTIVE_LEVEL 1U          // kullanıcının verdiği bilgi
#define SENSOR_AIR_POLARITY_CONFIRMED 1U   // hava etiketi açık
#define SENSOR_OPTICAL_DEBOUNCE_MS 20U
#define SENSOR_AIR_HOLD_MS 2000U
```

Hava/çıkış mantığı ters çıkarsa `SENSOR_AIR_ACTIVE_LEVEL` değerini 0 yapın ve
yeniden derleyin. Emin değilseniz `SENSOR_AIR_POLARITY_CONFIRMED=0` ile ham 0/1
modunu kullanın; bu mod hava etiketi vermez, kırmızı LED ham HIGH seviyesini
gösterir. `.ioc` içindeki PC4 EXTI kenarını da değiştirin. Başlangıçtaki
`Sensor_Init()` her zaman derlenen ayara göre kenarı yeniden yapılandırır.

## Projeye uygulama ve derleme

1. Çalışan projenizin yedeğini alın. İki orijinal ZIP'i aynı klasörde birleştirin.
2. `VENA_F469_Sensor_Guncelleme.zip` içindeki `VENA_F469_TouchGFX_3` klasörünü
   mevcut aynı adlı klasörün üstüne çıkarın; dosya değişimlerini uygulayın.
   `SENSOR_DEGISIKLIKLER.json` yalnızca bu güncellemenin dosyalarını listeler.
3. STM32CubeIDE'de projeyi yenileyin veya `STM32CubeIDE/.project` üzerinden
   yeniden içe aktarın. **Clean Project → Build Project** uygulayın.
   `sensor_monitor.c` için linked resource eklendi. Varsayılan derleyici ayarı
   Cortex-M4 / hard-float; motor ve TouchGFX kütüphanesi aynı kalır.
4. Hazır dosyalar güncellemenin `Firmware` klasöründedir:
   `VENA_F469_Sensors.elf` ve birleşik `VENA_F469_Sensors.hex`.
   HEX **dahili Flash + harici QSPI** bölümlerini içerir. Mevcut çalışan projede
   kullandığınız karta uygun QSPI external loader ve programlama ayarlarını
   kullanın. HEX'i tek bir ham BIN'e çevirmeyin. Bu ortamdan fiziksel yükleme
   yapılmadı; yeniden derleme gerekirse kaynak sürümünü kullanın.

Runtime ekranları `TouchGFX/gui/src/vena/VenaScene.cpp` ve ortak `VenaPanel`
üzerinden çizilir; mevcut projenin mimarisi korunmuştur. `.touchgfx` dosyasındaki
Designer referans ekranları bu güncellemenin canlı sensör yerleşimini içermez.
Designer'da Generate Code yapıldığında mevcut runtime kaynaklarını ve CubeIDE
linked resource'larını koruyun. `.ioc` pinleri ve EXTI4 kaydı eklendi, ancak bu
ortamda CubeMX/Designer ile yeniden üretim test edilmedi.

## Doğrulama ve tezgah denemesi

Kaynak kökünde:

```sh
python3 Validation/run_sensor_tests.py
python3 Validation/build_host.py
(cd Validation/host_build/runtime && ../vena_headless test ../click.raw)
python3 Validation/build_arm.py /path/to/arm-toolchain/bin
```

Sensör testleri gerçek C sürücüsünün donanım yolunu sahte HAL sınırıyla ve
gerçek model/sahne kodunu simülatörle test eder. HIGH/LOW aktif polariteler,
ham mod, optik titreşim, örneklemeler arasında biten hava darbesi, 2 sn tutma,
stale veri, 32-bit tick taşması ve motorun start/run/pause/resume/bolus/stop/KVO
davranışı kapsanır. ASan/UBSan açıktır. Gerçek TouchGFX kütüphanesiyle ekran
derleme/link ve tıklama testi ayrıca çalıştırılmıştır.

Kartta, sensörleri takmadan önce güvenli 0/3,3 V test sinyaliyle:

1. PC5'i LOW/HIGH yapın: yeşil LED ve optik yazısı yaklaşık 20 ms filtreyle
   değişmeli; PC4 LOW iken hava yazısı normal olmalı.
2. PC4'ü HIGH yapın: hava yazısı ve kırmızı LED yanmalı. LOW yaptıktan sonra
   yaklaşık 2 sn içinde normale dönmeli. Besleme veya çıkış pini kısa devre
   edilerek test yapılmamalıdır; sadece uygun dijital test kaynağı kullanın.
3. Aynı denemeyi motor çalışırken yapın. STEP frekansı ve darbe genişliğini
   osiloskop/lojik analizörle kontrol edin; sensörler START/PAUSE/STOP oluşturmamalı.
4. Önce 100, sonra 2000 mL/h mevcut tezgah komutunda; bolus, duraklat/devam,
   KVO ve ekran kilidi sırasında geçişleri deneyin.
5. Gerçek sensör çıkışını önce ölçün; sonra uygun arayüzle bağlayarak hava/sıvı
   ve optik hedef durumlarının ham 0/1 değerlerini doğrulayın.

Buradaki testler fiziksel kart, gerçek BS241, EMI veya motor zamanlama ölçümü
yerine geçmez. Bu sürümün sensör yolu bir motor güvenlik kilidi değildir.
