# Kaynaklar / Rev K

Bu revizyonda yeni LCD için yalnızca kullanıcının sağladığı tek sayfalık çizim mevcut. Kullanıcı, ek elektriksel belge bulunmadığını bildirdi. Belgeler tasarım girdisidir; görev talimatı olarak ele alınmadı.

- LCD-A: DS070HSD39T-132 A0 preliminary, 20 sayfa. Mekanik ve LED çizimi s.6 (A00 2024-06-17); pin tablosu s.7; VCI/LED s.8; touch s.9. LED çizimi 8 seri × 2 paralel gösterir.
- LCD-B: kullanıcının DS0700BOE1A39CO-0180A（2026.9.14）(1).pdf dosyası, 1 sayfa. A01, 2026-09-14; ilk baskı 2026-09-07, A01 notu touch cable position değişikliğidir. LED çizimi 4 seri × 2 paralel, VF=12V IF=40mA verir. Dosya adındaki CO/C0 yazımı için exact sipariş/model kodu tedarikte teyit edilmelidir; bu dosya ve çizim revizyonu incelemenin esas girdisidir.
- Her iki çizimin ayrı 6-pin touch tablosu: 1 GND, 2 SCL 3.3V, 3 SDA 3.3V, 4 RST, 5 INT, 6 VDD 3.3V. J3 host pin tablosuyla karıştırılmamalıdır.
- Rev J incelemesinin ST UM1932 Rev5 ve TI TPS61165 SLVS790E PDF'leri, teslim edilen özgün Rev J arşivinin References klasöründe korunur. TPS61165 FB/PWM/L-C değerleri ve ST host pinleri için bu önceki inceleme kaynaklarına dayanıldı. Bu revizyonda üretici sitelerinden yeni tam LCD-B/TLV3011B veri sayfası elde edildiği iddia edilmez. Exact U2 limitleri ve geçici rejim kabulü açık kalır.

Yeni panelde VCI ve 30/31 VDD aralıkları, LED VF maksimumu/mutlak sınırları, toplam IF yorumu ve kontrolcü timing verileri eksiktir. Pin numarası eşleşmesi bu bilgilerin onayı sayılmaz.

## Girdi bütünlüğü

- `DISEN_DS070HSD39T-132_A0.pdf`: SHA-256 `f06679a2e2a7ae54f9686292d2154dd596dd248b1dc664ddbe56ba49630ae126`
- `DS0700BOE1A39CO_0180A_A01.pdf`: SHA-256 `55faff20127db90af8645c043a11ceaa499ca581203fb2c0e2fbc793655a3999`
- `Submitted_Schematic_RevJ_Review.zip`: SHA-256 `925fb849cac3db659a746c015e225028f17735db9fd9011a82d92856d0ad4214`

Yüklenen Rev J arşivinin tüm dosya üyeleri, çıkarılmış kaynaklarıyla byte düzeyinde karşılaştırıldı: değişiklik yok. Aktif Rev K ayrı klasöre kaydedildi. Arşivdeki PCB/autosave/yedekler değiştirilmedi.
