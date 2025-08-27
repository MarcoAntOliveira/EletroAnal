within ModelicaByExample.Components.Electrical.VerboseApproach;
model Inductor "An inductor model"
  parameter Modelica.SIunits.Inductance L;
  Modelica.Electrical.Analog.Interfaces.PositivePin p
    annotation (Placement(transformation(extent={{-110,-10},{-90,10}})));
  Modelica.Electrical.Analog.Interfaces.NegativePin n
    annotation (Placement(transformation(extent={{90,-10},{110,10}})));
protected
  Modelica.SIunits.Voltage v = p.v-n.v;
equation
  p.i + n.i = 0 "Conservation of charge";
  L*der(p.i) = p.v;
end Inductor;
