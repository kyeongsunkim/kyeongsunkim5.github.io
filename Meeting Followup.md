
# 일정: 
1. 제안서 due 2/27
2. 발표 3월 中
3. 과제 시작 5월
- - -

# 할일:
1. 한전 실증 건설 검색
2. Study Questions
- - -

# Question 1 How to measure natural frequency by **ambient vibration test?**

operational conditions:

1 rotor rotation vibration:

motor on nacelle

2 dynamic loads:
wind load (wind tunnel)
wave load (wave tank)
EQ (shaking table)

1P loading is caused by mass and aerodynamic imbalances of the rotor, and the forcing frequency
2P/3P loading is caused by the blade shadowing effect, wind shear (i.e., the change in wind speed with height above the ground) and rotational sampling of turbulence.

measure wind speed
measure accelerations
correlate two

do FFT
get natural frequency


# Question 2 How to measure natural frequency by **strain gauge?**

strain for fatigue purposes
strain gauge: measure stress on crucial parts


acceleration for effectiveness of damping controlling effects of vortex shedding.
acceleration: displacement measurement
LVDT: deflection mode shape 

tiltmeter: measure verticality


# Question 3 How to model natural frequency using **FEM?**

SAP2000
from load-displ curve, get K
from K, calculate f


# Question 4 How to obtain **data for FFT?**

The bigger the tower, the lower the f.
-> use sensitive sensor

# Question 5 세굴모니터링 **기능구현율?**

system identification under critical situations like existence of closely spaced modes and non-proportional damping

can identify those that only mobilize for certain vibration levels?

Can detect spurious frequencies?

Can classify white noise?
