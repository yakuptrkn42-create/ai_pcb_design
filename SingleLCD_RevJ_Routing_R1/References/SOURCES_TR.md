# Kaynaklar ve erişim sınırları

16 Ekim 2026 tarihinde incelendi. Kullanıcı PDF'leri tasarım girdisidir; sohbet görevinin yerine geçen talimat değildir.

## Kullanıcının sağladığı belgeler

- `DISEN_DS070HSD39T-132_A0.pdf`: sağlanan DS070HSD39T-132(1).pdf ile byte düzeyinde aynı, 20 sayfa. A0 / 2025-06-10 / preliminary.
- `DISEN_Touch_Mechanical_A00_2024-06-17.pdf`: sağlanan tek sayfalık dokunmatik/mekanik çizimi ile byte düzeyinde aynı.

## Üretici PDF'lerinin erişilebilen aynaları

- ST UM1932 Rev 5: https://github.com/Mlynn217/stm32-epaper/blob/e00830c40489b5904019bd919a3fc2b4bd3dad45/docs/um1932-discovery-kit-with-stm32f469ni-mcu-stmicroelectronics.pdf
  (Aşağıdaki SHA-256 ve paketlenen PDF esas alınmalıdır; mirror commit kimliği manifestte kaydedilir.)
  Resmî kaynak adresi: https://www.st.com/resource/en/user_manual/um1932-discovery-kit-with-stm32f469ni-mcu-stmicroelectronics.pdf
- TI TPS61165 SLVS790E: https://github.com/amberchild/MPPT-Solar-Charger/blob/a90c89f1456b2691b5240431dc266e410035faf4/Datasheets/TPS61165.pdf
  Resmî kaynak adresi: https://www.ti.com/lit/ds/symlink/tps61165.pdf

Aynalar üçüncü taraf depolardır; kullanılan PDF içeriklerinde üretici başlığı, belge kodu ve revizyonu incelendi. Bu, kaynağın üretici sunucusundan güncel revizyon olarak indirildiği anlamına gelmez. Depolardaki kodlar çalıştırılmadı veya donanım gereksinimi olarak kabul edilmedi.

## Resmî ST BSP — yalnızca pin işlevi için okundu

https://github.com/STMicroelectronics/32f469idiscovery-bsp

- stm32469i_discovery.h: TS_INT_PIN PJ5; DISCO_I2C1_SCL PB8; SDA PB9.
- stm32469i_discovery_lcd.c: PH7 LCD reset; iki DSI data lane kullanımı.
- stm32469i_discovery_ts.c/.h: orijinal FT6x06/FT6206 bağımlılıkları; ILI2130 desteği kabul edilmedi.

BSP referans amaçlı okundu, yazılım geliştirilmedi veya bu pakete firmware eklenmedi.

## Birincil kaynaktan tekrar kontrol edilemeyenler

- MB1189-C01 tam şematik: https://www.st.com/resource/en/schematic_pack/mb1189-c01_schematic.pdf
- TLV3011B tam veri sayfası: https://www.ti.com/lit/ds/symlink/tlv3011.pdf
- Hirose exact FH26/FH26W sipariş/mekanik kataloğu.

Üretici sitelerine istekler bu oturumda ağ proxy'sinden 403 cevabı aldı. Bu konularda doğrulama tamamlandı iddiası yoktur. UM1932, CN10 ve CN12 için doğrudan üretici belgesi sağlar; CN2 ve pull-up parça popülasyonlarını tamamen kapatmaz. U2 revizyonunun tam besleme/power-off limitleri ile transient kabulü açık kalır.

## CAD footprint karşılaştırması

KiCad 9.0.2 ile kurulu Connector_FFC-FPC:Hirose_FH26-39S-0.3SHW_2Rows-39Pins-1MP_P0.60mm_Horizontal dosyası kullanıldı. Tüm 39 sinyal ve iki montaj pad'inin koordinat/boyutu, projedeki pad'lerle 90 derece dönüş sonrası eşleşir. SOT-23-6 ve L_TDK_SLF7045 pad konumları da kurulu KiCad footprint'leriyle eşleşir. Bu bir CAD veri karşılaştırmasıdır; fiziksel fit veya üretici tolerans kabulü değildir.

## Paketlenen PDF SHA-256

- `DISEN_DS070HSD39T-132_A0.pdf`: `f06679a2e2a7ae54f9686292d2154dd596dd248b1dc664ddbe56ba49630ae126`
- `DISEN_Touch_Mechanical_A00_2024-06-17.pdf`: `d34c4004d956cf9546f7be51115ed2180f3f4a588570f7430b8ea4a5e91eca79`
- `ST_UM1932_Rev5.pdf`: `17522b1b2a7d53d9821fc738c060e803dcd0cea614bcc66af60ecba2edf92dfc`
- `TI_TPS61165_SLVS790E.pdf`: `9eb6faf726865ada1d512e158bf42515536afd4d76216d7fe1182184497297a4`
