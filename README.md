## 🏗️ System Architecture

The Smart Street Light Control System consists of sensing, processing, and lighting sections.

```text
        ┌─────────────────┐
        │   Light / Day   │
        │  Environment    │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   LDR Sensor    │
        │ Light Detection │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ Microcontroller │
        │  Control Logic  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Relay Module  │
        │  Switching Unit │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   LED Street    │
        │      Light      │
        └─────────────────┘
```

### Architecture Description

The system is divided into four main stages:

1. **Sensing Stage**
   The LDR sensor detects the intensity of light in the surrounding environment.

2. **Processing Stage**
   The microcontroller receives the sensor information and determines whether the environment represents daylight or darkness.

3. **Switching Stage**
   The relay module acts as the switching interface between the controller and the street-light load.

4. **Lighting Stage**
   The LED represents the street light. It is switched ON when darkness is detected and switched OFF when sufficient daylight is present.

---

## 🔄 System Flow

```text
        START
          │
          ▼
   Read LDR Sensor
          │
          ▼
   Check Light Level
          │
      ┌───┴───┐
      │       │
   Daylight  Darkness
      │       │
      ▼       ▼
   Light OFF  Light ON
      │       │
      └───┬───┘
          │
          ▼
    Read Sensor Again
```

The controller continuously checks the light level so that the street light can respond automatically whenever the environmental condition changes.

---

## 🧠 Control Logic

The basic control principle is:

```text
Daylight detected  →  Street Light OFF
Darkness detected  →  Street Light ON
```

The LDR provides the environmental input, while the controller processes the input and produces the required switching signal.

For the digital logic implementation, the input conditions are represented using binary values and the corresponding street-light output is verified using a truth table.

---

## 📊 Truth Table

The truth table represents the relationship between the input conditions and the street-light output.

| E | D | M | Expected L |
| - | - | - | ---------- |
| 0 | 0 | 0 | 0          |
| 0 | 0 | 1 | 0          |
| 0 | 1 | 0 | 0          |
| 0 | 1 | 1 | 0          |
| 1 | 0 | 0 | 1          |
| 1 | 0 | 1 | 1          |
| 1 | 1 | 0 | 0          |
| 1 | 1 | 1 | 1          |

Where:

* **E, D, M** = digital input conditions used by the control logic.
* **L** = street-light output.
* `1` represents HIGH/ON.
* `0` represents LOW/OFF.

The complete table is also provided in `truth-table.csv`.

---

## 💻 Digital Logic Implementation

The digital version of the system demonstrates how basic logic gates can be used to control the street-light output.

The reference design uses:

* NOT gate
* OR gate
* AND gate

The gates process the input signals according to the required Boolean relationship and generate the final street-light output.

The circuit can be implemented and verified using **Logisim**.

---

## 🧪 Simulation and Validation

The circuit will be tested using all possible combinations of the digital inputs.

For each combination:

1. Input values are applied to the circuit.
2. The resulting street-light output is observed.
3. The output is compared with the expected value in the truth table.
4. Any mismatch is investigated and corrected.

This provides a systematic method for validating the digital logic design.

---

## 📁 Project Files

The repository contains the following project resources:

```text
├── README.md
├── truth-table.csv
├── simulation/
│   └── street-light.circ
├── screenshots/
│   ├── simulation-1.png
│   └── simulation-2.png
└── documentation/
```

---

## 📈 Expected Result

The expected behavior of the system is:

| Environmental Condition | Street Light |
| ----------------------- | ------------ |
| Daylight                | OFF          |
| Darkness                | ON           |

The digital simulation should produce the same output behavior represented by the project's truth table.

---

## 🌱 Advantages

* Automatic street-light operation
* Reduced unnecessary lighting
* Simple control mechanism
* Low-cost implementation
* Reduced human intervention
* Suitable for smart-city applications

---

## ⚠️ Limitations

* The current project represents a simulation/prototype implementation.
* Actual power savings depend on the physical implementation and operating conditions.
* LDR readings can be affected by environmental factors.
* A physical relay and lighting system require appropriate electrical protection.
* No physical energy-consumption measurements are claimed unless experimentally measured.

---

## 🚀 Future Scope

The project can be further improved by:

* Adding a PIR sensor for motion detection.
* Implementing automatic brightness control.
* Using PWM for LED brightness adjustment.
* Adding wireless monitoring.
* Connecting the system to an IoT platform.
* Recording energy-consumption data.
* Developing a physical hardware prototype.

---

## 📌 Project Status

| Task                   | Status            |
| ---------------------- | ----------------- |
| Project concept        | ✅ Completed       |
| System architecture    | ✅ Completed       |
| Control logic          | ✅ Designed        |
| Truth table            | ✅ Prepared        |
| Logisim circuit        | 🔄 To be verified |
| Simulation testing     | 🔄 In progress    |
| Simulation screenshots | 🔄 To be added    |
| Final validation       | 🔄 Pending        |

---

## 👥 Team

**KLH ECE 2026 Batch12**

| Team Member             | Registration Number |
| ----------------------- | ------------------- |
| Naga Sai Venkat Praveen | 2620040078          |
| N. Varun                | 2620040048          |
| M. Deepika              | 2620040063          |
| Sujith Kumar            | 2620040027          |

---

## 🎓 Academic Information

**Project:** Smart Street Light Control System
**Course:** Digital Design and Computer Architecture
**Institution:** Koneru Lakshmaiah University, Hyderabad
**Academic Year:** 2026

---

## 🏁 Conclusion

The Smart Street Light Control System demonstrates the application of digital logic and embedded control concepts to automatic street-light management. By detecting environmental light conditions and controlling the lighting output accordingly, the system provides an automated approach to street-light operation.

The project combines sensor-based input, control logic, switching, and LED output into a simple system that can be simulated, tested, and further developed into a physical smart-lighting prototype.
