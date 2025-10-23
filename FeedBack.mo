model FeedBack
  Modelica.Blocks.Continuous.PID PID(Ti = 10, Td = 0)  annotation(
    Placement(transformation(origin = {8, 20}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Continuous.SecondOrder secondOrder(k = 2, w = 1, D = 0.7)  annotation(
    Placement(transformation(origin = {60, 18}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Math.Feedback feedback annotation(
    Placement(transformation(origin = {-34, 18}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Sources.Step step annotation(
    Placement(transformation(origin = {-78, 18}, extent = {{-10, -10}, {10, 10}})));
equation
  connect(step.y, feedback.u1) annotation(
    Line(points = {{-66, 18}, {-42, 18}}, color = {0, 0, 127}));
  connect(secondOrder.y, feedback.u2) annotation(
    Line(points = {{71, 18}, {71, -60}, {-34, -60}, {-34, 10}}, color = {0, 0, 127}));
  connect(feedback.y, PID.u) annotation(
    Line(points = {{-24, 18}, {-4, 18}, {-4, 20}}, color = {0, 0, 127}));
  connect(PID.y, secondOrder.u) annotation(
    Line(points = {{20, 20}, {48, 20}, {48, 18}}, color = {0, 0, 127}));

annotation(
    uses(Modelica(version = "4.0.0")));
end FeedBack;