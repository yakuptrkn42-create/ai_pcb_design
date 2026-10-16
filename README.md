# STM32F469 / DISEN — Rev I, Layout 1

Elektriksel içerik korunarak üç sayfada yeniden düzenlenmiş KiCad 9 şematiği.

## Dosyaları indir

- [KiCad proje paketi (ZIP)](STM32F469_RevI_Professional_KiCad.zip)
- [Düzenlenmiş şematik (PDF)](STM32F469_RevI_Professional.pdf)
- [Düzenleme ve doğrulama raporu](STM32F469_DISEN_RevI_Layout/README_TR.md)

Dosya sayfasındaki **Download raw file / Download** simgesine tıklayın. Tüm depoyu indirmek için **Code → Download ZIP** yolunu da kullanabilirsiniz.

## KiCad ile aç

ZIP paketini çıkarın ve içindeki `STM32F469_DISEN_RevI.kicad_pro` dosyasını **KiCad 9** ile açın. Düzenlenebilir dosyalar ayrıca [`STM32F469_DISEN_RevI_Layout/`](STM32F469_DISEN_RevI_Layout/) klasöründedir; kütüphaneleriyle birlikte kullanın.

## Doğrulama

- 49 komponentin özellikleri ve DNP durumları korundu.
- 57 net kaydında 172 pin/net üyeliği özgün tasarımla eşleşti.
- 25 bağlantısız pin işareti korundu.
- KiCad CLI 9.0.2 ERC: **0 hata, 0 uyarı**.
- ZIP ayrı klasöre çıkarılarak ERC ve netlist karşılaştırması tekrar doğrulandı.

Şematik sayfaları: **MIPI/LCD arayüzü**, **mantık beslemesi ve dokunmatik**, **backlight güç katı**.
