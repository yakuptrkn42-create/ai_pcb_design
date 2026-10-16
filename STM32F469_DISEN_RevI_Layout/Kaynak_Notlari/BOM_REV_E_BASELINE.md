# Rev E malzeme listesi

Şematik netlistinden türetilmiştir. Pasiflerin kesin üretici kodları tedarik öncesinde dondurulmalı. R7: ±%1, TCR ≤50 ppm/°C. L1 eski tasarımdan korunmuştur; yaşam döngüsü ve muadili doğrulanmalı.

| Referans | Değer | MPN | Montaj | Footprint | Açıklama |
|---|---|---|---|---|---|
| C5 | 4.7uF / 10V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; place beside connector supply pins |
| C6 | 100nF / 10V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; place beside connector supply pins |
| C7 | 1uF / 10V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; place beside connector supply pins |
| C8 | 100nF / 10V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; place beside connector supply pins |
| J1 | FH26W-25S-0.3SHW(60) | FH26W-25S-0.3SHW(60) | Takılacak | Adapter_F469:FH26W-25S-0.3SHW | Cable must map CN10.n to J1.n. Pin 3 disables host boost via R117; R119 absent. |
| J2 | FH26W-39S-0.3SHW(60) | FH26W-39S-0.3SHW(60) | Takılacak | Adapter_F469:FH26W-39S-0.3SHW | DS070HSD39T-132 A0 pinout. FH26W FPC compatibility and contact face checked against final panel drawing. |
| J3 | FH19C-6S-0.5SH(10) | FH19C-6S-0.5SH(10) | Takılacak | Adapter_F469:FH19C-6S-0.5SH | CN2.5 is PH7, shared with LCD reset; intentionally unused. |
| J5 | CN12 1:1 / 2x08 socket | SSW-108-02-G-D | Takılacak | Adapter_F469:PinSocket_2x08_P2.54mm_Vertical | PC6: TIM3_CH1 AF2 PWM. PB12: independent touch reset GPIO. Pin numbering 1:1 to CN12. |
| R1 | 4.7k / DNP |  | DNP | Adapter_F469:R_0805_2012Metric | Host R140/R142 already supply I2C pull-ups; do not fit without rise-time review |
| R2 | 4.7k / DNP |  | DNP | Adapter_F469:R_0805_2012Metric | Host I2C pull-up present |
| R3 | 100R |  | Takılacak | Adapter_F469:R_0805_2012Metric | Independent reset, PB12 |
| R4 | 0R |  | Takılacak | Adapter_F469:R_0805_2012Metric | VCI 3.0-3.6 V; optional bead after validation |
| R5 | 0R |  | Takılacak | Adapter_F469:R_0805_2012Metric | Touch supply from CN2.1; verify guaranteed VDD min/max and measured current. |
| R14 | 10k |  | Takılacak | Adapter_F469:R_0805_2012Metric | Pull-up in touch domain |
| R15 | 100R |  | Takılacak | Adapter_F469:R_0805_2012Metric | PH7 open-drain reset |
| R16 | 0R |  | Takılacak | Adapter_F469:R_0805_2012Metric | Disconnect if TE unused; PJ2 is DSI_TE |
| R17 | 10k |  | Takılacak | Adapter_F469:R_0805_2012Metric | Required pull-up for PH7 open-drain |
| TP1 | HOST_3V3 |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP3 | GND |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP4 | LCD_RST |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP5 | TP_INT |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP10 | TP_RST |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP11 | LCD_VCI |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP12 | TP_VDD |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| C1 | 10uF / 16V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; effective capacitance >=4.7uF at 5V; use verified DC-bias curve. |
| C2 | 100nF / 16V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; C3 effective capacitance >=4.7uF at 30V, verify vendor DC-bias curve |
| C3 | 10uF / 50V |  | Takılacak | Adapter_F469:C_1210_3225Metric | X7R; C3 effective capacitance >=4.7uF at 30V, verify vendor DC-bias curve |
| C4 | 100nF / 50V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; C3 effective capacitance >=4.7uF at 30V, verify vendor DC-bias curve |
| C9 | 220nF / 16V |  | Takılacak | Adapter_F469:C_0805_2012Metric | X7R; C3 effective capacitance >=4.7uF at 30V, verify vendor DC-bias curve |
| C13 | 100nF / 10V |  | Takılacak | Adapter_F469:C_0805_2012Metric | Place at U2.6/U2.2 |
| D1 | SS16 / 60V 1A | SS16 | Takılacak | Adapter_F469:D_SMA | Boost rectifier; cathode to LEDA |
| D3 | SS14 / reverse block | SS14 | Takılacak | Adapter_F469:D_SMA | Input polarity / reverse-current isolation |
| F2 | 0.75A hold / 6V | 1206L075/6YR | Takılacak | Adapter_F469:Fuse_1206_3216Metric | Resettable fuse; derate hold current at temperature |
| J4 | EXT 5V / 1=GND 2=+5V |  | Takılacak | Adapter_F469:PinHeader_1x02_P2.54mm_Vertical | Regulated 5 V +/-5%, >=0.5 A. Observe polarity. |
| L1 | 22uH / shielded | SLF7045T-220M1R3-H | Takılacak | Adapter_F469:L_TDK_SLF7045 | Electrical reference: 22uH +/-20%, DCR 0.082ohm +/-20%, Isat 1.3A. Discontinued: source stock or qualify replacement. |
| R6 | 100k |  | Takılacak | Adapter_F469:R_0805_2012Metric | Backlight defaults OFF while MCU GPIO is high impedance |
| R7 | 5.23R / 1% |  | Takılacak | Adapter_F469:R_0805_2012Metric | 38.24mA nominal; 39.4mA max from 204mV and -1% R. Specify TCR <=50ppm/C. |
| R12 | 0R / isolation |  | Takılacak | Adapter_F469:R_0805_2012Metric | Remove to isolate boost during bring-up |
| R13 | 2.2k |  | Takılacak | Adapter_F469:R_0805_2012Metric | Limits comparator sink current; PC6 20kHz PWM, keep low through power-up |
| R18 | 33k / discharge |  | Takılacak | Adapter_F469:R_0805_2012Metric | 27.3mW at 30V; 0.33s nominal RC with 10uF. Not zero volts while input powered. |
| R19 | 221k / 0.1% |  | Takılacak | Adapter_F469:R_0805_2012Metric | OVP upper divider |
| R20 | 10k / 0.1% |  | Takılacak | Adapter_F469:R_0805_2012Metric | OVP lower divider |
| TP6 | BL_CTRL |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP9 | BL_POWER |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP13 | BL_LEDA |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP14 | BL_LEDK |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| TP15 | GND |  | Takılacak | Adapter_F469:TestPoint_Pad_D1.0mm |  |
| U1 | TPS61165DBVR | TPS61165DBVR | Takılacak | Adapter_F469:SOT-23-6 | SOT23-6 pinout verified from TI. LEDK to FB; never direct GND. |
| U2 | TLV3011BIDBVR | TLV3011BIDBVR | Takılacak | Adapter_F469:SOT-23-6 | Open-drain comparator. Output pulls CTRL low above ~28.7V; verify overshoot under open-load. |