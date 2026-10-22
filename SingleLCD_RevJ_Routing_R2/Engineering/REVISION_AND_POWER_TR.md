# Mevcut tasarımdan R2'ye geçiş

Kaynak 144 iz/via nesnesinin 48'i geometrik olarak aynen korundu. Güç çekirdeği ve onunla çakışan güzergâhlar yeniden çizildi; önceki denetlenmiş routing geometrisinin ilgili bölümleri gerçek konnektör pin koordinatlarıyla eşleştirilerek tekrar doğrulandı. Önceki projenin tamamı yeni dosya yerine geçirilmedi. J1/J2/J3, kart sınırı ve montaj delikleri aynı kaldı. 18 referansın konum/rotasyon farkı Placement_Changes.json içinde; 49 devre parçasına ek olarak dört montaj deliği bulunur.

U1, D1, C3/C4, R7 ve C9 çekirdeği, SW dal toplamını 5,54 mm / 0,6 mm / viasız yapacak şekilde toplandı. R7 üst padine LEDK yük dönüşü; bu padten FB'ye ayrı 0,2 mm Kelvin dalı gider. C4–U1 GND yerel bağlantısı iki dönüş via'sıyla desteklenir. COMP ve OVP ağı SW'den uzak tutulur. C2 VIN bypass U1'e yakındır. Ayrıntılı ölçüler Power_Geometry.json içindedir.

EXT_5V→FUSED_5V→BL_5V→BL_POWER netleri 0,8 mm ve viasızdır. Tüm bakır dallarını seri varsayan muhafazakâr R20 üst sınırı ~34,90 mΩ; 0,454 A varsayımında ~15,8 mV. Bu hesap sigorta/diyot/jumper/pad/konnektör/GND ve sıcaklık artışını içermez. LED ana yolları 0,4 mm; FPC yakınında 0,3 mm. OVP/bleeder ve Kelvin dalları 0,2 mm olup ana güç yolu değildir. Logic ana yolları 0,3 mm; J3 0,5 mm pitch çıkışında kısa 0,2 mm neck vardır. Isıl/akım kapasitesi test edilmedi.

R7=5,23 Ω ile nominal ILED=0,2/5,23=38,24 mA; kayıp ~7,65 mW. Panel 40 mA tipik; kesin maksimum olarak yorumlanmadı. 27,2 V/40 mA LED ve 33k bleeder için ~1,11 W çıkış; VIN=4,2 V, verim=%75 ve Lmin=17,6 µH/fsmin=1 MHz varsayımıyla tepe bobin akımı ~0,45 A. Bu sayılar parça seçimi ve yük ölçümüyle kapanır; generic 22 µH yeterli satın alma tanımı değildir. L1'in TDK legacy serisinde stok/EOL kontrolü gerekir.

Elektriksel topoloji ve 159 pin–net üyeliği korunur. R13 2,2k→8,2k/%1: TI SLVS790E §9.2.1.2.4 yanlış EasyScale ACK sink akımını ≤500 µA önerir; 3,6 V / 8,118k≈443 µA. C3 10 µF/50 V kaldı; X7R ve gerçek DC-bias niteliği belirtildi. J6'nın ters yazısı düzeltildi: pin1 +5 V, pin2 GND; konnektör gövdesini kart içine almak için 3 mm kaydırıldı. J4 alanı gerçek üç telli arayüzü gösterir: PC6/PB12/GND; pad eşleşmesi değişmedi. Üç tek kullanımlı global etiket local yapıldı; yalnız hiyerarşik net adları değişir, bağlantılar değişmez. Üretim kuralları gevşetilmedi ve DRC istisnası eklenmedi.

OVP=1,242×(1+221k/10k)=28,69 V nominaldir; sert clamp değildir. Açılış/açık yük/başlatma testleri, panel timing/akım ve touch besleme toleransı önceki şematik incelemede açık kalan koşullardır.
