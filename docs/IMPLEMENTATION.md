# Implementation and demonstration

## Components
Three one-bit input pins (D, M, E), one NOT gate, one two-input OR gate, one two-input AND gate, one output pin (L) and one LED.

## Signal path
D enters the NOT gate to produce darkness demand. The OR gate combines darkness demand with M. The AND gate combines that result with E. L and the LED show the resulting lamp command.

## Demonstration sequence
1. Set E=1, M=0 and D=1. Expected L=0: daylight, lamp OFF.
2. Change D to 0. Expected L=1: darkness, lamp ON.
3. Return D to 1 and set M=1. Expected L=1: manual ON.
4. Set E=0. Expected L=0: master disable overrides all other inputs.
5. Run all eight cases in the expected truth table and record observations.

## Model boundary
The project is a digital controller. The input pin models the binary output of a sensor/comparator. It does not simulate an LDR's resistance, an analog voltage divider, a real relay, or street-lamp power. A future physical implementation would need a defined sensing threshold, hysteresis and an appropriate lamp driver. No measured power savings are available.

## Suggested viva questions
- Why does the design invert D? Because D=1 represents daylight and automatic lamp demand is darkness.
- Which input has highest priority? E. E=0 forces the lamp OFF.
- Why is this combinational? The output depends only on current inputs, with no stored state.
- What happens if a sensor flickers near its threshold? This model may toggle the lamp command. Hysteresis in a future sensing stage can address it.
- Why are there eight test cases? Three binary inputs give 2^3=8 combinations.
