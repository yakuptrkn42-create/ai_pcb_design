# STM32F469 / DISEN — Şematik inceleme J-SR1

KiCad 9.0 veya daha yeni sürümle `Project/STM32F469_DISEN_RevJ_Prep1.kicad_pro` dosyasını açın. Kaynak basename ve sembol UUID'leri korundu. Project klasörünü bütün olarak taşıyın: üç şematik, yerel sembol/footprint tabloları ve kütüphaneler birlikte kalmalıdır.

- `PDF/Schematic_J_SR1.pdf`: native KiCad dosyalarından alınan üç sayfalık şema.
- `PDF/Engineering_Review_TR.pdf` ve `Engineering/ENGINEERING_REVIEW_TR.md`: bulgular, değişiklikler, koşullu uyumluluk ve ilk test prosedürü.
- `Verification/`: kaynak/son ERC, XML netlist, pin eşleme denetimleri ve hesaplar.
- `Engineering/BOM_J_SR1.csv`: değerler, footprint'ler, DNP ve seçim notları.
- `References/`: kullanıcı LCD PDF'i ve bu incelemede kullanılan üretici belgeleri.
- `Original/Submitted_Project.zip`: yüklediğiniz ZIP, değiştirilmeden saklandı; eski PCB ve yedekleri bunun içindedir.

Son ERC: 0 hata / 0 uyarı; kurallar veya exclusion'lar gevşetilmedi. 49 devre elemanı + 4 mekanik delik; fiziksel net grupları korundu. Sayfa içi üç düğüm artık local label olduğu için XML'de hiyerarşik net adları görünür.

**Bu teslim donanımda çalışma veya nihai PCB dondurma onayı değildir.** Özellikle touch beslemesinin host toleransıyla uyumu (3,365V olasılığı / panel çiziminde 3,3V üst sınırı), panel akımları/reset verileri, gerçek FPC sürekliliği ve açık yükte <30V backlight tepe değeri kapanmalıdır. Raporu okuyun. J3 yalnızca host CN2 içindir; panelin ayrı 6-pin touch flex'inin pin dizilimi farklıdır ve J3'e takılmaz.

PCB tasarımı ve yazılım kapsam dışıdır. Güncellenmiş şematiğin yanında eski PCB, yanlış güncel dosya izlenimi vermemesi için bulunmaz; özgün ZIP içinde aynen korunur. PCB'ye geçerken yeni J4/J6 footprint atamalarını ve local net adlarını şematikten aktarın. Geometrik DRC, routing ve SI ölçümü yapılmadı. Korunan 3D modellerin bir kısmı nominaldir; bu çalışma 3D mekanik kabulü değildir.

Yeniden doğrulama (Linux, depo kökü/teslim klasörü içinde):
```bash
mkdir -p /workspace/.cloud-onboarding/kicad/{config,cache,data}
export XDG_CONFIG_HOME=/workspace/.cloud-onboarding/kicad/config
export XDG_CACHE_HOME=/workspace/.cloud-onboarding/kicad/cache
export XDG_DATA_HOME=/workspace/.cloud-onboarding/kicad/data
kicad-cli sch erc --exit-code-violations --format json -o Verification/revised_erc.json Project/STM32F469_DISEN_RevJ_Prep1.kicad_sch
kicad-cli sch export netlist --format kicadxml -o Verification/revised.xml Project/STM32F469_DISEN_RevJ_Prep1.kicad_sch
python3 Engineering/validate_delivery.py
```
