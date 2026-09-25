# singleton-observable-py 
 
Una clase base reutilizable que agrega los patrones Singleton y Observer 
a cualquier clase de Python, sin tener que reescribir el mecanismo cada vez. 
 
## Instalación 
 
Copia `singleton_observable.py` a tu proyecto (por ahora no está publicada en PyPI). 
 
## Uso básico 
 
```python 
from singleton_observable import SingletonObservable 
 
class MiGestor(SingletonObservable): 
 def __init__(self): 
 if not hasattr(self, "datos"): 
 self.datos = [] 
 
 def registrar(self, dato): 
 self.datos.append(dato) 
 self.notificar(dato) 
``` 
 
## Por qué usarla 
 
- Garantiza una única instancia por cada clase que herede de ella (Singleton). 
- Permite suscribir funciones que se ejecutan automáticamente ante cada evento (Observer). 
- Cada clase que hereda mantiene su propio singleton, sin mezclarse con otras. 
 
## Licencia 
 
MIT License

Copyright (c) [2026] [Rommel Valda]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.