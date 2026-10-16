# Rev I – temel pin/net eşlemesi

| Kaynak | PCB / DISEN | Fonksiyon |
|---|---|---|
| STM32 CN10.12 / .14 | J1.12 / .14 → J2.25 / .24 | DSI CLK N / P |
| STM32 CN10.8 / .10 | J1.8 / .10 → J2.17 / .16 | DSI D0 N / P |
| STM32 CN10.16 / .18 | J1.16 / .18 → J2.21 / .20 | DSI D1 N / P |
| STM32 CN10.5 | J1.5 → R15 100R → J2.12 | LCD RESET |
| STM32 CN10.22 | J1.22 ↔ R16 0R ↔ J2.13 | LCD TE |
| STM32 CN2.3 / .4 | J3.3 / .4 ↔ J2.32 / .33 | I2C SCL/SDA |
| STM32 CN2.2 | J3.2 ↔ J2.35 | TP INT |
| STM32 CN12.12 | J5.12 → R3 100R → J2.34 | TP RESET |
| STM32 CN12.6 | J5.6 → R13 2.2k → U1.2 | LED PWM/CTRL |
| STM32 CN12.4 / .8 | J5.4 / .8 NC | NRST and PC7 unused |
| STM32 CN10.21 etc. | LCD VCI / TP VDD via R4 / R5 | 3.3 V separately |
| J4 ext 5 V | F2 → D3 → R12 → TPS61165 | LED boost, separate supply |
| TPS61165 LED+ / LED- | J2.1-2 / J2.3-4 | LEDA/LEDK |

**Uyarı:** Konektör pin-1, kontak yüzü, 1:1 FPC ve güç toleransları fiziken teyit edilmeden PCB siparişi verilmemelidir.
