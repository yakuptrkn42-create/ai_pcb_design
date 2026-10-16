# STM32F469 / DISEN · Rev I — Routing R1

Gerçek KiCad PCB üzerinde routing tamamlandı. Son doldurulmuş kartta **0 DRC ihlali, 0 açık bağlantı, 0 şematik eşleşme sorunu ve 0 ERC ihlali** bulunuyor. Şematik, 57 net / 172 pin-net üyeliği ve onaylanan komponent konumları korundu.

Kart: **46 × 40 mm, dört bakır katman, nominal 1,6 mm**. İki iç katman GND referansıdır. Bağımsız, kablolu adaptör düzeni korunmuştur.

- [Kısa inceleme PDF'i](Routing_Review_TR.pdf)
- [KiCad projesi](Project/STM32F469_DISEN_RevI.kicad_pro) · [Route edilmiş PCB](Project/STM32F469_DISEN_RevI.kicad_pcb)
- [Üst görünüm](Views/01_PCB_Top.png) · [Alt görünüm](Views/02_PCB_Bottom.png) · [3D görünüm](Views/03_PCB_3D_Isometric.png)
- [MIPI ayrıntısı](Views/09_MIPI_Detail.png) · [Katman yapısı ve mühendislik değerlendirmesi](Engineering/ENGINEERING_REVIEW_TR.md)
- [Gerber](Manufacturing/Gerber) · [PTH / NPTH drill](Manufacturing/Drill) · [IPC-D-356 test netlisti](Manufacturing/STM32F469_DISEN_RevI.d356)
- [DRC raporu](Verification/DRC.txt) · [Bağımsız üretim çıktısı kontrolü](Verification/manufacturing_audit.json)

ZIP'i tamamen çıkardıktan sonra `Project/STM32F469_DISEN_RevI.kicad_pro` dosyasını KiCad 9 veya daha yeni sürümde açın. Yerel footprint, sembol ve 3D kütüphaneleri paketin içindedir; klasör yapısını koruyun. R1/R2 DNP'dir.

Bu teslim **üretim öncesi mühendislik incelemesi** içindir. Üretici stackup'ı, empedans toleransı ve FPC/flex mekanik eşleşmesi henüz doğrulanmamıştır. 99,3 Ω sonucu nominal hesap değeridir. J1/J2/J3 ve L1'in 3D gövdeleri nominal hacim modelleridir. Bu açık noktalar ve güç hesabının sınırları mühendislik raporunda belirtilmiştir.
