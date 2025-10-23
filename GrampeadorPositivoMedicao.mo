model GrampeadorPositivoMedicao
  import Modelica.Electrical.Analog.Basic.*;
  import Modelica.Electrical.Analog.Sources.*;
  import Modelica.Electrical.Analog.Semiconductors.*;
  import Modelica.Blocks.Sources.*;
  import Modelica.Blocks.Math.*;
  import Modelica.Blocks.Continuous.*;
  import Modelica.Blocks.IO.*;

  // Fonte senoidal
  SineVoltage Vin(V=5, f=50, offset=0);

  // Circuito grampeador
  Diode D;
  Capacitor C(C=10e-6);
  Resistor R(R=1e6);
  Ground g;

  // Bloco para cálculo de média (offset)
  Integrator integrador(k=1) "Integra sinal de saída para calcular média";
  Gain ganho( k=1/0.1 ) "Dividir integral pelo tempo total para média";
  
  // Exportação CSV
  Real Vout "Tensão de saída";
  Modelica.Blocks.IO.CombiTimeTableExport csvExport(fileName="offset_saida.csv") "Exporta Vout";

equation
  // Conexões elétricas
  connect(Vin.p, D.p);
  connect(D.n, C.p);
  connect(C.n, g.p);
  connect(R.p, C.p);
  connect(R.n, g.p);
  connect(Vin.n, g.p);

  // Saída do grampeador
  Vout = C.p.v;

  // Cálculo de média do offset
  integrador.u = Vout;
  ganho.u = integrador.y;

  // Exporta saída (Vout) para CSV a cada passo de simulação
  csvExport.u = Vout;
end GrampeadorPositivoMedicao;
