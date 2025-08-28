<p align="center">
  <img src="https://lh3.googleusercontent.com/proxy/sdiuSV3YQdI3m1oOjjpGaqoE33ShTtn7Ba2MrkComBn9-wQ_L2osGSLbvL2fbKPye2_eAaHralh9NbjpwHBV_Me9NbRceNu8MbAQY76YzpYV6FxNQQGVT54sYxawlmgqaLXw" alt="Banner del Proyecto" width="100%" style="max-height:250px; max-width:600px;">
</p>


# Detección de Anomalías en el RPI

Prototipo de machine learning para **detectar anomalías en trámites de inhibiciones del RPI**, apoyando la validación manual de los registros.

## Objetivo
Desarrollar un prototipo funcional que detecte posibles irregularidades en los registros del RPI, adaptable a trámites de inhibiciones, según los datos accesibles. El sistema generará alertas claras para apoyar la validación manual y mejorar la transparencia.

## Participantes

- [@Baudano Walter](https://github.com/Chuni3)
- [@Lin Cain](https://github.com/DarkLin02)
- [@Quiroga Juan Pablo](https://github.com/Nickrosfire)
- [@Quiroga Agustin](https://github.com/guccho6w9)

## Tecnologías utilizadas

**Desarrollo y programación:** Python, SQL

**Control de versiones y repositorio:** Git, GitHub

**Entorno de trabajo y productividad:** Google Colab, Google Docs, Notion, Trello

**Comunicación:** WhatsApp

## FAQ

<details>
  <summary>¿A quién está dirigido?</summary>
  Este proyecto está dirigido al área de **Inhibiciones** del Registro de la Propiedad Inmueble de la provincia de Santiago del Estero.
</details>
<details>
    <summary>¿Qué necesidad cubre?</summary>
  La solución está diseñada para **asistir a los empleados** en la carga y levantamiento de inhibiciones.  
Cuando se sube una inhibición a la base de datos, el modelo analiza los datos e identifica posibles **anomalías**, por ejemplo:  
- Un **CUIL** que no coincida con el **DNI**.  
- Una **carátula** que no esté asociada a ninguna causa.  

Si se detecta alguna anomalía, el sistema genera una **alerta** para que el usuario decida si continuar con la carga o corregir el error, evitando inconsistencias en la base de datos.
</details>

## Feedback

Si tiene algún comentario, póngase en contacto con nosotros
📬 Contacto: [cain.sebastian.lin@gmail.com](mailto:cain.sebastian.lin@gmail.com)

---

> ⚠️ **Aviso de confidencialidad:**  
> Este proyecto contiene datos **confidenciales** de la organización.  
> El código disponible utiliza **datos de ejemplo** y su uso es solo con fines educativos.
