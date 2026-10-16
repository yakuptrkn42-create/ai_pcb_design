# Özgün şematik açıklamaları

Kaynak çizimdeki metinler, elektriksel tasarım bağlamını korumak için aynen aktarılmıştır. Eski sayfa başlıkları ve sürüm atıfları kaynak belgeye aittir.

## STM32F469_DISEN_RevI.kicad_sch

```text
PB8/PB9 = I2C1, open-drain. PJ5 = touch interrupt.
Start at 100 kHz; verify ILI2130 address and pull-up load.
No additional INT pull-up: MB1189 R36 is 4.7k to 3V3.
```

```text
MIPI D-PHY: three direct pairs, continuous GND.
Set PCB + flex differential impedance to 100 ohm.
No DSI stubs/testpoints; no generic TVS on DSI.
Final FPC contact direction and pin-1 must be checked
with connector drawings and end-to-end continuity.
```

```text
Power budget is not proven: LCD and touch current = TBD
in the supplied preliminary datasheet. Measure before release.
Touch 2.8-3.3 V range / 3.3 V nominal: confirm tolerance.
Do not connect 5 V to LCD_VCI or TP_VDD.
```

```text
CONTROL / no MIPI series resistors or AC coupling
```

```text
DISEN panel / 39-pin, 0.30 mm
```

```text
J1.23 / J1.24 intentionally unused: host LED output.
J1.3 = GND holds onboard backlight EN low via R117.
Confirm R117=0R and R119=DNP; do not drive PA3 high.
Use a purpose-made 1:1 FPC, not an assumed FFC pin order.
```

```text
MB1189 B-07 / B-08 / C-01 pin assignments | Remove original LCD and touch flexes
```

```text
CN12 -> J5 / 2x8, 2.54 mm socket
```

```text
CN10 -> J1 / 25-pin, 0.30 mm FPC
```

```text
Rev E: engineering prototype. Read OKU_ONCE.md before manufacturing.
```

```text
01 / STM32F469I-DISCO -> DISEN DS070HSD39T-132
```

```text
J3.1 supplies TP_VDD via R5; J1 supplies LCD only.
J3.5 unused: keeps LCD and touch resets independent.
CN12 socket orientation must follow physical pin-1.
```

```text
CN2 -> J3 / 6-pin, 0.50 mm FPC
```

```text
LOGIC POWER / host 3.3 V only
```

## Backlight.kicad_sch

```text
02 / EXTERNAL 5 V + TPS61165 BACKLIGHT
```

```text
Do not hot-plug. Turn PWM off before disconnecting panel.
PCB verification: SW loop, ground return, EMI and thermal.
All component values require prototype validation.
```

```text
External 5 V is mandatory for the LED boost.
No connection to the host +5 V or host LEDA/LEDK.
J4.1=GND and J4.2=+5V preserve original connector polarity.
Fuse is not an overvoltage limiter; use a regulated supply.
```

```text
OVP / transient validation required for 30 V rated FPC
```

```text
LED load: 21.6-27.2 V at 40 mA | Separate boost supply; common GND with F469
```

```text
I_LED nominal = 0.200 V / 5.23 ohm = 38.24 mA.
R7 loss = 7.65 mW; worst-case target <40 mA.
LEDK connects directly to U1.FB and R7 only.
Removed R8 link and dangerous LEDK-to-GND R9 option.
```

```text
OVP nominal: 1.242 x (1 + 221k/10k) = 28.690 V.
U2 supply is HOST_3V3; wait >=10 ms before PWM.
Open-load operation can hiccup; measure peak <30 V.
CTRL shutdown is NOT immediate (2.5 ms specification).
OVP <30 V is not certified; scope test is mandatory.
```

```text
BOOST POWER STAGE / short switching loop
```
