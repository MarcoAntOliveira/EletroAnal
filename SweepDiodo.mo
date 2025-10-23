model SweepDiodoComReta
  import Basic = Modelica.Electrical.Analog.Basic;
  import ESources = Modelica.Electrical.Analog.Sources;
  import Semiconductors = Modelica.Electrical.Analog.Semiconductors;
  import BSources = Modelica.Blocks.Sources;

  parameter Real R = 1000 "Resistor série (Ω)";
  parameter Real Vmax = 20 "Tensão máxima (V)";
  parameter Real Tfinal = 0.01 "Tempo final de sweep (s)";

  // Fonte controlada por sinal
  ESources.SignalVoltage Vin;
  Basic.Resistor R1(R=R);
  Semiconductors.Diode D1;
  Basic.Ground G;

  // Ramp sobe de 0 até Vmax em Tfinal
  BSources.Ramp ramp(
    height=Vmax,
    duration=Tfinal,
    offset=0,
    startTime=0);

  // Variável para reta de carga
  Real Ireta;

equation
  connect(ramp.y, Vin.v);
  connect(Vin.p, R1.p);
  connect(R1.n, D1.p);
  connect(D1.n, Vin.n);
  connect(Vin.n, G.p);

  // Definição da reta de carga
  Ireta = (ramp.y - D1.v) / R;

end SweepDiodoComReta;
