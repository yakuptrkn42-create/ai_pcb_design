# STM32F469I-DISCO / DISEN — Şematik Rev J

Rev J, laboratuvarda GUI ve dokunmatik denemesi için hazırlanmış ayrı bir şematik revizyondur. Gerçek KiCad dosyaları düzenlendi; PCB veya yazılım değiştirilmedi. Bu paket üretim onayı değildir; açık doğrulama maddeleri mühendislik raporunda listelenmiştir.

- **Açılacak proje:** `Project/STM32F469_DISEN_RevJ.kicad_pro` — KiCad 9.
- **Şematik PDF:** `PDF/STM32F469_DISEN_RevJ_Schematic.pdf` — üç A3 sayfa.
- **Komponent listesi:** `BOM/BOM_RevJ.csv` — 49 satır, R1/R2 DNP dahil.
- **İnceleme:** `Engineering/ENGINEERING_REVIEW_TR.md` ve `PDF/Engineering_Review_RevJ.pdf`.
- **ERC:** `Verification/ERC_RevJ.json` ve `Verification/ERC_RevJ.txt` — **0 hata, 3 uyarı**.
- **Elektriksel karşılaştırma:** `Verification/Electrical_Change_Audit.json`.
- **Pin tabloları:** `Verification/LCD_39_Pin_Audit.csv`, `Verification/Host_CN10_Audit.csv`.
- **Özgün teslim:** `Original/Submitted_RevI_Schematic.zip` — yüklediğiniz arşiv değiştirilmeden korunmuştur.

ZIP'in tamamını tek klasöre çıkarın; yalnızca `.kicad_sch` dosyasını ayırmayın. Sembol/footprint kütüphaneleri proje içinde ve taşınabilirdir. Standart GND/PWR_FLAG sembollerinin kullanılan kopyaları da paketlenmiştir.

## Uygulanan başlıca değişiklikler

1. U2 pin 6 ve C13 pin 1, `HOST_3V3` yerine `BL_POWER` ile besleniyor. Böylece OVP'nin besleme kaynağı, haricî backlight gücüyle birlikte geliyor. U2'nin ayrıntılı veri sayfası ve geçici rejim doğrulaması hâlâ kapanış maddesidir.
2. J2'nin FH26W adlandırması, panelin önerdiği **FH26-39S-0.3SHW** temel parça adına düzeltildi. Footprint kimliği güncellendi; pad koordinatları ve boyutları değişmedi. Sipariş eki ve gerçek flex eşleşmesi ayrıca kontrol edilmelidir.
3. 52 güç portu uygun güç sembollerine dönüştürüldü. `HOST_3V3`, `HOST_TP_3V3`, `LCD_VCI`, `TP_VDD` ve ara 5 V hatları ayrı kaldı. Eksik güç sürücüsü bildirimleri `PWR_FLAG` ile giderildi; bağlantı noktaları 50 mil ızgaraya hizalandı.

49 fiziksel komponent ve 57 net korundu. 172 fiziksel pin bağlantısının yalnızca yukarıdaki iki besleme bağlantısı değişti. R7=5,23 Ω, nominal 38,24 mA LED akımı ve diğer pasif değerler korundu.

Üç ERC uyarısı yalnızca tek kez kullanılan `BL_SW`, `BL_COMP`, `OVP_SENSE` global etiketleridir. Bu denetim kaynak projede kapalıydı; Rev J'de açıldı. Hata gizlemek için kural gevşetilmedi veya exclusion eklenmedi.

## Önceki PCB ile ilişki

Yüklenen arşivdeki PCB yerleşim dosyasıdır: 53 footprint, 0 iz/via/zone. Depodaki önceki Rev I routing dosyası da yalnızca okunarak karşılaştırıldı. İkisinde de **U2.6 ve C13.1 eski nete bağlıdır; J2 footprint kimliği eskidir**. Rev J'ye geçişte PCB ECO gerekir. Bu aşamada PCB düzenlenmedi ve güncel şematikle eşleşmeyen bir PCB aktif proje içine konmadı. Eski Gerber'ler Rev J üretim çıktısı olarak kullanılmamalıdır.

Üretimden önce başlıca açık konular: TLV3011B birincil veri sayfası kontrolü, OVP açılış/açık yük ölçümü, LCD/touch akım bütçesi, touch besleme toleransı, RESX/ILI2130 zamanlaması ve FPC fiziksel eşleşmesi. Fiziksel çalışma garantisi verilmez.
