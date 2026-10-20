# Güç değerlendirmesi — Routing R1

Son board geometrisinden ölçülen ayrıntılar `Power_Checks.json` ve `Power_Routes.json` içindedir. Tüm hesaplar nominal 35 µm bakır ve 20°C için; ölçüm değildir.

- 5 V netleri EXT_5V/FUSED_5V/BL_5V/BL_POWER boyunca **0,8 mm**, viasız. Dört netin tüm bakır dallarını seri varsayan muhafazakâr üst sınır yaklaşık **34,9 mΩ**; 0,454 A'da yaklaşık **15,9 mV**. Fuse, jumper, ferrit, konnektör/pad kontakları ve GND dahil değildir; gerçek uçtan uca ölçüm yerine geçmez.
- SW toplam dalları **5,54 mm / 0,6 mm / F.Cu / 0 via**. L1 korunarak U1-D1-C4-R7-C9 çekirdeği döndürüldü/taşındı. C4–U1 GND kısa 0,6 mm yerel bağlantı ve iki dönüş via'sıyla desteklenir. LEDK yük dönüşü R7 pozitif padine gelir; R7→FB ayrı **0,2 mm Kelvin dalıdır**. COMP/OVP sense sessiz bölgede tutulur.
- Backlight R7=5,23 Ω: I=0,200/5,23=**38,24 mA** nominal. VFB=196–204 mV ve direnç ±%1 varsayımıyla yaklaşık **37,1–39,4 mA**. Panel değeri modül toplamı 40 mA; 80 mA olarak alınmadı. R7 nominal kaybı ~7,65 mW.
- Panel VF=21,6–27,2 V, 40 mA; en yüksek güç yaklaşık 1,088 W, 33k bleeder dahil 1,110 W. VIN=4,2 V, verim %75 varsayımıyla IIN≈0,353 A. Lmin=17,6 µH ve fsmin=1 MHz ile tepe bobin akımı ~0,45 A. Bu varsayımlar gerçek MPN, verim ve dalga şekli ölçümüyle doğrulanmalıdır.
- LED ana yolları 0,4 mm; FPC yakınında 0,3 mm. BL_LEDA'da 0,2 mm OVP/bleeder dalı, BL_LEDK'da 0,2 mm Kelvin dalı vardır. BL_LEDA bütün dallarını seri sayan üst sınır 124,3 mΩ → 40 mA'da <5,0 mV; BL_LEDK 52,9 mΩ → <2,2 mV. Bu sayılar pad/konnektör/GND ve sıcaklık hariçtir.
- Host/panel/dokunmatik ana beslemeleri **0,3 mm**. Yalnızca J3 3V3 çıkışında 0,9 mm uzunlukta **0,2 mm** neck bulunur; 100 mA örneğinde bu kısa neck'in DC düşümü ~0,22 mV'dur. 0,5 mm pitch pad çıkışında 0,3 mm iz, komşu pad clearance'ını sınırda bırakacağı için neck kullanıldı. VCI/IVDD akımları datasheet'te **TBD**; 100 mA ölçülmüş/garanti yük değildir. Host besleme kapasitesi ve gerilim toleransı kapatılmalıdır.

Legacy IPC-2221 dış katman, 35 µm ve ΔT=10°C kaba tahmini: 0,8/0,6/0,4/0,3/0,2 mm için yaklaşık 2,03/1,65/1,23/1,00/0,74 A. Bunlar IPC-2152 termal doğrulaması, konnektör/pad/via akım sertifikası veya kartın izin verilen yük akımı değildir. Verilen backlight bütçesi bu iz tahminlerinin altındadır. Via plating 20 µm yalnızca direnç hesabı varsayımıdır; üretici kabulü değildir.

OVP nominal eşik 1,242×(1+221k/10k)=**28,69 V**. Bu bir comparator eşiğidir; sert voltaj clamp değildir. TLV3011B kesin parça davranışı, beslemesiz OUT, açılış/kapanış ve yük ayrılması transient'leri fiziksel doğrulama ister. TPS61165 CTRL filtresi/PWM–shutdown ayrımı korunur; yalnızca routing yapılmıştır.

L1 akım/doyma değeri tam MPN ile; C3'nin 30 V'ta etkin kapasitansı ≥4,7 µF hedefi DC-bias eğrisiyle; D1 termal/ileri düşümü, F1/F2 derating ve ferrit DCR'leri gerçek BOM ile doğrulanmalıdır. Nominal model/fiziksel footprint eşleşmesi bu elektriksel parça nitelendirmesinin yerine geçmez.
