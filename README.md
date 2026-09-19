# Design and Simulation of an Automatic Street Light Control System

## Team
- Student names and registration/ID numbers: [fill in]
- Supervisor: [fill in]
- Department and college: [fill in]
- Academic year and team ID: [fill in]

## Abstract
This DDCA project models street-light switching with combinational logic. A digital daylight input replaces the physical light-sensing stage. The controller includes a master enable and manual ON override. One NOT gate, one OR gate and one AND gate implement the output equation.

## Current phase and status
Reference design and presentation prepared. Circuit XML and gate-level connectivity are checked separately from Logisim. Actual Logisim execution and screenshots are pending. No physical hardware measurements or energy-savings results are claimed. Review and understand this reference design, adapt it to your team's work, and report contributions honestly.

## Logic
`L = E AND ((NOT D) OR M)`
- D=1: daylight, D=0: darkness.
- E=1: controller enabled. E=0 forces OFF regardless of D and M.
- M=1: manual ON while enabled. M=0 selects automatic operation.
- L=1: lamp ON, L=0: lamp OFF.

## Setup and execution
1. Open `src/automatic_street_light.circ` in classic Logisim 2.7.1. Newer Logisim-evolution versions may import it, but compatibility has not been tested.
2. Select the Poke tool and click input pins D, M and E to change their values.
3. Follow all eight rows in `data/expected_truth_table.csv`.
4. Compare output pin L and the LED with the expected output.
5. Fill `results/simulation_observations.csv` and save real screenshots in `results/`.
6. Open `docs/Automatic_Street_Light_Control.pptx`, replace identity placeholders, and update the results slide only after simulation.

Optional independent structural check with Python 3:
```
python src/verify_logic.py
```
This checker validates the supplied gate positions and wire connectivity and evaluates all eight cases. It does not run the Logisim simulator.

## Repository structure
- `src/`: Logisim circuit and independent logic checker.
- `docs/`: presentation and implementation guide.
- `data/`: expected truth table.
- `results/`: observations and verification status.
- `reports/`: project status and contribution template.

## Submission
See `docs/GITHUB_SUBMISSION.md` for the supplied course rules. Each student must commit their own actual contributions using their own GitHub account. This package contains no manufactured commit history and has not been uploaded to GitHub.

## References
- [Logisim NOT gate](https://www.cburch.com/logisim/docs/2.7/en/html/libs/gates/not.html)
- [Logisim AND/OR gates](https://www.cburch.com/logisim/docs/2.7/en/html/libs/gates/basic.html)
