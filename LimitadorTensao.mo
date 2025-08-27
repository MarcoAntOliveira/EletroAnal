model LimitadorTensao
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;
  import Modelica.Electrical.Analog.Semiconductors.*;
  import Modelica.Electrical.Analog.Basic.Ground;

  // Fonte senoidal
  SineVoltage fonte(
    V = 10,   // Amplitude pico [V]
    f = 50    // Frequência em Hz
  );

  Resistor R1(R=1000); // resistor de série (1kΩ)

  Diode D1(Ids=1e-14, Vt=0.025, N=1);
  Diode D2(Ids=1e-14, Vt=0.025, N=1);

  Ground GND;

equation
  // Ligações
  connect(fonte.p, R1.p);
  connect(fonte.n, GND.p);

  // connect(R1.n, D1.p);
  // connect(R1.n, D2.n);

  connect(D1.n,R1.n);
  connect(D1.p, GND.p);

end LimitadorTensao;
