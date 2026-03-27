# Análisis exploratorio de datos-SECOP I último mes
## Dimensión y estructura del dataset 
El dataset contiene:12.680 registros (contratos) y 79 variables, evidenciando una base de datos amplia. La diversidad de variables permite múltiples niveles de análisis (entidad, territorio, tipo de contrato, cuantía, estado del proceso, objeto a contratar, etc.)
## Tipificación de variables
Se observa que todas las variables están almacenadas como tipo string (texto), incluyendo: Variables numéricas(cuantía del contrato), Variables temporales (fechas).Teniendo en cuenta esto, no es posible  realizar análisis estadísticos directamente sin transformación.
## Valores nulos
Teniendo en cuenta los resultados, se observa un nivel importante de datos faltantes, en el caso de fecha_liquidacion: 12.483 valores siendo un (98.4%), por otro lado fechas de firma, inicio y fin: 5.035 valores nulos con un (39.7%).
## Duplicados
Se encontraron 295 registros duplicados según el identificador único (uid)
## Modalidad de contratación 
Las principales modalidades de contratación son: 
-Contratación de mínima cuantía: 3.992 contratos
-Régimen especial: 3.560 contratos
-Contratación directa: 3.198 contratos
## Estado del proceso
La mayoría de los contratos están en estado celebrado (7.386),seguido por procesos convocados (4.417). Sin embargo,esto indica que gran parte de la contratación ya ha sido formalizada.
## Tipo de contrato
En este caso predonomina altamente el tipo de contrato por prestación de servicios 8431,seguido de suministro 2050, obra 558 y compraventa 479.
## Estadisticas de cuantía
El análisis de las cuantías de los contratos muestra una alta dispersión en los valores registrados. Mientras el promedio se ubica alrededor de 31 millones, la mediana es significativamente menor, con apenas 2 millones, lo que evidencia una distribución fuertemente sesgada. Esta diferencia indica que, aunque existen algunos contratos de muy alto valor (alcanzando hasta 55.530 millones), la mayoría de los contratos son de montos bajos.
## Valores en 0
Se registran 5096 contrato en cuantía 0.
## Contratos más altos
El contrato de mayor valor corresponde al Fondo Adaptación con una cuantía de 55.530.000.000, muy por encima del resto. Le sigue la Alcaldía del municipio de Cabuyaro (Meta) con 27.000.000.000, lo que representa aproximadamente la mitad del primero. En tercer lugar se encuentra la Alcaldía de Ciénaga (Magdalena) con 21.493.720.601, seguida por Centrales Eléctricas de Nariño (CEDENAR) con 18.500.000.000. A partir de ahí se observa una caída más pronunciada en los montos, con la Alcaldía de Candelaria (Atlántico) en 10.000.000.000 y luego varios contratos en el rango de 4.700 a 6.600 millones, como Vigía del Fuerte (Antioquia), Cámara de Comercio de Bogotá y diferentes municipios de Córdoba y Sucre.
## Top Departamentos
El análisis de la distribución de contratos por departamento muestra una clara concentración territorial, liderada ampliamente por Nariño con 1.416 contratos, en segundo lugar, Santander, que registra 747. A partir de ahí, los demás departamentos presentan valores relativamente similares, como Bolívar (643), Córdoba (619) y Chocó (604), lo que indica una distribución más equilibrada entre estos territorios. También destacan regiones como San Andrés y Providencia (587), Antioquia (576), Magdalena (556), Risaralda (549) y Cundinamarca (541), todos con niveles cercanos entre sí. 
## Top municipios 
El análisis de los municipios con mayor número de contratos evidencia una concentración destacada en Providencia, con 598 registros, superando ampliamente al resto. Le sigue Pereira con 444 contratos, mientras que en un segundo lugar aparecen municipios como San José del Guaviare (280), Bucaramanga (279) y Puerto Carreño (267), con valores relativamente cercanos entre sí. Posteriormente, se observa una disminución gradual con Francisco Pizarro (234), San Pablo (202) y Montería (172). Llama la atención que Bogotá D.C. registre solo 168 contratos dentro del top.
## Entidades con más contratos
Las entidades con mayor número de contratos están lideradas por la Alcaldía de Providencia con 575 registros, seguida por la Cámara de Comercio de Pereira con 444 y la de Bucaramanga con 277. Luego aparecen entidades de salud y gobiernos territoriales como la red de salud del Guaviare (228), el centro de salud de Francisco Pizarro (223) y la Gobernación del Vichada (222).
## Fechas faltantes 
El análisis de las fechas faltantes muestra que 5.035 registros no cuentan con información sobre la fecha de firma, inicio y fin de ejecución del contrato, lo que representa una proporción considerable del dataset.
## Rango de fechas
El análisis muestra que los datos cubren el periodo entre el 19 de febrero y el 18 de marzo de 2026, correspondiente aproximadamente a un mes de actividad contractual.
## Contratos por día
 Se observa un patrón marcado en la distribución diaria: los días hábiles concentran la mayor cantidad de contratos, con picos como el 24 de febrero (887), 25 de febrero (844) y 3 de marzo (760), mientras que los fines de semana presentan una caída significativa en la actividad, con valores mucho más bajos como el 1 de marzo (46), 8 de marzo (48) y 15 de marzo (29).

# Exploración de datos SECOP-I últimos 3 meses
## Dimensión y estructura del dataset
El dataset contiene: 101.499 registros (contratos) y 79 variables, lo que evidencia un volumen de información considerablemente mayor frente al análisis de un solo mes. Esta ampliación permite una visión más completa y representativa del comportamiento de la contratación pública. La diversidad de variables permite múltiples niveles de análisis (entidad, territorio, tipo de contrato, cuantía, estado del proceso, objeto a contratar, entre otros).
## Tipificación de variables
Se observa que todas las variables están almacenadas como tipo string (texto), incluyendo variables numéricas (como la cuantía del contrato) y variables temporales (fechas). Esto implica que no es posible realizar análisis estadísticos directamente sin una transformación previa de los datos.
En ambos periodos, todas las variables están en formato string (texto), incluyendo cuantías y fechas.
## Valores nulos
Se mantiene un nivel importante de datos faltantes. En el caso de fecha_liquidacion, se registran 100.321 valores nulos (98.8%), lo que indica que la gran mayoría de contratos no han sido liquidados o no cuentan con este registro. Por otro lado, las variables de fecha de firma, inicio y fin de ejecución presentan 17.224 valores nulos (16.9%), lo que sigue siendo significativo aunque menor que en el análisis del último mes.
## Duplicados
Se identificaron 4.392 registros duplicados según el identificador único (uid), lo que evidencia posibles inconsistencias en la calidad de la información.
## Modalidad de contratación
Las principales modalidades de contratación son:
-Contratación directa: 76.527 contratos
-Régimen especial: 9.890 contratos
-Contratación de mínima cuantía: 9.207 contratos
Se evidencia un claro predominio de la contratación directa, muy por encima del resto de modalidades.
## Estado del proceso
La mayoría de los contratos se encuentran en estado:
-Celebrado: 81.269 contratos
-Convocado: 17.052 contratos
Esto indica que la mayor parte de los procesos ya han sido formalizados.En ambos casos predomina el estado celebrado.
## Tipo de contrato
Predomina ampliamente el tipo de contrato por:
-Prestación de servicios: 87.759 contratos
Muy por encima de otros tipos como suministro (5.451), obra (1.578) y compraventa (1.155), lo que evidencia una fuerte orientación hacia este tipo de contratación.Se mantiene una fuerte dependencia de la contratación por prestación de servicios en ambos periodos.
## Estadísticas de cuantía
El análisis de las cuantías muestra una alta dispersión en los valores. El promedio se ubica alrededor de 48 millones, mientras que la mediana es de 12.6 millones, lo que indica una distribución sesgada. Esto significa que, aunque existen contratos de valores extremadamente altos (alcanzando hasta 956.764 millones), la mayoría de contratos se concentran en montos relativamente bajos.En 3 meses aparecen contratos mucho más grandes, lo que aumenta el promedio y evidencia mayor concentración del gasto.
## Valores en 0
Se registran 17.808 contratos con cuantía 0, lo cual es considerablemente alto en comparación con el último mes.
## Contratos más altos
El contrato de mayor valor corresponde al Ministerio de Salud, con una cuantía de 956.764.192.641, seguido por otro contrato de la misma entidad con 423.613.931.367. Posteriormente aparece el Fondo Adaptación con 55.530.000.000, seguido por el Ministerio de Hacienda con 33.048.675.000 y la Alcaldía de Cabuyaro (Meta) con 27.000.000.000. A partir de estos valores se observa una disminución progresiva, con contratos en el rango de 21.000 a 26.000 millones, evidenciando una fuerte concentración del gasto en pocos contratos de gran magnitud.
## Top Departamentos
El análisis de la distribución por departamento muestra una concentración territorial liderada por Nariño con 14.830 contratos, seguido por Cundinamarca (6.884) y Santander (5.990). Posteriormente se encuentran Tolima (5.429), Antioquia (5.302) y Bolívar (5.248), lo que indica una participación relevante pero más equilibrada entre estos territorios.Nariño se mantiene como el departamento con mayor actividad contractual en ambos periodos.
## Top municipios
El análisis de municipios muestra una fuerte concentración en San Andrés de Tumaco con 4.277 contratos, seguido por Providencia (2.058) y San José del Guaviare (1.909). También destacan Bogotá D.C. (1.496), Inírida (1.195) y Medellín (1.102). Esto evidencia que algunos municipios concentran una parte importante de la actividad contractual.El liderazgo cambia al ampliar el periodo.
## Entidades con más contratos
Las entidades con mayor número de contratos están lideradas por la Alcaldía de Tumaco con 3.873 registros, seguida por la Alcaldía de Providencia con 1.881 y la Gobernación de Guainía con 896. También destacan otras gobernaciones y entidades territoriales, lo que evidencia una alta participación de entidades locales.Caso contrario en el último mes predominan cámaras de comercio y entidades locales.
## Fechas faltantes
El análisis muestra que 17.224 registros no cuentan con información sobre la fecha de firma, inicio y fin de ejecución del contrato, lo que limita el análisis temporal y de duración de los procesos contractuales.
## Rango de fechas
El dataset cubre el periodo comprendido entre el 26 de diciembre de 2025 y el 24 de marzo de 2026, lo que corresponde aproximadamente a tres meses de actividad contractual.
## Contratos por día
Se observa un patrón claro en la distribución diaria: los días hábiles concentran la mayor cantidad de contratos, mientras que los fines de semana presentan una caída significativa en la actividad. Esto es consistente con el funcionamiento institucional del sector público, donde la mayor parte de los procesos se gestionan en días laborales.
