# Análisis Financiero con datos de Yahoo Finance y MongoDB

## Descripción

Este proyecto utiliza la biblioteca `yfinance` para obtener datos financieros de varias empresas y los almacena en una base de datos MongoDB. Los datos recopilados incluyen información sobre empresas como el nombre, el sector, el CEO y datos financieros clave como el impuesto sobre la renta, la depreciación, el EBITDA, los gastos de interés y el beneficio bruto.

## Instalación

Para instalar las dependencias del proyecto, asegúrate de tener `yfinance`, `pandas` y `pymongo` instalados en tu entorno Python. Puedes instalarlos utilizando pip:

```
pip install yfinance pandas pymongo
```

##Uso
Para ejecutar el código, simplemente ejecuta el script main.py. Asegúrate de tener una instancia de MongoDB en ejecución y especifica la dirección IP y el puerto correctos en la variable client.

bash
Copy code
python main.py
Contribución
Si deseas contribuir al proyecto, puedes abrir issues para informar sobre problemas o sugerir mejoras. También puedes enviar pull requests con cambios propuestos.

Ejemplo de Resultado
python
Copy code
[
    {
        "Nombre de la empresa": "Tesla, Inc.",
        "Sector": "Consumer Cyclical",
        "CEO": "Elon Reeve Musk",
        "Edad del CEO": 50,
        "Volumen promedio": 16528784,
        "Tax Rate For Calcs": 0.11,
        "Reconciled Depreciation ": 3172000000,
        "EBITDA ": 5375000000,
        "Interest Expense": 561000000,
        "Gross Profit": 6706000000
    },
    {
        "Nombre de la empresa": "Netflix, Inc.",
        "Sector": "Communication Services",
        "CEO": "Reed Hastings",
        "Edad del CEO": 61,
        "Volumen promedio": 4442937,
        "Tax Rate For Calcs": 0.218,
        "Reconciled Depreciation ": 373442498,
        "EBITDA ": 5399060058,
        "Interest Expense": 318158673,
        "Gross Profit": 17776718096
    },
    # Más datos de otras empresas...
]
Licencia
Este proyecto está bajo la Licencia MIT.

Enlaces
Documentación de yfinance
Documentación de pymongo
Esta es solo una estructura sugerida, puedes personalizarla según tus necesidades y la complejidad del proyecto. Recuerda que el objetivo principal es hacer que la información sea clara y accesible para otros desarrolladores.
