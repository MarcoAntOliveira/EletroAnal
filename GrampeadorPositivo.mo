model GrampeadorPositivo
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;
  import Modelica.Electrical.Analog.Semiconductors.*;

  // Fonte senoidal: amplitude, frequência, offset
  SineVoltage Vin(V=5, f=50, offset=0) "Fonte senoidal de entrada (Vp=5V, 50Hz)";
  Diode D "Diodo do MSL (não ideal)";
  Capacitor C(C=10e-6) "Capacitor de grampeamento (10µF)";
  Resistor R(R=1e6) "Resistor de fuga (1MΩ)";
  Ground g;
equation
  connect(Vin.p, D.p);
  connect(D.n, C.p);   // nó de saída
  connect(C.n, g.p);
  connect(R.p, C.p);
  connect(R.n, g.p);
  connect(Vin.n, g.p);
end GrampeadorPositivo;
