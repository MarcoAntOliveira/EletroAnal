block DynamicController
  import Modelica.Units.SI; // importa unidades físicas
  extends Modelica.Blocks.Interfaces.SISO; // cria conectores padrão u, y

  parameter SI.Time T = 0.5 "Constante de tempo do sistema";
  parameter Real K = 2 "Ganho proporcional";
  
protected 
  Real x(start=0);
  
equation
  der(x) = (K*u - x)/T;
  y = x;
end DynamicController;
