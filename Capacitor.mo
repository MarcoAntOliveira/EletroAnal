within ModelicaByExample.Components.Electrical.VerboseApproach;

model Capacitor "A capacitor model"

  parameter Modelica.SIunits.Capacitance C;
  
  Modelica.Electrical.Analog.Interfaces.PositivePin p
    annotation (Placement(transformation(extent={{-110,-10},{-90,10}})));
  Modelica.Electrical.Analog.Interfaces.NegativePin n
    annotation (Placement(transformation(extent={{90,-10},{110,10}})));
protected
  Modelica.SIunits.Voltage v = p.v-n.v;
equation
  p.i + n.i = 0 "Conservation of charge";
  C*der(v) = p.i;
end Capacitor;
