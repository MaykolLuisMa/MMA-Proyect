# Informe

## Integrantes
Davier Sánchez Bello C412

Maykol Luis Martínez Rodríguez C412

José Carlos Pendás C412

Max Bonachea C412

David Alba C412

## Resumen:
Este programa pertenece a una serie de proyectos vinculados a la gestión de las defensas de tesis en MATCOM. El objetivo de este trabajo es, habiendo confeccionado el tribunal de cada tesis, asignar el horario y lugar para realizar estas. Para realizar esto, cada profesor indica cuál es su preferencia entre los horarios indicados y el programa trata de alcanzar el máximo nivel de cumplimiento posible para sus solicitudes usando los locales disponibles.

## Descripción del problema y consideraciones:
Se ha considerado que todos los locales están disponibles en cualquier horario por lo que, mientras no coincidan dos tesis en el mismo local, estos se asignan de forma arbitraria.

Se asigna 1 hora para cada defensa de tesis, 45 minutos de defensa y un margen de 15 minutos para problemas técnicos. Cada profesor asigna un valor de conveniencia para entre 0 y 3 para cada hora en dependencia de qué horarios prefieran, y el programa asigna los horarios de tal forma que los profesores queden lo más satisfechos posible. 

Los tribunales ya están confeccionados, cada tribunal está compuesto por 5 roles y los profesores asignadoa a cada rol desempeñan una función diferente durante la exposición. Es decir, hay 5 tareas que realizar para cada tesis, cada una con uno o más profesores asignados y nuestro trabajo es indicar el horario para cada tarea, lo que equivale a asignar el horario de sus respectivas tesis.

Nuestro programa permite agregar y eliminar los locales disponibles, modificar la preferencia de cada profesor por cada horario y establecer la fecha de comienzo y la duración total de las defensas (usualmente de 3 días) .
Para las tesis, estas se extraen de un archivo xlsx que debe contener las columnas estudiante, tutor, oponente, presidente, secretario, vocal y local. Los profesores también se extraen de aquí, casi cualquier texto en la casilla indicada será considerado un profesor, estos se separarán por comas, sin embargo no se admiten caracteres ? por considerarse que indica falta de información y conduce a errores.    

## Modelo

### Elementos:
Conjunto de profesores P = {1, … , p}

Conjunto de tesis 𝑊 = {1, … , w}

Conjunto de tareas 𝑇 = {1, … , t}

Conjunto 𝐻 = {1, … , h} de horarios de exposición

Conjunto C = {1, … , c} de locales disponibles

$𝑌_𝑤$ Conjunto de tareas asociadas a la tesis 𝑤

$P_{pxh}= $ {$x \in \mathbb{Z}, 0 \leq x \leq 3$} matriz que representa lo conveniente que es para el profesor p realizar una exposición en el horario h

$R_{pxt}= $ { $x \in$ {0,1}} matriz que indica si el profesor p realiza la tarea t

### Variables:

$x_{th} = { 
  { 1    \text{ si la tarea t se realiza en el hora h}} \atop
  { 0 \text{ si se realiza en otro horario  }}
}
$
### Función objetivo:

$\text{max} \sum_t^T{\sum_h^H{c_{th}x_{th}}}
$

Donde $c_{th}$ es la preferencia que tengan los en promedio los profesores asignados a la tarea t por el horario h, y se calcula mediante la fórmula:

$c_{th} = \frac{\sum_p^P{P_{pxh}(p,h)R_{pxt}(p,t)}}{\sum_p^PR_{pxt}}
$

### Restricciones:

(1) $\sum_t^T{R_{pxt}(p,t)x_{th}} \leq 1, \forall{p \in P,\forall{h \in H}}$ 

(2) $c_{th} \geq x_{th},\forall{t \in T,\forall{h \in H}}$

(3) $\frac{1}{5}\sum_t^T{x_{th}} \leq |C|,\forall{h \in H}$

(4) $\sum_t^{Y_w}{x_{th}} = 5y_{wh},\forall{w \in W},\forall{h \in H}$

(5) $\sum_h^H{x_{th}} = 1,\forall{t \in T}$

La restricción (1) garantiza que cada profesor realice como máximo una tarea en un mismo horario.

La restricción (2) garantiza que si a un profesor se le asigna una hora h para realizar una de sus tareas, su conveniencia por esa hora debe ser de al menos 1.

La restricción (3) garantiza que solo se pueden llevar a cabo tantas tesis en una misma hora como locales disponibles hallan, esto se logra usando el hecho de que cada tesis involucra 5 tareas.

La restricción (4) garantiza que todas las tareas vinculadas a una tesis se realizan en el mismo horario que la tesis.

La restricción (5) garantiza que cada tarea solo se realizará una vez.  

### Solución
Para resolver el problema se utilizó la biblioteca pulp de python, especializada en programación lineal.

### Ejecución
Para ejecutar el programa use el comando:

streamlit run src/app.py

Necesitará tener la ya mencionada biblioteca pulp así como streamlit.

### Datos extra:
En caso que se desee agregar nuevas tesis, eliminarla o modificar su tribunal, puede editar el correspondiente archivo tribunales.xlsx en data.