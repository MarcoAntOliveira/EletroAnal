model ClamperCircuit
    import Modelica.Electrical.Analog.Basic.*;
    import Modelica.Electrical.Analog.Sources.*;
    import Modelica.Electrical.Analog.Semiconductors.*;
    import Modelica.Electrical.Analog.Basic.Ground;

  parameter Real R = 1000;
  parameter Real C = 1e-6;

  Modelica.Electrical.Analog.Basic.Resistor resistor(R=R);
  Modelica.Electrical.Analog.Basic.Capacitor capacitor(C=C);
  Modelica.Electrical.Analog.Ideal.IdealDiode diode;

  SineVoltage vin(V=1, f=1000);
  Modelica.Electrical.Analog.Basic.Ground ground;
  Modelica.Electrical.Analog.Basic.Resistor load(R=1000);

equation
  connect(vin.p, capacitor.p);
  connect(capacitor.n, diode.p);
  connect(diode.n, resistor.p);
  connect(resistor.n, ground.p);
  connect(vin.n, ground.p);
  connect(capacitor.n, load.p);
  connect(load.n, ground.p);
end ClamperCircuit;
