model test_filter
  Modelica.Blocks.Continuous.Filter filter(analogFilter = Modelica.Blocks.Types.AnalogFilter.Butterworth, f_cut = 50)  annotation(
    Placement(transformation(origin = {18, 22}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Sources.Sine sine(amplitude = 5)  annotation(
    Placement(transformation(origin = {-56, 18}, extent = {{-10, -10}, {10, 10}})));
equation
  connect(sine.y, filter.u) annotation(
    Line(points = {{-44, 18}, {-38, 18}, {-38, 22}, {6, 22}}, color = {0, 0, 127}));

annotation(
    uses(Modelica(version = "4.0.0")));
end test_filter;