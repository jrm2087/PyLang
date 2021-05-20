# TraductorPy

Esta librería te ayudara a traducir el texto que necesites utilizar.

## Instalación 
Para instalar y ejecutar este proyecto, simplemente escriba y ejecute
```py
    pip install traductorPy
```
## Uso  
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

|   Idioma  | Valor |
|-----------|-------|
| Alemán    |**DE** |
| Búlgaro   |**BG** |
| Checo     |**CS** |
| Chino     |**ZH** |
| Danés     |**DA** |
| Eslovaco  |**SK** |
| Esloveno  |**SL** |
| Español   |**ES** |
| Estonio   |**ET** |
| Finés     |**FI** |
| Francés   |**FR** |
| Griego    |**EL** |
| Húngaro   |**HU** |
| Inglés    |**EN** |
| Italiano  |**IT** |
| Japonés   |**JA** |
| Letón     |**LV** |
| lituano   |**LT** |
| neerlandés|**NL** |
| polaco    |**PL** |
| portugués |**PT** |
| rumano    |**RO** |
| ruso      |**RU** |
| sueco     |**SV** |