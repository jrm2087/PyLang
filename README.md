# TraductorPy

Esta librería te ayudara a traducir el texto que necesites utilizar.


## Demo
Si desea ver más sobre el proyecto puede visitar [este Link.](https://github.com/jrm2087/PyLang)


## Instalación 
Para instalar y ejecutar este proyecto, simplemente escriba y ejecute
```py
    pip install traductorPy
```
### Dependencias  
    - Python 3
    - selenium
### Preview

![](/preview.jpg)


#### Uso  
```py
from traductorPy import Traductor
```
```py
translate = 'Hola mundo !'
lan_source = 'ES'
lan_to = 'PT'
print(Traductor.translater(translate, lan_source, lan_to))
```
> Olá mundo!
```py
print(Traductor.translater(translate))
```
> Hello world !

#### Propiedades de translater

|Propiedad | Tipo | Descripción     | Uso                   | Valor por Defecto |
|----------|------|-----------------|-----------------------|-------------------|
|lan_source|string|Idioma           |lan_source ="DE"       |       EN          |
|lan_to    |string|Idioma           |lan_to ="DE"           |       ES          |
|translate |string|Texto a traducir |translate ="Hola MundO"|       ''          |


# Idiomas Disponibles

| Idioma            |
|---------------    |
|**DE** - alemán    |
|**BG** - búlgaro   |
|**CS** - checo     |
|**ZH** - chino     |
|**DA** - danés     |
|**SK** - eslovaco  |
|**SL** - esloveno  |
|**ES** - español   |
|**ET** - estonio   |
|**FI** - finés     |
|**FR** - francés   |
|**EL** - griego    |
|**HU** - húngaro   |
|**EN** - inglés    |
|**IT** - italiano  |
|**JA** - japonés   |
|**LV** - letón     |
|**LT** - lituano   |
|**NL** - neerlandés|
|**PL** - polaco    |
|**PT** - portugués |
|**RO** - rumano    |
|**RU** - ruso      |
|**SV** - sueco     |

