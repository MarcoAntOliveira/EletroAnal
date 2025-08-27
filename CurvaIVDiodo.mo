within ;
model CurvaIVDiodo
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;
  import Modelica.Electrical.Analog.Semiconductors.*;
  import Modelica.Electrical.Analog.Sensors.*;
  import Modelica.Electrical.Analog.Basic.Ground;

  // Fonte DC controlada por tempo (vai varrer a tensão)
  Voltage rampSource(V = 0);

  // Gerador de rampa (0 → 1 V em 0.1s, depois fica)
  Modelica.Blocks.Sources.Ramp rampa(
    height = 2,     // vai de 0 até 2 V
    duration = 0.1, // tempo da rampa
    offset = -1     // começa em -1 V
  );

  // Diodo
  Diode D1(Ids=1e-14, Vt=0.025, N=1);

  // Medidores
  VoltageSensor Vs;
  CurrentSensor Is;

  Ground GND;

equation
  connect(rampa.y, rampSource.V);  // rampa controla a fonte

  connect(rampSource.p, Is.p);
  connect(Is.n, D1.p);
  connect(D1.n, Vs.p);

  connect(rampSource.n, GND.p);
  connect(Vs.n, GND.p);
  connect(GND.p, D1.n);

end CurvaIVDiodo;
