# [박광희 등 2022] Natural Frequency Degradation Prediction for Offshore Wind Turbine Structures

However, there are no actual sensor data on the dynamic response of OWTs over their lifespan (approximately 20 years).

Specifically, a virtual dynamic response was generated using a three-dimensional OWT and a seabed finite element model. Then, the LSTM model was trained to predict the natural frequency degradation using the dynamic response as the model input.

Li et al. [16] developed deep convolution neural networks for aero-engine degradation using the publicly available C-MAPSS dataset.
16. Li, X.; Ding, Q.; Sun, J.-Q. Remaining useful life estimation in prognostics using deep convolution neural networks. Reliab. Eng. Syst. Saf. 2018, 172, 1–11. [CrossRef]

First, a finite element model (FEM) was built using a 3-MW WinDS3000 TC-2 wind turbine (Doosan Heavy Industries & Construction, Changwon, Korea) [21] installed in the southwestern sea region of the Korean Peninsula.
![[Pasted image 20230204114409.png]]
![[Pasted image 20230204114425.png]]

Then, the OWT model parameters were determined using the sensor data from the actual structure.

Next, the long-term virtual sensor data of the OWT were obtained using the FEM, and the acceleration, strain, and NF of the OWT structure were collected.

the model parameter values are determined using structural health monitoring data.

$$
F_a=\frac{1}{2} \rho_a \pi R_b^2 V_h^2 C_t
$$

The WinDS3000 TC-2 turbine was provided by Doosan Heavy Industries & Construction [28]
28. Nam, W.; Oh, K.-Y.; Epureanu, B.I. Evolution of the dynamic response and its effects on the serviceability of offshore wind turbines with stochastic loads and soil degradation. Reliab. Eng. Syst. Saf. 2019, 184, 151–163. [CrossRef]

The stochastic wind speed Vh was obtained from the Kaimal spectrum, as described in [30].
30. IEC. IEC61400-1. In Wind Turbines–Part 1: Design Requirements, 3rd ed.; IEC: London, UK, 2005; Volume 61400-1.

The wave-caused dynamic pressure should be considered to predict the dynamic response of the structure and soil. The stochastic wave elevation was obtained from Pierson and Moskowitz [30], which describes the wave power spectrum as a function of wind speed.

The pressure applied to the submerged part of the structure by a wave can be calculated using potential theory [28].
28. Nam, W.; Oh, K.-Y.; Epureanu, B.I. Evolution of the dynamic response and its effects on the serviceability of offshore wind turbines with stochastic loads and soil degradation. Reliab. Eng. Syst. Saf. 2019, 184, 151–163. [CrossRef]

Once the wind speed is determined, the aero/hydrodynamic loads are determined.

The Weibull distribution shape and scale parameters (k and c, respectively) were used for the wind speed probability

Long-term simulations were conducted using the FEM and the different wind distributions in order to acquire the virtual sensor dataset. The simulations were performed for the lifespan of the OWT (i.e., 20 years). The acceleration and strain frequency response functions (at 14 different positions) were acquired; these data correspond to the sensor data. The data were stored every 0.1 years; thus, a total of 200 samples were obtained for a 20-year simulation for a specific (k, c) set

- - -

# ★[Capilla 2021]Ambient vibration testing and operational modal analysis of monopole telecoms structures

A structural health monitoring (SHM) system was developed to study the ambient response of monopole communication structures in the UK operated by Arqiva Ltd.

This paper describes the instrumentation and procedures used during monitoring of a lightweight fexible 14.5 m tubular tapered monopole supporting an array of mobile telecoms antennas.

A Bayesian OMA (BAYOMA) approach is implemented to identify structural modal properties under diferent time windows as comparison for further assessments.

The correlation between modal properties and monitoring wind-response data reveals specifc tendencies such as nonlinear stifness behaviour, the existence of aerodynamic damping and typical directionality of the mode shapes with future implications for reformulation of current methods of assessing dynamics on monopole

Currently, a high percentage of monopole structures are invalidated to support new antennas according to standards, i.e., the most modern Eurocode BS EN 1991-1-4: 2005 “Wind Actions” [1], British Standard BS 8100: Part 1:1986 [2] and the Institution of Lighting Engineers (UK) Technical Report Number 7 [3].
1. E. Commission (1991) BS EN 1991-1-4:2005 General actions— Wind actions. Brussels
2. British Standards Institution (1986) BS 8100-1. Lattice towers and masts—Part 1: Code of practice for loading, vol 3, no 1. London
3. The Institution of Lighting Engineers (2013) PLG07: High Masts for lighting and CCTV


SHM aims at acquiring information about wind loading and response of the structure under a variety of working conditions

USED anemometer

The system has been sequentially deployed in several structures but this paper will cover the data obtained during more than 2 months on a Portasilo Monopole in St Ives; see Fig. 1.
![[Pasted image 20230204121211.png]]


For this purpose and to improve current approaches, the present paper introduces modal identifcation procedures to identify and explain dynamic load/response mechanisms. This exercise executes the operational modal analysis (OMA) procedure based on innovative Fast Bayesian ambient modal identifcation method (BAYOMA) [10, 11],which has been applied to other civil structural types such as buildings, bridges and lighthouses [12].
10. Au SK (2012) Fast Bayesian ambient modal identifcation in the frequency domain, Part I: posterior most probable value. Mech Syst Signal Process 26:60–75
11. Au SK (2012) Fast Bayesian ambient modal identifcation in the frequency domain, Part II: posterior uncertainty. Mech Syst Signal Process 26:76–90
12. Brownjohn JMW, Au SK, Li B, Bassitt J (2017) Optimised ambient vibration testing of long span bridges. In: EURODYN 2017, p 10

This paper compares and contrasts the procedures applied to assessing monopole performance using three diferent lengths of data time frame (Tfr). It will set a fnal decision where to base technical conclusions in terms of dynamic parameters like frequencies, damping or mode shapes to apply to other SHM

Results are also compared with those from Stochastic Subspace Identifcation method (SSI, [13]), which is one conventional method used in several types of dynamic sensitive structures [14] for the last two decades, here implemented by ARTeMIS software

To capture the monopole response the system is based on two monoaxial PCB accelerometers model 393B04, with a sensitivity of 1000 mV/g able to measure between ±5 g (±49m∕s2 pk) placed in a waterproof box

A RM Young mechanical anemometer to capture wind loading in terms of horizontal wind speed and direction (with respect to North). This produces an AC sine wave signal with frequency proportional to wind speed with three cycles per propeller revolution (0.0980 m/s per Hz) and FFT of 2-s data blocks was used to extract wind speed values up to 100 m/s with operating temperature between − 50 and+50 ºC, far beyond the expected range in this application. A threshold minimum frequency corresponding to a wind speed of 2 m/s is set to avoid erroneous readings for low wind speeds.

![[Pasted image 20230204121610.png]]

The 76 days of continuous measurements over the length of the monitoring were divided into consecutive data fles of 10-min time frame. Each fle comprises fve channels: acceleration records of both accelerometers, wind speed, wind direction and temperature.

Operational modal analysis

The application of operational modal analysis (OMA) is attractive in practice because it avoids the logistical challenges of using mechanical shakers, using service windambient loading

, i.e., a plot of singular values of the cross-spectral density matrix. Within a frequency band, the number of lines taking the shape of dynamic amplifcation indicates the dimension of the subspace spanned by the mode shapes, which is often equal to the number of modes in the band.


The structural response of a monopole under normal buffeting is defned by an oval/elliptical horizontal movement with major axis in the along-wind direction

# [Foti 2011]Ambient vibration testing, dynamic identification and model updating of a historic tower

The results of an ambient-vibration based investigation conducted on a historical tower in Italy, to update the 3-D finite element model of the building are presented in this work. The main difficulties are related to the extreme in-homogeneity of the building and the presence of an elevator vain that occupies the posterior part of the tower, forcing to locate the accelerometers only on one fac-ade of the building.

A very good match between theoretical and experimental modal parameters was reached and the model updating has been performed to identify some structural parameters.

One main problem in the Operational Modal Analysis (OMA) is the maintenance of the data acquisition system [9]. Field measurements, in fact, are often performed in very harsh environmental conditions, requiring high accuracy both in the control of the test set-up and in the analysis of the measured data.

Ambient vibration test has been conducted on the above mentioned tower, in a particularly windy day (24th July 2009), with the aim of determining its dynamic response and developing a procedure for modeling the tower. The Operation Modal Analysis (OMA) has been carried out both in the frequency domain and in the time domain to extract the dominant frequencies and mode shapes. The application of well-known different identification techniques—the Enhanced Frequency Domain Decomposition (EFDD) method [11], the Stochastic Subspace Identification (SSI) method [12] and the Crystal-Clear Stochastic Subspace Identification (CC-SSI) method [13]—implemented in a commercial software, yields to very similar results for all the identified modes, providing consistent information for the following finite element model updating

The tower of the Provincial Administration Building in Bari, Italy (Fig. 1), dating back to the thirties of the 20th century and bout 60 m tall, is not only a typical example of the fascist architectural style, but it is an important symbol of the city itself


![[Pasted image 20230204122447.png]]

The extraction of the modal parameters from ambient vibration data was carried out using the ARTeMIS software [14]. Three different OMA methods were used: EFDD, SSI and CC-SSI. Fig. 5(a)–(c) show the experimental results with reference to one of the eleven intervals considered. All the results were obtained with the maximum resolution allowed (8192 lines of spectral density).

![[Pasted image 20230204122519.png]]


# [Gentile and Saisi 2007] Ambient Vibration Testing of historic masonry towers for structural identification and damage assessment

Ambient vibration tests were conducted on the tower at the beginning of July 2001 to measure the dynamic response in 20 different points, with the excitation being associated to environmental loads and to the bell ringing.

![[Pasted image 20230204122642.png]]

![[Pasted image 20230204122653.png]]

![[Pasted image 20230204122720.png]]

![[Pasted image 20230204122737.png]]

non-homogeneous distribution of the Young’s modulus was assumed


# ★★[Magalhaes 2010] Damping estimation using free decays and ambient vibration tests
During ambient vibration tests, the accelerations of structures excited by ambient loads are measured. Accordingly, the traffic over the bridge and the wind are welcome, to increase the signal intensity of the measured time series. Still, the levels of excitation are generally low, and so, the used accelerometers have to be very sensitive. Furthermore, the test of slender structures demands the use of transducers that should present a linear response from very low frequencies. Besides that, when the size of the structure is considerable, the use of wireless systems duly synchronized by GPS is advantageous.
GPS to continuously update the internal clock using information provided by the satellites, in order to have a perfect synchronization between acquisition units,

It can be shown [5] that, under some assumptions (white noise excitation, low damping and orthogonal mode shapes for close modes), the singular values (SV) of the spectral matrix are auto-spectral density functions of single degree of freedom systems with the same frequency and damping as the structure vibration modes
[5] R. Brincker, L. Zhang, P. Andersen, Modal identification from ambient responses using frequency domain decomposition, IMAC XVIII, San Antonio, USA, 2000.

A review of the most commonly used methods in civil applications can be found in Ref. [3].
[3] A´ . Cunha, E. Caetano, Experimental modal analysis of Civil Engineering structures, Sound and Vibration, 2006, pp. 12–20.


A sampling frequency of 5 Hz was adopted in all the simulations. The responses were evaluated using a discrete-time state-space model following the methodology described by Juang [9]
![[Pasted image 20230204123250.png]]

![[Pasted image 20230204123231.png]]
![[Pasted image 20230204123313.png]]

![[Pasted image 20230204123339.png]]

The results provided by the ambient vibration tests showed a fairly high scatter, expressed by relative standard deviations around 50%. This stems mainly from two reasons. One is the use of relatively short time series (16 min), taking into account that the first frequency of two of the analysed structures is around 0.3 Hz and that the modal damping ratios are small (generally lower than 1%). The relative standard deviations observed in the simulations when time segments of 20 min were used were around 20%. The other main reason is the non-stationarity of the structures excitation, not reproduced in the simulations. During the ambient vibration tests, sometimes performed during more than one day, significant variations of the intensity and frequency content of the excitation can occur, which can lead to variations of the structural damping, that is commonly dependent on the amplitude of structural oscillations (e.g. existence of friction forces that are only mobilized for certain vibration levels). The variation of wind characteristics during the ambient vibration test can also induce damping variations motivated by the existence of aerodynamic damping, as already observed during the ambient vibration test of a cable-stayed bridge [15].
[15] F. Magalha˜es, E. Caetano, A´ . Cunha, Challenges in the application of stochastic modal identification methods to a cable-stayed bridge, Journal of Bridge Engineering 12 (6) (2007) 746–754.

The results taken from the free decays are more accurate, because the noise influence is smaller (higher amplitudes), there is no need to make assumptions about the loading (in ambient vibration tests it is assumed a stationary white noise) and the influence of wind can be reduced if the impulse is applied with low wind velocities.

The ambient vibration tests need long periods of acquisition to provide reliable results and so it is more difficult to ensure low wind velocities during the test to reduce the effect of aerodynamic damping. Anyway, they provide reasonable estimates of the modal damping coefficients with very economical and practical procedures. It is important to develop further research in order to better understand all the reasons for the observed dispersion and to find a process to reduce it. The data collected by permanent dynamic monitoring systems that allow the tracking of the damping evolution during long periods under different ambient conditions can be very useful in this context.

# [Paultre 2000]Ambient and forced-vibration tests of the Beauharnois suspension bridge

Ambient and forced vibration tests were carried out on the Beauharnois Bridge, a unique, 177-m combined suspension and cable-stayed structure near Montreal

m. The paper presents a series of dynamic tests performed to evaluate the dynamic properties and the dynamic amplification factor (DAF) for the rehabilitated bridge.

The experimental program involved the measurement of vertical, transverse, and longitudinal acceleration responses of the deck and tower under ambient and controlled traffic loads. Displacement, strain, and integrated acceleration DAFs were computed under different loading conditions. Modal properties were evaluated and used to correlate a three-dimensional finite element model for the bridge, including nonlinear cable behaviour. The paper discusses the experimental setup and the techniques used to evaluate vibration frequencies, mode shapes, and the DAF. Correlation of numerical dynamic properties and experimental results is also presented.

![[Pasted image 20230204124125.png]]

Three pairs of accelerometers were successively placed at each of the 14 positions on both sides of the deck. Two accelerometers remained at reference stations 1 and 2 throughout the tests, which are located halfway between the stay-cable anchor points on both sides of the deck (Fig. 3a). Only three accelerometer configurations were necessary to cover all measurement stations on the deck. Accelerometers were also placed inside the east tower to record longitudinal and transverse motions.

# Design of Foundations for Offshore Wind Turbines-Wiley (2019)
Figure 2.5 shows the main frequencies for a three-bladed National Renewable Energy Laboratory (NREL) standard 5 MW wind turbine with an operational interval of 6.9–12.1 rpm. The RPM can be converted to Hz and therefore the rotor frequency (often termed 1P) lies in the range 0.115–0.2 Hz. The corresponding ‘blade passing frequency’ for a three-bladed turbine can be obtained by multiplying 1P range by 3 and therefore lies in the range 0.345–0.6 Hz. The figure also shows typical frequency distributions for wind and wave loading. The spectrum for wind is Froya based on Andersen and Løvseth (1992) and for the wave is Pierson-Moskowitz (1964) is used.
![[Pasted image 20230204124816.png]]

![[Pasted image 20230204124921.png]]

must avoid resonance

![[Pasted image 20230204125422.png]]

# [Bhattacharya et al 2021] Physical modelling of offshore wind turbine foundations for trl 

Physical Modelling in Geotechnical Engineering: A Brief Overview
To validate a hypothesis or a theoretical failure mode/mechanism of foundations.
To recreate a failure or a collapse mechanism for settling liabilities or insurance claims
To gain new insights into unexplored complex phenomena like cyclic behaviour of foundations in shallow gassy sediments
modes of vibration or the modes of ultimate collapse.
To understand the deformations of foundations under various design situations and limit states
To develop design methods that may lead to the path of standardization
To validate the constitutive models of soils used in numerical models

Readers are referred to PISA-based projects, which are near full-scale; see reference [17].

One of the aims of the model test is to represent these load effects appropriately in the scaled model tests. This constitutes one of the important steps in the scaled model testing [6], including aspects such as new materials [7], site-specific estimates [8], and future monitoring strategies [9]. The readers are referred to further details of physical modelling in general and its applicability in [6].


Geotechnical centrifuge enables replication of the stress levels that the soil experiences in the field. However, the whole model is spun at a high rate which creates unwanted small vibrations. Therefore, the subtle dynamics of the problem is difficult to study as filtering of signals are inevitable during the processing of data

Ideally, a tiny wind tunnel together with a tiny wave tank onboard a geotechnical centrifuge may serve the purpose, but this is not viable and will add more uncertainty to the models than it tries to unearth.

Therefore, the focus of the experiments needs to be on the governing laws or mechanics or process.

In wind tunnel tests, aerodynamic effects are modelled efficiently and correctly, and as a result, the loads on the blade and towers can be simulated. By comparison, in a wave tank, the hydrodynamic loads on the sub-structure and scouring on the foundation can be modelled.

Our extensive experience with small-scale tests showed that connecting the actuator rod to the tower modified the natural frequency of the system significantly (in one case from 6.5 to 8 Hz) as a result of the added stiffness of the actuator; damping was also increased. This effect was found to be greater if the actuator connection was moved up the tower, as dictated by fundamental dynamics, because the mode shape displacement increases with the increasing height of the tower. This implies that the evaluation of natural frequency and damping of the free system during an experiment requires significant post-processing of results and is undesirable. The Type 3 technique removes all of the above effects.


6.5. Modes of Vibration of Systems
In this method, a small displacement/perturbation is applied to the tower manually, and the tower is then released and allowed to vibrate freely—this is often known as the snap-back test. An accelerometer is used to measure the movement this induces, which will occur at the resonant frequencies of the system because no force is involved. Analysis of the signal will provide the damping and resonant frequencies of the system and can be performed in either the time domain (through measurement of peak-to-peak distances) or the frequency domain (by finding a power spectrum). The power spectrum of each signal was obtained through a fast Fourier transform using the method proposed by [40]. Free vibration can be carried out on a range of scaled model tests to understand the modes of vibration and how they evolve with cycles of loading. There is an important scaling law that must be maintained in order to recreate the modes of vibration.

Scaling laws for modelling modes of vibration: to capture the modes of vibration, one needs to have the following similarities: (a) Mass similarities, i.e., mass distribution along the length of the tower; (b) Stiffness similarity, i.e., relative tower to foundation similarity; (c) Geometric similarity, i.e., the relative distance between the foundation in proportion to the tower must be preserved. Readers are referred to [41] for further details.


The purpose of the tests was to understand the different aspects of (cyclic and dynamic) soil–structure interaction (SSI) behavior rather than replicating a particular field problem. The scaling of understanding gained to predict the prototype behaviour is beyond the scope of the current paper.


testing small-scale model wind turbines on a shake table (see Figure 29). Before the shaking is applied, it is important that the natural frequency of the system is measured using the snap-back test, in which the frequency can be obtained from a free-decay response using either frequency- or time-domain methods (for more details, the reader is referred to [54]). During the shaking, the natural frequency of the system can be calculated using transfer functions in the frequency domain

The dynamics of wind turbines appear to face a number of unresolved issues. Previous research work aiming to accurately account for resonance predictions has proved the existence of specific patterns in the change in frequency [43,55]. Here the influence of an earthquake-type loading with a range of loading frequencies under nearresonant conditions showed a multitude of interesting phenomena. Existence of double response peaks, a global stiffening of the response, and, most importantly, the implication of motion-induced forces appear to raise a number of new questions that require further research to answer.

![[Pasted image 20230204131658.png]]

![[Pasted image 20230204131820.png]]

# [유무성 2021]Closed Form Solutions for Predicting Lateral Response of Tripod Suction Pile for Offshore Wind Turbine Foundation

4. Natural Frequency Derivation of Wind Turbine System 4.1. Equivalent Spring Coefficient of System

Influence factors:
Mass system
Length of foundation

varying analysis sections


![[Pasted image 20230204133721.png]]

5.1. Design Parameters Table 4 shows the main design parameters of offshore wind turbines that applied the derived simple analysis method for the basic design. Based on the load conditions provided by the turbine company, a horizontal load of 1 MN was applied to the top of the 3 MW turbine, and the specifications and properties of the tower and turbine were also prepared based on the actual turbine information [17].
17. Technical Description of WinDS3000 in Supply. Doosan Heavy Industry; Contract Documents: Madison, WI, USA, 2012
18. Technical Report of Young’s Modulus of Ground Soil for Project: SuCCESS; KAIST Soil Dynamic Lab: Daejeon, Korea, 2015



![[Pasted image 20230204133811.png]]

, equivalent stiffness matrix of suction pile has been evaluated using a commercial FE program, MIDAS GTS NX.

Field test was performed at each installation stage in order to check the accuracy of installation and safety of structure. Accelerometers and tilt and strain gauges were installed for measuring the natural frequency, verticality, and stresses on crucial parts of the system.

![[Pasted image 20230204134027.png]]


As a result of the analysis, the first natural frequency of the system was 0.322 Hz; this value did not overlap with the blade pass frequency of 0.18 to 0.26 Hz and its triple value of 0.54 to 0.78 Hz, as mentioned in Section 2.1, which indicated that the design requirements were satisfied. I

![[Pasted image 20230204134124.png]]

The equation for calculating the primary natural frequency of the offshore wind turbine was derived using the effective mass of the structure, which was determined using the kinetic energy formula and the influence factor obtained for the entire supporting structure

the pattern of the change in the first natural frequency according to the stiffness ratio of the ground/support structure and the mass ratio of the turbine/support structure was analyzed.

The frequency was almost unaffected by the ground soil when the soil had a high stiffness value ( ksoil kstructure>>100) compared to that of the support structure.

there are some limitations to using an approximated influence curve for the intermediate pile range and assuming that the support structure is a simple beam when calculating the natural frequency of the system.. However, these assumptions do not affect the accuracy of our simplified analysis method because the turbine component is the dominant driver of system behavior.
Moreover, to our knowledge, this study is the first to investigate the mechanics of a tripod suction bucket foundation for offshore wind turbines in Korea. The findings of this study will provide design guidelines and a basis for field test indicators in other research projects. In the future, a more accurate influence curve for the intermediate pile range suitable for suction buckets should be studied.

Influence factors:

1. Poulos: Length-to-diameter ratio L/D
2. Poulos: Pile Flexibility factor (flexibility of pile relative to soil) E/G

ratio of area moment of inertia
length ratio
shape and spacing of beam members


13. Test Bed for 2.5 GW Offshore Wind Farm at Yellow Sea Design Basis; Final Report; Korea Electric Power Corporation Research Institute (KEPRI): Daejeon, Korea, 2016; pp. 153–168
7. Houlsby, G.; Kelly, R.; Huxtable, J.; Byrne, B. Field trials of suction caissons in sand for offshore wind turbine foundations. Geotechnique 2006, 56, 3–10. [CrossRef]
1. Wind Europe. Offshore Wind in Europe: Key Trends and Statistics 2019; Wind Europe: Brussels, Belgium, February 2020; p. 7.
2. Ministry of Trade, Industry and Energy. Korea’s Renewable Energy 3020 Plan; Ministry of Trade, Industry and Energy: Seoul, Korea, December 2017; pp. 4–7.
3. Offshore Wind Accelerator (OWA)/Foundations, Carbon Trust. Available online: www.carbontrust.com (accessed on 8 September 2020).
