# traductorPy
## Idiomas Disponibles
Los idiomas disponibles se deben indicar en los parámetros **lan_source** y **lan_to** de la función **translater**. Por defecto si no se envían traduce de español a inglés.

### Idiomas:


- **DE** - alemán
- **BG** - búlgaro
- **CS** - checo
- **ZH** - chino
- **DA** - danés
- **SK** - eslovaco
- **SL** - esloveno
- **ES** - español
- **ET** - estonio
- **FI** - finés
- **FR** - francés
- **EL** - griego
- **HU** - húngaro
- **EN** - inglés
- **IT** - italiano
- **JA** - japonés
- **LV** - letón
- **LT** - lituano
- **NL** - neerlandés
- **PL** - polaco
- **PT** - portugués
- **RO** - rumano
- **RU** - ruso
- **SV** - sueco


## Instalación 
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