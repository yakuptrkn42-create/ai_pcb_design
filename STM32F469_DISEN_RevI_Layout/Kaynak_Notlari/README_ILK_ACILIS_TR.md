# STM32F469 DISEN Rev I – Açılış

- KiCad 9 ile `STM32F469_DISEN_RevI.kicad_pro` dosyasını açın. Şematik: ana sayfa + `Backlight.kicad_sch`.
- Gerçek PCB layout/routing dosyası yoktur. Önce elektronik ERC (KiCad → Inspect → Electrical Rules Checker) ve pin/footprint orientation denetimi yapın.
- `REV_H_to_REV_I.md`, `ERC_REV_I.txt`, `BOM_REV_I.csv`, `PIN_MAPPING_REV_I.md` ve `RevI_Schematic.pdf` dosyalarını inceleyin.
- R12 **0R/FIT**, R1 ve R2 **DNP**. Kartın arka aydınlatma kısmı harici **regüle 5 V** ile beslenir, MCU 5V çıkışından beslenmez.
- Rev I, koruma için U2 ile CTRL pinini düşük tutar; 30V limitini doğrulayacak tek başına yeterli bir koruma/garanti değildir.
- Host orijinal LCD FPC bağlantısı enerjisizken kaldırılmalıdır. Resmî MB1189-C01 şeması baz alındı, fiziksel board revision ve FPC contact yüzü kontrol edilmeli.
- Bu prototip dosyası üretime onaylı değildir.
