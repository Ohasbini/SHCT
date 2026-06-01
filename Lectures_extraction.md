# Lecture 1: Introduction to Heating and Cooling and Simple Heat Pump Model

**Source: SHCT_26_Lec1.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #1

Introduction to Heating and Cooling Simple Heat Pump model

Lana Liebl Dr. Leon Brendel 18 February 2026

===== Page 2 =====

What will we deal with? Sustainable Heating and Cooling Technologies

===== Page 3 =====

Course information

===== Page 4 =====

"Learning by (guided) doing"

===== Page 5 =====

Dates and times

[Image: Four small calendar/clock icons with text indicating lecture times: Wednesdays HG E 21 10:15 - 12:00 a.m. and Wednesdays HG E 19 02:15 - 03:45 p.m.]

===== Page 6 =====

Communication

[Image: Icons for Moodle and recordings. Text: Moodle course - Name: 151-0950-00L Sustainable Heating and Cooling Technologies FS2026 - You are already signed up. Recordings - Lectures are recorded, exercises not - https://video.ethz.ch/lectures/d-mavt.html]

===== Page 7 =====

2epse

[Table with weeks and dates: Feb. 18 L1, Feb. 18 E1; Feb. 25 L2, Feb. 25 E2; Mar. 04 L3, Mar. 04 E3; Mar. 11 L4, Mar. 11 E4; Mar. 18 L5, Mar. 18 E5; Mar. 25 L6, Mar. 25 E6; Apr. 01 L7, Apr. 01 E7; Apr. 08 Easter; Apr. 15 L8, Apr. 15 E8; Apr. 22 L9, Apr. 22 E9; Apr 29 Excursion, Apr 29 Sem. Proj.; May 06 L10, May 06 E10; May 13 L11, May 13 E11; May 20 L12, May 20 E12; May 27 L13, May 27 Q&A. Also note: Handing out the semester project task, Submission due Jun. 21]

===== Page 8 =====

Excursion 29.04.2026: 10:00-12:00 Lake heat network (Kongresshaus) and big heat pumps with ewz and Scheco

Please let us know if you participate by filling out the survey in moodle until 02.03.26

===== Page 9 =====

Topics at a glance

| Lecture | Topics |
|---------|--------|
| L1 | Introduction Simple heat pump model |
| L2 | Fluid property models |
| L3 | Heat sources and sinks Pinch model |
| L4 | Components #1: Heat exchanger |
| L5 | Components #2: Expansion valves Transcritical process |
| L6 | Components #3: Compressors Advanced flowsheets |
| L7 | Refrigerants |
| L8 | Controlling Residential heating |
| L9 | High-temperature industrial heat pumps |
| L10 | Cooling – everything different now? |
| L11 | Air-conditioning |
| L12 | Low-temperature and cryo cooling |
| L13 | Niche technologies |

===== Page 10 =====

Performance assessment / exam

[Image: Icons for semester project and oral exam]

Semester project
- Group work of two students
- Solving a defined problem
- Written report (5-10 pages) → we provide a template
- Grading based on:
  - Solving approach (40%)
  - Report (40%)
  - Python code (20%)

Oral exam
- 30 minutes
- Date during the examination session (08/03 – 08/28)
- Content of the lectures (50%)
- Discussion of the student project (50%)

===== Page 11 =====

Grade Statistics from last year

[No text, likely a graph]

===== Page 12 =====

Programming in Python What will you need?

What should you already know (prerequisites):
- Variable types (also pandas)
- Definition of variables
- Usage of loops
- Definition and usage of functions
- Usage of simple solvers, e.g., fsolve, brentq
- Basic knowledge in creating plots (matplotlib)

What you will learn with us:
- Constrained NLP optimization with minimize
- Solving ODEs with odeint
- Curve fitting
- Interpolation
- Usage of fluid property models
- Creating contour plots

Beware! We do that briefly! Use the tutorial on moodle!

For your personal computers:
- We recommend installing the latest version of Anaconda
- We prefer working with the Spyder IDE
- Required packages: scipy, numpy, pandas, matplotlib, coolprop

===== Page 13 =====

• Hyundai; Refrigeration, Air Conditioning and Heat Pumps
• Bryant; Refrigeration Equipment
• Kreith, Norton, Wang; Air-conditioning and refrigeration engineering
• Granet, Alvarado, Bluestein; Thermodynamics and Heat Power
• Kakac, Smirnov, Avelino; Low Temperature and Cryogenic Refrigeration
• VDI Heat Atlas
• Python programming: Youtube tutorials

German books:
• Pohlmann; Taschenbuch der Kältetechnik
• Schädlich; Kompendium Kälte-, Klimatechnik
• Baehr, Kabelac; Thermodynamik

===== Page 14 =====

Before we

[Image: Possibly a diagram about sign conventions] 
Transferred to the system (inputs): values are positive
Released by the system (outputs): values are negative
For all variables: heat, work, mass, enthalpy, entropy...

===== Page 15 =====

Introduction to heating and cooling

Introduction to heating and cooling

===== Page 16 =====

Cooling

Cooling a space, substance or system...
...below the ambient temperature

[Image: Source: tis-gdv.de, likely showing cooling below ambient]
...above the ambient temperature

===== Page 17 =====

Cooling demand

[Image: Source: Getty Images, likely showing cooling demand graph]

===== Page 18 =====

Cooling technologies

[Image: Diagram of cooling technologies, possibly showing vapor compression, absorption, etc.]

===== Page 19 =====

How to decarbonize cooling?

===== Page 20 =====

How to decarbonize cooling?

===== Page 21 =====

6352 10^9 kWh

Figure 1: Total final energy in 2015 (EU28)

===== Page 22 =====

Heat generation by energy carrier European Union (EU28), 2015

[Image: Source: heatroadmap.eu, likely a pie chart or bar chart]

===== Page 23 =====

Ways to decarbonize heating

[Image: Three columns with icons and text, likely showing different technologies]

===== Page 24 =====

Ways to decarbonize heating

[Image: More detailed diagram of decarbonization pathways]

===== Page 25 =====

2021

Residential heat pump statistics Europe

Germany

===== Page 26 =====

Residential heat pump statistics Switzerland, 2023

===== Page 27 =====

Industrial heat pump statistics Switzerland

Source: Adapted from Wolf et al. (2012): Industrial Heat Pumps in Germany with newer data from 2020 (fws.ch)

===== Page 28 =====

Heat pump technologies

[Image: Diagram of heat pump technologies, likely vapor compression highlighted]
Cooling cycles are always heat pumps!
As you might assume...
Vapor-compression > 90% market share

===== Page 29 =====

Heat pump companies

[Image: Logos of various heat pump companies including: Daikin, Viessmann, NIBE, Bosch, Stiebel Eltron, Mitsubishi, Panasonic, Hitachi, etc.]

===== Page 30 =====

Refresher in Thermodynamics

===== Page 31 =====

Direction of spontaneous heat transfer

[Image: Diagram of two reservoirs at T1 and T2 with heat flow Q]
Entropy balance
δS_irr = (-|δQ|)/T1 + δQ/T2
T1 < T2 → δS_irr < 0 impossible process
T1 ≥ T2 → δS_irr ≥ 0 possible process
Heat spontaneously flows from hot to cold

===== Page 32 =====

Thermodynamics of cooling

[Image: Diagram of system at T_sys and ambient at T_amb]
"Removing heat from a space, substance or system to lower and/or maintain its temperature below the ambient one"
δS_irr = (-|δQ|)/T_sys + δQ/T_amb
T_sys < T_amb
[Image: Small diagram indicating impossible process]
Impossible process!

===== Page 33 =====

Thermodynamics of cooling Second try

[Image: Diagram of machine with Q_high and Q_low]
Energy balance (machine)
Q_high + Q_low = 0
|Q_high| = Q_low
Entropy balance
δS_irr = dS_machine + (-|δQ_low|)/T_sys + δQ_high/T_amb
T_sys < T_amb
δQ_high/|δQ_low| ≥ T_amb/T_sys

===== Page 34 =====

Thermodynamics of cooling Third try

[Image: Diagram including Q_in and W_in]
Energy balance (machine)
Q_high + Q_low + Q_in + W_in = 0
|Q_high| = Q_low + Q_in + W_in

===== Page 35 =====

Thermodynamics of cooling Third try, power added

[Image: Diagram with power added]
Energy balance (machine)
Q_high + Q_low + W_in = 0
|Q_high| = Q_low + W_in
Entropy balance (power added)
δS_irr = dS_machine + (-|δQ_low|)/T_sys + (|δQ_low|+δW_in)/T_amb
δW_in ≥ |δQ_low|·(T_amb/T_sys - 1)

===== Page 36 =====

Thermodynamics of cooling Third try, heat added

[Image: Diagram with heat added]

===== Page 37 =====

Thermodynamics of cooling What we have invented

[Image: Diagram of a machine removing heat from low T and transferring higher amount at high T]
A machine that removes heat from a system at lower temperature and transfers a higher amount of heat at higher temperature to another system while absorbing power and/or heat
[Image: Second diagram]
Every cooling process is a heat pump

===== Page 38 =====

Thermodynamics of heating Heat pump

[Image: Diagram of heat pump with T_sys > T_amb]
T_sys > T_amb
The difference between T_in and T_sys must be large enough so that B compensates for A
Power added: δW_in ≥ |δQ_low|·(T_sys/T_amb - 1)
Heat added

===== Page 39 =====

Thermodynamics of heating Simpler processes are possible

[Image: Two small diagrams: work added and heat added]
Work added (non pressure-volume work): δS_irr = ΔS_sys = δW/T_sys > 0
Heat added: δS_irr = ΔS_sys - |δQ_in|/T_in = |δQ_in|/T_sys - |δQ_in|/T_in
Ambient T_amb: δS_irr > 0 for T_in > T_sys

===== Page 40 =====

Thermodynamics of heat pumps Coefficient of Performance (COP)

[Image: Diagram of heat pump with Q_high, Q_low, W_in]
How can we assess the performance of heat pumps?
For heating purposes: Objective: Rejected heat Q_high, Effort: Added Work W_in → COP_H = Q_high / W_in
For cooling purposes: Objective: Absorbed heat Q_low, Effort: Added Work W_in → COP_C = Q_low / W_in
COPs for heating are always ≥ 1

===== Page 41 =====

Thermodynamics of heat pumps The simple heat pump cycle (reverse Rankine)

[Image: T-s diagram of simple heat pump cycle]
- Point 1 is shifted to superheated steam (superheating)
- Point 3 is often shifted to subcooled liquid (subcooling)

===== Page 42 =====

Thermodynamics of heat pumps The simple heat pump cycle (reverse Rankine)

[Image: Another T-s diagram with states labeled]
- Point shifted to superheated steam (superheating)
- Point 3 is often shifted to subcooled liquid (subcooling)

===== Page 43 =====

Calculating the simple heat pump cycle

Known properties:
Evaporation temperature T_ev, Condensation temperature T_co, Superheating ΔT_sh, Subcooling ΔT_sc, Isentropic compressor efficiency η_is, Refrigerant

[Image: T-s diagram with states 1-4]

Pressure levels: p_ev = p_sat(T_ev), p_co = p_sat(T_co) (Standard assumption: No pressure losses)

State 1: h1, s1 = f(T_ev + ΔT_sh, p_ev)

State 2: We know p2 = p_co and compressor efficiency η_is
η_is = w_comp,is / w_comp = (h2,is - h1)/(h2 - h1)
h2,is = f(p_co, s1)
→ h2 = (h2,is - h1)/η_is + h1, State 2 is defined by p_co and h2

===== Page 44 =====

Calculating the simple heat pump cycle

Known properties: Evaporation temperature T_ev, Condensation temperature T_co, Superheating ΔT_sh, Subcooling ΔT_sc, Isentropic compressor efficiency η_is, Refrigerant

[Image: T-s diagram]

State 3: h3, s3 = f(T_co - ΔT_sc, p_co)

State 4: Assumption h4 = h3, T4, s4, x4 = f(p_ev, h4) (Usually: T4 = T_ev)

Specific heat flow rates: q_high = h3 - h2, q_low = h1 - h4

Coefficient of Performance: COP = |q_high| / w_comp = (h2 - h3)/(h2 - h1)

===== Page 45 =====

Calculating the simple heat pump cycle

Known properties: As you see... ...we need refrigerant properties! Vapor-liquid equilibrium data, Caloric data (enthalpies, entropies...), maybe pVT-data

[Image: T-s diagram with entropy axis labeled]
Coming soon... (next week)

===== Page 46 =====

After this lecture, you are able to...
... point out the importance of heating and cooling for decarbonization
... use basic thermodynamic equations to show the differences between heating and cooling
... sketch the flow sheet of a simple Rankine-based heat pump cycle
... calculate all states and the COP of simple Rankine-based heat pump

===== Page 47 =====

Introduction to this week’s exercise

===== Page 48 =====

In this exercise, you will calculate the states of a heat pump process and evaluate its performance. The heat pump process is shown in Figure 1 and consists of an evaporator, compressor (compressor efficiency: η_is = 0.5), condenser, and throttle.

The temperatures in the condenser and evaporator are given (T_ev = -5°C, T_co = 39.35°C). Assume full condensation of the working fluid. After evaporating, the working fluid is superheated (ΔT_sh = 10K). The selected fluid is R134a.

a) Use the given steam tables for R134a to calculate the states of the heat pump process as defined in Table 1.
b) Use the results of a) to calculate the heat pump's coefficient of performance (COP).
c) Now use Fluid_CP.py to calculate the heat pump's thermodynamic states and COP. A tutorial for the use of this program is available in the moodle course.
d) Compare the results from tasks a)-c)

===== Page 49 =====

Using steam tables

[Image: A table snippet showing pressure, volume, density, enthalpy, entropy columns for R134a]

===== Page 50 =====

Using steam tables

[No additional text]

===== Page 51 =====

From known properties to full states

[Image: Three small diagrams showing state determination from T,x; p,h; p,s]
Remember: Usually, two intensive properties must be known to fully define a thermodynamic state, e.g., T and x, p and h, p and s... Exception: T and p in two phase region
[Image: Table with states and properties: State, Properties, X? T,x; p,x; ρ,x; h,x; s,x; x,x]

===== Page 52 =====

Linear interpolation

TABLE 2 (continued) HFC-134a Superheated Vapor-Constant Pressure Tables

[Table with TEMP °C and columns for PRESSURE = 101.325 kPa (abs): V, H, S, Cp, Cp/Cv, Vs]
Values from -26.06 to 70°C.

What is the specific enthalpy of R134a at ambient pressure and T = 27°C? ⇒ Not in the table
Use a linear interpolation approach to approximate the desired value!
y = y1 + (y2-y1)/(x2-x1) * (x-x1)

===== Page 53 =====

Linear interpolation (continued)

[Same table as page 52]
h(T) = h1 + (h2-h1)/(T2-T1)*(T-T1) = 424.8 kJ/kg + (429.1-424.8)/(30-25)*(27-25) = 424.8 + (4.3/5)*2 = 426.52 kJ/kg

===== Page 54 =====

How to prepare for this week's exercise
- Read the tutorials on moodle:
  - "Tutorial_python_installation" → pdf
  - "Tutorial_on_Fluid_CP" → Jupyter notebook
- If necessary, install Python + required packages on your own computer
- Maybe refresh your knowledge on thermodynamic cycle calculations

---

# Lecture 2: Fluid Property Models

**Source: Lecture#2_Slides.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #2

Fluid property models

Carl Hemprich 25 February 2026

===== Page 2 =====

Since last week, you are able to...
... point out the importance of heating and cooling for decarbonization
... use basic thermodynamic equations to show the differences between heating and cooling
... sketch the flow sheet of a simple Rankine-based heat pump cycle
... calculate all states and the COP of simple Rankine-based heat pump
... calculate the maximum efficiency of heat pumps and explain what it depends on

===== Page 3 =====

Thermodynamics of heat pumps Coefficient of Performance (COP)

[Image: Diagram showing heat pump with Q_high, Q_low, W_in]
How can we assess the performance of heat pumps?
For heating purposes: Objective: Rejected heat Q_high, Effort: Added Work W_in → COP_H = Q_high / W_in
For cooling purposes: Objective: Absorbed heat Q_low, Effort: Added Work W_in → COP_C = Q_low / W_in
COPs for heating are always ≥ 1

===== Page 4 =====

Thermodynamics of heat pumps Thermodynamic limit → Ideal process

[Image: T-s diagram of ideal cycle]
Entropy balance: δS_irr = dS_machine + (-|δQ_low|)/T_low + δQ_high/T_high
Ideal process must be reversible δS_irr = 0 → ∫ |δQ_low|/T_low = ∫ δQ_high/T_high
We consider T_low, T_high = const. → |Q_low| = (T_low/T_high)·Q_high
Coefficient of Performance: COP_H,max = Q_high/W_in = Q_high/(Q_high - |Q_low|)

===== Page 5 =====

Thermodynamics of heat pumps Thermodynamic limit (2)

[Image: T-s diagram]
We assumed δS_irr = 0, that means: The heat pump cycle is internally reversible. All heat transfers are reversible ⇒ no temperature differences ⇒ heat transfer takes infinite time. T_low = T_low,process, T_high = T_high,process

===== Page 6 =====

Thermodynamics of heat pumps Carnot-cycle

[Image: T-s diagram of Carnot cycle]
[Image: p-v diagram of Carnot cycle]
1→2: Reversible, adiabatic compression
2→3: Reversible, isothermal heat transfer
3→4: Reversible, adiabatic expansion
4→1: Reversible, isothermal heat transfer

===== Page 7 =====

Thermodynamics of heat pumps Carnot-cycle

[Image: T-s diagram]
We derived: COP_H = T_high/(T_high - T_low), COP_C = T_low/(T_high - T_low)
Carnot proposed such an ideal cycle in the 19th century. Without the knowledge of entropy. He found equal equations. Actually, for a heat engine.

===== Page 8 =====

1. We have a thermodynamic maximum on which real processes can be assessed.
[Image: Diagram showing Carnot COP as function of temperature ratio]
2. We can evaluate how the COP depends on temperatures. The COP increases for:
- decreasing temperature ratio between heat source and sink
- higher source temperatures
Keep the temperature ratio (T_high/T_low) as small as possible!

===== Page 9 =====

Thermodynamics of heat pumps How fair is the Carnot-limit?
Carnot assumed isothermal heat sources and sinks. However, sources and sinks are often not isothermal!
[Image: T-s diagram showing non-isothermal sources/sinks]
- The real process must follow the temperature regimes of the heat sink and source!
- Using the max. temperature ratio advantages the real process
- Using the min. temperature ratio disadvantages the real process
- Actually, we need an infinite number of Carnot-cycles connected in series

===== Page 10 =====

Thermodynamics of heat pumps Carnot-limit for non-isothermal sources and sinks
We need a kind of mean temperature: COP_H = T̄_high/(T̄_high - T̄_low)
These are not the arithmetic mean values, but the thermodynamic mean temperatures:
T̄_i = (∫ T·ds)/Δs = Δh/Δs (isobaric)
[Image: T-s diagram showing mean temperatures]
Keep the temperature ratio of T̄_high to T̄_low as small as possible!

===== Page 11 =====

Thermodynamics of heat pumps Why do we not build Carnot-cycles?
[Image: T-s diagram of Carnot with issues marked]
We need temperature differences to realize heat transfer in finite time.
Compressors are usually not reversible and cannot cope with wet compression (3→4).
Expanders are usually not reversible and cannot cope with wet compression (3→4).

===== Page 12 =====

Thermodynamics of heat pumps The simple heat pump cycle (reverse Rankine)
[Image: Flow sheet and T-s diagram]
A simple throttle replaces the expander isentropic ⇒ isenthalpic state change
The compressor is no longer isentropic
Point 1 is shifted to superheated steam (superheating)
Point 3 is often shifted to subcooled liquid (subcooling)

===== Page 13 =====

The simple heat pump cycle Carnot-limit and thermodynamic mean temperatures
We look at the inner cycle: COP_H = Q_high/(Q_high - Q_low) = (∫ T_high·dS_high)/(∫ T_high·dS_high - ∫ T_low·dS_low)
with T̄_i = (∫ T·ds)/Δs → COP_H = (T̄_high·ΔS_high)/(T̄_high·ΔS_high - T̄_low·ΔS_low)
[Image: T-s diagram]
If the process is not reversible, ΔS_high and ΔS_low are no longer equal. COP no longer solely depends on the mean temperatures. However, keep the temperature ratio as small as possible is still a good rule of thumb.

===== Page 14 =====

Where we stopped last week...
Known properties: As you see... ...we need refrigerant properties! Vapor-liquid equilibrium data, Caloric data (enthalpies, entropies...), maybe pVT-data.
Coming soon... (next week)
[Image: T-s diagram with entropy axis]

===== Page 15 =====

What you did in the exercise
# Calculating thermodynamic process states using

===== Page 16 =====

After this lecture, you will be able to...
... point out how refrigerant properties can be calculated
... Differentiate between fundamental equations, thermal and Helmholtz energy equations of state
... use equations of state to calculate real gas properties
... estimate the accuracy of property models
... select an appropriate property model for a certain application

===== Page 17 =====

Why can't we just use steam tables? A brief look into the history of refrigerants
Source: IPCC & EPA; https://www.epa.gov/ghgemissions/global-greenhouse-gas-overview

===== Page 18 =====

Why can't we just use steam tables? A brief look into the history of refrigerants
[No additional text]

===== Page 19 =====

Why can't we just use steam tables? A brief look into the history of refrigerants
[Image: Newspaper clipping about HCFC-123]
Da Pont produces HCFC-123, a hydrochlorofluorocarbon, in small quantities for evaluation in applications like industrial refrigeration, but is delaying full production until deadlines for phasing out HCFC's are clear.
Ozone Issue: Economics of a Ban
Continued on Page 04

===== Page 20 =====

Why can't we just use steam tables? A brief look into the history of refrigerants
[No additional text]

===== Page 21 =====

Why can't we just use steam tables? A brief look into the history of refrigerants
[Image: Title "REVIEW New refrigerants and system configurations for vapor-compression refrigeration"]
Search for alternative refrigerants remains relevant!

===== Page 22 =====

Which properties do we need
Thermal properties: Pressure p, Temperature T, Specific volume v

===== Page 23 =====

Which properties do we need
Thermal properties: Pressure p, Temperature T, Specific volume v
Caloric properties: Specific internal energy u, Specific enthalpy h, Specific entropy s

===== Page 24 =====

Which properties do we need
[No additional text]

===== Page 25 =====

Which properties do we need
[Image: Possibly diagram of transport properties]
Transport properties: Viscosity ν, Thermal conductivity λ

===== Page 26 =====

Two systems of equations of state open the world
[Image: Diagram comparing thermal EOS + ideal gas heat capacity vs Helmholtz EOS]
medium / good accuracy, strongly depends on molecule

===== Page 27 =====

Two systems of equations of state open the world Thermal equation of state
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)

===== Page 28 =====

Two systems of equations of state open the world Thermal equation of state
Thermal properties: p, T, v
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)

===== Page 29 =====

Two systems of equations of state open the world Thermal equation of state
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)
Thermal properties: p, T, v
Caloric properties: (dh_id/dT) = c_p,id(T), ds_id = dh_id/T + R/p (ideal gas)

===== Page 30 =====

Two systems of equations of state open the world Thermal equation of state
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)
Thermal properties: p, T, v
Caloric properties: (dh_id/dT) = c_p,id(T), ds_id = dh_id/T + R/p (ideal gas)
h - h_id = ∫_0^p [v - T(∂v/∂T)_p] dp

===== Page 31 =====

Two systems of equations of state open the world Thermal equation of state
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)
Thermal properties: p, T, v
Caloric properties: (dh_id/dT) = c_p,id(T), ds_id = dh_id/T + R/p (ideal gas)
h - h_id = ∫_0^p [v - T(∂v/∂T)_p] dp
ds = dh/T - v/T dp
u = h - pv, g = h - Ts, a = u - Ts

===== Page 32 =====

Two systems of equations of state open the world Thermal equation of state
Thermal equation of state: v = f(T, p) + Ideal gas heat capacity: c_p,id = f(T)
Thermal properties: p, T, v
Caloric properties: (dh_id/dT) = c_p,id(T), ds_id = dh_id/T + R/p (ideal gas)
h - h_id = ∫_0^p [v - T(∂v/∂T)_p] dp, ds = dh/T - v/T dp
u = h - pv, g = h - Ts, a = u - Ts
Vapor-liquid equilibrium: g_liquid = g_vapor, T_liquid = T_vapor, p_liquid = p_vapor

===== Page 33 =====

Two systems of equations of state open the world Helmholtz free energy
Thermodynamic potentials or Fundamental equations of thermodynamics:

===== Page 34 =====

Two systems of equations of state open the world Helmholtz free energy Helmholtz free energy equation of state a = f(T, v)

===== Page 35 =====

Two systems of equations of state open the world Helmholtz free energy
Thermal properties: T, ν, p = -(∂a/∂ν)_T
Helmholtz free energy equation of state: a = f(T, ν)

===== Page 36 =====

Two systems of equations of state open the world Helmholtz free energy
Helmholtz free energy equation of state: a = f(T, ν)
Thermal properties: T, ν, p = -(∂a/∂ν)_T
Caloric properties: h = a - T(∂a/∂T)_ν - ν(∂a/∂ν)_T, u = a - T(∂a/∂T)_ν, s = -(∂a/∂T)_ν, g = h - Ts

===== Page 37 =====

Two systems of equations of state open the world Helmholtz free energy
Helmholtz free energy equation of state a = f(T, v)
Thermal properties: T, v, p = -(∂a/∂v)_T
Caloric properties: h = a - T(∂a/∂T)_v - v(∂a/∂v)_T, u = a - T(∂a/∂T)_v, s = -(∂a/∂T)_v, g = h - Ts
Vapor-liquid equilibrium: g_liquid = g_vapor, T_liquid = T_vapor, p_liquid = p_vapor

===== Page 38 =====

Two systems of equations of state open the world Helmholtz free energy
Helmholtz free energy equation of state: a = f(T, ν)
Models often describe only the residual function a - a_id = a^res(T, ν)
Thermal properties: T, ν, p = -(∂a/∂ν)_T
Caloric properties: h = a - T(∂a/∂T)_ν - ν(∂a/∂ν)_T, u = a - T(∂a/∂T)_ν, s = -(∂a/∂T)_ν, g = h - Ts
Vapor-liquid equilibrium: g_liquid = g_vapor, T_liquid = T_vapor, p_liquid = p_vapor

===== Page 39 =====

Two systems of equations of state open the world Helmholtz free energy
Helmholtz free energy equation of state: a = f(T, v)
Models often describe only the residual function a - a_id ⇐ a^res(T, v)
Thermal properties: T, v, p = -(∂a/∂v)_T
Caloric properties: (du_id/dT) = c_v,id(T), ds_id = dh_id/T + R/p dp, g = h - Ts
Vapor-liquid equilibrium: g_liquid = g_vapor, T_liquid = T_vapor, p_liquid = p_vapor

===== Page 40 =====

Important equations of state for heat pumps

===== Page 41 =====

Fundamental equations of state
a - a_id = a^R(T, ν)

===== Page 42 =====

Fundamental equations of state
a - a_id = a^R(T, v)
E.g., according to Span and Wagner (2003)
α^R(τ,δ) = Σ_i=1^8 Σ_j=-8^12 n_i,j δ^i τ^(i/8) + Σ_i=1^5 Σ_j=-8^24 n_i,j δ^i τ^(i/8) exp(-δ) + Σ_i=1^5 Σ_j=16^56 n_i,j δ^i τ^(i/8) exp(-δ^2) + Σ_i=2^4 Σ_j=24^38 n_i,j δ^i τ^(i/2) exp(-δ^3)
Reduced spec. volume δ = v_critical / v
Reduced temperature τ = T_critical / T
Up to 583 terms (usually much less are used in practice)
Fitted to experimental data for each fluid

===== Page 43 =====

1
a - a_id = a^R(T, v)
E.g., according to Span and Wagner (2003)
α^R(τ,δ) = Σ_i=1^8 Σ_j=-8^12 n_i,j δ^i τ^(i/8) + Σ_i=1^5 Σ_j=-8^24 n_i,j δ^i τ^(i/8) exp(-δ) + Σ_i=1^5 Σ_j=16^56 n_i,j δ^i τ^(i/8) exp(-δ^2) + Σ_i=2^4 Σ_j=24^38 n_i,j δ^i τ^(i/2) exp(-δ^3)
Reduced spec. volume δ = v_critical / v
Reduced temperature τ = T_critical / T
Up to 583 terms (usually much less are used in practice)
Fitted to experimental data for each fluid
Highly accurate
Usually basis for property tables ("steam tables")

===== Page 44 =====

Fundamental equations of state
a - a_id = a^R(T, v)
E.g., according to Span and Wagner (2003)
[Equation repeated]
Up to 583 terms (usually much less are used in practice)
Fitted to experimental data for each fluid
Highly accurate
Usually basis for property tables ("steam tables")
But: Only available for a few substances ⇒ We need predictive methods for all others

===== Page 45 =====

Important equations of state for heat pumps

===== Page 46 =====

Ideal gas

===== Page 47 =====

pV = mR_i T
It has "gas" in its name!
• No liquid states
• No two-phase states

===== Page 48 =====

[Page contains a large grid of numbers from 0.1 to 100, likely a pressure-temperature grid or numerical data]

===== Page 49 =====

100
It has "gas" in its name!
- No liquid states
- No two-phase states
[Image: T-s diagram showing ideal gas region]
Unfortunately, large parts of vapor-compression heat pump processes mainly take place within two-phase region.
However, the compression step is in the vapor region

===== Page 50 =====

Ideal gas Limits in validity - accuracy

===== Page 51 =====

Ideal gas Limits in validity - accuracy
[Image: Graph showing deviation from ideal gas behavior as function of reduced pressure and reduced temperature]

===== Page 52 =====

Ideal gas Limits in validity - accuracy
[Image: Same graph as page 51]

===== Page 53 =====

Ideal gas Limits in validity - accuracy
[Image: Graph with refrigerant R1234yf data]
Poor accuracy for:
- Medium/low temperatures
- Medium/high pressures
- Large molecules
- Polar molecules
- Close to the dew line
Refrigerant: R1234yf

===== Page 54 =====

Ideal gas Limits in validity - accuracy
[Image: Graph with R1234yf data and a zoomed inset]
Poor accuracy for:
- Medium/low temperatures
- Medium/high pressures
- Large molecules
- Polar molecules
- Close to the dew line
[Image inset showing close to dew line region]

===== Page 55 =====

1. Ideal gas Caloric properties
dh = c_p,id(T) dT, ds = dh/T - ν/T dp = c_p,id(T)/T dT - R_i/p dp
h2 - h1 = ∫_{T1}^{T2} c_p,id(T) dT, s2 - s1 = ∫_{T1}^{T2} c_p,id(T)/T dT - R_i·ln(p2/p1)
Perfect gas: c_p,id = const.

===== Page 56 =====

Main assumption: v = const. ≠ f(T, p)

===== Page 57 =====

Incompressible fluid
Main assumption: v = const. ≠ f(T, p)
dh = c_IL(T) dT + v dp
h2 - h1 = ∫_{T1}^{T2} c_IL(T) dT + v(p2 - p1)
ds = c_IL(T)/T dT
s2 - s1 = ∫_{T1}^{T2} c_IL(T)/T dT
- c_p and c_v are equal → c_IL
- the vdp is often neglected
- c_IF is often assumed to be constant

===== Page 58 =====

Incompressible fluid
02/25/2026
62
v = const. ≠ f(T, p)
Main assumption:
dh = c_iL(T) dT + v dp
h2 - h1 = ∫_{T1}^{T2} c_iL(T) dT + v(p2 - p1)
ds = c_iL(T)/T dT
s2 - s1 = ∫_{T1}^{T2} c_iL(T)/T dT
• cp and cv are equal → ciL
• the vdp is often neglected
• ciF is often assumed to be constant
• Good model for liquids if temperature and pressure changes are small
• Only a small part of a heat pump process (subcooling) takes place in the liquid region
• However, simple and suitable property model, e.g. for liquid heat sinks and sources
C. Hemprich - Sustainable Heating and Cooling Technologies #2

===== Page 59 =====

Important equations of state for heat pumps

===== Page 60 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
Ideal gas: pv_m = nRT
First cubic EOS (Van der Waals)

===== Page 61 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
[No additional text]

===== Page 62 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
[Image: Graph comparing ideal gas and Van der Waals isotherms]
Why cubic equations of state?

===== Page 63 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
[No additional text]

===== Page 64 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
[No additional text]

===== Page 65 =====

Cubic equations of state (EOS) From ideal gas to Van der Waals
[No additional text]

===== Page 66 =====

Cubic equations of state (EOS) Peng-Robinson
p = (RT)/(V_m - b) - (aα)/(V_m^2 + 2bV_m - b^2)
a ≈ 0.45724 (R^2 T_c^2)/p_c
b ≈ 0.07780 (R T_c)/p_c
α = (1 + κ(1 - T_r^(1/2)))^2
κ ≈ 0.37464 + 1.54226ω - 0.26992ω^2
T_r = T/T_c

===== Page 67 =====

Cubic equations of state (EOS) Peng-Robinson
p = (RT)/(V_m - b) - (aα)/(V_m^2 + 2bV_m - b^2)
a ≈ 0.45724 (R^2 T_c^2)/p_c
b ≈ 0.07780 (R T_c)/p_c
α = (1 + κ(1 - T_c^(1/2)))^2 (Note: T_c instead of T_r? Typo in slide)
κ ≈ 0.37464 + 1.54226ω - 0.26992ω^2
T_r = T/T_c
Inputs: Critical temperature T_c, Critical pressure p_c, Acentric factor ω

===== Page 68 =====

Cubic equations of state (EOS) Peng-Robinson
[Same equations as page 67, with T_r formula]
Inputs: Critical temperature T_c, Critical pressure p_c, Acentric factor ω
Refrigerant: R1234yf

===== Page 69 =====

Cubic equations of state (EOS) Peng-Robinson
[Same equations, with T_r in α formula correctly]
Inputs: Critical temperature T_c, Critical pressure p_c, Acentric factor ω
Refrigerant: R1234yf

===== Page 70 =====

Cubic equations of state (EOS) Peng-Robinson
[Same equations, with T_c in α? possibly a typo, but as shown]
Combined with c_p,id(T) → caloric properties
Refrigerant: R1234yf

===== Page 71 =====

1. Are a sufficiently accurate model for many applications
2. Often used in industry
3. Easy to implement
4. Require less information about the substance
5. Large number of different forms are available → Often for special conditions
6. Most used forms:
7. Peng-Robinson
8. Redlich-Kwong / Soave-Redlich-Kwong
9. Still inaccurate for polar molecules

===== Page 72 =====

1. Are a sufficiently accurate model for many applications
- Often used in industry
- Easy to implement
- Require less information about the substance
- Large number of different forms are available → Often for special conditions
- Most used forms:
- Peng-Robinson
- Redlich-Kwong / Soave-Redlich-Kwong
- Still inaccurate for polar molecules

===== Page 73 =====

Important equations of state for heat pumps

===== Page 74 =====

Perturbed-Chain-Polar – Statistical Associating Fluid Theory

===== Page 75 =====

Perturbed-Chain-Polar – Statistical Associating Fluid Theory
[No additional text]

===== Page 76 =====

Perturbed-Chain-Polar - Statistical Associating Fluid Theory
[Image: Diagram of PC-SAFT contributions]
a_res = a_hard_spheres + a_chain + a_dispersion + a_association + a_polar

===== Page 77 =====

Perturbed-Chain-Polar - Statistical Associating Fluid Theory
[Image: Diagram showing the same contributions plus ideal gas]
[Image: Table of required parameters]
Ideal gas Helmholtz energy → c_p,id(T) is required
Required parameters: segment diameter σ, segment number m, segment dispersion energy ε/k, association energy ε^AB/k, association volume κ^AB, dipole moment μ, ideal gas heat capacity c_p,id

===== Page 78 =====

Perturbed-Chain-Polar - Statistical Associating Fluid Theory
[No additional text]

===== Page 79 =====

From where do we get the required parameters? Some important databases
Thermodynamic properties, e.g., T_c, p_c, ω, c_p,id(T), VLE, and more
AIChE DIPPR 801, DDBST Dortmund database
[Image: Logo of DDBST]
Chemistry webbook, Scientific papers

===== Page 80 =====

From where do we get the required parameters? Group contribution methods

===== Page 81 =====

From where do we get the required parameters? Group contribution methods
[Image: Diagram showing molecular structure with functional groups]

===== Page 82 =====

From where do we get the required parameters? Group contribution methods
[Image: Same diagram]

===== Page 83 =====

From where do we get the required parameters? Group contribution methods
[Image: Two diagrams: molecular structure and a table of group contribution methods]
Some group contribution methods:
- Joback and Reid
- Ambrose
- Constantinou and Gani
- Marrero and Pardillo
- UNIFAC
For PCP-SAFT:
- Sauer et al., 2014 (Link)
- Hemprich et al., 2024 (Link)

===== Page 84 =====

Greetings from science Deep learning methods
[Image: Paper title "Understanding the language of molecules: predicting pure component parameters for the PC-SAFT equation of state from SMILES" by Benedikt Winter, Philipp Rehner, Timm Esper, Johannes Schilling and André Bardow]

===== Page 85 =====

Transport properties
We usually also need transport properties, e.g., for flow and heat transfer calculations

===== Page 86 =====

Transport properties
We usually also need transport properties, e.g., for flow and heat transfer calculations
[Image: Diagram showing thermal conductivity and viscosity correlations]
Mostly used are empirical correlations, e.g.,
Thermal conductivity λ_vapor = (A T^B)/(1 + C/T + D/T^2)
Dynamic viscosity η_liquid = exp(A + B/T + C·ln(T) + D T^E)
Can be found in:

===== Page 87 =====

Transport properties
We usually also need transport properties, e.g., for flow and heat transfer calculations
[Image: Same correlations and an additional graph]
Also, calculating transport properties from equilibrium properties is possible, e.g. by entropy scaling

===== Page 88 =====

Combine parameter databases with implementations of property models

===== Page 89 =====

Combine parameter databases with implementations of property models

===== Page 90 =====

Combine parameter databases with implementations of property models

===== Page 91 =====

Combine parameter databases with implementations of property models

===== Page 92 =====

Introduction to this week’s exercise

===== Page 93 =====

Task description
[Image: Diagram of simple heat pump cycle]
No superheating and subcooling, isentropic compressor
a) Write a function to calculate the heat pump's coefficient of performance (COP) as function of evaporation and condensation temperatures.
b) Determine the COP for varying evaporator temperature T_ev between -5°C and 10°C and condenser temperature T_co between 25°C and 40°C.
With superheating and real compressor behavior
a) Extend the function from a) to consider the compressor efficiency η_is and superheating ΔT_sh as input parameters. T_co is now 35°C, and T_ev is 0°C with 10K superheating after the evaporator. Calculate the COP and the thermodynamic mean temperatures T_m,i of the refrigerant in the heat exchangers while varying the compressor efficiency between 0.4-1.0.

===== Page 94 =====

Calculating process states Without superheating and subcooling
[Table of states and state changes: 1→2 Compression with η_is, 2→3 Isobaric condensation, 3→4 Isenthalpic expansion, 4→1 Isobaric evaporation]
[Image: T-s diagram]
[Image: p-h diagram]
Known properties: Evaporation temperature T_ev, Condensation temperature T_co, Isentropic compressor efficiency η_is, Refrigerant
[Table of determined properties: State 1: T1=T_ev, x1=1; State 3: T3=T_co, x3=0; State 2: h2=(h2,is-h1)/η_is+h1, p2=p_co; State 4: h4=h3, p4=p1]

===== Page 95 =====

Calculating process states With superheating and subcooling
Known properties: Evaporation temperature T_ev, Superheating ΔT_sh, Condensation temperature T_co, Subcooling ΔT_sc, Isentropic compressor efficiency η_is, Refrigerant
[Image: T-s diagram]
[Table of states: State 1': T1'=T_ev, x1'=1; State 1: T1=T1'+ΔT_sh, p1=p_ev; State 3': T3'=T_co, x3'=0; State 3: T3=T3'-ΔT_sc, p3=p_co; State 2: h2=(h2,is-h1)/η_is+h1, p2=p_co; State 4: h4=h3, p4=p1]

===== Page 96 =====

Calculating the COP
[Image: T-s diagram with states]
Energy balance for the heat pump: w_comp + q_low - q_high = 0
COP equals revenue per effort!
q_high: revenue, w_comp: effort, q_low: for free!
COP = revenue/effort = q_high/w_comp = (h2 - h3)/(h2 - h1)

===== Page 97 =====

Calculating thermodynamic mean temperatures
[Image: T-s diagram showing mean temperature definition]
Mean temperature of heat rejection from state 2 to state 3
Mean temperature of heat uptake from state 4 to state 1
[Image: T-s diagram with shaded areas]
ṁ ∫ T(s) ds = ṁ·T̄·Δs
T̄ = (∫ T(s) ds)/Δs = (∫ dh - ∫ x dp̄)/Δs = Δh/Δs

===== Page 98 =====

Why are the mean temperatures important?
Not exactly valid if compressor and throttle are not reversible, but nevertheless useful
[Image: T-s diagrams showing mean temperatures]
Keep the temperature ratio of T̄_high to T̄_low as small as possible!
It is easy to estimate how changes to the process (evaporation and condensation temperatures, compressor efficiency...) will change the thermodynamic mean temperatures.
[Image: Small diagram with arrow]
Get a feeling for it and you will always know what to do to increase the COP

===== Page 99 =====

Please go through the tutorial on "Contour" before the exercise It explains how to create contour plots Available on moodle

---

# Lecture 3: Heat Sources and Sinks – Pinch Model

**Source: SHCT26_Lec3.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #3

Heat sources and sinks Pinch model

Lana Liebl Leon Brendel, PhD 04 March 2026

===== Page 2 =====

Excursion 29.04.2026: 10:00-12:00 Lake heat network (Kongresshaus) and big heat pumps with ewz and Scheco
Please let us know if you participate by filling out the survey in moodle until 05.03.26

===== Page 3 =====

Since the last lecture, you are able to...
... point out how refrigerant properties can be calculated
... Differentiate between fundamental equations, thermal and Helmholtz energy equations of state
... use equations of state to calculate real gas properties
... estimate the accuracy of property models
... select an appropriate property model for a certain application

===== Page 4 =====

How the COP depends on the process temperatures Results from last week's exercise
Propane, no superheating, isentropic compressor
[Two graphs: COP as function of T_ev and T_co?]
The COP of a heat pump substantially depends on evaporation and condensation temperatures. The COP increases with increasing evaporation and decreasing condensation temperature

===== Page 5 =====

How the COP depends on the process temperatures Results from last week's exercise
[Image: Three small graphs - COP as function of T_ev and T_co, mean temperatures, etc.]
Higher compression efficiency decreases the compressor outlet temperature and, thus, the thermodynamic mean temperature in the condenser.
No effect on thermodynamic mean temperature in the evaporator
The closer the ratio of the thermodynamic mean temperatures of evaporator and condenser is to 1, the higher the COP of the heat pump process.

===== Page 6 =====

After this lecture, you will be able to...
...classify common heat pump heat sources and sinks by
- Temperatures
- Availability
- Costs for tapping
- Prevalence
[Image: Small photo of a heat pump?]
...use pinch models to connect process states with the heat sink and source
...understand the principles of constraint optimization

===== Page 7 =====

Heat sources and sinks Overview residential heating
[Image: Icons for Water, Brine/geothermal heat, Air]

===== Page 8 =====

Heat sources and sinks Overview residential heating
[Image: Diagram showing groundwater, geothermal probe, air source]

===== Page 9 =====

Heat sources and sinks Overview residential heating
[No additional text]

===== Page 10 =====

Heat sources and sinks Overview residential heating
[No additional text]

===== Page 11 =====

Heat source: groundwater

===== Page 12 =====

The temperature of groundwater is nearly constant over the year.
Depending on the location and depth, mean temperatures are between 8 and 14 °C

===== Page 13 =====

Groundwater must be available at an acceptable depth
Extraction capacity must match the regeneration capability of the ground water
Groundwater usage is usually subject to approval by the municipality
Costs for the wells only slightly correlate with the heating capacity

===== Page 14 =====

Groundwater must be available at an acceptable depth
Extraction capacity must match the regeneration capability of the ground water
Groundwater usage is usually subject to approval by the municipality
Costs for the wells only slightly correlate with the heating capacity
Advantages: Constant high temperatures → high COPs; Usually, high heating capacities possible

===== Page 15 =====

Groundwater must be available at an acceptable depth
Extraction capacity must match the regeneration capability of the ground water
Groundwater usage is usually subject to approval by the municipality
Costs for the wells only slightly correlate with the heating capacity
Advantages: Constant high temperatures ⇒ high COPs; Usually, high heating capacities possible
Disadvantages: Drilling the wells is very expensive (approx. 15'000 - 25'000 CHF); Minimum distance of the wells must be kept ⇒ plot size must be sufficient

===== Page 16 =====

Heat source: groundwater Wrap-up
- Groundwater must be available at an acceptable depth
- Extraction capacity must match the regeneration capability of the groundwater
- Groundwater usage is usually subject to approval by the municipality
- Costs for the wells only slightly correlate with the heating capacity
Advantages: Constant high temperatures → high COPs; Usually, high heating capacities possible
Disadvantages: Drilling the wells is very expensive (approx. 15'000 - 25'000 CHF); Minimum distance of the wells must be kept → plot size must be sufficient
[Image: Small photo of a drilling rig?]

===== Page 17 =====

Two concepts
Ground horizontal collector "large space - low depth"
[Image: Diagram of horizontal collector]
Brine is circulating, e.g. water glycol mixture

===== Page 18 =====

Two concepts
Ground horizontal collector "large space - low depth"
Ground vertical collector "small space - large depth"

===== Page 19 =====

Rule of thumb: From 10 m depth the temperature increases by 1 K every 30 m
[Image: Diagram showing geothermal gradient]

===== Page 20 =====

Rule of thumb: From 10 m depth the temperature increases by 1 K every 30 m
[Image: Same diagram with additional labels]

===== Page 21 =====

Rule of thumb: From 10 m depth the temperature increases by 1 K every 30 m
[No additional text]

===== Page 22 =====

20 3 cm Tiefe Depth (cm) 63 125 251 502 753 0 5 8-12°C 10-14°C 15 150 40-100°C
[Image: Diagram of temperature vs depth]

===== Page 23 =====

Ground horizontal collector Various types
[Image: Two photos of ground horizontal collector installations]

===== Page 24 =====

Ground horizontal collector Wrap-up
- Heating capacity correlates with area
- Typical heat extraction capacity is 25 W·m⁻²
- Rule of thumb: A_collector = 1.5 · A_heated
- Costs correlate with heating capacity
[Image: Diagram of horizontal collector]

===== Page 25 =====

Ground horizontal collector Wrap-up
Heating capacity correlates with area
- Typical heat extraction capacity is 25 W·m⁻²
- Rule of thumb: A_collector = 1.5 · A_heated
- Costs correlate with heating capacity
[Image: Same diagram]
Advantages: Always temperatures above the ambient temperature; Moderate costs: 5 - 8 kCHF for a single family house

===== Page 26 =====

Ground horizontal collector Wrap-up
Heating capacity correlates with area
- Typical heat extraction capacity is 25 W·m⁻²
- Rule of thumb: A_collector = 1.5 · A_heated
- Costs correlate with heating capacity
[Image: Photo of horizontal collector installation]
Advantages: Always temperatures above the ambient temperature; Moderate costs: 5 – 8 kCHF for a single family house
[Image: Small icon of a house?]
Disadvantages: The temperature slightly fluctuates during the year; Large space required which cannot be built upon

===== Page 27 =====

Ground vertical collector Wrap-up
- Heating capacity and temperature correlates with depth
- Typical heat extraction capacity is 45 W·m⁻¹
- Costs correlate with heating capacity

===== Page 28 =====

Ground vertical collector Wrap-up
- Heating capacity and temperature correlates with depth
- Typical heat extraction capacity is 45 W·m⁻¹
- Costs correlate with heating capacity
Advantages: Constantly high temperatures; Low space requirement

===== Page 29 =====

Ground vertical collector Wrap-up
Heating capacity and temperature correlates with depth
- Typical heat extraction capacity is 45 W·m⁻¹
- Costs correlate with heating capacity
Advantages: Constantly high temperatures; Low space requirement
[Image: Photo of vertical collector drilling]
Disadvantages: The drilling is subject to approval (often soil survey required); Drilling is expensive (approx. 100 CHF/m); Total collector costs about 20 kCHF for single family house; Not possible everywhere (e.g., in water protection areas)

===== Page 30 =====

Ground vertical collector
[Image: Two photos of vertical collector installations]

===== Page 31 =====

Three types of installation
[Image: Diagram of three types: direct expansion, brine-to-water, water-to-water]
Water/glycol mixture
Evaporator, compressor, throttle

===== Page 32 =====

Three types of installation
[Image: Three diagrams showing direct expansion, brine-to-water, water-to-water with labels]
Water/glycol mixture
Evaporator, compressor, throttle

===== Page 33 =====

Heat source: ambient air Examples
[Image: Two photos of air-source heat pumps]

===== Page 34 =====

Air temperature substantially fluctuates over the year.
[No additional text]

===== Page 35 =====

Air temperature substantially fluctuates over the year.
[No additional text]

===== Page 36 =====

Air temperature substantially fluctuates over the year.
[Image: Graph of air temperature vs month showing fluctuation]
Source temperature (resp. COP, supplied heat) contradicts heating demand!

===== Page 37 =====

Heat source: ambient air Wrap-up
Advantages: Very cheap; Low space requirement; Can easily be installed in existing buildings

===== Page 38 =====

Heat source: ambient air Wrap-up
Advantages: Very cheap; Low space requirement; Can easily be installed in existing buildings given available space
Disadvantages: COP and supplied heat are the lowest when the heating demand is the highest; Freezing problem requires additional energy for defrosting; High noise emissions (depending on installation)

===== Page 39 =====

Heat sources - costs vs. efficiency Residential heating
[No additional text]

===== Page 40 =====

Heat sources - costs vs. efficiency Residential heating
[No additional text]

===== Page 41 =====

Heat sources - costs vs. efficiency Residential heating
[No additional text]

===== Page 42 =====

New developments – greetings from science Ultra-low-temperature district heating networks
Currently common heating networks

===== Page 43 =====

New developments – greetings from science Ultra-low-temperature district heating networks
Currently common heating networks

===== Page 44 =====

New developments – greetings from science Ultra-low-temperature district heating networks
[Image: Diagram of 4th generation district heating network]
Pipes must be well insulated and partly pressure resistant

===== Page 45 =====

5th generation heating network
Pipes must not be well insulated and pressure resistant

===== Page 46 =====

5th generation heat
Promises: Every building gets access to a high-efficient heat source; Lower investment costs for consumers; Improved integration of renewables and waste heat sources; Lower heat losses; Decreased investment costs for the network
Current research: Thermo-economic and life cycle assessment on case studies; Challenges in construction and operation; Integration of decentralized waste heat; Business models
Interested in more? ⇒ e.g., https://doi.org/10.1016/j.rser.2018.12.059
Pipes must not be well insulated and pressure resistant

===== Page 47 =====

Domestic heating
[Image: Four photos/diagrams of heating systems with temperature labels]
50 < T < 70 °C
30 < T < 40 °C
40 < T < 52 °C
55 - 60 °C
Lower temperatures are critical due to legionella bacteria

===== Page 48 =====

Industrial heat sources and sinks
[Image: Diagram of industrial processes with temperature ranges]
Everything is possible!
Follow-up in lecture 9

===== Page 49 =====

Pinch model

===== Page 50 =====

The condensation temperature can be decreased until the refrigerant's state change from 2 to 3 touches the state change of the heat sink.
The evaporation temperature can be increased until the refrigerant's state change from 4 to 1 touches the state change of the heat source.

===== Page 51 =====

The condensation temperature can be decreased until the refrigerant's state change from 2 to 3 touches the state change of the heat sink.
The evaporation temperature can be increased until the refrigerant's state change from 4 to 1 touches the state change of the heat source.
[No additional text]

===== Page 52 =====

The condensation temperature can be decreased until the refrigerant's state change from 2 to 3 touches the state change of the heat sink.
The evaporation temperature can be increased until the refrigerant's state change from 4 to 1 touches the state change of the heat source.
[Image: T-s diagram showing pinch points]
We call these touching points "pinch points"
In real processes we need at the pinch point a temperature difference >0 K, otherwise there would be no heat transfer

===== Page 53 =====

The condensation temperature can be decreased until the refrigerant's state change from 2 to 3 touches the state change of the heat sink.
The evaporation temperature can be increased until the refrigerant's state change from 4 to 1 touches the state change of the heat source.
[Image: T-s diagram]
We call these touching points "pinch points"
In real processes we need at the pinch point a temperature difference >0 K to enable heat transfer in finite time
We call the temperature difference at a pinch point "approach temperature"

===== Page 54 =====

Possible positions of pinch points Counterflow heat exchangers, sensible media
[No additional text]

===== Page 55 =====

Possible positions of pinch points Counterflow heat exchangers, sensible media
[No additional text]

===== Page 56 =====

Possible positions of pinch points Isothermal heat sources and sinks
- Condensing and evaporating steam
- Melting or freezing ice
- Sensible media in cross-flow heat exchangers (single layer), e.g., air heat pump

===== Page 57 =====

Possible positions of pinch points Isothermal heat sources and sinks
- Condensing and evaporating steam
- Melting or freezing ice
- Sensible media in cross-flow heat exchangers (single layer), e.g., air heat pump
[No additional text]

===== Page 58 =====

Possible positions of pinch points Isothermal heat sources and sinks
- Condensing and evaporating steam
- Melting or freezing ice
- Sensible media in cross-flow heat exchangers (single layer), e.g., air heat pump
Condenser [diagram], Evaporator [diagram]

===== Page 59 =====

Conditions to keep a minimum approach temperature Evaporator
Counterflow, sensible media
[Image: T-s diagram of evaporator with source temperatures]
Minimum approach temperature: ΔT_app,min
1) T_source_in - T1 ≥ ΔT_app,min
2) T_source_out - T4 ≥ ΔT_app,min

===== Page 60 =====

Conditions to keep a minimum approach temperature Condenser
Counterflow, sensible media
Minimum approach temperature: ΔT_app,min
1) T3 - T_sink_in ≥ ΔT_app,min
2) T2 - T_sink_out ≥ ΔT_app,min
3) T_ref_dew - T_sink_dew ≥ ΔT_app,min

===== Page 61 =====

Conditions to keep a minimum approach temperature Condenser
Counterflow, sensible media
Minimum approach temperature: ΔT_app,min
1) T3 - T_sink_in ≥ ΔT_app,min
2) T2 - T_sink_out ≥ ΔT_app,min
3) T_ref_dew - T_sink_dew ≥ ΔT_app,min
T_ref_dew = T_co

===== Page 62 =====

Conditions to keep a minimum approach temperature Condenser
[Image: T-s diagram of condenser with sink temperatures]
Minimum approach temperature: ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
T_ref_dew = T_co
Energy balances:
0 = ṁ_ref(h_ref_dew - h2) + ṁ_sink(h_sink_out - h_sink_dew)

===== Page 63 =====

Conditions to keep a minimum approach temperature Condenser
[Image: Same T-s diagram]
Minimum approach temperature: ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
T_ref_dew = T_co
Energy balances:
0 = ṁ_ref(h_ref_dew - h2) + ṁ_sink(h_sink_out - h_sink_dew)
0 = ṁ_ref(h3 - h2) + ṁ_sink(h_sink_out - h_sink_in)

===== Page 64 =====

Conditions to keep a minimum approach temperature Condenser
[Image: Same T-s diagram]
Minimum approach temperature: ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
T_ref_dew = T_co
Energy balances:
0 = ṁ_ref(h_ref_dew - h2) + ṁ_sink(h_sink_out - h_sink_dew)
0 = ṁ_ref(h3 - h2) + ṁ_sink(h_sink_out - h_sink_in)
h_sink_dew = h_sink_out - (h2 - h_ref_dew)/(h2 - h3) (h_sink_out - h_sink_in)
h_sink_dew → T_sink_dew

===== Page 65 =====

It is straightforward but not that straightforward Counterflow heat exchangers, sensible media
[Image: T-s diagram of condenser]

===== Page 66 =====

It is straightforward but not that straightforward Counterflow heat exchangers, sensible media
[No additional text]

===== Page 67 =====

It is straightforward but not that straightforward Counterflow heat exchangers, sensible media
[No additional text]

===== Page 68 =====

It is straightforward but not that straightforward Counterflow heat exchangers, sensible media
[No additional text]

===== Page 69 =====

It is straightforward but not that straightforward (2) Counterflow heat exchangers, sensible media
[No additional text]

===== Page 70 =====

It is straightforward but not that straightforward (2) Counterflow heat exchangers, sensible media
[Image: T-s diagram showing condensation temperature decreased]

===== Page 71 =====

It is straightforward but not that straightforward (2) Counterflow heat exchangers, sensible media
[Image: Same diagram with annotation "Condensation temperature decreased"]

===== Page 72 =====

It is straightforward but not that straightforward (2) Counterflow heat exchangers, sensible media
Condensation temperature decreased [diagram]

===== Page 73 =====

Which minimum approach temperature is appropriate?
Q̇ = U·∫_0^L (T_hot(A) - T_cold(A)) dA
Reducing the temperature difference leads to an increase in heat transfer area

===== Page 74 =====

Which minimum approach temperature is appropriate?
Q̇ = U·∫_0^L (T_hot(A) - T_cold(A)) dA
Reducing the temperature difference leads to an increase in heat transfer area
[Image: Graph showing area vs approach temperature for common heat exchangers]
Common heat exchangers (e.g., liquid/liquid) Small approach temperatures can massively increase the heat transfer area

===== Page 75 =====

Which minimum approach temperature is appropriate?
Q̇ = U·∫_0^L (T_hot(A) - T_cold(A)) dA
Reducing the temperature difference leads to an increase in heat transfer area
[Image: Same graph]
Common heat exchangers (e.g., liquid/liquid) Small approach temperatures can massively increase the heat transfer area
ΔT_app,min: 5-20 K

===== Page 76 =====

Which minimum approach temperature is appropriate?
Q̇ = U·∫_0^L (T_hot(A) - T_cold(A)) dA
Reducing the temperature difference leads to an increase in heat transfer area
[Image: Graph]
Common heat exchangers (e.g., liquid/liquid) Small approach temperatures can massively increase the heat transfer area
Heat pump condenser and evaporator Mean temperature difference still large even for small approach temperatures

===== Page 77 =====

Which minimum approach temperature is appropriate?
Q̇ = U·∫_0^L (T_hot(A) - T_cold(A)) dA
Reducing the temperature difference leads to an increase in heat transfer area
[Image: Graph]
ΔT_app,min
Common heat exchangers (e.g., liquid/liquid) Small approach temperatures can massively increase the heat transfer area
Heat pump condenser and evaporator
Mean temperature difference still large even for small approach temperatures
[Image: Second graph showing area vs approach temperature for heat pump heat exchangers]
heat transfer area A

===== Page 78 =====

Introduction to this week’s exercise

===== Page 79 =====

Task of the today's exercise
The following parameters are given for the heat pump process:
Superheating ΔT_sh = 10 K, Subcooling ΔT_sc = 5 K, Compressor efficiency: η_is = 0.52
Source: liquid water, T_so_in = 10°C, T_so_in = 5°C? (typo likely T_so_out)
Sink: liquid water, T_si_in = 30°C, T_si_out = 36°C
The heat exchangers operate in counterflow
a) Implement a function that calculates the heat pump COP as a function of evaporation and condensation temperature and returns the reciprocal value of the COP (1/COP). You might copy parts from the last exercise.
b) Implement two functions that calculate the approach temperatures at all possible pinch points in the evaporator and condenser. The functions should return a vector containing the approach temperatures.
c) Optimize the heat pump process regarding the COP. The optimal temperatures T_ev and T_co are determined while meeting the constraint of a minimum approach temperature of 0.5K in the heat exchanger. Print the optimal values of T_ev, T_co, and COP and plot the optimized process in a T-h-diagram using the program plotDiag_Th_Ts.py. The program and a tutorial are available in the module course.

===== Page 80 =====

Calculation of approach temperatures
[Image: T-s diagram with states and approach temperatures]
First, calculate all required process states
Evaporator: ΔT_app,P1 = T_so_out - T4, ΔT_app,P2 = T_so_in - T1
Condenser: ΔT_app,P3 = T2 - T_si_out, ΔT_app,P4 = T_dew - T_si_dew = T_co - T_si_dew
h_si_dew = h_si_out - (h_si_out - h_si_in)/(h2 - h3) (h2 - h_dew)
T_si_dew = f(h_si_dew, p_dew)
ΔT_app,P5 = T3 - T_si_in

===== Page 81 =====

Optimization

===== Page 82 =====

Evaporation and condensation temperatures have a major impact on the COP
"Keep the temperature lift small"

===== Page 83 =====

What we have learned so far
Evaporation and condensation temperatures have a major impact on the COP
"Keep the temperature ratio small"
Evaporation and condensation temperatures are not freely chosen. They are limited by the heat source and sink

===== Page 84 =====

What we have learned so far
Evaporation and condensation temperatures have a major impact on the COP
"Keep the temperature ratio small"
Evaporation and condensation temperatures are not freely chosen. They are limited by the heat source and sink
Our task: designing the best heat pump process for a given heat source and sink

===== Page 85 =====

What we have learned so far
Evaporation and condensation temperatures have a major impact on the COP
"Keep the temperature ratio small"
Evaporation and condensation temperatures are not freely chosen. They are limited by the heat source and sink
Our task: designing the best heat pump process for a given heat source and sink
# Constrained optimization

===== Page 86 =====

Heat pump optimization
max_{T_ev, T_co} COP(T_ev, T_co, w)
s.t. g1(T_ev, T_co, w) ≥ ΔT_app,min
T_ev,min ≤ T_ev ≤ T_ev,max ∈ R
T_co,min ≤ T_co ≤ T_co,max ∈ R

===== Page 87 =====

Heat pump optimization
max COP(T_ev, T_co, w)
s.t. g1(T_ev, T_co, w) ≥ ΔT_app,min
T_ev,min ≤ T_ev ≤ T_ev,max ∈ R
T_co,min ≤ T_co ≤ T_co,max ∈ R
w: constant variables, e.g., ΔT_superheating, Q̇_high, T_source_in etc.

===== Page 88 =====

Heat pump optimization
[Image: T-s diagram with constraints]
Constraints:
T_source_in - T1 ≥ ΔT_app,min
T_source_out - T4 ≥ ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
w: constant variables, e.g., ΔT_superheating, Q̇_high, T_source_in etc.

===== Page 89 =====

1
max COP(T_ev, T_co, w) T_ev,T_co
s.t. g1(T_ev, T_co, w) ≥ ΔT_app,min
T_ev,min ≤ T_ev ≤ T_ev,max ∈ R
T_co,min ≤ T_co ≤ T_co,max ∈ R
Constraints:
T_source_in - T1 ≥ ΔT_app,min
T_source_out - T4 ≥ ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
Bounds: e.g., T_co < T_crit → subcritical process
w: constant variables, e.g., ΔT_superheating, Q̇_high, T_source_in etc.

===== Page 90 =====

1. Heat pump optimization
max COP(T_ev, T_co, w) T_ev,T_co
s.t. g1(T_ev, T_co, w) ≥ ΔT_app,min
T_ev,min ≤ T_ev ≤ T_ev,max ∈ R
T_co,min ≤ T_co ≤ T_co,max ∈ R
Constraints:
T_source_in - T1 ≥ ΔT_app,min
T_source_out - T4 ≥ ΔT_app,min
T3 - T_sink_in ≥ ΔT_app,min
T2 - T_sink_out ≥ ΔT_app,min
T_ref_dew - T_sink_dew ≥ ΔT_app,min
The objective function and the constraints are not linear functions
e.g., T_co < T_crit → subcritical process
Constrained non-linear problem (NLP)
w: constant variables, e.g., ΔT_superheating, Q̇_high, T_source_in etc.

===== Page 91 =====

Optimization algorithm
Variables to be optimized x = [T_ev, T_co]
Objective value, e.g., COP

===== Page 92 =====

Optimization algorithm
Variables to be optimized x = [T_ev, T_co]
Objective value, e.g., COP
Objective: COP [diagram]

===== Page 93 =====

Optimization algorithm
Variables to be optimized x = [T_ev, T_co]
Objective value, e.g., COP
[No additional text]

===== Page 94 =====

Optimization algorithm
Variables to be optimized x = [T_ev, T_co]
Objective value, e.g., COP
Objective: COP [diagram]

===== Page 95 =====

Your tasks prior to the exercise
Go through the tutorials on:
- minimize (optimization routine)
- plotDiag_Th_Ts (plot program for Th and Ts diagrams)
The tutorials are available on moodle

---

# Lecture 4: Components #1 – Heat Exchanger

**Source: Lecture4_Slides.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #4

Components #1: Heat exchanger

Lana Liebl Leon Brendel, PhD 11 March 2026

===== Page 2 =====

Heat sources and sinks Overview residential heating

===== Page 3 =====

Heat sources - costs vs. efficiency Residential heating

===== Page 4 =====

Calculation of approach temperatures
First, calculate all required process states
[Image: T-s diagram with states and approach temperatures]
Evaporator: ΔT_app,P1 = T_so_out - T4, ΔT_app,P2 = T_so_in - T1
Condenser: ΔT_app,P3 = T2 - T_si_out, ΔT_app,P4 = T_dew - T_si_dew = T_co - T_si_dew
h_si_dew = h_si_out - (h_si_out - h_si_in)/(h2 - h3) (h2 - h_dew)
T_si_dew = f(h_si_dew, p_dew)
ΔT_app,P5 = T3 - T_si_in

===== Page 5 =====

Since the last lecture, you are able to...
...classify common heat pump heat sources and sinks by
- Temperatures
- Availability
- Costs for tapping
- Prevalence
[Image: Small photo of a heat pump]
...use pinch models to connect process states with the heat sink and source
...understand the principles of constraint optimization

===== Page 6 =====

Today: Heat exchangers

===== Page 7 =====

After this lecture, you will be able to...
...remember the fundamentals of heat transfer
...point out important design aspects of heat exchangers
...select appropriate heat exchanger types for heat pumps
...calculate and pre-design heat exchangers
...explain the freezing problem of air-source heat pumps

===== Page 8 =====

Refresher on heat transfer Heat transfer at a heat exchanger wall

===== Page 9 =====

Refresher on heat transfer Heat transfer at a heat exchanger wall
[No additional text]

===== Page 10 =====

Refresher on heat transfer Heat transfer at a heat exchanger wall
[Image: Diagram of pipe heat transfer with inner and outer radii]
Heat flow rate per infinitesimal length: dQ̇/dx = 1/(R·L0)·(T_H - T_L)
Thermal resistances: R·L0 = 1/(h_i·2πr_i) + ln(r_o/r_i)/(λ·2π) + 1/(h_o·2πr_o)
The largest resistance dominates or The weakest wins

===== Page 11 =====

Refresher on heat transfer Heat flow rate across the entire heat exchanger
[Image: Diagram of pipe with temperature profiles]
Q̇ = ∫_0^L 1/(R(x)·L0)·(T_H(x) - T_L(x)) dx
R(x)·L0 = 1/(h_i(x)·2πr_i) + ln(r_o/r_i)/(λ(x)·2π) + 1/(h_o(x)·2πr_o)
We also know the energy balances: dḢ_L/dx = dQ̇/dx (id.gas/liquid), dḢ_H/dx = dQ̇/dx (id.gas/liquid)

===== Page 12 =====

Refresher on heat transfer Heat transfer coefficients, calculation
Nusselt number: Nu_L = (h·L)/λ_fluid
Dimensionless number, based on similarity theory
Nusselt number is correlated as a function of geometry, flow conditions and thermodynamic state
Nu = f(Re, Pr) for a certain geometry

===== Page 13 =====

Refresher on heat transfer Heat transfer coefficients, typical values
Internal flow, single phase [table?]
Internal flow, condensation [table?]

===== Page 14 =====

Refresher on heat transfer Heat transfer coefficients, typical values
[No additional text]

===== Page 15 =====

Measured temperature profiles from a lab-scale heat pump Evaporator, counterflow
[Image: Graph of temperature vs share of energy/area for evaporation and superheating]
Evaporation: 92% energy, 36% area
Superheating: 8% energy, 64% area

===== Page 16 =====

Heat exchanger Flow arrangement

===== Page 17 =====

Heat exchanger Flow arrangement

===== Page 18 =====

Integration along x
Assumptions: h, λ, geometry ≠ f(x); T(h) or T(x) must be differentiable function
Q̇ = 1/R·ΔT_LM
ΔT_LM = (ΔT'' - ΔT')/ln(ΔT''/ΔT'), ΔT'' at x=0
Not only valid for pipe heat exchangers (as long as the heat transfer area does not depend on the location)

===== Page 19 =====

LMTD-method ΔT_LM as function of the flow arrangement
[Image: Diagrams of parallel flow, counterflow, crossflow with LMTD correction factors]
If both streams are isothermal along x, e.g., due to a phase change: ΔT_LM = T1 - T2

===== Page 20 =====

1
Integration along x
Assumptions: h, λ, geometry ≠ f(x); T(h) or T(x) must be differentiable function
- h is significantly different for a phase change and a single phase
- Transition from phase change to single phase results in a kink - not differentiable
[Image: Graph showing kink in temperature profile]
We need to divide the heat exchanger for calculation

===== Page 21 =====

Moving boundary method
[Image: T-s diagram with sections A, B, C]
si: heat sink, so: heat source

===== Page 22 =====

Moving boundary method
Example: refrigerant enters superheated, is condensed and leaves subcooled; heat sink is sensible medium, e.g., water
[Image: Temperature vs heat flow diagram showing three sections A, B, C]
Heat exchanger is divided into parts with constant flow regimes of each stream

===== Page 23 =====

Moving boundary method
03/11/2026
L.Liebl, L. Brendel - Sustainable Heating and Cooling Technologies #4
23
3, 2, si_out, si_in, si_AB, si_BC, AB, BC
Temperature and heat flow diagrams with sections A, B, C
Q̇_A = 1/R_A·ΔT_LM,A, Q̇_B = 1/R_B·ΔT_LM,B, Q̇_C = 1/R_C·ΔT_LM,C
ΔT_A' = T3 - T_si_in, ΔT_A'' = T_AB - T_si_AB, ΔT_B'' = T_BC - T_si_BC, ΔT_B' = T_AB - T_si_AB, ΔT_C'' = T2 - T_si_out, ΔT_C' = T_BC - T_si_BC
Q̇_A = ṁ(h_AB - h3), Q̇_B = ṁ(h_BC - h_AB), Q̇_C = ṁ(h2 - h_BC)
Q̇_A = ṁ_si (h_si_AB - h_si_in), Q̇_B = ṁ_si (h_si_BC - h_si_AB), Q̇_C = ṁ_si (h_si_out - h_si_BC)
Q̇ = Q̇_A + Q̇_B + Q̇_C
Q̇ = ṁ(h2 - h3) = ṁ_si (h_si_out - h_si_in)

===== Page 24 =====

Moving boundary method
03/11/2026
L.Liebl, L. Brendel - Sustainable Heating and Cooling Technologies #4
24
R_i must be calculated for each section due to the differences in heat transfer coefficients
R_A = 1/(h_liq·2πr_i·L_A) + ln(r_o/r_i)/(λ·2π·L_A) + 1/(h_si·2πr_o·L_A)
R_B = 1/(h_tp·2πr_i·L_B) + ln(r_o/r_i)/(λ·2π·L_B) + 1/(h_si·2πr_o·L_B)
R_C = 1/(h_vap·2πr_i·L_C) + ln(r_o/r_i)/(λ·2π·L_C) + 1/(h_si·2πr_o·L_C)
Example: double-pipe

===== Page 25 =====

How do we account for heat exchanger design in heat pump design?

===== Page 26 =====

How do we account for heat exchanger design in heat pump design?

===== Page 27 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 28 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 29 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 30 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 31 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 32 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 33 =====

Objectives of heat exchanger design For a given heat transfer task

===== Page 34 =====

Typically heat exchangers for residential heat pumps Which media?
Fortunately, somebody has already solved the problem for you of which heat exchanger type is best

===== Page 35 =====

Typically heat exchangers for residential heat pumps Which media?
Fortunately, somebody has already solved the problem for you of which heat exchanger type is best
We have to distinguish by the media involved
| Heat pump type | Evaporator | Condenser |
|----------------|------------|-----------|
| Air / air | | |
| Air / water | | |
| Water / water | | |
| Brine / water | | |
| Brine / air | | |

===== Page 36 =====

Typically heat exchangers for residential heat pumps Which media?
Fortunately, somebody has already solved the problem for you of which heat exchanger type is best
We have to distinguish by the media involved
| Heat pump type | Evaporator | Condenser |
|----------------|---------------------|---------------------|
| Air / air | Gas / phase change | Phase change / gas |
| Air / water | Gas / phase change | Phase change / liquid |
| Water / water | Liquid / phase change | Phase change / liquid |
| Brine / water | Liquid / phase change | Phase change / liquid |
| Brine / air | Liquid / phase change | Phase change / gas |

===== Page 37 =====

Typically heat exchangers for residential heat pumps Which media?
Fortunately, somebody has already solved the problem for you of which heat exchanger type is best
We have to distinguish by the media involved
| Heat pump type | Evaporator | Condenser |
|----------------|---------------------|---------------------|
| Air / air | Gas / phase change | Phase change / gas |
| Air / water | Gas / phase change | Phase change / liquid |
| Water / water | Liquid / phase change | Phase change / liquid |
| Brine / water | Liquid / phase change | Phase change / liquid |
| Brine / air | Liquid / phase change | Phase change / gas |
Remember the weakest wins! ⇒ Gas/phase change = Phase change/gas; Liquid/phase change = Phase change/liquid

===== Page 38 =====

Typical heat exchangers for residential heat pumps Which media?
We have to consider only two types of heat transfer: liquid ←→ phase change, gas ←→ phase change
| Heat pump type | Evaporator | Condenser |
|----------------|---------------------|---------------------|
| Air / air | Gas / phase change | Phase change / gas |
| Air / water | Gas / phase change | Phase change / liquid |
| Water / water | Liquid / phase change | Phase change / liquid |
| Brine / water | Liquid / phase change | Phase change / liquid |
| Brine / air | Liquid / phase change | Phase change / gas |
Remember the weakest wins! → Gas/phase change = Phase change/gas; Liquid/phase change = Phase change/liquid

===== Page 39 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
- High heat transfer coefficients on both sides

===== Page 40 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
High heat transfer coefficients on both sides. Moderate volume flow rates.
[Image: Table of mass flow rate and max volume flow rate for Propane and Water]
| | Mass flow rate (kg/s) | Max. volume flow rate (m³/s) |
|----------|----------------------|------------------------------|
| Propane | 0.0158 | 0.00160 |
| Water | 0.2383 | 0.00024 |

===== Page 41 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
High heat transfer coefficients on both sides. Moderate volume flow rates. Both media only cause moderate pressure losses.
[Image: Same table]

===== Page 42 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
High heat transfer coefficients on both sides. Moderate volume flow rates. Both media only cause moderate pressure losses.
[Image: Small photo of a plate heat exchanger]
Small heat exchange areas and small cross-sectional flow areas required.
[Image: Same table]

===== Page 43 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
[Image: Photo of a plate heat exchanger]

===== Page 44 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
Double tube heat exchanger e.g., if the media contain particles
[Image: Photo of a double tube heat exchanger]

===== Page 45 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
- Different heat transfer coefficients
- Gas ≪ phase change

===== Page 46 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Different heat transfer coefficients Gas << phase change. Volume flow rate Gas >> phase change. Pressure losses Gas > phase change.
[Image: Table of mass flow rate and max volume flow rate for Propane and Air]
| | Mass flow rate (kg/s) | Max. volume flow rate (m³/s) |
|----------|----------------------|------------------------------|
| Propane | 0.0158 | 0.0016 |
| Air | 0.9900 | 1.2400 |

===== Page 47 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Different heat transfer coefficients Gas ≪ phase change. Volume flow rate Gas ≫ phase change. Pressure losses Gas ≫ phase change.
[Image: Small diagram of a fin heat exchanger]
Much larger heat transfer area and cross-sectional flow area required on gas side.
[Image: Same table]

===== Page 48 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Fin heat exchanger
[Image: Diagram of a fin heat exchanger]
Cross flow, Small tubes (refrigerant), Small cross-sectional flow area, Small heat transfer area, Fins, Large cross-sectional flow area, Large heat transfer area

===== Page 49 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Fin heat exchanger: often multiple rows

===== Page 50 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Fin heat exchanger: often multiple rows [diagram]

===== Page 51 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface

===== Page 52 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface

===== Page 53 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface
[Image: Photo of ice on evaporator fins]
Additional heat resistance

===== Page 54 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface
[Image: Photo of ice on evaporator]
Additional heat resistance
[Image: Small diagram showing decreased flow area]
Decreased flow area

===== Page 55 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface
[Image: Photo of ice on evaporator]
Additional heat resistance
[Image: Small diagrams of flow area reduction]
Decreased flow area worsened flow and heat transfer, decreased heating capacity and COP

===== Page 56 =====

Freezing problem of air source heat pumps
Periodic defrosting by heating the evaporator
- Requires additional energy
- ≈5% of yearly electricity demand
- Heat pump does not supply heat during this period
Two common defrosting strategies [diagrams]

===== Page 57 =====

Introduction to the exercise

===== Page 58 =====

In this exercise, you will focus on the evaporator. Compared to the exercises before, we model an air/water instead of a water/water heat pump. The heat is now exchanged between air and the refrigerant in the evaporator. In typical air/water heat pumps, cross-flow heat exchangers are used. Here, the air is mixed by a ventilator and flows perpendicular to the refrigerant. For simplicity, we consider a straight tube where the refrigerant evaporates and is superheated.

===== Page 59 =====

The following parameters are given for the heat pump processes and the evaporator:
- Evaporation temperature T_ev = -5°C
- Condensation temperature T_co = 40°C, full condensation, no subcooling
- Superheating ΔT_sh = 10 K
- Source: air, T_so_in = 10°C
- Refrigerant: R1234yf, m_ref = 0.031 kg·s⁻¹
- Refrigerant heat transfer coefficients:
  - Two phase: h_ref,VL = 2000 W/m²K,
  - Vapor: h_ref,V = 200 W/m²K
- Air heat transfer coefficient h_air = 300 W/m²K,
- Thermal conductivity: λ_steel = 25 W/mK, λ_ice = 2.31 W/mK
- Tube: inner tube diameter d_i = 12 mm, wall thickness d_w = 1.5 mm
- Neglect any temperature decrease in the air while flowing around the tube

===== Page 60 =====

Task a)
a) Calculate both thermal resistances times 1 meter of tube R_L,evap and R_L,sh.
[Image: Diagram of tube cross-section]
R_L = 1/(h_i·2πr_i) + ln(r_o/r_i)/(λ·2π) + 1/(h_o·2πr_o)
L = 1m

===== Page 61 =====

Task b)
b) Determine the needed length of the tube L_t.
- Calculate the refrigerant's states
- Calculate the heat flow rate of the entire evaporator using the refrigerant states
- Split the heat exchanger into a pure evaporator and a superheater
- Calculate the heat flow rates of evaporation and superheating
- Calculate the logarithmic mean temperatures differences
- Calculate the required lengths
L_evap = (Q̇_evap·R_L,evap)/ΔT_LM,evap, L_sh = (Q̇_sh·R_L,sh)/ΔT_LM,sh

===== Page 62 =====

Task c)
c) Consider heat transfer degradation due to a cylindrical ice layer on the tube. The ice layer only acts as extra thermal resistance (heat conduction). Analyze how the thickness of the ice layer affects the heat uptake in the evaporator. The heat pump's control ensures that the process temperatures remain constant by decreasing the refrigerant mass flow rate.
[Image: Diagram of tube with ice layer]
R = 1/(h_i·2πr_i·L) + ln(r_o/r_i)/(λ·2π·L) + ln((r_o + w_ice)/r_o)/(λ_ice·2π·L) + 1/(h_o·2π(r_o + w_ice)·L)
Use the tube length and states from task b)

---

# Lecture 5: Expansion Valves – Transcritical Process

**Source: SHCT26_Lec5_Slides.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #5

Expansion valves Transcritical process

Lana Liebl Dr. Leon Brendel 18 March 2026

===== Page 2 =====

Since last week, you are able to...
...remember the fundamentals of heat transfer
...point out important design aspects of heat exchangers
...select appropriate heat exchanger types for heat pumps
...calculate and pre-design heat exchangers
...explain the freezing problem of air-source heat pumps

===== Page 3 =====

Moving boundary method
03/18/2026
L. Liebl, L. Brendel - Sustainable Heating and Cooling Technologies #5
3
3, 2, si_out, si_in, si_AB, si_BC, AB, BC
Temperature and heat flow diagrams with sections A, B, C
Q̇_A = 1/R_A·ΔT_LM,A, Q̇_B = 1/R_B·ΔT_LM,B, Q̇_C = 1/R_C·ΔT_LM,C
ΔT_A' = T3 - T_si_in, ΔT_A'' = T_AB - T_si_AB, ΔT_B'' = T_BC - T_si_BC, ΔT_B' = T_AB - T_si_AB, ΔT_C'' = T2 - T_si_out, ΔT_C' = T_BC - T_si_BC
Q̇_A = ṁ(h_AB - h3), Q̇_B = ṁ(h_BC - h_AB), Q̇_C = ṁ(h2 - h_BC)
Q̇_A = ṁ_si (h_si_AB - h_si_in), Q̇_B = ṁ_si (h_si_BC - h_si_AB), Q̇_C = ṁ_si (h_si_out - h_si_BC)
Q̇ = Q̇_A + Q̇_B + Q̇_C
Q̇ = ṁ(h2 - h3) = ṁ_si (h_si_out - h_si_in)
Lecture #4

===== Page 4 =====

Moving boundary method
03/18/2026
L. Liebl, L. Brendel - Sustainable Heating and Cooling Technologies #5
4
R_i must be calculated due to the flow regimes and the heat exchanger geometry
R_A = 1/(h_liq·2πr_i·L_A) + ln(r_o/r_i)/(λ·2π·L_A) + 1/(h_si·2πr_o·L_A)
R_B = 1/(h_tp·2πr_i·L_B) + ln(r_o/r_i)/(λ·2π·L_B) + 1/(h_si·2πr_o·L_B)
R_C = 1/(h_vap·2πr_i·L_C) + ln(r_o/r_i)/(λ·2π·L_C) + 1/(h_si·2πr_o·L_C)
Example: double-pipe
Lecture #4

===== Page 5 =====

Refresher on heat transfer Heat transfer coefficients, typical values
Internal flow, single phase [table]
Internal flow, condensation [table]

===== Page 6 =====

Typical heat exchangers for residential heat pumps Which media?
We have to consider only two types of heat transfer: liquid ←→ phase change, gas ←→ phase change
| Heat pump type | Evaporator | Condenser |
|----------------|---------------------|---------------------|
| Air / air | Gas / phase change | Phase change / gas |
| Air / water | Gas / phase change | Phase change / liquid |
| Water / water | Liquid / phase change | Phase change / liquid |
| Brine / water | Liquid / phase change | Phase change / liquid |
| Brine / air | Liquid / phase change | Phase change / gas |
Remember the weakest wins! → Gas/phase change = Phase change/gas; Liquid/phase change = Phase change/liquid

===== Page 7 =====

Typical heat exchangers for residential heat pumps Liquid ←→ phase change
Plate heat exchanger
[Image: Photo of a plate heat exchanger]

===== Page 8 =====

Typical heat exchangers for residential heat pumps Gas ←→ phase change
Fin heat exchanger
[Image: Diagram of fin heat exchanger]
- Cross flow
- Small tubes (refrigerant)
- Small cross-sectional flow area
- Small heat transfer area
- Fins
- Large cross-sectional flow area
- Large heat transfer area

===== Page 9 =====

Freezing problem
Humid air is cooled down ⇒ water condenses ⇒ ice formation on the evaporator surface
[Image: Photo of ice on evaporator]
[Image: Small diagram of ice formation]
Additional heat resistance
[Image: Small diagram]
Decreased flow area
[Image: Small diagram]
worsened flow and heat transfer, decreased heating capacity and COP

===== Page 10 =====

Results from last exercise Part a)
| | Q_i (kW) | R_Li (m·K/W) | L_i (m) |
|------------|----------|--------------|---------|
| Evaporation | 3.26 (92%) | 0.085 | 18.56 (75%) |
| Superheating | 0.28 (8%) | 0.205 | 6.34 (25%) |

===== Page 11 =====

Results from last exercise Ice formation
Thermal resistances are increased ⇒ heat transfer is worsened
We assumed: temperatures in the evaporator are kept, refrigerant mass flow rate is decreased
[Image: Graph of heat flow vs ice thickness]
Transferred heat in the evaporator decreased. Rejected heat in the condenser also decreases ⇒ heat pump delivers less heat

===== Page 12 =====

Results from last exercise Ice formation
Example: 40 mm ice layer
| | Q_i (kW) | R_L,i (m·K/W) | L_i (m) | Q_i/L_i (kW/m) |
|------------|----------|---------------|---------|----------------|
| Evaporation | 1.94 (92%) | 0.153 | 19.86 (80%) | 0.098 |
| Superheating | 0.17 (8%) | 0.272 | 5.04 (20%) | 0.034 |
Without ice
| | Q_i (kW) | R_L,i (m·K/W) | L_i (m) | Q_i/L_i (kW/m) |
|------------|----------|---------------|---------|----------------|
| Evaporation | 3.26 (92%) | 0.085 | 18.56 (75%) | 0.176 |
| Superheating | 0.28 (8%) | 0.205 | 6.34 (25%) | 0.044 |
Thermal resistance of evaporation increases more → Position where superheating begins changes
[Image: Graph showing moving boundary]
That is why the method is called moving boundary!

===== Page 13 =====

After this lecture, you will be able to...
explain the function of the expansion valve in a heat pump process
derive why an isenthalpic state change is reasonable assumption
explain why the expansion is usually not carried out by an expander
describe the different types of expansion valves
explain and optimize a transcritical heat pump cycle

===== Page 14 =====

Expansion valves (throttle) Function in a heat pump process
[Image: Flow sheet with throttle]
- Re-expansion of the condensed/subcooled refrigerant
- Pressure decreases
- Refrigerant partly evaporates
- Evaporation pressure is controlled by the pressure decrease over the throttle
- It ensures that the heat transfer in the evaporator works and enough heat for evaporation can be transferred

===== Page 15 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?

===== Page 16 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
Q + P = m(h4 + 1/2 c4^2 + gH4) - m(h3 + 1/2 c3^2 + gH3)

===== Page 17 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
[Same equation]

===== Page 18 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
Q + P = m(h4 + 1/2 c4^2 + gH4) - m(h3 + 1/2 c3^2 + gH3)
Q/m + (h3 + 1/2 c3^2) = (h4 + 1/2 c4^2)

===== Page 19 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
[Same equation]
Propane heat pump, Q̇_H = 6 kW
Enthalpy flow: ṁ·h3 = 4400 W

===== Page 20 =====

Expansion valves (throttle) Thermodynamics
[Same equation]
Propane heat pump, Q̇_H = 6 kW
Enthalpy flow: ṁ·h3 = 4400 W
Heat transfer to environment: Q̇ = U·A(T̄_valve - T_amb)

===== Page 21 =====

Expansion valves (throttle) Thermodynamics
[Same equation]
Propane heat pump, Q̇_H = 6 kW
Enthalpy flow: ṁ·h3 = 4400 W
Heat transfer to environment: Q̇ = U·A(T̄_valve - T_amb)
U = 5 W·m⁻²·K⁻¹, A = 2·10⁻³ m², T_co = 35°C, T_amb = 0°C

===== Page 22 =====

Expansion valves (throttle) Thermodynamics
[Image: Diagram of throttle]
Propane heat pump, Q̇_H = 6 kW
Enthalpy flow: ṁ·h3 = 4400 W
Heat transfer to environment: Q̇ = U·A(T̄_valve - T_amb)
U = 5 W·m⁻²·K⁻¹, A = 2·10⁻³ m², T_co = 35°C, T_amb = 0°C
Q̇ = 0.35 W

===== Page 23 =====

Expansion valves (throttle) Thermodynamics
[Same equation]
Propane heat pump, Q̇_H = 6 kW
h4 = h3 - (1/2 c4^2 - 1/2 c3^2)

===== Page 24 =====

Expansion valves (throttle) Thermodynamics
[Same equation]
Propane heat pump, Q̇_H = 6 kW
Flow velocity: c_i = (ṁ·v_i)/A_cross

===== Page 25 =====

Expansion valves (throttle) Thermodynamics
Q̇ + Ṗ = ṁ(h4 + 1/2 c4^2 + gH4) - ṁ(h3 + 1/2 c3^2 + gH3)
Q̇/ṁ + (h3 + 1/2 c3^2) = (h4 + 1/2 c4^2)
h4 = h3 - (1/2 c4^2 - 1/2 c3^2)
Propane heat pump, Q̇_H = 6 kW
Flow velocity: c_i = (ṁ·v_i)/A_cross
[Image: Diagram showing similar cross sections at inlet and outlet]
Similar cross sections at in- and outlet

===== Page 26 =====

Expansion valves (throttle) Thermodynamics
[Image: Diagram of throttle]
Propane heat pump, Q̇_H = 6 kW
Flow velocity: c_i = (ṁ·v_i)/A_cross
[Image: Diagram]
Similar cross sections at in- and outlet
1/2 ṁ (c4^2 - c3^2) = 0.15 W
ṁ·h3 = 4400 W

===== Page 27 =====

Why not use an expander?
[Image: Small diagram of expander]
Propane heat pump, Q̇_H = 6 kW
P_compressor ≈ 1.05 kW

===== Page 28 =====

3
[Image: Same diagram]
Let's assume we could overcome the engineering issues of wet compression
Propane heat pump, Q̇_H = 6 kW
P_compressor ≈ 1.05 kW

===== Page 29 =====

3
[Image: Same diagram]
Propane heat pump, Q̇_H = 6 kW
Ṗ_compressor ≈ 1.05 kW
Let's assume we could overcome the engineering issues of wet compression
Best expander ⇒ isentropic state change: S4 = S3
P_expander,max = ṁ (h3 - h4(p_ev, s3))
P_expander,max = 0.09 kW
⇒ Less than 10% of compressor work could be recuperated ⇒ Expander efficiency further decreases the share

===== Page 30 =====

3
[Image: Same diagram]
Propane heat pump, Q̇_H = 6 kW
P_compressor ≈ 1.05 kW
Best expander ⇒ isentropic state change: S4 = S3
P_expander,max = ṁ (h3 - h4(p_co, s3)) [note: p_co? probably p_ev]
P_expander,max = 0.09 kW
⇒ Less than 10% of compressor work could be recuperated ⇒ Expander efficiency further decreases the share
Why? P_flow,rev = ṁ ∫ v·dp
dp_expander = dp_compressor, v̄_expander ≪ v̄_compressor

===== Page 31 =====

3
[Image: Same diagram]
Let's assume we could overcome the engineering issues of wet compression
Compression work recuperation is more interesting for processes / refrigerants with higher pressure ratios. However, alternatives to an expander have been found for such processes.
Follow-up in lecture #6
Propane heat pump, Q̇_H = 6 kW
Less than 10% of compressor work could be recuperated ⇒ Expander efficiency further decreases the share
P_compressor ≈ 1.05 kW
Why? P_flow,rev = ṁ ∫ v·dp, dp_expander = dp_compressor, v̄_expander ≪ v̄_compressor

===== Page 32 =====

Types of expansion valves Capillary tubes
- Refrigerant flows through a thin tube
- Pressure drop caused by friction
- Often used in domestic refrigerators

===== Page 33 =====

Types of expansion valves Capillary tubes
[Image: Diagram of capillary tube]
- Refrigerant flows through a thin tube
- Pressure drop caused by friction
- Often used in domestic refrigerators
- Very cheap
- No failing except fracture due to vibrations

===== Page 34 =====

Types of expansion valves Capillary tubes
[Image: Diagram of capillary tube]
- Refrigerant flows through a thin tube
- Pressure drop caused by friction
- Often used in domestic refrigerators
- Very cheap
- No failing except fracture due to vibrations
- No controlling possible
Δp = f(length, inlet state, mass flow rate)
- Constant heat source → p_ev / T_ev nearly constant
- Process often works at non-optimal operation point (too low T_ev)
- Limits operating limits (heat source) of the heat pump

===== Page 35 =====

Types of expansion valves Thermostatic expansion valve
[Image: Diagram of thermostatic expansion valve]
Refrigerant flows through a valve. Flow losses cause pressure drop. Most used type in heat pumps.
Controlling possible (fixed characteristic)
Ensures a fixed superheating at evaporator outlet. No energy or electronics required.

===== Page 36 =====

Types of expansion valves Thermostatic expansion valve
[No additional text]

===== Page 37 =====

3 Condenser
[Diagram?]

===== Page 38 =====

Types of expansion valves Thermostatic expansion valve
[No additional text]

===== Page 39 =====

Example

===== Page 40 =====

Example

===== Page 41 =====

Types of expansion valves Thermostatic expansion valve
[Image: Diagram of thermostatic expansion valve]
[Image: Another diagram]
Refrigerant flows through a valve. Flow losses cause pressure drop. Most used type in cooling cycles not in heat pumps.
Controlling possible (fixed characteristic)
Ensures a fixed superheating at evaporator outlet. No energy or electronics required.
Fixed controlling characteristic. Only based on the superheating. No special controlling possible, e.g., cold start. System is sluggish ⇒ small superheating cannot be controlled. Mechanical parts (spring, diaphragm..) can fail.

===== Page 42 =====

Types of expansion valves Electronic expansion valve
- Refrigerant flows through a valve
- Flow losses cause pressure drop
- Valve orifice can be electrically controlled
- Most used type in modern heat pumps

===== Page 43 =====

1. Refrigerant flows through a valve
- Flow losses cause pressure drop
- Valve orifice can be electrically controlled
- Most used type in modern heat pumps
[Image: Diagram of electronic expansion valve]
Controlling based on any variable or combination of variables
- No fixed characteristic → individual controlling possible
- Rapid response

===== Page 44 =====

Types of expansion valves Electronic expansion valve
- Refrigerant flows through a valve
- Flow losses cause pressure drop
- Valve orifice can be electrically controlled
- Most used type in modern heat pumps
[Image: Diagram of electronic expansion valve]
[Image: Small diagram of controller]
- Controlling based on any variable or combination of variables
- No fixed characteristic → individual controlling possible
- Rapid response
[Image: Small icon]
- More expensive
- Controller required
- Must be integrated in heat pump controller
- Must be pre-configured specific to the heat pump / refrigerator
- Potential of failure

===== Page 45 =====

Transcritical process

===== Page 46 =====

Transcritical heat pump process
[Image: T-s diagram of transcritical cycle]
Transcritical process:
- Refrigerant is compressed to pressures larger than the critical pressure
- Heat rejection occurs along a supercritical isobar

===== Page 47 =====

What is a supercritical fluid Example: CO2
[Image: Phase diagram of CO2]
Supercritical fluids:
- Substance with both gas- and liquid-like properties
- No phase change
- Density, viscosity and thermal conductivity are close to that of liquids

===== Page 48 =====

Transcritical heat pump process
[Image: T-s diagram of transcritical cycle]

===== Page 49 =====

Why / when transcritical processes

===== Page 50 =====

Why / when transcritical processes
[Image: T-s diagram]

===== Page 51 =====

There is refrigerant with many desirable properties but low critical temperature
[Image: Small diagram of CO2 properties]
- Not flammable
- GWP = 1
- ODP = 0
- Low normal boiling point
- Not toxic
- Cheap
- Available everywhere
CO2 has major disadvantages, in particular, for heat pumps → Figure it out in the exercise

===== Page 52 =====

General disadvantages of transcritical processes
[Image: T-s diagram]
Higher mechanical and thermal stress on the compressor and heat exchanger (deheater). Larger compressor work. Less efficient for heat sinks with small temperature change. Larger investment costs.

===== Page 53 =====

Introduction into this week’s exercise

===== Page 54 =====

In this exercise, you will optimize a transcritical heat pump process concerning heat sources and sinks for two applications. The selected refrigerant is CO2.
The following parameters are given for the heat pump process:
Superheating ΔT_sh = 10 K, Compressor efficiency: η_comp = 0.7, p_out,max = 150 bar
Minimum approach temperature ΔT_app = 5 K
Application 1: Heating
Source: air, T_so_in = -10°C, ΔT_so = 5 K, cross-flow
Sink: water, T_si_in = 30°C, ΔT_si = 5 K, counter-flow
Application 2: Hot water
Source: air, T_so_in = -10°C, ΔT_so = 5 K, cross-flow
Sink: water, T_si_in = 10°C, ΔT_si = 55 K, counter-flow
a) Optimize the heat pump process regarding the COP for both applications. The optimal pressure p3 and the temperatures T_ev and T3 shall be determined while meeting the constraint of a minimum approach temperature of 5 K in the heat exchangers. Evaluate the pressure ratio, the specific work, and the outlet temperature of the compressor. Display the processes in a T-h-diagram.
b) Compare the results of the two applications. Explain why the transcritical CO2 process performs better in one application than in the other.
c) Compare your results to the COP of a subcritical heat pump with Propane (COP_heating=2.7, COP_hot_water=2.2)

===== Page 55 =====

Subcritical cycle
Cycle defined by:
- Evaporation temperature
- Condensation temperature
- Superheating
- Subcooling
Optimized variables mostly are:
- Evaporation temperature
- Condensation temperature

===== Page 56 =====

Subcritical cycle
[Image: T-s diagram of subcritical cycle]
Cycle defined by: Evaporation temperature, Condensation temperature, Superheating, Subcooling
Optimized variables: Evaporation temperature, Condensation temperature
Transcritical cycle
[Image: T-s diagram of transcritical cycle]
Cycle defined by: Evaporation temperature, Condensation temperature, High pressure (p2, p3), Temperature at state 3, Superheating, Subcooling
Optimized variables: Evaporation temperature, High pressure (p2, p3), Temperature at state 3

===== Page 57 =====

Optimizing a transcritical cycle Constraints
[Image: T-s diagram]
High pressure must be larger than critical pressure
Heat sinks with small temperature change
- Only 1 pinch point at the outlet
Heat sinks with large temperature change
Pinch point can be between state 2 and 3
Constrains the approach temperatures along the entire heat transfer (e.g., at 10-20 points)
Other common constraints (e.g., evaporator pinch points) are still required

===== Page 58 =====

Optimizing a transcritical cycle Pinch-constraint
Heat sinks with large temperature change. Pinch point can be between state 2 and 3. Constrain the approach temperatures along the entire heat transfer (e.g., at 10-20 points).
[Image: T-s diagram]
1) Define n points between h2 and h3. For each h_i:
2) Calculate the refrigerant's temperature for all h_i: T_i = f(p2, h_i)
3) Calculate the corresponding heat sink's temperatures: T_si,i = f(h2, h3, T_si,in, T_si,out) → energy balances
4) Calculate the approach temperatures: ΔT_app = T_i - T_si,i
5) Constrain all ΔT_app > ΔT_app,min

---

# Lecture 6: Compressors – Advanced Flowsheets

**Source: SHCT26_Lec6.pdf and SHCT26_Lec6_annotated.pdf (combined, with annotations noted)**

## SHCT26_Lec6.pdf

===== Page 1 =====

Sustainable Heating and Cooling Technologies #6

Compressors Advanced flowsheets

Lana Liebl Leon Brendel, PhD 25 March 2026

===== Page 2 =====

Since last week, you are able to...
explain the function of the expansion valve in a heat pump process
derive why an isenthalpic state change is reasonable assumption
explain why the expansion is usually not carried out by an expander
describe the different types of expansion valves
explain and optimize a transcritical heat pump cycle

===== Page 3 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
[Image: Diagram]
Propane heat pump, Q̇_H = 6 kW
Enthalpy flow: ṁ·h3 = 4400 W
Heat transfer to environment: Q̇ = U·A(T̄_valve - T_amb)
U = 5 W·m⁻²·K⁻¹, A = 2·10⁻³ m², T_co = 35°C, T_amb = 0°C
Q̇ = 0.35 W

===== Page 4 =====

Expansion valves (throttle) Thermodynamics
Usually, we assume an isenthalpic state change → justified?
[Image: Diagram]
Propane heat pump, Q̇_H = 6 kW
Flow velocity: c_i = (ṁ·v_i)/A_cross
[Image: Diagram]
Similar cross sections at in- and outlet
1/2 ṁ (c4^2 - c3^2) = 0.15 W
ṁ·h3 = 4400 W

===== Page 5 =====

Types of expansion valves
[Image: Diagrams of capillary tube, thermostatic expansion valve, electronic expansion valve]

===== Page 6 =====

Why / when transcritical processes
Transcritical cycles enable larger temperature lifts ⇒ interesting for high-temperature heat pumps
[Image: T-s diagram]

===== Page 7 =====

Last week's exercise
Heating [diagram]
Domestic hot water [diagram]

===== Page 8 =====

After this lecture, you will be able to...
...explain the thermodynamics of compressors
...use the different compressor efficiencies and evaluate their accuracy and limitations
...describe the different compressor types and their application area
...explain and model advanced heat pump flowsheets

===== Page 9 =====

The "best" compressor → lowest compression work

===== Page 10 =====

The "best" compressor → lowest compression work
[No additional text]

===== Page 11 =====

The "best" compressor - lowest compression work
[No additional text]

===== Page 12 =====

The "best" compressor → lowest compression work
[No additional text]

===== Page 13 =====

The "best" compressor → lowest compression work
[No additional text]

===== Page 14 =====

Why isothermal beats isentropic
Reversible steady-flow work: w = ∫_{p_in}^{p_out} v dp = ∫_{p_in}^{p_out} R_i·T dp (Ideal gas)

===== Page 15 =====

Why isothermal beats isentropic
Reversible steady-flow work: w = ∫ v dp = ∫ R_i·T dp (Ideal gas)
Isotherm: T = const.

===== Page 16 =====

Why isothermal beats isentropic
Reversible steady-flow work: w = ∫ v dp = ∫ R_i·T dp (Ideal gas)
Isotherm: T = const.
Isentropic: T increases with p: T = T_in (p/p_in)^(R_i/c_p)

===== Page 17 =====

Why isothermal beats isentropic
[Image: p-v diagram showing isothermal vs isentropic compression]
Isotherm: T = const.
Isentropic: T increases with p: T = T_in (p/p_in)^(R_i/c_p)
Isothermal compression in a heat pump cycle?

===== Page 18 =====

Why isothermal beats isentropic
[Image: Same diagram]
Isotherm: T = const.
Isentropic: T increases with p
Isothermal compression in a heat pump cycle?
Process cannot supply heat to the heat sink ⇒ purpose failed

===== Page 19 =====

Why isothermal beats isentropic
[No additional text]

===== Page 20 =====

However...
[Image: T-s diagram]
A mixture of isentropic and isothermal compression would be beneficial

===== Page 21 =====

However...
[Image: Same diagram]
A mixture of isentropic and isothermal compression would be beneficial
However #2: Not a good reference process since it is substantially connected to heat pump process and its purpose. Usually, compressors do not allow for significant heat rejection due to small surfaces.

===== Page 22 =====

Compressor losses
Depending on compressor type:
- Friction of mechanical parts
- Electrical losses
- Flow losses / pressure losses
  - suction / discharge potentials
  - valves and tubes
  - reverse flow / re-expansion
- Over and - under compression
- Refrigerant leakage
- Heat transfer
- Driving auxiliary aggregates, e.g., oil pumps.

===== Page 23 =====

Compressor losses
Depending on compressor type:
- ... [same list]
Larger energy demand than isentropic compression

===== Page 24 =====

Compressor losses
Depending on compressor type:
- ... [same list]

===== Page 25 =====

Compressor losses
Depending on compressor type:
- ... [same list]

===== Page 26 =====

Compressor efficiencies Energetic efficiencies
η_energetic = P_reference_process / P_real_process

===== Page 27 =====

Compressor efficiencies Energetic efficiencies
[Image: p-h diagram showing isentropic compression]
η_energetic = P_reference_process / P_real_process
Reference process: isentropic compression, same inlet state as real process, same pressure ratio as real process, same mass flow rate as real process

===== Page 28 =====

Compressor efficiencies Energetic efficiencies
[Image: Same diagram]
Reference process: isentropic compression, same inlet state, same pressure ratio, same mass flow rate

===== Page 29 =====

Compressor efficiencies Energetic efficiencies
Isentropic efficiency: η_isentropic = (ṁ/ṁ)·(h_out^s - h_in)/(h_out - h_in) = P_isentropic / P_fluid
The isentropic efficiency only considers the compression chamber. ⇒ Direct connection to the state change of the fluid.

===== Page 30 =====

Compressor efficiencies Energetic efficiencies
Isentropic efficiency: η_isentropic = (h_out^s - h_in)/(h_out - h_in) = P_isentropic/P_fluid
The isentropic efficiency only considers the compression chamber. ⇒ Direct connection to the state change of the fluid.
Actually, we are interested in the electrical power demand. The electrical power demand is higher.
COP = Q̇_High / P_elec
P_elec = P_fluid + P_loss,chamber + P_loss,mech + P_loss,elec

===== Page 31 =====

Compressor efficiencies Energetic efficiencies
Global efficiency: η_global = P_isentropic / P_elec

===== Page 32 =====

Compressor efficiencies Energetic efficiencies
Global efficiency: η_global = P_isentropic / P_elec
However... P_elec ≠ ṁ·(h_out - h_in) due to heat losses to the environment
→ h_out ≠ h_in + (h_out^s - h_in)/η_global
We cannot calculate the outlet state

===== Page 33 =====

Compressor efficiencies Energetic efficiencies
Global efficiency: η_global = P_isentropic / P_elec
However... P_elec ≠ ṁ·(h_out - h_in) due to heat losses to the environment
→ h_out ≠ h_in + (h_out^s - h_in)/η_global
We cannot calculate the outlet state
Best case: We know, e.g., η_isentropic, η_mech, η_elec
P_elec = P_isentropic / (η_elec·η_mech·η_isentropic)
h_out = h_in + (h_out^s - h_in)/η_isentropic

===== Page 34 =====

Compressor efficiencies Energetic efficiencies ⇒ one more thing
[Image: Diagram of motor cooling with refrigerant]
[Image: p-h diagram]
For some compressor types, refrigerant is used to cool the motor
⇒ h_in we know is not h_in chamber ⇒ Wrong calculation of P_isentropic ⇒ Usually neglected
Efficiencies are just a concept that is often not exact

===== Page 35 =====

Compressor efficiencies Volumetric efficiency

===== Page 36 =====

Compressor efficiencies Volumetric efficiency
η_vol = V̇_real / V̇_theoretical = ṁ_real / ṁ_theoretical
Theoretical volume flow rate:
- Volume flow rate that would result for loss-free pumping at equal frequency
- Depends on compressor geometry

===== Page 37 =====

Compressor efficiencies Volumetric efficiency
η_vol = V̇_real / V̇_theoretical = ṁ_real / ṁ_theoretical
Theoretical volume flow rate:
- Volume flow rate that would result for loss-free pumping at equal frequency
- Depends on compressor geometry
Example: Reciprocating piston compressor
[Image: Diagram of piston compressor]
V̇_theoretical = V_cylinder · f_mech · n_cylinder

===== Page 38 =====

Compressor efficiencies Volumetric efficiency
η_vol = V̇_real / V̇_theoretical = ṁ_real / ṁ_theoretical
Theoretical volume flow rate:
- Volume flow rate that would result for loss-free pumping at equal frequency
- Depends on compressor geometry
Example: Reciprocating piston compressor
[Image: Diagram]
V̇_theoretical = V_cylinder · f_mech · n_cylinder
Beware! f_mech and f_elec can be different. It depends on the motor.

===== Page 39 =====

The two physical approaches of compression

===== Page 40 =====

The two physical approaches of compression
[Image: Diagrams of positive displacement and dynamic compressors]

===== Page 41 =====

The two physical approaches of compression
[No additional text]

===== Page 42 =====

The two physical approaches of compression
[Image: Diagram of centrifugal compressor]
[Image: Diagram of flow through impeller and diffusor]
Compression increasing the kinetic energy by adding energy and subsequently decreasing the velocity (isenthalpic)
First step: adding work by acceleration (impeller): m(h_out + 1/2 c_out^2) = m(h_in + 1/2 c_in^2) + P
Second step: retard the fluid (diffusor): 1/2 ρ_out c_out^2 + (κ-1)/κ ρ_out = 1/2 ρ_in c_in^2 + (κ-1)/κ ρ_in (Ideal gas)

===== Page 43 =====

Compressor sub-types

===== Page 44 =====

Compressor sub-types
[No additional text]

===== Page 45 =====

Compressor sub-types
[No additional text]

===== Page 46 =====

(adapted from CRC Handbook, 2017)

===== Page 47 =====

Comparison Principle of compression

===== Page 48 =====

Comparison Capacity range and efficiencies
Source: Hundy, 5th edition [graph]

===== Page 49 =====

Comparison Capacity range and efficiencies
Source: Hundy, 5th edition [graph]

===== Page 50 =====

Comparison Capacity range and efficiencies
Source: Hundy, 5th edition [graph]

===== Page 51 =====

Selection for residential heat pumps
Typical conditions:
- Heating capacity: 5 - 20 kW
- Compressor power: 1 - 7 kW
- Pressure ratio: 2.5 - 4.0

===== Page 52 =====

Selection for residential heat pumps
Reciprocating piston: High noise emissions / vibrations; Slow rotational speed → large volumes
Typical conditions: Heating capacity: 5-20 kW, Compressor power: 1-7 kW, Pressure ratio: 2.5-4.0

===== Page 53 =====

Selection for residential heat pumps
Reciprocating piston: High noise emissions / vibrations; Slow rotational speed → large volumes
Typical conditions: Heating capacity: 5-20 kW, Compressor power: 1-7 kW, Pressure ratio: 2.5-4.0
[Image: Diagram of screw compressor]
Screw: Not available for the required power range

===== Page 54 =====

Selection for residential heat pumps
Reciprocating piston: High noise emissions / vibrations; Slow rotational speed ⇒ large volumes
Typical conditions: Heating capacity: 5-20 kW, Compressor power: 1-7 kW, Pressure ratio: 2.5-4.0
[Image: Diagram of scroll compressor]
Scroll: slightly more efficient, cheaper

===== Page 55 =====

Selection for residential heat pumps
Reciprocating piston: High noise emissions / vibrations; Slow rotational speed ⇒ large volumes
Typical conditions: Heating capacity: 5-20 kW, Compressor power: 1-7 kW, Pressure ratio: 2.5-4.0
[Image: Diagram of scroll compressor]
Scroll: slightly more efficient, cheaper? [annotations: "slightly more efficient", "Cheaper"]

===== Page 56 =====

Another important classification: architecture
[Image: Three diagrams of open, semi-hermetic, hermetic compressors]
Open: Motor and compressor are separate units, Non-hazardous and/or harmful refrigerants, Outdoor installation, Industrial application
Semi-hermetic: Motor and compressor are in one closed housing, Housing can be opened for maintenance, Installation in separate room, Typical for residential heat pumps
Hermetic: Motor and compressor are in one fully closed housing, Housing cannot be opened, Highest safety level, Typical for refrigerators

===== Page 57 =====

Where do we get compressor efficiencies?
Manufacturers provide efficiencies of their products (e.g., Bitzer, GEA)
- Compressor maps on request
- Often, they provide a software tool for the design of the entire heat pump process (very simplified)
- Compressor efficiencies can be derived from the outputs
- Product specific and only available for a few refrigerants
Models to simulate compressors are available from scientific literature
- Calculate compressor efficiencies as a function of operation point
- Often, much information on the compressor design required
- No refrigerant extrapolation
- High numerical effort

===== Page 58 =====

AHRI: Air-Conditioning, Heating, and Refrigeration Institute
X = C1 + C2·T_s + C3·T_d + C4·T_s^2 + C5·(T_s·T_d) + C6·T_d^2 + C7·T_s^3 + C8·(T_s^2·T_d) + C9·(T_s·T_d^2) + C10·T_d^3
X: Power input, refrigerant mass flow rate
T_d: Discharge dew point temperature (condensation temperature)
T_s: Suction dew point temperature (evaporation temperature)
C1-C10: Regression coefficients. Must be fitted to experimental data

===== Page 59 =====

Refrigerant dependence on compressor efficiency

===== Page 60 =====

This week's exercise The envelope of positive displacement compressors
Every compressor has an operation range → called envelope. Usually, compressor manufacturers provide an envelope for each of their products. The operation range of compressor is mainly limited by: Minimum pressure → usually evaporation pressure p_ev, Maximum pressure → usually condensation pressure p_co, Maximum temperature → usually outlet temperature T_out, Power of the electric motor P.
p_ev, p_co, T_out, and P depend on the operation point of the compressor. The compressor operation point depends on: → Heat pump operation point: T_ev, T_co, superheating, refrigerant

===== Page 61 =====

This week's exercise The envelope of positive displacement compressors
Evaporation temperature T_ev [diagram]

===== Page 62 =====

This week's exercise The envelope of positive displacement compressors
The following parameters are given:
Maximum outlet temperature T_out,max = 100°C, Power of the electric motor P_el = 1.2 kW, Superheating ΔT_sh = 10 K
Compressor: GEA-Bock, HG-HC-12P, Theoretical volume flow at f_elec = 50 Hz V̇_theo = 5.4 m³·h⁻¹
Refrigerant: Propane
You will use a compressor model that calculates isentropic and volumetric efficiencies as function of the operation point and the refrigerant ⇒ Have a look at the tutorial on moodle
Task 1: Plot the isentropic and volumetric efficiencies as a function of the pressure ratio (p_out/p_in) for a constant evaporation temperature of T_ev = 0°C and 5 ≤ T_co ≤ 70°C.
Task 2: a) Display the compressor's envelope in a contour plot as a function of T_ev and T_co. b) Check which condition(s) is/are broken in each area outside the envelope. c) Display the isentropic and volumetric efficiencies as a function of T_ev and T_co in separate contour plots.

===== Page 63 =====

Advanced flowsheets

===== Page 64 =====

Internal heat exchanger (IHX) Principle

===== Page 65 =====

Internal heat exchanger (IHX) Principle
[No additional text]

===== Page 66 =====

Internal heat exchanger (IHX) Benefits
[Image: T-s diagram showing IHX effect]
Pinch point (evaporator) moves from outlet to inlet. Evaporation temperature can be increased. Quantitative benefit depends on application and refrigerant.

===== Page 67 =====

Internal heat exchanger (IHX) Benefits
[Image: Same diagram]
- Pinch point (evaporator) moves from outlet to inlet
- Evaporation temperature can be increased
- Compressor work and released heat decreases but COP increases

===== Page 68 =====

Vapor injection with flash tank Principle

===== Page 69 =====

Vapor injection with flash tank Principle
[Image: Flow sheet of vapor injection cycle]
Three pressure levels:
- P_low: states 1 and 9
- P_medium: states 2, 3, 4, 7, and 8
- P_high: states 5 and 6

===== Page 70 =====

Vapor injection with flash tank Principle
[Image: Same flow sheet]
Three pressure levels: P_low, P_medium, P_high
Compressor options:
- Two compressors
- One compressor with two stages
- One compressor with injection

===== Page 71 =====

Vapor injection with flash tank Principle
[Image: Same flow sheet]
Three pressure levels, Compressor options
Flash tank splits mass flow rates:
- ṁ1 = ṁ2 = ṁ8 = ṁ9
- ṁ4 = ṁ5 = ṁ6 = ṁ7
- ṁ3
- ṁ3 + ṁ8 = ṁ7
- ṁ3 + ṁ2 = ṁ4

===== Page 72 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Flow sheet with flash tank]
Assumptions: adiabatic, isobar

===== Page 73 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Same diagram]
State 7: wet vapor, defined by p_medium and h = h6 → x7. For a defined state 6, x7 depends on the chosen p_medium.
Assumptions: adiabat, isobar

===== Page 74 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Same diagram]
State 7: wet vapor, defined by p_medium and h = h6 → x7.
The flash tank just separates the liquid and vapor phase.
State 3 → p_medium, x = 1
State 8 → p_medium, x = 0
Assumptions: adiabat, isobar

===== Page 75 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Same diagram]
State 7: wet vapor...
The flash tank just separates the liquid and vapor phase.
State 3 → p_medium, x = 1, State 8 → p_medium, x = 0
Mass flow rates:
State 3 → ṁ3 = x7·ṁ7
State 8 → ṁ8 = (1 - x7)·ṁ7

===== Page 76 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Same diagram]
State 7: wet vapor...
The flash tank separates liquid and vapor.
Mass flow rates as above.
Assumptions: adiabat, isobar
p_medium is the only degree of freedom

===== Page 77 =====

Vapor injection with flash tank T-h-plot
[Image: T-s diagram of vapor injection cycle]

===== Page 78 =====

Vapor injection with flash tank T-h-plot
[Image: Same diagram]

===== Page 79 =====

Vapor injection with flash tank Benefits
Only a share of the total mass flow rate is compressed from p_ev to p_co.
The remaining share is compressed with a smaller pressure ratio from p_medium to p_co.
Discharge temperature can be substantially reduced.
[Image: Small diagram]
Vapor injection is a possible cycle architecture adding complexity but improving efficiency (many other cycle architectures exist).
[Image: Second diagram]
More beneficial for processes with higher pressure ratios.

## SHCT26_Lec6_annotated.pdf (additional annotations)

[This file contains essentially the same slides as SHCT26_Lec6.pdf but with some handwritten annotations. Key additional notes from annotations: Page 56 includes annotation "Could leak through shaft" on open compressor diagram. Page 58 has heading "AHRI" (corrected from AHR1). Otherwise content matches the above.]

---

# Lecture 7: Advanced Flowsheets – Refrigerants

**Source: SHCT26_Lec7.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #7

Advanced flowsheets Refrigerants

Lana Liebl Leon Brendel, PhD April 1st 2026

===== Page 2 =====

Since last week, you are able to...
...explain the thermodynamics of compressors
...use the different compressor efficiencies and evaluate their accuracy and limitations
...describe the different compressor types and their application area

===== Page 3 =====

1
[Image: p-h diagram]
Isentropic efficiency: η_isentropic = (ṁ·(h_out^s - h_in))/(ṁ·(h_out - h_in)) = P_isentropic/P_fluid
We can accurately calculate the compressor outlet state, but not the power consumption (P_elec) of the compressor
Global efficiency: η_global = P_isentropic/P_elec
We can accurately calculate the power consumption (P_elec) of the compressor, but not the outlet state (P_elec ≠ ṁ·(h_out - h_in))

===== Page 4 =====

1
Best case: We know, e.g., η_isentropic, η_mech, η_elec
P_elec = P_isentropic / (η_elec·η_mech·η_isentropic) [η_global as denominator]
h_out = h_in + (h_out^s - h_in)/η_isentropic

===== Page 5 =====

For small to medium capacities: Mainly positive displacement compressors
[Image: Table of compressor types and their capacity ranges]
Most used types for residential heat pumps

===== Page 6 =====

[Graphs: Isentropic and volumetric efficiency vs pressure ratio for different compressor types?]
1.0 0.8 0.6 0.4 0.2 0.0 1.1 5 10 15 20 Pressure ratio p_out/p_in (-) 1.0 0.8 0.6 0.4 0.2 0.0 1.1 5 10 15 20 Pressure ratio p_out/p_in (-)

===== Page 7 =====

1. explain and model advanced heat pump flowsheets
...describe the requirements on refrigerants
...name different refrigerant classes
...explain the impacts of certain refrigerants on the environment
...explain the problem of flammable refrigerants
...explain the differences and advantages of refrigerant mixtures
...model heat pump processes with refrigerant mixtures

===== Page 8 =====

ETH Zürich
Advanced flowsheets

===== Page 9 =====

Internal heat exchanger (IHX) Principle

===== Page 10 =====

Internal heat exchanger (IHX) Principle
[Image: Flow sheet with IHX]

===== Page 11 =====

Internal heat exchanger (IHX) Benefits
[Image: T-s diagram]
Pinch point (evaporator) moves from outlet to inlet. Evaporation temperature can be increased. Compressor work and released heat decreases but COP increases.

===== Page 12 =====

Internal heat exchanger (IHX) Benefits
[Image: Same diagram]
- Pinch point (evaporator) moves from outlet to inlet
- Evaporation temperature can be increased
- Compressor work and released heat decreases but COP increases

===== Page 13 =====

Vapor injection with flash tank Principle

===== Page 14 =====

3
Vapor injection with flash tank Principle
[Image: Flow sheet]
Three pressure levels: P_low: states 1 and 9, P_medium: states 2,3,4,7,8, P_high: states 5 and 6

===== Page 15 =====

1
Vapor injection with flash tank Principle
[Image: Flow sheet]
Three pressure levels
Compressor options: Two compressors, One compressor with two stages, One compressor with injection

===== Page 16 =====

1
Vapor injection with flash tank Principle
[Image: Flow sheet]
Three pressure levels, Compressor options
Flash tank splits mass flow rates: ṁ1=ṁ2=ṁ8=ṁ9, ṁ4=ṁ5=ṁ6=ṁ7, ṁ3, ṁ3+ṁ8=ṁ7, ṁ3+ṁ2=ṁ4

===== Page 17 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Flow sheet]
Assumptions: adiabat, isobar
State 7: wet vapor defined by p_medium and h=h6→x7. For a defined state 6, x7 depends on chosen p_medium.

===== Page 18 =====

1
Vapor injection with flash tank Balances of the flash tank
[Image: Flow sheet]
State 7: wet vapor...
The flash tank just separates the liquid and vapor phase.
State 3 → p_medium, x=1; State 8 → p_medium, x=0
Assumptions: adiabat, isobar

===== Page 19 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Flow sheet]
Assumptions: adiabat, isobar
State 7: wet vapor...
The flash tank separates liquid and vapor.
Mass flow rates: State 3 → ṁ3 = x7·ṁ7, State 8 → ṁ8 = (1-x7)·ṁ7

===== Page 20 =====

Vapor injection with flash tank Balances of the flash tank
[Image: Flow sheet]
Assumptions: adiabat, isobar
State 7: wet vapor...
The flash tank separates liquid and vapor.
Mass flow rates as above.
p_medium is the only degree of freedom

===== Page 21 =====

7
[Image: T-s diagram of vapor injection cycle]

===== Page 22 =====

7
[Image: Same T-s diagram]

===== Page 23 =====

1
Only a share of the total mass flow rate is compressed from p_ev to p_co.
The remaining share is compressed with a smaller pressure ratio from p_medium to p_co.
[Image: Small diagram]
Vapor injection is a kind of pressure recuperation.
[Image: Second diagram]
More beneficial for processes with higher pressure ratios.

===== Page 24 =====

Other complex cycle architectures CO2 supermarket refrigeration
[Image: Flow sheet of CO2 booster cycle]
CO2-Booster-Kälteanlage und Ejektoren - Kälte Klima Aktuell (kka-online.info)
2023 - Bärtsch - CO2-Kälteanlage mit integriertem EnergieTransfer-System Energie-Transfer-System ETS

===== Page 25 =====

Other complex cycle architectures CO2 supermarket refrigeration
[Image: Same flow sheet]
Field tests

===== Page 26 =====

Topics at a glance
| Lecture | Topics |
|---------|--------|
| L1 | Introduction Simple heat pump model |
| L2 | Fluid property models |
| L3 | Heat sources and sinks Pinch model |
| L4 | Components #1: Heat exchanger |
| L5 | Components #2: Expansion valves Transcritical process |
| L6 | Components #3: Compressors |
| L7 | Advanced flowsheets Refrigerants |
| L8 | Controlling Residential heating |
| L9 | High-temperature industrial heat pumps |
| L10 | Cooling – everything different now? |
| L11 | Air-conditioning |
| L12 | Low-temperature and cryo cooling |
| L13 | Niche technologies |

===== Page 27 =====

ETH Zürich
Refrigerants

===== Page 28 =====

1
[Bullet points on refrigerant requirements]
Critical and triple point well outside the working range
High latent heat of vaporization
High critical temperature
Positive but no excessive pressures at evaporating and condensing conditions
Low critical pressure
High suction gas (compressor inlet) density
High density → small volume flow rates → small components
Large molar mass
High efficiency

===== Page 29 =====

1
[Continuation]
Chemically stable
Compatible with construction materials (e.g., non-corrosive)
Miscible with lubricants
Lubrication of the compressor

===== Page 30 =====

How it started

===== Page 31 =====

0

===== Page 32 =====

0

===== Page 33 =====

[Large grid of numbers from 1 to 1000? Possibly periodic table or refrigerant numbering]

===== Page 34 =====

Halogenated molecules Halogens

===== Page 35 =====

Halogenated molecules Halogenation
Kick away hydrogen, Add halogens
[Image: Diagram of methane halogenation]

===== Page 36 =====

Halogenated molecules Halogenation
[Image: Same diagram]
[Image: Second diagram]
All hydrogen atoms replaced: fully halogenated, Otherwise: partially halogenated

===== Page 37 =====

Halogenated molecules Dichlorodifluoromethane (R12)

===== Page 38 =====

Halogenated molecules Dichlorodifluoromethane (R12)

===== Page 39 =====

Halogenated molecules Dichlorodifluoromethane (R12)

===== Page 40 =====

Halogenated molecules Dichlorodifluoromethane (R12)

===== Page 41 =====

Halogenated molecules #1 Hydrochlorofluorocarbons (HCFC) / Chlorofluorocarbons (CFC)
| Name | Crit. temp. (°C) | Crit. pres. (bar) | norm. boiling point (°C) |
|------|------------------|-------------------|--------------------------|
| Trichlorofluoromethane R11 | 197.96 | 44.1 | 23.3 |
| Dichlorodifluoromethane R12 | 111.97 | 41.4 | -30.1 |
| Dichlorofluoromethane R21 | 179.33 | 51.8 | 8.5 |
| Chlorodifluoromethane R22 | 96.15 | 49.9 | -41.1 |
| 1,2-Dichloro-1,1,12,2-Tetrafluoroethane R114 | 145.68 | 32.6 | 3.2 |
| ... | | | |

===== Page 42 =====

Halogenated molecules #1 Hydrochlorofluorocarbons (HCFC) / Chlorofluorocarbons (CFC)
[Same table]
Appropriate refrigerant for all applications

===== Page 43 =====

Swapping out atoms
Methane based refrigerants with their normal boiling point and toxicity and flammability.

===== Page 44 =====

1974
Rank Sherwood Rowland and Mario J. Molina suggested that CFCs and HCFCs deplete the ozone layer
More precise: Chlorine and Bromine are problematic
1987 Montreal Protocol: Ban of ozone-depleting chemicals, also CFCs and HCFCs
1989 The ban came into effect (stepwise)

===== Page 45 =====

Halogenated molecules #1 Hydrochlorofluorocarbons (HCFC) / Chlorofluorocarbons (CFC)
Ozone depletion potential (ODP): functional value, ODP of R11 is set to 1
[Same table with ODP column added: R11 ODP=1, R12 ODP=1, R21 ODP=0.0055, R22 ODP=0.02, R114 ODP=1, etc.]

===== Page 46 =====

Halogenated molecules #1 Hydrochlorofluorocarbons (HCFC) / Chlorofluorocarbons (CFC) Ozone depletion potential (ODP): functional unit, normalized to the effect of R11
[Table with ODP values]

===== Page 47 =====

1
ABSTRACT
By introducing HFC-134a as the replacement refrigerant for CFC-12 in motorcar air conditioning, the automobile industry will comply with the present national and international legislation for the phase-out of ozone-depleting substances.
A transition to this new fluid will, however, result in emissions of several hundred thousand tonnes of a new and unfamiliar chemical compound to the atmosphere each year, involving both known negative consequences like global warming, and potential risks of serious unknown environmental effects.
A new, efficient and environmentally benign automobile air conditioning system "MAC-2000" has been developed at The Norwegian Institute of Technology, in cooperation with Hydro Aluminium.
The new system is based on a trans-critical vapour compression cycle with carbon dioxide as the refrigerant. Although working pressures and role [1-3]. HFC-134a emission may increase the lifetime global warming impact from a car by as much as 15-20%, a quite significant effect considering that every second of the 40-45 million cars produced each year have factory-installed A/C. This fraction is expected to rise in the years to come, further increasing the refrigerant consumption. Historically, automobile air conditioning has been the by far
Assuming total driving distance 160.000 km and a lifetime refrigerant emission of 3 kg HFC-134a. Fuel economy 0.65 l/10km (31.4 MPG), and GWP = 1200 for HFC-134a

===== Page 48 =====

What next?
[Image: Icons for natural refrigerants]
Natural refrigerants: Butane, isobutane... Flammability is not a problem due to small charges
All other applications
[Image: Icon for halogenated molecules]
Round #2 of halogenated molecules but without Chlorine and Bromine

===== Page 49 =====

Halogenated molecules #2 Hydrofluorocarbons (HFC) / Fluorocarbons (FC)

===== Page 50 =====

Halogenated molecules #2 Hydrofluorocarbons (HFC) / Fluorocarbons (FC)

===== Page 51 =====

Halogenated molecules #2 Hydrofluorocarbons (HFC) / Fluorocarbons (PFC)

===== Page 52 =====

Halogenated molecules #2 Hydrofluorocarbons (HFC) / Perfluorocarbons (PFC)
| Name | Crit. temp. (°C) | Crit. pres. (bar) | norm. boiling point (°C) |
|------|------------------|-------------------|--------------------------|
| 1,1,1,2-Tetrafluoroethane R134a | 101.06 | 40.6 | -26.4 |
| Difluoromethane R32 | 78.11 | 57.8 | -51.9 |
| 1,1-Difluoroethane R152a | 113.26 | 45.2 | -24.3 |
| 1,1,1,2,3,3,3-Heptafluoropropane R227ea | 101.75 | 29.3 | -16.6 |
| Pentafluoroethane R125 | 66.02 | 36.2 | -48.36 |
| ... | | | |
Azeotropic mixtures:
| 50% R32 / 50% R125 | R410A | 71.34 | 49.0 | -51.7 |
| 85% R143a / 44% R125 / 4% R134a | R404A | 72.12 | 37.3 | -46.5 |

===== Page 53 =====

1997 Commitment to reduce greenhouse gas emissions, also hydrofluorocarbons (HFCs) and perfluorocarbons (PFCs)

===== Page 54 =====

Halogenated molecules #2 Hydrofluorocarbons (HCFC) / Perfluorocarbons (PFC) [typo: should be HFC/PFC]
Global warming potential (GWP): normalized to the global warming potential of CO2
[Table with GWP values: R134a GWP=1300, R32 GWP=675, R152a GWP=140, R227ea GWP=2900, R125 GWP=2800, R410A GWP=2088, R404A GWP=3260]

===== Page 55 =====

1997 Commitment to reduce greenhouse gas emissions, also hydrofluorocarbons (HFCs) and perfluorocarbons (PFCs)
2006 (EC) No 842/2006 Regulation on certain fluorinated greenhouse gases
2014 (EU) No 517/2014 Regulation on fluorinated greenhouse gases
2016 Kigali amendment. International agreement to gradually reduce the consumption and production of HFCs with global warming potential

===== Page 56 =====

2015: Verbot von Haushalts-kühigeräten mit Kältemitteln mit GWP ≥ 150
Global warming
1997 Commitment to reduce greenhouse hydrofluorocarbons (HFCs) and pe
2006 (EC) No 842/2006 Regulation on certain fluorinated g
2014 (EU) No 517/2014 Regulation on fluorinated greenhouse gases
2016 Kigali amendment. International agreement to gradually reduce the consumption and production of HFCs with global warming potential

===== Page 57 =====

"Low GWP refrigerants"
[Image: Diagram of HFO structure]

===== Page 58 =====

1. GWP depends on Absorption and emission spectra, Lifetime in the atmosphere
#2 Hydrofluorocarbons (HFC) / Perfluorocarbons (PFC) [list of HFCs]
Fluorinated alkanes
#3 HFO: Hydrofluorolefins (old designation for alkenes)
| Name | |
|------|-----------------|
| 2,3,3,3-Tetrafluoropropene | R1234yf |
| 3,3,3-Trifluoropropene | R1243zf |
Alkenes have a double bond making them less stable ⇒ short atmospheric lifetime ⇒ lower GWP, although absorption and emission spectra are similar

===== Page 59 =====

"Low GWP refrigerants"
[No additional text]

===== Page 60 =====

1
Why is flammability such a big problem?
Refrigerant leakage can cause fire or explosions. Particularly dangerous in case of indoor or split installation.
[Image: Small diagram of fire]
The norm EN 378-1:2021 regulates the use of flammable and toxic refrigerants.

===== Page 61 =====

Norm EN 378-1:2021 Safety classifications
Toxicity: A: lower toxicity, B: higher toxicity
[Image: Diagram of toxicity classes]
Flammability: 1: No flame propagation, 2L: Very low flammability, 2: Low flammability, 3: High flammability
[Image: Diagram of flammability classes]
Classification: Propane is a A3 refrigerant, Ammonia is a B2L refrigerant
- HFCs and PFCs are usually A1 refrigerants (but with large GWPs)
- HFOs are usually A2L refrigerants
- Hydrocarbons are usually A3 refrigerants

===== Page 62 =====

Norm EN 378-1:2021 Consequences for indoor and split installation
Maximum refrigerant charge without special requirements on the installation
| Safety class | 3 | 2L |
|--------------|---|---|
| Refrigerant | R290 | R32 |
| max. charge (kg) | 0.15 | 1.84 |

===== Page 63 =====

Norm EN 378-1:2021 Consequences for indoor and split installation
Maximum refrigerant charge without special requirements on the installation
[Same table]
Achievable heating power with market available heat pumps
| Safety class | 3 | 2L |
|--------------|---|---|
| Refrigerant | R290 | R32 |
| ≈ max. heating power (kW) | 1 | 10 |

===== Page 64 =====

Norm EN 378-1:2021 Consequences for indoor and split installation
Maximum on the in
Heating power too small for many applications, in particular, for A3 refrigerants
[Image: Small diagram]
- Outdoor installation (but not possible everywhere)
- Manufacturers are working on low-charge heat pumps
[Table with max heating power: R290 ~1 kW, R32 ~10 kW]

===== Page 65 =====

Degradation products of fluorinated refrigerants
Fluorinated refrigerants decompose in the atmosphere to other fluorochemicals ...most of them are so called PFAS: Per- and Polyfluoroalkyl Substances

===== Page 66 =====

1
Most PFAS are:
- of artificial origin ⇒ they do not occur naturally in nature
- "forever" chemicals ⇒ once produced and emitted, they will never disappear
- hygroscopic ⇒ absorb moisture from air and fall down as rain
- highly soluble in water ⇒ can be found in nearly any body of water
Are they harmful?
- For some, we know that they are certainly harmful
- If they are harmful in general, is an ongoing dispute
- But emitting chemical that are forever is never a good idea

===== Page 67 =====

There is a request from various countries to include PFAS in the EU REACH regulation → All PFAS would be banned that are not irreplaceable or proven to be harmless. → Some PFAS refrigerants will be banned through the F-Gas regulation
https://echa.europa.eu/hot-topics/perfluoroalkyl-chemicals-pfas
Not only refrigerants are PFAS
[Image: Diagram of PEM fuel cell]
Polymer electrolyte membranes (PEM)

===== Page 68 =====

We are still searching for new refrigerants
[Image: Graph from "Wärmepumpen, Bundesamt für Energie, Zurich 2018"]
The hunt for nonflammable refrigerant blends to replace R-134a (Ian H. Bell et al.)
Reverse engineering of fluid selection for thermodynamic cycles with cubic equations of state (Dennis Roskosch, Burak Atakan)
Limited options for low-global-warming-potential refrigerants (Mark O. McLinden et al., Nature Communications)

===== Page 69 =====

Refrigerant mixtures with temperature glide

===== Page 70 =====

Thermodynamics of mixtures
[Image: T-s diagram of mixture showing temperature glide]
Azeotropic mixtures at azeotropic composition behave like pure fluids.
Zeotropic mixtures and azeotropic mixtures at non-azeotropic composition:
Isobar evaporation and condensation is not isotherm. Temperature change is called temperature glide. Temperature glide depends on the mixture components and the composition.

===== Page 71 =====

How does it change the heat pump process?
[Image: T-s diagram]
- The isobars change temperature in the two-phase dome
- There is no longer one evaporation and condensation temperature
- Consider that in the pinch-model
- Best practice where to define T_ev and T_co for optimizations is at the dew line

===== Page 72 =====

1
[Image: T-s diagram comparing pure fluid and mixture]
Ratio of thermodynamic mean temperatures T̄_H/T̄_L is decreased → COP increases. Temperature glide of the mixture must fit the temperature changes of heat sink and source.

===== Page 73 =====

Mixtures promise more benefits than efficiency increase
[Image: Graph of COP vs temperature lift for different mixtures]
One mixture ⇒ many options

===== Page 74 =====

Mixtures promise more benefits than efficiency increase
[Image: Same graph]
One mixture ⇒ many options

===== Page 75 =====

1
[Image: Same graph]
Promising, in particular, for high-temperature heat pumps. Current research project at EPSE. Follow-up in lecture #10

===== Page 76 =====

Are mixtures already used?
Yes, but...
R-numbers of mixtures by definition always start with a 4 or a 5.
- Most refrigerant mixtures used are azeotropic (R410A) mixtures → no temperature glide
- Some have a glide, but it was not intended
| Name | Composition by mass | GWP | ODP | Safety class | T-Glide at 20°C |
|------|---------------------|-----|-----|--------------|-----------------|
| R436A | 56% propane, 44% isobutane | 20 | A3 | 7.2 |
| R454C | 21.5% R32, 78.5% R1234yf | 148 | 0 | A2L | 7.5 |
| R445A | 85% R1234ze(E), 9% R134a, 6% CO2 | 146 | 0 | A2L | 22.4 |

===== Page 77 =====

1
- We need a refrigerant property model for mixtures
- Evaporation and condensation temperatures are no longer constant
- Pinch point can be anywhere in the heat exchangers

===== Page 78 =====

How can the states be calculated?
Evaporation and condensation temperatures are not clearly defined!
But we want to optimize the process based on evaporation and condensation temperatures.
⇒ We define the evaporation and condensation temperatures at a specified location as optimization variables.
Good options: T_ev,opt = T_ev(x=1), T_co,opt = T_co(x=1)

===== Page 79 =====

How can the states be calculated?
Temperatures change along evaporation and condensation, but pressures can still be assumed to be constant.
[Image: T-s diagram showing mixture isobars]

===== Page 80 =====

Location of pinch points
The isobars of mixture can have a curved shape in the two-phase region.
⇒ Pinch points can be anywhere!
[Image: T-s diagram]
Check the pinch condition in increments along the isobar! For the condenser and the evaporator!

===== Page 81 =====

1
Ever thought about the nomenclature?
Default:
- R-01 bis R-399
R-WXYZ: w: Number of double bonds, x: Number carbon atoms - 1, Y: Number hydrogen atoms +1, Z: Number fluoride atoms
(Whatever is lacking are the chloride atoms. Lower case letters at the end distinguish isomers or define the specific locations of atoms within the molecule)
Others:
- R-4XX - zeotropic mixtures
- R-401A: R-22/R-152a/R-124 (53/13/34)
- R-407B: R-32/R-125/R-134a (10/70/20)
- R-407C: R-32/R-125/R-134a (23/25/52)
- R-5XX - azeotropic mixtures
- R-500: R-12/R-152a (73.8/26.2)
- R-501: R-22/R-12 (75/25)
- R-6XX - hydrocarbons
- R-600, R-600a, R-601
- R-7XX - inorganic refrigerants
- R-717: Ammoniak
- R-718: Wasser
- R-744: Kohlendioxid

===== Page 82 =====

Introduction to this week's exercise

===== Page 83 =====

Task
In this exercise, you will extend the simple heat pump process model by a recuperator (counter-flow). You will optimize the heat pump temperatures, including the superheating regarding the COP, and compare the configurations (with/without recuperator). You will calculate both flowsheets for a refrigerant mixture. The results shall be compared to the pure fluid Propane. We have already carried out the calculations for Propane for you.
a) Consider no recuperator. Optimize the process temperatures (T_ev and T_co, ΔT_sh) for the mixture R436A with respect to the COP.
b) Consider the recuperator. Optimize the process temperatures (T_ev and T_co, ΔT_sh) for the mixture R436A with respect to the COP.
The following parameters are given:
Minimal superheating ΔT_sh = 8 K, Pinch ΔT_min = 0.5 K
Source: water, ΔT_si = 5 K, T_so_in = 11°C
Sink: water, ΔT_si = 5 K, T_si_in = 35°C
Fluid: R436A
Compressor efficiency: R436A: η_is = 0.52
The refrigerant always leaves the condenser as saturated liquid. Assume that the recuperator fully provides the superheating by subcooling the condensed fluid before throttling.

===== Page 84 =====

Task
[Image: T-s diagram of cycle with recuperator]
- Optimization variables: T_ev (defined at dew line), T_co (defined at dew line), ΔT_SH
- Whole superheating from recuperator
- Condenser outlet: saturated

===== Page 85 =====

3' Condenser 3' 1 3' 1' 3' 1' 3' 1' 3' 1' 1' 3' 1' 3' 1' 3'
Energy balances for recuperator:
adiabat (no heat transfer to ambient), superheating only in recuperator
LHS: Q̇ = ṁ·(h3' - h3)
RHS: Q̇ = ṁ·(h1 - h1'')
set by ΔT_sh !
Definition of state 3:
→ h3 = h3' - (h1 - h1'')
→ p3 = p3'

===== Page 86 =====

1
[Image: T-s diagram]
[Table of states: 1": T1"=T_ev; 1: T1=T1"+ΔT_sh; 3": T3"=T_co; 3': p3'=p3"; 3: h3 = h3' - (h1 - h1"); 2is: s2is=s1; 2: h2=(h2,is-h1)/η_is+h1; 4: h4=h3]

===== Page 87 =====

Required constraints
Pinch constraint evaporator, Pinch constraint condenser as usual, but....
Now, states 3' and 1" are important
[Image: T-s diagram]
Location of pinch points not clear for mixtures → check states along entire condensation and evaporation

===== Page 88 =====

Required constraints
- Additional pinch constraint for the recuperator!
[Image: Diagram of recuperator]
Assumption: counterflow
T3 - T1 > ΔT_approach
T3' - T1" > ΔT_approach

---

# Lecture 8: Controlling – Residential Heating

**Source: SHCT26_Lec8.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #8

Controlling Residential Heating

Lana Liebl Leon Brendel, PhD 15 April 2026

===== Page 2 =====

Since last week, you are able to...
...explain and model advanced heat pump flowsheets
...describe the requirements on refrigerants
...name different refrigerant classes
...explain the impacts of certain refrigerants on the environment
...explain the problem of flammable refrigerants
...explain the differences and advantages of refrigerant mixtures
...model heat pump processes with refrigerant mixtures

===== Page 3 =====

1930 approx. 1989
[Image: Timeline of refrigerants]
"Current low-GWP alternatives"

===== Page 4 =====

Maximum refrigerant charge without special requirements on the installation
| Safety class | 3 | 2L |
|--------------|---|---|
| Refrigerant | R290 | R32 |
| max. charge (kg) | 0.15 | 1.84 |
Achievable heating power with market available heat pumps
| Safety class | 3 | 2L |
|--------------|---|---|
| Refrigerant | R290 | R32 |
| ~ max. heating power (kW) | 9? | ? |

===== Page 5 =====

The drawbacks of pure HFOs
[Image: Graph comparing HFO to other refrigerants]
Currently many mixtures are used: → Compromise between efficiency and performance
HFOs have:
- Lower COPs
- Lower volumetric heating capacities
- Larger components required

===== Page 6 =====

We are still searching for new refrigerants
[Image: Graph from "Wärmepumpen, Bundesamt für Energie, Zurich 2018"]
The hunt for nonflammable refrigerant blends to replace R-134a (Ian H. Bell et al.)
Reverse engineering of fluid selection for thermodynamic cycles with cubic equations of state (Dennis Roskosch, Burak Atakan)
Limited options for low-global-warming-potential refrigerants (Mark O. McLinden et al., Nature Communications)

===== Page 7 =====

Refrigerant mixtures
[Image: T-s diagram]
Ratio of thermodynamic mean temperatures T̄_H/T̄_L is decreased → COP increases. Temperature glide of the mixture must fit the temperature changes of heat sink and source.

===== Page 8 =====

Student project Group selection open in Moodle
Group registration: until Apr. 21
Release of the tasks: Apr. 27
Submission deadline: Jun. 28
Introduction to Student Project: Apr. 29, 02:15 - 03:45 PM, HG E 19
We offer an additional Q&A Session where you can discuss your questions regarding the student project with us:
Q&A Session: May 27, 02:15 - 03:45 PM, HG E 19

===== Page 9 =====

Date and time: Wednesday, April 29, Tour starts at 10:30 (be a little early, we meet at 10:25), Takes 60 min.
Meeting place: Claridenstrasse 5 (Main entrance Kongresshaus Zürich)

===== Page 10 =====

After this lecture, you will be able to...
explain controlling concepts of heat pumps
sketch and describe the real heat pump cycle
integrate a heat pump cycle into a residential heating systems
describe and calculate storage concepts

===== Page 11 =====

Control options of vapor-compression cycles Fixed heat source and sink

===== Page 12 =====

Control options of vapor-compression cycles Fixed heat source and sink
[No additional text]

===== Page 13 =====

Control options of vapor-compression cycles Fixed heat source and sink
[No additional text]

===== Page 14 =====

Control options of vapor-compression cycles Fixed heat source and sink
[No additional text]

===== Page 15 =====

Control options of vapor-compression cycles Fixed heat source and sink
[No additional text]

===== Page 16 =====

2
[Image: Graph of compressor speed vs heating power]
Data from compressor manufacturer Bitzer
Increasing the compressor speed increases the mass flow rate and therefore the heating power

===== Page 17 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat source: Change of the inlet temperature [diagram]

===== Page 18 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat source: Change of the inlet temperature [diagram]; Change of the mass flow rate [diagram]
Remember Q̇ = ṁ·c_p·ΔT. If ṁ_so and/or T_in decreases, T_out decreases

===== Page 19 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat source (cross flow), process reactions to decreasing T_out

===== Page 20 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat source (cross flow), process reactions to decreasing T_out
[Image: T-s diagrams showing decrease in evaporation temperature]
Evaporation temperature decreases, COP and heating capacity decrease

===== Page 21 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat sink: Change of the inlet temperature [diagram]; Change of the mass flow rate [diagram]

===== Page 22 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat sink (cross flow), process reactions to increasing T_out

===== Page 23 =====

Control options of vapor-compression cycles Influences of heat source and sink
Heat sink (cross flow), process reactions to increasing T_out
[Image: T-s diagrams]

===== Page 24 =====

Control options of vapor-compression cycles
Usual controlling options:
- Compressor speed
- Orifice of the throttle
- Heat source mass flow rate
Usual changes caused by external factors:
- Heat source inlet temperature
- Heat sink mass flow rate
- Heat sink inlet temperature
Initiates control interventions

===== Page 25 =====

Control options of vapor-compression cycles Wrap-up
Usual controlling options: Compressor speed, Orifice of the throttle, Heat source mass flow rate
Usual changes caused by external factors: Heat source inlet temperature, Heat sink mass flow rate, Heat sink inlet temperature
Initiates control interventions
Please note! Every change of a process variable causes multiple reactions ⇒ the entire process must find a new equilibrium of the characteristics of all components. Here we just presented the major process reactions.

===== Page 26 =====

→ A heat pump must be designed to deliver enough heating power on the coldest day to be expected.
→ On warmer days, the nominal heating power is then too high

===== Page 27 =====

#1 Start/stop
→ A heat pump must be designed to deliver enough heating power on the coldest day to be expected.
→ On warmer days, the nominal heating power is then too high
[Image: Graphs of heating power and heat demand vs time]
Compensation of a too high heating power by start/stop regulation

===== Page 28 =====

Controlling concepts to meet the heating demand #1 Start/stop
[Image: Graph of storage temperature vs time]
Compensation of a too high heating power by start/stop regulation
Water storage tank, Concrete ceiling (underfloor heating), Thermal mass of radiator

===== Page 29 =====

Controlling concepts to meet the heating demand #1 Start/stop
[No additional text]

===== Page 30 =====

Controlling concepts to meet the heating demand #1 Start/stop
[Image: Graph of compressor power and heating power vs time]
Compressor start causes high starting current → High stress for the winding

===== Page 31 =====

Controlling concepts to meet the heating demand #1 Start/stop
Compressor power already high. Heating power only slowly increases. First, the thermal mass of the heat pump must be heated up. Poor COP.
[Image: Graphs]
Compressor start causes high starting current → High stress for the winding

===== Page 32 =====

Controlling concepts to meet the heating demand #1 Start/stop
Compressor power already high. Heating power only slowly increases. First, the thermal mass of the heat pump must be heated up. Poor COP.
[Image: Graphs]

===== Page 33 =====

#1 Start/stop
Compressor power already high. Heating power only slowly increases. First, the thermal mass of the heat pump must be heated up. Poor COP.
[Image: Graphs]

===== Page 34 =====

Controlling concepts to meet the heating demand #1 Start/stop
Compressor power already high. Heating power only slowly increases. First, the thermal mass of the heat pump must be heated up. Poor COP.
Normal operation point is reached.
Every start and stop causes high thermal stress. All materials are heated up and cooled down again. Every motor start stresses the winding and causes peak demand in the grid. Usually, the number of starts and stops has a major impact on the lifetime.
[Image: Graph]
Compressor start causes high starting current → High stress for the winding

===== Page 35 =====

Controlling concepts to meet the heating demand #2 Compressor speed
[Image: Diagram of frequency inverter]
With a frequency inverter, compressor speed can be changed. Usually between 30 and 70 Hz (→ 885 - 2065 rpm). Strongly depending on compressor type. Start/stop controlling is additional if demand undercuts min. supply (30 Hz)

===== Page 36 =====

Controlling concepts to meet the heating demand #2 Compressor speed
[Image: Same diagram]
With a frequency inverter, compressor speed can be changed. Usually between 30 and 70 Hz (→ 885 – 2065 rpm). Start/stop controlling is additional if demand undercuts min. supply (30 Hz)

===== Page 37 =====

Controlling concepts to meet the heating demand #2 Compressor speed
[Image: Diagram]
With a frequency inverter, compressor speed can be changed.
[Image: Three graphs of COP vs part load for start/stop vs speed regulation]
Start/stop frequency is decreased, but efficiency also decreases

===== Page 38 =====

Comparison
Inner HP COP vs. COP with degradation due to start/stop regulation
COP with degradation start/stop vs. speed regulation
[Image: Graph]

===== Page 39 =====

To avoid frequent starts and stops: Minimal operation time, Minimal down time
To relieve the energy grid: external lock
- Electricity supplier can externally lock the heat pump
- Number of possible locks and max. duration are defined in the contract
- Usually, the heat pump is blocked at times peak demands occur on the grid
- In return, suppliers offer a special rate for heat pumps

===== Page 40 =====

Residential heating

===== Page 41 =====

The real flow sheet of an air/water heat pump

===== Page 42 =====

The real flow sheet of an air/water heat pump
[No additional text]

===== Page 43 =====

The real flow sheet of an air/water heat pump
[No additional text]

===== Page 44 =====

The real flow chart of an air/water heat pump Venturi distributor
Equally distributes the refrigerant to the different rows of the evaporator

===== Page 45 =====

The real flow sheet of an air/water heat pump
Sight glass: The technician can check the phase of the refrigerant and if the refrigerant contains water. Liquid flows and bubbles are visible, gases not. Usually, sight glasses include a pH-paper which indicates if water is present.
[Image: Diagram of expansion valve and evaporator]

===== Page 46 =====

The real flow sheet of an air/water heat pump
[No additional text]

===== Page 47 =====

The real flow sheet of an air/water heat pump
[No additional text]

===== Page 48 =====

4-way valve, electrically controlled
Switching between heating and defrosting mode
[Image: Diagram of 4-way valve]

===== Page 49 =====

4-way valve, electrically controlled
[No additional text]

===== Page 50 =====

4-way valve, electrically controlled
[No additional text]

===== Page 51 =====

The real flow sheet of an air/water heat pump
[No additional text]

===== Page 52 =====

The (typical) entire heating system

===== Page 53 =====

The (typical) entire heating system
The heating and domestic water circuits cannot be supplied simultaneously. They usually operate at different temperatures. Depending on the demand, the heat pump switches between the circuits

===== Page 54 =====

The (typical) entire heating system Heat pump heating mode

===== Page 55 =====

The (typical) entire heating system Heating from storage

===== Page 56 =====

The (typical) entire heating system Charging storage

===== Page 57 =====

The (typical) entire heating system Domestic hot water

===== Page 58 =====

Simplest form: Insulated tank

===== Page 59 =====

Storage Tanks
[Image: Diagram of simple insulated tank]
Simplest form: Insulated tank
Distinguishing criteria:
- Homogeneous temperature or stratified
- With or without inner heat exchanger
- For heating water and/or domestic water

===== Page 60 =====

Storage Tanks
Simplest form: Insulated tank
Distinguishing criteria: [same]

===== Page 61 =====

Storage Tanks Homogeneous temperature
Storage temperature is a function of time but not a function of the position.
[Image: Diagram of tank with temperature profile]
Uncharged, charging is initiated

===== Page 62 =====

Storage Tanks Homogeneous temperature
[Image: Same diagram]
The difference between T_max and T_min is usually only a few Kelvin (5-10 K)

===== Page 63 =====

Storage Tanks Homogeneous temperature
[No additional text]

===== Page 64 =====

Storage Tanks Homogeneous temperature
[Image: Graph of storage temperature vs time]

===== Page 65 =====

Storage Tanks Homogeneous temperature
[Image: Same graph]

===== Page 66 =====

Storage Tanks Homogeneous temperature
[Image: Graph of storage temperature vs time]
[Image: Diagram of tank with temperature sensor]

===== Page 67 =====

Storage Tanks Stratified temperature

===== Page 68 =====

Storage Tanks Stratified temperature
[Image: Diagram of stratified tank with temperature layers]
Stratification can be realized only due to differences in density. But the flows must be slow to avoid mixing.

===== Page 69 =====

Storage Tanks Stratified temperature
[Image: Graph of stratified tank temperature vs time]
The heat pump always works at the same operation point. The COP is constantly high. Disadvantage: At the same storage volume, stratified tanks store less thermal energy. More frequent starts and stops of the heat pump. Larger storage volume required.

===== Page 70 =====

Balances of the homogeneous storage tank

===== Page 71 =====

Balances of the homogeneous storage tank Mass balance
[Image: Diagram of storage tank with flows]
Mass balance: dm_st/dt = -ṁ_HC - ṁ_HPC + ṁ_HC + ṁ_HPC = 0 → m_st = const.

===== Page 72 =====

Balances of the homogeneous storage tank Energy balance, heating from storage
[Image: Diagram]
m_st·c_l·dT_st/dt = ṁ_HC·c_l·T_BF - ṁ_HC·c_l·T_st - Q̇_loss

===== Page 73 =====

Balances of the homogeneous storage tank Energy balance, heating from storage
[Image: Diagram]
m_st·c_l·dT_st/dt = ṁ_HC·c_l·T_BF - ṁ_HC·c_l·T_st - Q̇_loss
T_st - T_BF = ΔT_heat

===== Page 74 =====

Balances of the homogeneous storage tank Energy balance, heating from storage
[Image: Diagram]
m_st·c_l·dT_st/dt = ṁ_HC·c_l·T_BF - ṁ_HC·c_l·T_st - Q̇_loss
T_st - T_BF = ΔT_heat
Substituting: m_st·c_l·dT_st/dt = ṁ_HC·c_l·(T_st - ΔT_heat) - ṁ_HC·c_l·T_st - Q̇_loss
= -ṁ_HC·c_l·ΔT_heat - Q̇_loss

===== Page 75 =====

1
[Image: Diagram]
[Image: Graph of storage temperature vs time]

===== Page 76 =====

Balances of the homogeneous storage tank Energy balance, heating from storage
[Image: Diagram]

===== Page 77 =====

Balances of the homogeneous storage tank Energy balance, heating and charging

===== Page 78 =====

Balances of the homogeneous storage tank Energy balance, heating and charging
[No additional text]

===== Page 79 =====

1
[No additional text]

===== Page 80 =====

Balances of the homogeneous storage tank Energy balance, heating and charging
[No additional text]

===== Page 81 =====

1
[Image: Diagram with HP and heating circuit]
[Image: Graph of storage temperature vs time with charging]
[Image: Graph of HP power vs time]

===== Page 82 =====

Introduction to this week’s exercise

===== Page 83 =====

In this exercise, you will investigate the temperature of a stirred thermal storage tank connected to a heat pump. We do not model the heat pump here but consider it as a start/stop controlled device with a fixed heating power. The heat pump is switched on if the storage temperature decreases below the minimum storage temperature. The heat pump is switched off if the storage temperature exceeds the maximum storage temperature. The thermal storage is connected to a heating circuit and insulated to reduce the heat transfer to the environment.
You will examine two different thermal storage tanks and compare the temperature-time profile of the storage temperature and the operating profile of the heat pump.
The following parameters are given:
Heat pump: Q̇_high = 5 kW
Heating circuit: water, c_water = 4.18 kJ/kgK, ΔT = 6 K, ṁ_w = 0.05 kg·s⁻¹
Environment: T_env = 5°C
Use the given thermal resistances to calculate the heat transfer to the environment
The thermal storage is fully charged at the beginning.
Calculate the temperature-time profile of the storage for one day (solution in seconds). Plot the storage temperature against the time. Further, plot the operation of the heat pump (heating power) against the time. Do the calculations for the following cases:
a) Case 1: V_store = 200L, thermal resistance R_300 = 1.8 K·W⁻¹, T_store,max = 38°C, T_store,min = 32°C
b) Case 2: V_store = 600L, thermal resistance R_600 = 0.9 K·W⁻¹, T_store,max = 38°C, T_store,min = 32°C

===== Page 84 =====

Flowsheet
[Image: Diagram of storage tank with HP and heating circuit]

===== Page 85 =====

Initial conditions: T_st = T_max
From t = 0 only heating mode:
m_st·c_l·dT_st/dt = -ṁ_HC·c_l·ΔT_heat - (1/R)·(T_st - T_env)
If T_st undercuts T_min heat pump starts → heating and charging mode:
m_st·c_l·dT_st/dt = -ṁ_HC·c_l·ΔT_heat + Q̇_HP - (1/R)·(T_st - T_env)
If T_st exceeds T_max heat pump stops → only heating mode:
m_st·c_l·dT_st/dt = -ṁ_HC·c_l·ΔT_heat - (1/R)·(T_st - T_env)
Check and solve for each time step along the simulation time.

---

# Lecture 9: High Temperature and Industrial Heat Pumps

**Source: SHCT26_Lec9.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #9

High temperature and industrial heat pumps

Leon Brendel, PhD Lana Liebl 22 April 2026

===== Page 2 =====

Since last week, you are able to...
...explain controlling concepts of heat pumps
...sketch and describe the real heat pump cycle
...integrate a heat pump cycle into a residential heating systems
...describe and calculate storage concepts

===== Page 3 =====

Control options of vapor-compression cycles Wrap-up
Usual controlling options: Compressor speed, Orifice of the throttle, Heat source mass flow rate
Usual changes caused by external factors: Heat source inlet temperature, Heat sink mass flow rate, Heat sink inlet temperature
Initiates control interventions
Please note! Every change of a process variable causes multiple reactions ⇒ the entire process must find a new equilibrium of the characteristics of all components. Here we just presented the major process reactions.

===== Page 4 =====

Controlling concepts to meet the heating demand #1 Start/stop

===== Page 5 =====

Controlling concepts to meet the heating demand #2 Compressor speed
[Image: Diagram of frequency inverter]
With a frequency inverter, compressor speed can be changed. Usually between 30 and 70 Hz (→ 885 – 2065 rpm). Start/stop controlling is additional if demand undercuts min. supply (30 Hz)
[Image: Three graphs]
Start/stop frequency is decreased, but efficiency also decreases

===== Page 6 =====

The (typical) entire heating system

===== Page 7 =====

Topics of today's lecture
Market potential of high-temperature heat pumps
Current products
Thermodynamic limits
Challenges of high-temperature vapor-compression heat pumps
Decarbonizing steam production

===== Page 8 =====

Temperature ranges for heat pumps
Residential heat pumps → up to 75°C
Industrial heat pumps → approx. 65 - 100°C (not firmly defined)
High temperature heat pumps → approx. >100°C

===== Page 9 =====

100 bis 150°C, 80 bis 100°C, Raumwärme/Warmwasser < 80°C
[Image: Diagram of temperature ranges with process heat]
Space heating / domestic water T<80°C, Process heat 80 to 100°C, Process heat 100-150°C
Source: Arpagaus, Hochtemperatur-Wärmepumpen

===== Page 10 =====

Table 1 (continued)
[Table of industrial subsectors and processes with energy demand and temperature distribution]
Source: Rehfeldt, M., Fleiter, T., & Toro, F. (2018). A bottom-up estimation of the heating and cooling demand in European industry. Energy Efficiency, 11(5), 1057-1082.

===== Page 11 =====

Overview of processes in industrial sectors
[Same table continued]
Heat transfer media mostly are: Water, Hot gases, Thermal oils, Steam
Careful! Such data can be erroneous. Many processes could run with much lower temperatures than they are currently operated with.

===== Page 12 =====

Fig. 5. Cumulative process heat <200°C in EU28 identified in processes which make up the heat pump market study.

===== Page 13 =====

1200
Fig. 6. Cumulative waste heat <200°C in EU28 identified in processes which make up the heat pump market study.

===== Page 14 =====

2024 50 HTWPs > 100°C
[Image: Map or graph of high-temperature heat pumps]

===== Page 15 =====

See other slide deck

===== Page 16 =====

2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030
For capacity range 500 kW bis 10 MW. Source: Annex 58: Task 1 Final Report

===== Page 17 =====

Thermodynamic potential

===== Page 18 =====

Thermodynamic potential

===== Page 19 =====

COP as a function of the lift
[Image: Graph of COP vs temperature lift]

===== Page 20 =====

200 175 150 125 100 75 50 25 0 0 20 40 60 80 100 Source temperature [°C]
[Image: Contour plot of COP as function of source and sink temperatures]
For large temperature differences, use Lorenz efficiency!

===== Page 21 =====

COP as a function of the lift - products
[Image: Graph from Arpagaus et al. (2018) showing COP of commercial high-temperature heat pumps]

===== Page 22 =====

Are industrial high-temperature heat pumps simply larger and hotter residential heat pumps?
Yes, but with special challenges regarding:
- Refrigerants
- Compressor
- Oils
- System integration

===== Page 23 =====

First challenge: suitable refrigerants
[Bullet list of refrigerant requirements]
- Critical and triple point well outside the working range
- Very high critical temperature
- High latent heat of vaporization
- Very high critical temperature
- Positive but no excessive pressures at evaporating and condensing conditions
- Low critical pressure
- High suction gas (compressor inlet) density
- Trade off between suction gas density and heat of vaporization
- High efficiency
- Chemically stable
- Compatible with construction materials (e.g., non-corrosive)
- Miscible with lubricants
- Lubrication of the compressor
- No ODP
- No GWP
- No PFAS?
- Not flammable?

===== Page 24 =====

Refrigerants for high temperature heat pumps Selection of commonly used or proposed refrigerants
Hydrocarbons table:
| Fluid | MM | p_cr | T_cr | T_nb | p_dew_30°C | Delta_h_60 |
|--------|-----|------|------|------|------------|------------|
| Propen | 42.14 | 55.09 | 91.1 | -47.9 | 27.7 | 342.8 |
| Propan | 44.14 | 42.51 | 96.7 | -42.4 | 23.5 | 381.2 |
| Isobutan | 58.14 | 36.29 | 134.7 | -12.1 | 10.5 | 337.3 |
| Butan | 58.14 | 37.96 | 152.0 | -0.8 | 7.1 | 321.3 |
| Isopentan | 72.14 | 33.78 | 187.2 | 27.4 | 3.3 | 315.1 |
| Pentan | 72.14 | 33.67 | 196.6 | 35.7 | 2.4 | 284.9 |
| Hexan | 86.17 | 30.44 | 234.7 | 68.3 | 0.9 | 342.9 |
| Cyclopentan | 70.13 | 45.82 | 238.6 | 48.9 | 1.5 | 259.2 |
HFO refrigerants table:
| Fluid | MM | p_cr | T_cr | T_nb | p_dew_30°C | Delta_h_60 |
|--------|-----|------|------|------|------------|------------|
| R1234ze(E) | 114.0 | 36.34 | 109.4 | -19.3 | 30.5 | 171.2 |
| R1336mzz(E) | 164.0 | 27.79 | 130.4 | 7.5 | 16.4 | 145.2 |
| R1234ze(Z) | 114.0 | 35.30 | 150.1 | 9.4 | 10.4 | 169.1 |
| R1224yd(Z) | 148.5 | 33.37 | 155.5 | 14.3 | 11.2 | 123.0 |
| R1233zd(E) | 130.5 | 36.23 | 166.5 | 17.9 | 8.5 | 135.5 |
| R1336mzz(Z) | 164.1 | 29.03 | 171.4 | 33.1 | 6.1 | 110.4 |

===== Page 25 =====

Comparison of two hydrocarbons
[Image: T-s diagrams of propane and isopentane]
More C-atoms lead to higher critical temperature and slightly wider dome at given sat. temperature.

===== Page 26 =====

Comparison of HFO and hydrocarbon
Strongly differing width of dome and density.

===== Page 27 =====

Overview of domes
[Image: T-s diagrams of multiple refrigerants]

===== Page 28 =====

Optional further reading
Figure 3. Effect of thermodynamic parameters on the shape of the saturation dome; (a) effect of critical temperature, T_c on (T-s) coordinates; (b) effect of critical pressure, p_c on (p-h) coordinates; (c) effect of vapor molar heat capacity, C_p^0, on (T-s) coordinates.
With the low C_p^0 of ammonia the vapor dome is "upright;" this results in a high compressor discharge temperature (which decreases efficiency), but the expansion losses are relatively small (increasing efficiency). As the value of C_p^0 increases the vapor dome increasingly "leans over." With the high C_p^0 of R-218 the result is "wet compression" (where an isentropic compression process starting with saturated vapor would result in a two-phase state exiting the compressor); the saturated-liquid (left) side of the saturation dome is also much more tilted, resulting in increased expansion losses. The result of these offsetting effects is that there is an optimal value of C_p^0 for a given cycle; in this...

===== Page 29 =====

Operation relative to dome
[No additional text]

===== Page 30 =====

Operation relative to dome
[No additional text]

===== Page 31 =====

- CO2
  - Critical temperature of 31°C
  - Upper limit on source temperature
  - Limit on sink temperature
- Ammonia
  - Critical temperature of 132°C
  - Limit on sink temperature
- Water
  - Critical temperature of 373°C
  - Limited availability of compressors
  - Available: High capacity and small pressure ratio

===== Page 32 =====

Constraint for refrigerant selection

===== Page 33 =====

Table A.1 Working fluid screening.
[Large table of working fluids with properties: name, short formula, critical temperature, critical pressure, GWP ≤150?, ODP=0?, etc.]
Vieren, E., et al. (2023). The thermodynamic potential of high-temperature transcritical heat pump cycles for industrial processes with large temperature glides. Applied Thermal Engineering, 234, 121197.
Also from EPSE at ETH: Widmaier, P., Brendel, L. P. M., Bertsch, S. S., Bardow, A., & Rookshock, D. (2025). One Mixture to Rule Them All: Enhancing Efficiency and Standardization of Industrial High-Temperature Heat Pumps. to be published in ACS Engineering.

===== Page 34 =====

Option: Cascade heat pump cycles
[Image: Flow sheet of cascade cycle]
Source: https://doi.org/10.1016/j.energy.2021.120097

===== Page 35 =====

Option: Cascade heat pump cycles for higher lifts
- Heat transfer between the cycles causes exergy losses and decreases the COP
- Controlling and part load behavior are getting more complicated
- Larger investment costs
[Image: T-s diagram of cascade cycle]

===== Page 36 =====

Second challenge: large compressor temperatures
[Image: Graph of compressor outlet temperature vs sink temperature for ammonia]
E.g., Ammonia, T_sink,out = 150°C, Compressor outlet: up to 300°C. More expensive materials are required. Oil degradation → lubrication fails. Oil-free compressors → expensive. Intercooling.

===== Page 37 =====

During the compression, the gas is cooled down by:
- heat transfer (e.g., suitable for multistage compressors)
- liquid or vapor injection (all types of compressors)
[Image: Diagram of liquid injection]
Liquid injection: Injected liquid evaporates and cools the gas
[Image: Diagram of compressor stages]

===== Page 38 =====

350 300 250 200 150 100 50 0 -50 enthalpy Source: MAN
[Image: T-s diagram of compression with intercooling]
sor stages [diagram]

===== Page 39 =====

[Same as page 38]

===== Page 40 =====

Sustainable process steam generation

===== Page 41 =====

Who needs steam and how is it used?
Industries using steam:
- Food industry
- Breweries
- Dairies
- Textile industry
- Pharmaceuticals industry
- Pulp and Paper industry
- Chemical industry
How steam is used: Heating, Heating and material utilization, Drying, Mechanical energy generation, Sterilization and disinfection

===== Page 42 =====

Who needs steam and how is it used? Pulp and paper production
[Image: Photo of paper machine dryer section]
Steam is used to heat the drying cylinders

===== Page 43 =====

Who needs steam and how is it used? Dairy: pasteurization of milk
[Image: Photo of plate heat exchanger]
Steam delivers the heat to heat up the milk

===== Page 44 =====

Who needs steam and how is it used? Food industry
[Image: Steam peeling of carrots, autoclaves]

===== Page 45 =====

Who needs steam and how is it used? Chemical and pharmaceuticals industry
[Image: Diagram of reactors and distillation columns]
Heating and cooling of reactors, Heating of distillation columns, Steam cracker, Steam reforming
BASF Ludwigshafen (GER) requires approx. 18 mio. tons steam per year

===== Page 46 =====

Steam production and distribution Industrial sites
- Usually, steam is produced in centralized heat and power plants
- Slightly superheated
- At different pressure (temperature) levels
- Distributed to the various factories via steam lines
[Image: Photos of industrial sites]
Usual steam pressure and temperatures: 2 bar (120°C), 6 bar (159°C), 32 bar (237°C), 50 bar (264°C)

===== Page 47 =====

Why is steam such a good energy carrier?
Non-toxic, not flammable, environmentally friendly. Easy to distribute. Large energy content. Isothermal heat rejection. Product is just water ⇒ can be emitted to the environment.
Heating an endothermic reaction [diagram]

===== Page 48 =====

How steam is produced
[Image: Diagram of steam generation methods]
- Nowadays, steam production is mainly based on burning fossil fuels (gas and oil)
- Also in incineration or fossil fuel power plants (combined heat and power)

===== Page 49 =====

How can steam production be decarbonized?

===== Page 50 =====

Direct electrification Electrode steam boilers
[Image: Diagram of electrode boiler]
[Image: Photo of electrode boiler]
- Current flows through the water
- Due to its resistance water is heated up and evaporates
- Voltage up to 35 kV
- Efficiency approx. 99%
- Can operate at different pressures (temperatures)
- Available in various sizes

===== Page 51 =====

Steam generation with vapor compression heat pumps
[Image: Flow sheet of heat pump with steam generation]
Optionally add vapor recompression

===== Page 52 =====

Vapor re-compression
[Image: Flow sheet of vapor recompression]
Low-pressure steam is compressed to higher pressures. Number of compressor stages depends on entire pressure ratio. Usual pressure ratio per stage 3 - 3.5. Steam is cooled between the stages by water injection → Usually to the saturation state (x=1)

===== Page 53 =====

Low-pressure evaporation and vapor re-compression
[Image: Flow sheet with low-pressure evaporation]
- Liquid water is expanded to a pressure p_sat (T < T_source)
- Fully evaporated by ambient heat
- Compressed to a higher pressure

===== Page 54 =====

Examples of steam compressors

===== Page 55 =====

From next week on....
....cooling

===== Page 56 =====

Introduction to this week’s exercise

===== Page 57 =====

In this exercise, you will investigate a mechanical vapor recompression process to generate steam. The low-pressure evaporation is driven by ambient or waste heat. After throttling (state 1) and evaporating (state 2), the saturated vapor enters the multi-stage compressor. Between the stages, pressurized water is injected until the saturated vapor state is reached. The maximum number of stages is five.
The following parameters are given:
Maximum pressure ratio per compressor stage: pr_max = 3.5
Isentropic efficiency of the vapor compressor: η_is,vc = 0.85
Isentropic efficiency of the liquid pump: η_is,lp = 0.95
Injected water: T_w,inj = 25°C, p_w,inj = 1 bar
Inlet (state 0): water, T0 = 25°C, p0 = 1 bar, ṁ0 = 1.0 kg·s⁻¹
Pressure losses can be neglected
Consider a minimum approach temperature of 5 K in the evaporator
Consider an isothermal heat source (e.g., due to cross flow)
Evaluate the COP of the process dependent on the outlet pressure (1 ≤ p_out ≤ 60 bars) for the following source temperatures. Plot and discuss your results.
a. T_so = 10°C
b. T_so = 50°C
c. T_so = 80°C

===== Page 58 =====

Setup
[Image: Flow sheet of the vapor recompression process]

===== Page 59 =====

Mass balance: ṁ_steam,out = ṁ_steam,in + ṁ_injection
Energy balance: P_com + P_pump + ṁ_st,in·h_st,in + ṁ_inj·h_inj = ṁ_st,out·h_st,out
h_st,out = h(p_out, x=1)
Calculation of power and outlet state of compressor and pump through isentropic efficiency

---

# Lecture 10: Cooling – Everything Different Now?

**Source: SHCT26_Lec10_Slides.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #10

Cooling: Everything different now? Numerics and programming

Lana Liebl Dr. Leon Brendel 06 May 2026

===== Page 2 =====

Topics of the last lecture
Market potential of high-temperature heat pumps
Current products
Thermodynamic limits
Challenges of high-temperature vapor-compression heat pumps
Decarbonizing steam production

===== Page 3 =====

Are industrial high-temperature heat pumps simply larger and hotter residential heat pumps?
Yes, but with special challenges regarding:
- Refrigerants
- Compressor

===== Page 4 =====

Properties of possible substances Wrap-up and options
Available are: Fluids with large critical temperatures but too small vapor pressures near ambient temperature.
[Image: T-s diagrams]
Option 1: transcritical cycles
Option 2: cascade heat pump cycle

===== Page 5 =====

During the compression, the gas is cooled down by:
- heat transfer (e.g., suitable for multistage compressors)
- liquid or vapor injection (all types of compressors)
[Image: Diagram of liquid injection]
[Image: Diagram of compressor stages]

===== Page 6 =====

350 300 250 200 150 100 50 0 0 - 50 enthalpy
[Image: T-s diagram with compression cooling]

===== Page 7 =====

25 °C
[Image: T-s diagram]

===== Page 8 =====

From now on....
[Image: Diagram of cooling applications]
...cooling

===== Page 9 =====

Topics of today's lecture
Typical applications of cooling
Conditions of usual heat sinks and sources
From heat pumps to cooling machines - What is different?
CO2 for cooling processes
Supermarket refrigeration

===== Page 10 =====

Cooling a space, substance or system...
...below the ambient temperature [image]
...above the ambient temperature [image]
# > Refrigeration

===== Page 11 =====

2nd disclaimer

===== Page 12 =====

4 [Image: Ice production, food refrigeration and freezing]
Ice production, Food refrigeration and freezing

===== Page 13 =====

1 [Images: ceiling cooling, air conditioner, etc.]
Heat sources: Air (15 < T < 22°C), Water (5 < T < 18°C)
Heat sink: Ambient air (T > 20°C)

===== Page 14 =====

1 [Images: cold storage, cold room, etc.]
Heat sources: Mostly air, Brine, Products (-40 < T < 15°C)
Heat sink: Ambient air

===== Page 15 =====

1 [Images: process cooling, etc.]
Heat sinks: Ambient air [diagram]

===== Page 16 =====

1 [Images: ice rink, snow cannon, etc.]
Heat sources: Mostly products (sensible, latent), brine (-20 < T < 0°C)
Heat sink: Ambient air

===== Page 17 =====

1 [Images: data center cooling]
Heat sinks: Ambient air

===== Page 18 =====

Heat sinks and sources
[Image: Diagram]
Mostly air, Products (sensible / latent), Water / Brine, -40 < T < 15°C

===== Page 19 =====

Heat sinks and sources
[Image: Diagram]
| Application | T_evap |
|-------------|--------|
| Air-conditioning | +10 to 0°C |
| Food cooling (cold water) | 0 to -10°C |
| Food cooling (cold brine) | -10 to -35°C |
| Domestic freezers | -25°C |
| Food freezing | -35 to -55°C |
| Food quick freezing | -35 to -55°C |

===== Page 20 =====

Heat sinks and sources

===== Page 21 =====

Coefficient of performance
[Image: T-s diagram of cooling cycle]
COP_C = Q_low / W_in = (h1 - h4)/(h2 - h1)

===== Page 22 =====

Coefficient of performance
[Image: Same diagram]
COP_C = Q_low/W_in = (h1 - h4)/(h2 - h1)
Comparison to heat pump mode: COP_C = Q_low/W_in = (Q_high - W_in)/W_in = COP_H - 1
+ higher temperature ratio T_con/T_evap
⇒ COP_C ≪ COP_H

===== Page 23 =====

Coefficient of performance Carnot-limit
[Image: T-s diagram]
[Image: Formula]
COP_C,rev = T̄_low/(T̄_high - T̄_low)
COP_C,rev = 1/(T̄_high/T̄_low - 1), T̄_high > T̄_low
Keep the temperature ratio of T̄_high/T̄_low as small as possible!

===== Page 24 =====

Coefficient of performance Influence of subcooling
[Image: T-s diagram]
Heat pump: COP_H = q_high/W, Δh_sc is small compared to q_high
Cooling: COP_C = q_low/W, q_low < q_high → Share of Δh_sc on q_low is larger

===== Page 25 =====

Coefficient of performance Influence of subcooling
[Image: T-s diagram]
[Image: Graph of COP vs subcooling]
Subcooling should be exploited, as long as the condensation temperature must not be increased.

===== Page 26 =====

From heat pumps to cooling machines Real flow sheet
[Image: Flow sheet of heat pump with additional components]
Lecture #8
Cooling machines have similar additional components than heat pump cycles

===== Page 27 =====

From heat pumps to cooling machines Advanced flow sheets
[Image: T-s diagram of IHX for cooling]
Still beneficial, but: Mass flow rate through evaporator is decreased → Q_low is decreased

===== Page 28 =====

From heat pumps to cooling machines Controlling
[Image: Graph of controlling options]
Usual controlling options:
- Compressor on/off, speed
- Orifice of the throttle
- Heat sink mass flow rate
Also, for cooling cycles:
- T_evap can be controlled
- T_con is related to the heat sink

===== Page 29 =====

From heat pumps to cooling machines Compressors

===== Page 30 =====

From heat pumps to cooling machines Expansion valves
[Image: Diagram of expansion valve types]
Lecture #5
Still applies, but capillary tubes are more common for cooling machines than for heat pumps since the heat source temperature is well known and less volatile

===== Page 31 =====

From heat pumps to cooling machines Heat exchanger
[Image: Diagram of heat exchanger types]
Lecture #4
- Since air is the most common heat source and sink, fin and cool plate heat exchangers are most common
- Large cooling machines with refrigeration distribution system also use flooded evaporators

===== Page 32 =====

From heat pumps to cooling machines Refrigerants
First challenge: suitable refrigerants
[Bullet list of refrigerant requirements]
Still applies, but evaporation temperatures of cooling machines can be much smaller. Thus, refrigerants with lower normal boiling points are required to keep pressures above 1 bar

===== Page 33 =====

From heat pumps to cooling machines Refrigerants
Norm EN 378-1:2021 Consequences for indoor and split installation
Max charge table (R290 0.15kg, R32 1.84kg)
Achievable heating power (R290 ~1kW, R32 ~10kW)
[Image: Diagrams of installation types]
Indoor installation: refrigerators, domestic freezers, mobile air-conditioner
Outdoor installation: Water / brine cooler (chiller)
Split installation: Most common for all air/air cooling machines

===== Page 34 =====

From heat pumps to cooling machines The problem of flammable low-GWP refrigerants still applies, but
Many devices have a small cooling capacity and, thus, only require small refrigerant charges (e.g., domestic refrigerators and freezers, mobile air-conditioner...). flammable refrigerants are not a problem if the refrigerant charge is below 150 g.
Large industrial cooling machines often produce cold water or brine (chillers) and are installed outside. flammable refrigerants are less dangerous.
Nevertheless, industry prefers refrigerants with no or low flammability.
[Table of max heating power]
Split installation Most common for all air/air cooling machines

===== Page 35 =====

From heat pumps to cooling machines Refrigerants
Used so far
| Components / Group | Boiling point (°C) | GWP100 | Safety class | Typical application |
|--------------------|--------------------|--------|--------------|---------------------|
| R134a (HFC) | -26.3 | 1430 | A1 | Car air-conditioner, Distribution systems |
| R410A (R125/R32) | -51.7 | 2088 | A1 | Air-conditioner, Chillers |
| R404A (R143a/R125/R134a) | -46.5 | 3922 | A1 | Commercial coolers and freezers, Medium-temperature cooling |
| R508A (R23/R116) | -84.9 | 613396? | A1 | Low-temperature cooling, Quick freezers |
| Ammonia (nat. ref) | -33.5 | 0 | B2L | Industrial chillers |
| Isobutane (nat. ref) | -12.0 | 4 | A3 | Domestic refrigerators |
| Propane (nat. ref) | -42.1 | 3 | A3 | Domestic refrigerator and freezers |

===== Page 36 =====

From heat pumps to cooling machines Refrigerants
Replacement refrigerants, some examples
[Image: R1234yf (HFO) GWP=4 A2L]
[Image: R32 (HFC) GWP=675 A2L]
R444B (HFC/HFO) GWP=295 A2L
[Image: R1234ze (HFO) GWP<1 A2L]
R455A (HFC/HFO) GWP=148 A2L
Low-GWP refrigerants have efficiency drawbacks and are flammable. Refrigerants for low-temperature cooling with a small GWP are still problematic, e.g., R473A → GWP=1830

===== Page 37 =====

CO2 as refrigerant
• Not flammable
• GWP = 1
• ODP = 0
• Low normal boiling point
• Not toxic
• Cheap
• Available everywhere

===== Page 38 =====

CO2 as refrigerant
[Same list]
High pressure ratios, Large compressor outlet temperatures, Critical temperature of T_c = 31°C
Performance strongly depends on the climate

===== Page 39 =====

COP of CO₂ cycles as function of ambient T

===== Page 40 =====

COP of CO₂ cycles as function of ambient T

===== Page 41 =====

CO2 as refrigerant
[Same list]
[Image: Map of Europe showing regions]
Cold regions: Performs well
Medium and hot regions: T_c too small for an efficient subcritical cycle, T_c too large for an efficient transcritical cycle

===== Page 42 =====

CO2 as refrigerant
[Same list]
[Image: Same map]
Cold regions: Performs well
Medium and hot regions: T_c too small for an efficient subcritical cycle, T_c too large for an efficient transcritical cycle

===== Page 43 =====

Supermarket refrigeration

===== Page 44 =====

1 [Images: supermarket, refrigeration equipment]

===== Page 45 =====

Supermarket refrigeration CO2 booster cycle
[Image: Flow sheet of CO2 booster cycle]

===== Page 46 =====

Supermarket refrigeration CO2 booster cycle
[Image: Same flow sheet]

===== Page 47 =====

Supermarket refrigeration CO2 / X cascade cycle
[Image: Flow sheet of cascade cycle]
Common refrigerant cycle

===== Page 48 =====

The cycle with the common refrigerant generates a heat sink (e.g., at 20°C) for the CO2-cycle and rejects heat to the ambient. The CO2-cycle is much more efficient.
Common refrigerant cycle [diagram]

===== Page 49 =====

Programming and numerics Fitting routines and solvers

===== Page 50 =====

How to get data into Python?
[Image: Diagram of data import]

===== Page 51 =====

How to get data into Python? numpy.loadtxt
[Image: Code example]
Filename: data1.txt, File is in same path as Python file
Specified path

===== Page 52 =====

How to get data into Python? numpy.loadtxt
[Image: Code example with more options]

===== Page 53 =====

7
[Image: Graph of discrete data points]
Often, we have discrete data points but need values in between or mathematical continuous functions

===== Page 54 =====

Data fitting scipy.interpolate: Library including interpolation routines
[Image: Code example]

===== Page 55 =====

Data fitting scipy.interpolate: Library including interpolation routines
[Image: Code example]
Beware!
- Interpolation does not provide a continuous function
- Partly problematic for numerical integration
- Poor accuracy when few data points are available

===== Page 56 =====

Data fitting numpy.polyfit: A routine to fit polynomials to x,y data
[Image: Graph of polynomial fit]
Polynomial of third degree
[Image: Coefficients]

===== Page 57 =====

Data fitting numpy.polyfit: A routine to fit polynomials to x,y data
[Image: Code example]
To get values write a function or use poly1d

===== Page 58 =====

Data fitting numpy.polyfit: A routine to fit polynomials to x,y data
[Image: Code example]
Degree of polynomial: 1: y=a0+a1*x, 2: y=a0+a1*x+a2*x^2, 3: y=a0+a1*x+a2*x^2+a3*x^3, n: ...
polyfit provides a continuous function. But: You need to know whether your data can be described by a polynomial. You have to choose a suitable degree. Usually, polynomials of higher degree are more flexible, but you can run into overfitting. Oscillations between the points. Always check the result of the fit!

===== Page 59 =====

Data fitting scipy.optimize.curve_fit
A routine to fit coefficients of any mathematical function to data.
Limits of the parameters to fit: scipy.optimize.curve_fit(function_name, x_data, y_data, bounds=(-inf, inf))
def function_name(x,a0,a1,a2): y= ...f(x,a0,a1,a2) return y
The function must take the independent variable as the first argument and the parameters to fit as separate remaining arguments.

===== Page 60 =====

Data fitting scipy.optimize.curve_fit
[Image: Code example]

===== Page 61 =====

7
[Image: Graph of curve fit]
curve_fit provides a continuous function. But: You need to have an idea on which mathematical function is suitable to describe the data. Always check the result of the fit!

===== Page 62 =====

Root finding (simple solvers) scipy.optimize.fsolve

===== Page 63 =====

Root finding (simple solvers) scipy.optimize.fsolve
[Image: Code example]
We search for the x value, for which y=10. I guess the solution is 1.
Beware! fsolve always works with arrays, even though the function only depends on one variable. Input to function: [x_value], Result: [x_searched]

===== Page 64 =====

Introduction to this week’s exercise

===== Page 65 =====

In this exercise, you will help layout an air ventilation system for an office building.
The property manager of the building already has been made a lucrative offer by a compressor manufacturer and wants to use the compressor specified in the attached datasheet (RICM60S, 50Hz, pressure operation). For noise protection reasons, the compressor must be installed on the roof of the building. From the compressor outlet, the compressed air is intended to be transported through 200m of piping in the ventilation system. As the property manager is about to order 200m of air piping, he hesitates – what piping diameter should he choose?
a) For the given air ventilation system, plot the achievable volume flow rate V̇ as a function of the available pipe diameters from 5-50cm.
b) Use the data from the manufacturer to calculate the compressor power P_comp as a function of the pipe diameter and plot your results. Use both plots – What pipe diameter do you suggest to the property manager if the minimum required volume flow rate is 250 m³·h⁻¹.

===== Page 66 =====

Setup
[Image: Diagram of ventilation system]

===== Page 67 =====

Side channel blower
[Image: Graph of volume flow vs pressure difference]
[Image: Graph of blower power vs volume flow]
You need to fit this data!

===== Page 68 =====

Pressure losses in pipes Lockhart-Martinelli correlation
Pressure drop in pipe: Δp = 2 f (L/d) ρ c_m^2
- L: pipe length
- d: pipe diameter
- c_m: bulk velocity
- f: friction coefficient
- ρ: fluid density
Friction coefficient for gaseous fluids: f = K Re_d^{-m}
- K=0.079 and m=0.2 for laminar flow (Re_d < 2300)
- K=0.046 and m=0.25 for transitional/turbulent flow
Reynolds number: For a specific d_pip
- Volume flow V̇ of blower depends on Δp_pip
- Δp_pip depends on volume flow V̇
- ⇒ V̇ must be iterated
Re_d = (ρ c_m d)/μ = (V̇ ρ d)/(A μ)
- μ: dynamic viscosity
- A: cross-sectional area

===== Page 69 =====

Function (input: V̇)
- Calculate Re_d
- Calculate friction coefficient f
- Calculate Δp_pipe
- Calculate V̇_blower from Δp_pipe
- Return V̇_blower - V̇
Use fsolve to iterate V̇

---

# Lecture 11: Air-Conditioning

**Source: SHCT26_Lec11.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #11

Air-Conditioning

Lana Liebl Dr. Leon Brendel 13 May 2026

===== Page 2 =====

Topics of last week's lecture
Typical applications of cooling
Conditions of usual heat sinks and sources
From heat pumps to cooling machines - What is different?
CO2 for cooling processes
Supermarket refrigeration

===== Page 3 =====

Heat sinks and sources of cooling machines
[Image: Diagram]
The fluctuating part now!
| Application | T_evap |
|-------------|--------|
| Air-conditioning | +10 to 0°C |
| Food cooling (cold water) | 0 to -10°C |
| Food cooling (cold brine) | -10 to -35°C |
| Domestic freezers | -25°C |
| Food freezing | -35 to -55°C |
| Food quick freezing | -35 to -55°C |

===== Page 4 =====

Coefficient of performance Influence of subcooling
[Image: T-s diagram]
[Image: Graph of COP vs subcooling]
Subcooling should be exploited, as long as the condensation temperature must not be increased.

===== Page 5 =====

Supermarket refrigeration CO2 booster cycle
[Image: Photos of supermarket refrigeration]
[Image: Flow sheet]

===== Page 6 =====

The cycle with the common refrigerant generates a heat sink (e.g., at 20°C) for the CO2-cycle and rejects heat to the ambient. The CO2-cycle is much more efficient.

===== Page 7 =====

Topics of today's lecture
Fluid property model of moist air
Mollier's h* - X diagram
Balances for moist air
Challenges of air-conditioning

===== Page 8 =====

It's all about handling air!
[Images: air handling unit, fog, air conditioner, fogged windows]

===== Page 9 =====

Moist air

===== Page 10 =====

How much water can be dissolved in air?
[Image: Graph of water content vs temperature]
Max. content depends on temperature and pressure
[Image: Small diagram of floating]

===== Page 11 =====

How much water can be dissolved in air? Relative humidity
Relative humidity: φ(T,p) = dissolved water / max. solubility = x_water / x_water,max

===== Page 12 =====

How much water can be dissolved in air? Relative humidity
05/13/2026
Relative humidity: φ(T,p) = dissolved water / max. solubility = x_water / x_water,max = p_water / p_sat,water(T)
Partial pressures: p_air = x_air·p, p_water = x_water·p, x_air + x_water = 1
x: molar fraction
0 ≤ φ ≤ 1, dry air, saturated air

===== Page 13 =====

How much water can be dissolved in air? Relative humidity
[Image: Diagram of water vapor partial pressure]
Relative humidity: φ(T,p) = x_water/x_water,max
Ideal mixtures: A component behaves like the pure fluid at T and p_i (partial pressure)
Partial pressures: p_air = x_air·p, p_water = x_water·p, x_air + x_water = 1, x_air = 1

===== Page 14 =====

How much water can be dissolved in air? Relative humidity
[Image: Same diagram]
Relative humidity: φ(T,p) = dissolved water/max. solubility = x_water/x_water,max (dry air, saturated air)
Ideal mixtures: A component behaves like the pure fluid at T and p_i (partial pressure)
Water vapor starts condensing when the saturation pressure at T undercuts the water pressure (mixture → partial pressure)

===== Page 15 =====

How much water can be dissolved in air? Relative humidity

===== Page 16 =====

How much water can be dissolved in air? Relative humidity
[Image: Diagram]
Initial conditions: T=40°C, p=1 bar, φ=0.50
p_sat,water(40°C)=0.074 bar
p_water = φ·p_sat,water = 0.037 bar
p_air = p - p_water = 0.963 bar
As long as no water is added or removed, p_water and p_air are constant

===== Page 17 =====

How much water can be dissolved in air? Relative humidity
[Same as page 16]

===== Page 18 =====

Further variables to describe moist air Water content
[Image: Diagram]
For φ ≤ 1:
X = (M_water/M_air) · (p_sat,water(T))/(p/φ - p_sat,water(T)) = 0.622· p_sat,water(T)/(p/φ - p_sat,water(T))
Correlates the rel. humidity and the thermodynamic state (T,p) with the water mass per mass of air

===== Page 19 =====

Further variables to describe moist air Specific volume
We relate the Volume of moist air only to the air mass: v* = V_moist / m_dryair [m³_moistair/kg_dryair]
Ideal mixtures: A component behaves like the pure fluid at T and p_i (partial pressure). Because each component takes the entire volume.
We can calculate the Volume either from the air or the water: V_moist = V_dryair = V_water
V_dryair = m_dryair·ν_air(T,p_air)
V_water = m_water·ν_water(T,p_water)
p_water = φ·p_sat,water(T), p_air = p - p_water
v* = V_dryair/m_dryair = ν_air(T,p_air)
v* = (R_air·T)/p · (1 + X/0.622)

===== Page 20 =====

Further variables to describe moist air Enthalpy
Ideal mixture: H_moist air = H_air + H_water

===== Page 21 =====

Further variables to describe moist air Specific enthalpy (unsaturated)
H_moistair = H_air + H_water,vapor
H_moistair = m_air·h_air + m_water·h_water,vapor
We relate the enthalpy of moist air only to the air mass:
H_moistair = h_air + (m_water/m_air) h_water,vapor
h_moistair = h_air + X·h_water,vapor
Water content X = m_water/m_air

===== Page 22 =====

Further variables to describe moist air Specific enthalpy (oversaturated)
H'_moist air = H_air + H_water,vapor + H_water,liquid
h*_moist air = h_air + X(φ=1)·h_water,vapor + (X - X(φ=1))·h_water,liquid

===== Page 23 =====

We wrote a Fluid_CP_moist_air for you!

===== Page 24 =====

Fluid_CP_moist_air
[Image: Diagram of functions]
The reference points for the enthalpy are aligned!

===== Page 25 =====

Fluid_CP_moist_air Function: state_moist
[Image: Code snippet]
Possible inputs: "T","X"; "T","phi"; "T","h"; "X","phi"; "X","h"; "phi","h". The order doesn't matter.
Variables and units:
| Variable | Index | Unit |
|----------|-------|------|
| Temperature, T | "T" | °C |
| Water content, X | "X" | kg_water/kg_dry_air |
| Rel. humidity, φ | "phi" | - |
| Spec. enthalpy, h* | "h" | kJ_moist_air/kg_dry_air |
| Spec. volume, v* | "v*" | m³_moist_air/kg_dry_air |
Output: pandas data series, always containing [T, X, φ, h*, v*], Index: ["T","X","phi","h","v*"]

===== Page 26 =====

One diagram combines all variables Mollier diagram
[Image: Mollier diagram with enthalpy vs water content lines]

===== Page 27 =====

The Mollier diagram uses a skewed coordinate system

===== Page 28 =====

Three types of balances
05/13/2026
Inflows: Moist air, Pure water, Pure air. Outflows: Moist air, Pure water, Pure air. Q̇, P
Mass balance (dry air): dm_air/dt = Σ_in ṁ_air,i - Σ_out ṁ_air,i
Mass balance (water): dm_water/dt = Σ_in ṁ_water,i - Σ_out ṁ_water,i
Energy balance: dE/dt = Σ_in (ṁ_air,i·h_i* + ṁ_air,j·h_air,j + ṁ_water,j·h_water,j) - Σ_out (...) + Q̇ + P

===== Page 29 =====

Three types of balances
[Image: Diagram of control volume]
Mass balance (dry air) equation, Mass balance (water) equation
Energy balance equation

===== Page 30 =====

Challenges of air-conditioning
# We have to distinguish

===== Page 31 =====

What are comfortable conditions?
[Image: Diagram of office workplace]
Criteria: Temperature, Humidity, Flow velocity, Vertical temperature gradient, Quality of the air
Pleasant conditions for office workplaces (summer): 22 ≤ T ≤ 26°C, Rel. humidity φ_min=0.4, from 22°C → φ_max<0.65, from 24°C → φ_max<0.60, from 26°C → φ_max<0.55

===== Page 32 =====

Challenges of air-conditioning Flow velocity vs. temperature
[Image: Diagrams of room and air stream]
To increase the cooling capacity ⇒ increase temperature change ⇒ increase mass flow rate

===== Page 33 =====

Challenges of air-conditioning Flow velocity vs. temperature
[Image: Graphs]
To increase the cooling capacity ⇒ increase temperature change ⇒ increase mass flow rate

===== Page 34 =====

Challenges of air-conditioning Flow velocity vs. temperature
[Image: More graphs]

===== Page 35 =====

Challenges of air-conditioning Flow velocity vs. temperature
[Image: Graphs]
Cooling capacity (kW)
Even if you are not sitting directly under the stream, the air in the room is clearly moved. We always have to find a compromise. A minimum temperature change of approx. 10 K is needed to avoid high flow velocities.

===== Page 36 =====

Challenges of air-conditioning How to control temperature and relative humidity
What happens when moist air is cooled down? [diagram]

===== Page 37 =====

Challenges of air-conditioning How to control temperature and relative humidity

===== Page 38 =====

Challenges of air-conditioning Saturated air is uncomfortable
[Image: Diagram of room with saturated air]
Saturated air φ=1: Not comfortable conditions ⇒ Air cannot absorb water ⇒ Sweating is hardly possible ⇒ It feels wet
[Image: Diagram of air mixing]
Not a problem ⇒ Air is mixed with room air ⇒ Air is heated up ⇒ Humidity in the room < 1

===== Page 39 =====

Challenges of air-conditioning How to control temperature and relative humidity
[Image: Mollier diagram path]
Inefficient for the cooling cycle → smaller evaporation temperatures are required
Cool down further, Heating up again

===== Page 40 =====

Challenges of air-conditioning Usual process to control temperature and humidity
[Image: Diagram]

===== Page 41 =====

Challenges of air-conditioning Usual process to control temperature and humidity
[No additional text]

===== Page 42 =====

Challenges of air-conditioning How to control temperature and relative humidity
[Image: Diagram of recirculating air-conditioner]
Recirculating air-conditioners are not able to re-heat. Outlet air is saturated. But it is quickly mixed with the room air (heated up ⇒ undersaturated). Humidity in the room cannot be controlled. Final humidity depends on outlet T, room T, water added to room air (see this week's exercise).

===== Page 43 =====

Challenges of air-conditioning Dehumidification
[Image: Mollier diagram]
Even if the outlet stream is saturated, air-conditioners dry the room air.
Relative humidity ≠ water content! ⇒ The rel. humidity might increase ⇒ The water content always decreases

===== Page 44 =====

Challenges of air-conditioning Dehumidification
[Image: Mollier diagram]
Air to be cooled, Desired outlet conditions
Water content decreases, if the outlet temperature is below the saturation temperature of the inlet air

===== Page 45 =====

Resulting water content
[Image: Graph of room air cooling line]
The room air cools down along the mixing line until the desired temperature is reached. Then: air-conditioner in on/off operation. Room water content approaches water content of outlet air

===== Page 46 =====

Challenges of air-conditioning Dehumidification
[Image: Mollier diagram]
Why is it a problem?

===== Page 47 =====

As long as the room air is undersaturated, it can absorb water from our skin and mucosa (respiratory system, eyes etc.)
The potential for the mass transfer is the difference of partial densities → water on surface to water in the air
Water, e.g., on mucosa: ρ_muc(37°C, x=1) = 0.044 kg·m⁻³

===== Page 48 =====

Challenges of air-conditioning The problem of dry air
[Image: Diagram of human with dry air effects]
As long as the room air is undersaturated, it can absorb water from our skin and mucosa.
The potential for the mass transfer is the difference of partial densities.

===== Page 49 =====

Introduction to this week’s exercise

===== Page 50 =====

Task
[Image: Diagram of room with air-conditioner]
Evaluate the air temperature T_room, the water content X_room and the humidity φ in the room during one hour.
Initial conditions:
m_dryair,room = 60 kg, T_room(t=0)=30°C, φ_room(t=0)=0.55
Fluid_CP_moist_air
X_water,room(t=0), h*_room(t=0)
m_water,room(t=0) = X_water,room(t=0)·m_dryair,room

===== Page 51 =====

Mass balance dry air: dm_dryair,room/dt = 0
Mass balance water: dm_water,room/dt = -ṁ_water,out(t)
Energy balance: dh*_air,room/dt = ṁ_dryair·h*_AC(t) - ṁ_dryair·h*_air,room(t) + Q̇_in

===== Page 52 =====

Mass balance dry air: dm_dryair,room/dt = 0
Mass balance water: dm_water,room/dt = -ṁ_water,out(t)
Energy balance: dh*_air,room/dt = ṁ*_dryair·h*_AC(t) - ṁ*_dryair·h*_air,room(t) + Q̇_in
Given values

===== Page 53 =====

Balances of the room
Mass balance dry air: dm_dryair,room/dt = 0
Mass balance water: dm_water,room/dt = -ṁ_water,out(t)
[Image: Diagram of room with air-conditioner (recirculation)]
Given values

===== Page 54 =====

Mass balance dry air: ṁ_dryair = const.
Mass balance water: 0 = -ṁ_water,out(t) - ṁ_water,AC(t) + ṁ_water,room(t)
⇒ 0 = -ṁ_water,out(t) - X_AC(t)·ṁ_dryair + X_room(t)·ṁ_dryair
[Image: Small diagram]
Two cases:
Case 1: X_room > X(T_AC, φ=1) → water condenses → Outlet state at T_AC and φ=1
Case 2: X_room ≤ X(T_AC, φ=1) → no water condenses → Outlet state at T_AC and X_room

---

# Lecture 12: Ultra-Low Temperature and Cryogenic Cooling

**Source: SHCT26_Lec12.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #12

Ultra-low temperature and cryogenic cooling

Lana Liebl Dr. Leon Brendel 20 May 2026

===== Page 2 =====

Topics of last week's lecture
Fluid property model of moist air
Mollier's h* - X diagram
Balances for moist air
Challenges of air-conditioning

===== Page 3 =====

It's all about handling air!
[Images: air handling unit, fog, air conditioner, fogged windows]

===== Page 4 =====

Properties to describe moist air
Relative humidity: φ(T,p) = dissolved water/max. solubility = x_water/x_water,max = p_water/p_sat,water(T)
Water content: X = 0.622·(p_sat,water(T))/(p/φ - p_sat,water(T))
Specific volume: v* = (R_air·T)/p · (1 + X/0.622)
Specific enthalpy: h*_moist air = h_air + X·h_water,vapor

===== Page 5 =====

One diagram combines all variables Mollier diagram
[Image: Mollier diagram]

===== Page 6 =====

Challenges of air-conditioning How to control temperature and relative humidity
[Image: Mollier diagram path]
Inefficient for the cooling cycle → smaller evaporation temperatures are required
Cool down further, Heating up again

===== Page 7 =====

Challenges of air-conditioning Dehumidification
[Image: Mollier diagram]
[Image: Small diagram]
Why is it a problem?

===== Page 8 =====

Challenges of air-conditioning The problem of dry air
As long as the room air is undersaturated, it can absorb water from our skin and mucosa (respiratory system, eyes etc.)
The potential for the mass transfer is the difference of partial densities → water on surface to water in the air
Water, e.g., on mucosa: ρ_muc(37°C, x=1) = 0.044 kg·m⁻³
[Image: Graph of water content vs relative humidity]

===== Page 9 =====

Topics of today's lecture
Processes for ultra-low temperature cooling
- Cascade cycles
- Autocascade cycles
Cryogenic cooling via cold media (e.g., liquified gases)
Production of liquified gases
Storage of liquified gases
On-site reliquefication

===== Page 10 =====

Cooling by temperature ranges

===== Page 11 =====

Ultra-low temperature cooling Applications
Most applications are from biology and medicine
[Image: Vaccine storage, blood banks, forensic labs]
E.g., Covid-19 vaccine storage, blood banks, forensic labs for long-term evidence storage, establishing performance specs for parts used in extreme environments
[Image: Process engineering applications]
But also important for process engineering: Synthesis, Crystallization

===== Page 12 =====

Ultra-low temperature cooling Processes
[Image: Cascade cycle diagram]
Cascade vapor-compression cooling cycles
Refrigerant for usual cooling applications, ⇒ large critical temperature e.g., R1234ze, R455A
Special refrigerant ⇒ small normal boiling points
| Components / Group | T_ev,min (°C) |
|--------------------|---------------|
| R508A (R23/R116) | -84.9 |
| R23 | -82.3 |
| CO2 | ≈ -50.0 |

===== Page 13 =====

Ultra-low temperature cooling Processes
[Image: Cascade cycle with two stages]
Cascade vapor-compression cooling cycles
Refrigerant for usual cooling applications, e.g., R1234ze, R455A
Special refrigerant [table]

===== Page 14 =====

Ultra-low temperature cooling Processes
[Image: Autocascade cycle diagram]
Autocascade vapor-compression cooling cycles → Ultra-low temperatures with only one compressor
Refrigerant: Mixture of low and high boiling fluids

===== Page 15 =====

Ultra-low temperature cooling Processes
[Image: Autocascade cycle]
Autocascade vapor-compression cooling cycles → Ultra-low temperatures with only one compressor
Refrigerant: Mixture of low and high boiling fluids
Only two pressure levels: Low pressure, High pressure

===== Page 16 =====

Ultra-low temperature cooling Processes
[Image: Same diagram]
Autocascade → only one compressor
Refrigerant: Mixture of low and high boiling fluids
Only two pressure levels. But three mixture compositions: Initial composition, Low boiling composition, High boiling composition

===== Page 17 =====

Ultra-low temperature cooling Processes
[Image: Autocascade cycle with separator]
Autocascade → Ultra-low temperatures with only one compressor
How is the mixture separated? Refrigerant is not fully condensed (state 3). Gas and liquid phase are separated.
[Image: Enlarged separator detail]
The vapor phase (state 4) contains more of the low-boiling fluid

===== Page 18 =====

Ultra-low temperature cooling Processes
[Image: Same diagram]
Autocascade → only one compressor
How is the mixture separated? Refrigerant is not fully condensed (state 3). Gas and liquid phase are separated.
The mixture flowing through the evaporator has a lower boiling point than the initial mixture

===== Page 19 =====

Ultra-low temperature cooling Processes
[Image: Same diagram]
Autocascade → only one compressor
What is the trick now?
The mixture that is condensed has a high boiling point → large critical temperature → efficient, subcritical process
The mixture that is evaporated has a low boiling point → small evaporation temperatures at p>1 bar possible

===== Page 20 =====

Cryogenic cooling Applications
[Images: Cryogenic milling, Cryogenic shrink-fitting, Preservation (biology, medicine), Drug synthesis]

===== Page 21 =====

1 [Images: LNG, MRI, Particle accelerator]
Liquefication of natural gas, MRI, Particle accelerator

===== Page 22 =====

Cryogenic cooling is mostly processed by cold media
| Medium | Sublimation point at 1 bar |
|--------|---------------------------|
| CO2-ice | 194.75 K |
| Medium | Boiling point at 1 bar |
| Oxygen | 90.18 K |
| Argon | 84.24 K |
| Air | 78.8 K |
| Nitrogen | 77.09 K |
| Helium | 4.21 K |
[Image: Photo of liquid nitrogen]

===== Page 23 =====

Cryogenic cooling is mostly processed by cold media

===== Page 24 =====

1 [Images: Air separation plant, tank truck supply, liquid nitrogen handling]

===== Page 25 =====

1 [Image: Liquid nitrogen tank]
- T = T_sat(ρ)
- Tank is insulated ⇒ but heat transfer cannot be avoided totally
- Cooling (keeping T) is realized by evaporating and blowing-off a small share of the medium
ṁ_loss = Q̇_in/Δh_evap(p) = (1/R·(T_amb - T))/Δh_evap(p)
Typical values: 0.2 - 0.6 %/d

===== Page 26 =====

Joule-Thompson effect
[Image: Diagram of throttling]
Isenthalpic throttling
It describes the temperature change of a real gas or liquid when it is isenthalpic throttled (pressure decrease)
μ > 0 → Temperature decreases, μ < 0 → Temperature increases

===== Page 27 =====

The Joule-Thompson coefficient depends on temperature and pressure.
Usually, a fluid has temperature ranges with positive and negative values of μ. The temperature at which μ changes is called inversion temperature.
μ > 0 → Temperature decreases, μ < 0 → Temperature increases

===== Page 28 =====

0.5 0.4 0.3 0.2 0.1 0 -0.1 0 100 200 300 400 500 600 700 800 900 1000 Temperature (K)
The effect is very small
At ambient temperature: Nitrogen, Argon, Carbon dioxide have μ>0 (T decreases); Helium, Hydrogen have μ<0 (T increases)

===== Page 29 =====

Ideal gas law does not account for Joule-Thompson effect
Joule-Thompson coefficient: μ = (∂T/∂p)_h
Temperature change due pressure change at constant enthalpy
Ideal gas enthalpy change: dh = c_p(T)·dT → No temperature change ⇒ no enthalpy change
Joule-Thompson effect comes from intermolecular interactions that are not covered by ideal gases ⇒ A more realistic property model is needed, e.g. cubic equations of state

===== Page 30 =====

7 5 200 bar 200 bar ... Still a gas!
[Image: Hampson-Linde cycle diagram with temperatures]

===== Page 31 =====

Hampson-Linde cycle Air
05/20/2026
[Image: Cycle diagram with states and temperatures]
Ambient air: T1=25°C, p1=1 bar, p2=200 bar, T3=25°C, p3=200 bar, T4=-9.79°C, p4=1 bar → Still a gas!
With precooling: T4=-140°C, p4=200 bar, T5=-193°C, p5=1 bar, x5=0.56

===== Page 32 =====

Hampson-Linde cycle Air (continued)
[Same as page 31]

===== Page 33 =====

Hampson-Linde cycle Helium
05/20/2026
Ambient air, Helium: T1=25°C, p1=1 bar, p2=200 bar, T3=25°C, p3=200 bar, T4=+37.34°C, p4=1 bar
Inversion temperature << 25°C → Helium gets warmer

===== Page 34 =====

Hampson-Linde cycle Helium
[Image: Cycle diagram]
Which conditions are needed to achieve a cooling effect?

===== Page 35 =====

Hampson-Linde cycle Helium
[No additional text]

===== Page 36 =====

Reverse-Brayton cycle
[Image: Cycle diagram and T-s diagram]
Compression work is partly recuperated. Also fluids with μ<0 can be cooled.
Not suitable for liquification. State 4 must be superheated. Second process needed. Additional turbine required.

===== Page 37 =====

Claude-cycle
[Image: Cycle diagram]
Combination of Hampson-Linde and reverse-Brayton cycle

===== Page 38 =====

Claude-cycle
[Image: Same diagram]
Hampson-Linde cycle [indicated]

===== Page 39 =====

Claude-cycle
[Image: Same diagram]
Combination of Hampson-Linde and reverse-Brayton cycle. Brayton part is used to precool the gas in the Hampson-Linde cycle. Pressure recuperation. Lower pressure ratios required than for Hampson-Linde.

===== Page 40 =====

1 [Images: Air separation plant, tank truck supply, liquid nitrogen handling]

===== Page 41 =====

The coils of the electromagnets must be cooled to around 4 K to make them superconducting
[Image: MRI machine]
[Image: Diagram of MRI cooling]
Liquid helium. Typically, 1700 liters.

===== Page 42 =====

Cooling scheme of a MRI
[Image: Detailed diagram of MRI cooling system]

===== Page 43 =====

Gifford-McMahon (GM) cycle Cryo-cooler for small cooling capacities
[Image: Cycle diagram]
Cold head

===== Page 44 =====

Gifford-McMahon (GM) cycle
[Image: Cycle diagram]
[Image: Detailed cold head diagram]
Cold head

===== Page 45 =====

Gifford-McMahon (GM) cycle
[Image: Cycle diagram]
[Image: PV diagram]
Helium is partly removed, remaining gas expands. Isothermal → heat is taken up

===== Page 46 =====

Cooling scheme of a MRI
[Image: Diagram of MRI with cooling stages]
What happens if one part of the cooling chain fails?
Helium is heated up (can happen very quickly). Coils lose superconductivity (getting extremely hot). MRI can no longer be used. Helium expands ⇒ MRI would be destroyed. Last option: quenching (total blow-off).
[Image: Chiller diagram]

===== Page 47 =====

Total blow-off
https://www.youtube.com/watch?v=9SOUJP5dFEq
MRI often require up to 1800 L Helium. Current Helium price is approx. 45 US$/L → Total blow-off costs min. 81000 US$

---

# Lecture 13: Niche Technologies – Oral Exams

**Source: SHCT26_Lec13.pdf**

===== Page 1 =====

Sustainable Heating and Cooling Technologies #13

Niche Technologies Oral exams

Lana Liebl Dr. Leon Brendel 27 May 2026

===== Page 2 =====

Topics of last week's lecture
Processes for ultra-low temperature cooling
- Cascade cycles
- Autocascade cycles
Cryogenic cooling via cold media (e.g., liquified gases)
Production of liquified gases
Storage of liquified gases
On-site reliquefication

===== Page 3 =====

Ultra-low temperature cooling
[Image: Cascade cycle diagram]
Cascade vapor-compression cooling cycles
Refrigerant for usual cooling applications, ⇒ large critical temperature e.g., R1234ze, R455A
Special refrigerant ⇒ small normal boiling points
| Components / Group | T_ev,min (°C) |
|--------------------|---------------|
| R508A (R23/R116) | -84.9 |
| R23 | -82.3 |
| CO2 | ≈ -50.0 |

===== Page 4 =====

Ultra-low temperature cooling Processes
[Image: Autocascade cycle diagram]
Autocascade vapor-compression cooling cycles → Ultra-low temperatures with only one compressor
How is the mixture separated? Refrigerant is not fully condensed (state 3). Gas and liquid phase are separated.
[Image: Separator detail]
The mixture flowing through the evaporator has a lower boiling point then the initial mixture

===== Page 5 =====

1 [Images: Air separation plant, tank truck supply, liquid nitrogen handling]

===== Page 6 =====

Joule-Thompson effect
[Image: Diagram of throttling]
Isenthalpic throttling
It describes the temperature change of a real gas or liquid when it is isenthalpic throttled (pressure decrease)
Joule-Thompson coefficient: μ = (∂T/∂p)_H
μ>0 → Temperature decreases, μ<0 → Temperature increases

===== Page 7 =====

Hampson-Linde cycle Air
05/27/2026
[Cycle diagram with states]
Ambient air: T1=25°C, p1=1 bar, p2=200 bar, T3=25°C, p3=200 bar, T4=-9.79°C, p4=1 bar → Still a gas!
With precooling: T4=-140°C, p4=200 bar, T5=-193°C, p5=1 bar, x5=0.56

===== Page 8 =====

Claude-cycle
[Image: Cycle diagram]
Combination of Hampson-Linde and reverse-Brayton cycle. Brayton part is used to precool the gas in the Hampson-Linde cycle. Pressure recuperation. Lower pressure ratios required than for Hampson-Linde.
Hampson-Linde cycle [indicated]

===== Page 9 =====

Topics of today's lecture
[Image: Icons for different niche technologies]
What we have dealt with so far
# Today:
- Electrical → thermoelectric
- Magnetic → magnetocaloric
- Chemical → electrochemical
- Thermal → adsorption, absorption
Niche technologies are mostly described as cooling cycles.
But don't forget: Every cooling cycle is a heat pump

===== Page 10 =====

Absorption cooling cycle
Uses a binary mixture (solution) of a refrigerant (e.g., ammonia) and solvent (e.g., water)
For one pressure: The refrigerant has a lower boiling point, evaporates first. The boiling point of the mixture is a function of composition. A condensation can be achieved just by adding water.
[Image: T-x diagram of mixture]
Changing the pressure shifts the lines

===== Page 11 =====

Absorption cooling cycle
[No additional text]

===== Page 12 =====

Absorption cooling cycle
[Image: Flow sheet of absorption cycle]
Distillation column, Heat exchanger, Pump, Absorber

===== Page 13 =====

Absorption cooling cycle
[Image: Same diagram with labels]

===== Page 14 =====

Absorption cooling cycle
[Image: Same diagram]

===== Page 15 =====

Absorption cooling cycle
[Image: Same diagram]

===== Page 16 =====

Absorption cooling cycle
[Image: Same diagram]

===== Page 17 =====

Absorption cooling cycle
[No additional text]

===== Page 18 =====

Absorption cooling cycle
[No additional text]

===== Page 19 =====

Absorption cooling cycle
[No additional text]

===== Page 20 =====

1 What is the trick now?
Vapor-compression: compression step requires pure exergy (e.g., electricity)
Absorption cycle:
- Ab- and desorption change the phase that only a pump is required
- Only pump requires electricity → much less work
- Most energy is added as heat ( → waste heat can be used)

===== Page 21 =====

Absorption cooling cycle
Less electrical energy required. Can be driven by heat (waste heat, power-to-heat, gas-to-heat). Heating mode can be switched. Low temperature cooling (ammonia).
If electrically heated, lower COPs than vapor-compression. Sluggish system. Harmful fluids (ammonia, lithium bromide). High investment costs.
[Image: Photo of large absorption chiller at Roche, 2 MW thermal]

===== Page 22 =====

Adsorption cooling cycle What is adsorption?
Adsorption: Adsorption is the adhesion of atoms, ions or molecules from a gas, liquid or dissolved solid to a surface. Reverse process: desorption.
Adsorption: exothermic process, Desorption: endothermic process

===== Page 23 =====

Adsorption cooling cycle Working principle

===== Page 24 =====

Adsorption cooling cycle Working principle
[Image: Flow sheet of adsorption cycle]
Adsorbent and refrigerant must fit together. Adsorption cooling cycle is a discontinuous process.

===== Page 25 =====

Adsorption cooling cycle Working principle
[Image: Cycle diagram - Step 1]
Step 1: Starting point: Evaporator is filled with water at T_amb and p_sat(T_amb), Adsorbent is unloaded. Operations: Valve 1 is opened, Water evaporates and is adsorbed by the adsorbent, The adsorbent is cooled, e.g., by ambient air. Effects: Water in the evaporator takes heat (useful cooling), The adsorbent is heated up due to the exothermic process.

===== Page 26 =====

Adsorption cooling cycle Working principle
[Image: Step 2 diagram]
Step 2: Starting point: The adsorbent is loaded and warm. Operations: Both valves are closed. The adsorbent is heated up by high-temperature heat (energy input, e.g., by waste heat). Effects: Pressure increases up to p_sat(T_con). Load of the adsorbent stays nearly constant.

===== Page 27 =====

Adsorption cooling cycle Working principle
Q to ambient, Step 3, Condenser, Valve 2, Throttle, Q_in, Valve 1, Evaporator
Valve 2 is opened. Adsorbent is heated. Water is desorbed from the adsorbent. Effects: Water (-vapor) flows in the condenser and condenses. Is then expanded to p_ev and flows back to the evaporator.

===== Page 28 =====

Adsorption cooling cycle Working principle
[Image: Step 4 diagram]
Step 4: Starting point: The adsorbent is unloaded but still hot (p_sat(T_con)). Operations: Both valves are closed. The adsorbent is cooled down. Effects: The pressure of the adsorbent decreases to p_ev. The cycle starts from the beginning.

===== Page 29 =====

Adsorption cooling cycle
[Image: Condenser diagram]
No electrical energy required. Can be driven by heat (waste heat, power-to-heat, gas-to-heat). Heating mode can be switched.
If electrically heated, lower COPs than vapor-compression. Discontinuous process. High mass due to the adsorbent. Cooling temperature mostly limited (water >0°C)

===== Page 30 =====

1
[Image: Same diagram]
No electrical energy required. Can be driven by heat. Heating mode can be switched.
If electrically heated, lower COPs than vapor-compression. Discontinuous process. High mass due to the adsorbent. Cooling temperature mostly limited (water >0°C)

===== Page 31 =====

The Peltier-effect
- is one of the thermoelectric effects
- is the inversion of the Seebeck-effect
[Image: Diagram of Peltier element]
At the contact point of two current-carrying conductors made of different materials, cooling or heating occurs.
The heat flow rate depends on the materials and the current: Q̇ = (Π1 - Π2)·I
Peltier-coefficients: Q̇<0 → contact point cools down, Q̇>0 → contact point is heated up

===== Page 32 =====

0

===== Page 33 =====

0
[Image: Diagram of Peltier cooler]
COP_C = Q̇_low/P
typically, COP_Peltier ≈ (1/15)·COP_Vapor-compression
Major losses:
- Joule heating in the conductors
- Parasitic heat flow rate from the hot to the cold side
- Good electron conductors are also good heat conductors
Typical cooling capacity: 1.5 - 2.5 W/cm²

===== Page 34 =====

Peltier cooler advantages:
- Compact construction
- No moving parts
- No noise emissions
- No vibrations
- Exact temperature adjustment
- Small cooling capacities possible
[Image: Photo of Peltier element]

===== Page 35 =====

Magnetocaloric cooling Magnetocaloric effect

===== Page 36 =====

Magnetocaloric cooling Magnetocaloric effect
[Image: Diagram of magnetic material with and without field]
(T1 - T0)_ad = -∫_{H0}^{H1} (T/C)_H (∂M/∂T)_H dH
T: temperature, C: heat capacity, H: applied magnetic field, M: magnetization

===== Page 37 =====

Magnetocaloric cooling Process

===== Page 38 =====

Magnetocaloric cooling
[Image: Diagram of magnetocaloric device]
Typically, COP ≈ 30 – 60% of vapor-compression COP
Compact construction, No harmful refrigerants, Good COPs, Very low temperatures possible (stacks)
High investment costs, Requires rare materials, Discontinuous process, Strong magnetic fields

===== Page 39 =====

Electrochemical cooling cycle Greetings from science

===== Page 40 =====

Electrochemical cooling Modeling and optimization
[Image: Diagram of electrochemical cell]
Equilibrium-based cell model. Composition optimization for each molecule pair. Large-scale screening: 5633 molecule pairs.

===== Page 41 =====

Evaluation of electrochemical cooling in case study Composition optimization with equilibrium-based cell model
[Image: Graphs of COP vs current density]

===== Page 42 =====

Evaluation of electrochemical cooling in case study Composition optimization with equilibrium-based cell model
[Image: Same graphs]
Process efficiency is strongly molecular-pair dependent. 35 particularly promising molecule pairs (COP > 4.0). Electrochemical cooling potentially outperforms vapor-compression systems.
[Table of promising molecule pairs with COP values]
Benchmark: R410A, superheating: 5K, ηs: 0.52 - 0.63 → COP 3.8 - 4.7
Lieb L, Bardow A, Roskosch D: Indirect Electrochemical Cooling: Model-Based Performance Analysis and Working Fluid Selection. Ind Eng Chem Res 2024;63(2):1055-65.

===== Page 43 =====

0.0 0.2 0.4 0.6 0.8 1.0 100 0.0 0.2 0.4 0.6 0.6 0.8 1.0 100 0.0 5 10 15 20 25 Material COP -| Material COP -| Magnetocaloric VaporCompression Thermoelectric Brayton Stirling Electrocaloric Elastocaloric
S. Qian et al., International Journal of Refrigeration, 2016

===== Page 44 =====

Information on the oral exams

===== Page 45 =====

Oral exam General remarks
- Individual exam → no groups
- Time frame: approx. 30 min
- Period: Aug. 03 - Aug. 28
- Concrete appointments are still to be defined
- You will get an appointment via myStudies
- Passing the semester projects is mandatory for the admission
- The oral exam counts as 50% of the final grade
Office hour student project: May 27: HG E 19 (02:15 - 03:45 p.m.), Jun 11: ML J 13.2 (10:30-11:30 a.m.)
Content and objectives:
- We will talk minimum 15 min. about the semester projects
- Objective: Figuring out if you actively participated in the group work. Have you rethought your work related to our comments?
- The remaining <15 min., we will ask you questions about the lecture content and perhaps we will give you short tasks.

===== Page 46 =====

Lecture topics
| Lecture | Topics |
|---------|--------|
| L1 | Introduction Simple heat pump model |
| L2 | Fluid property models |
| L3 | Heat sources and sinks Pinch model |
| L4 | Components #1: Heat exchanger |
| L5 | Components #2: Expansion valves Transcritical process |
| L6 | Components #3: Compressors Advanced flowsheets |
| L7 | Refrigerants |
| L8 | Controlling Residential heating |
| L9 | High-temperature industrial heat pumps |
| L10 | Cooling – everything different now? |
| L11 | Air-conditioning |
| L12 | Low-temperature and cryo cooling |
| L13 | Niche technologies |

===== Page 47 =====

1
Please give us a short review on the problem, your solving approach and the results. Why did you assume XY? Why do you think it is justified? Would it not have been better to assume XZ? How do your results change if ... happens? Questions about the lecture content that come across → "Why decreases a compressor on/off controlling the COP?" How did you perform the calculations in code?

===== Page 48 =====

Oral exam What kind of answers do we expect?
We are not interested in precise numbers!
Example: EPSE: "What are typical minimum approach temperatures?" Student: "Maybe up to 20 K. But it depends" EPSE: "On what does it depend?"

===== Page 49 =====

Possible questions

===== Page 50 =====

Please note!
The questions do not add up to a complete list of possible questions. These are only examples to give you a feeling about the nature of the questions we might ask.

===== Page 51 =====

Topics: Introduction to heating and cooling Simple heat pump model
Typical questions:
- Why are heat pumps an important future technology?
- How does a heat pump cycle work?
- What is in thermodynamics the difference between heating and cooling?
- How is the efficiency of a heat pump / cooling cycle defined?
- How efficient can such cycles be?
- What limits the efficiency?
- Which variables must be set to calculate a heat pump process?

===== Page 52 =====

Topics: Fluid property models
Typical questions:
- Which fluid properties are usually required for a process calculation?
- What is the difference between an equation of state and a fundamental equation?
- What is the difference between PC-SAFT and a cubic equation of state?
- Which fluid property model should we prefer?
- For which conditions does the ideal gas law provide good results and for which does it not?
- Can we calculate a heat pump process only with the ideal gas law?

===== Page 53 =====

Topics: Heat sources and sinks, Pinch model
Typical questions:
- What are possible heat sources of heat pumps?
- How do the heat sources differ?
- What are specifications of the respective heat sources?
- How does the heat source influence the process?
- What are typical heat sinks of residential heat pumps?
- How does the heat sink influence the process?
- Pinch-model: What is it good for? How is it used? What are typical minimum approach temperatures?

===== Page 54 =====

Topics: Heat exchanger
Typical questions:
- On what does the heat transfer in a heat exchanger depend?
- What are typical values of the heat transfer coefficients?
- Which types of flow arrangements exist?
- What are advantages and disadvantages of the flow arrangements?
- Which types of heat exchangers are commonly used for heat pumps?
- What is the moving boundary approach?
- What is the freezing problem?
- How does freezing influence the process?
- What are the options for defrosting?

===== Page 55 =====

Topics: Expansion valves Transcritical processes
Typical questions:
- Why is it justified to assume an isenthalpic state change for expansion valves?
- Is the state change in the expansion valve reversible?
- Why is an expander not used instead of an expansion valve?
- Which types of expansion valves exist?
- How do they work? How can they be controlled? For which processes are they usually used? What are advantages and disadvantages?
- What are transcritical processes ⇒ advantages / disadvantages

===== Page 56 =====

Topics: Compressors, Advanced flowsheets
Typical questions:
- Why is the compressor so important for the performance of the entire process?
- What is the best compressor thermodynamically?
- What are typical losses of compressors?
- Which efficiencies are commonly used to describe the performance of a compressor?
- How are the efficiencies used in process simulations?
- What are typical values of compressor efficiencies? On what do they usually depend?
- Which types of compressors exist? How do they differ?
- What is the difference between hermetic, semi-hermetic, and open compressors?
- What is an internal heat exchanger? How can it improve the COP?

===== Page 57 =====

Topics: Refrigerants
Typical questions:
- What are typical requirements of refrigerants?
- Please give a short summary of the history of refrigerants (from the beginning until today)
- Which molecules have been used? Which problems are connected to the respective molecules (groups)? Why have they been replaced? Where do we stand today?
- Why are flammable refrigerants a problem?
- Which advantages do refrigerant mixtures with temperature glide have?

===== Page 58 =====

Topics: Controlling, Residential heating
Typical questions:
- What are usual controlling options of heat pump processes?
- What happens when the orifice of the expansion valve is changed?
- How can the condensation temperature be influenced?
- When does the process become unstable?
- Which controlling options exist to meet a certain heat demand?
- What are advantages and disadvantages?
- What is the difference between a mixed and a stratified water storage tank?
- How does the type of water storage tank influence the heat pump process?

===== Page 59 =====

Topics: High temperature and industrial heat pumps
Typical questions:
- Why are high-temperature heat pumps so important for our future energy system?
- Which temperatures do market-available heat pumps currently achieve?
- What are perspectives and limits regarding the maximum temperature?
- Which special requirements do high-temperature heat pumps have on refrigerants?
- Why is it difficult to find suitable refrigerants?
- Which concepts allow for circumventing the refrigerant problem (→ cascade, transcritical cycle)
- Why is steam production so important but challenging for heat pumps?
- What is the vapor re-compression cycle?

===== Page 60 =====

Topics: Cooling: Everything different now?
Typical questions:
- What are typical cooling applications?
- What are typical heat sources and sinks?
- How do the process temperatures of cooling cycles differ from those of heat pumps?
- Why are the COPs of cooling cycles smaller than those of heat pumps?
- Why is subcooling important?
- What are advantages and disadvantages of CO2 as refrigerant?

===== Page 61 =====

Topics: Air-conditioning
Typical questions:
- Which states can moist air have?
- Which variables are commonly used to describe the state of moist air?
- What are comfortable air conditions (room and stream)
- Why is the outlet flow of an air-conditioner usually saturated?
- How can the humidity of the outlet flow be decreased?
- Why does an air-conditioner dry the room air?
- Why is too dry air uncomfortable for us?

===== Page 62 =====

Topics: Ultra-low temperature and cryogenic cooling
Typical questions:
- What are usual applications of ultra-low temperature cooling?
- Why is it challenging to find suitable refrigerants?
- How can the refrigerant problem be circumvented?
- What is an autocascade cycle?
- What are typical applications of cryogenic cooling?
- How is cryogenic cooling mostly realized?
- What is the supply chain of liquified gases?
- How are liquified gases stored? How is the temperature kept?
- What is the Joule-Thompson effect? What is the inversion temperature?

===== Page 63 =====

Topics: Niche technologies
Typical questions:
- Which alternative cooling (heat pump) technologies do you know?
- How do the processes work?
- What are advantages and disadvantages of the technologies?

---

*End of extracted lecture content.*