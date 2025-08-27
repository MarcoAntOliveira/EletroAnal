within ModelicaByExample.Components.Electrical.DryApproach;
model Resistor "A DRY resistor model"
  parameter Modelica.SIunits.Resistance R;
  extends TwoPin;
equation
  v = i*R "Ohm's law";
end Resistor;


model Capacitor "A DRY capacitor model"
  parameter Modelica.SIunits.Capacitance C;
  extends TwoPin;
equation
  C*der(v) = i;
end Capacitor;


model Inductor "A DRY inductor model"
  parameter Modelica.SIunits.Inductance L;
  extends TwoPin;
equation
  L*der(i) = v;
end Inductor;




model StepVoltage "A DRY step voltage source"
  parameter Modelica.SIunits.Voltage V0;
  parameter Modelica.SIunits.Voltage Vf;
  parameter Modelica.SIunits.Time stepTime;
  extends TwoPin;
equation
  v = if time>=stepTime then Vf else V0;
end StepVoltage;


