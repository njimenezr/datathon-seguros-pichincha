# Datathon Grupo Pichincha — equipo **Seguros del Pichincha**

Bienvenido al datathon del **Grupo Pichincha**. El reto es **generar valor de negocio
combinando datos entre las empresas del grupo** (Deuna, Banco Pichincha y Seguros del
Pichincha) de forma **segura**, usando **Databricks Clean Rooms** — sin que ninguna empresa
vea la información cruda de la otra.

> **Todos los datos son sintéticos** (cero PII). Las estructuras imitan las reales de Seguros.

## Tu rol: Seguros del Pichincha

Tú aportas el **modelo real de producción de seguros**, en 3 tablas:

- `seguros.clean_room.clientes_seguros` — resumen por asegurado (**tabla de cruce**).
- `seguros.clean_room.dim_documento` — puente póliza → cliente.
- `seguros.clean_room.fact_produccion_individual` — ~1.68M **movimientos de prima**.

Sabes producción de prima, upsell/downsell, cancelaciones y retención. Tu oportunidad está en
la gente que **aún no tiene póliza** (clientes de Banco y dueños de comercios de Deuna) y en
usar señales de riesgo que hoy no ves para tarifar y retener mejor.

## Quick start

1. Lee **[`reto.md`](reto.md)** — tu desafío de negocio y los entregables por nivel.
2. Ten a mano **[`diccionario.md`](diccionario.md)** — qué significa cada columna y cada término.
3. Revisa **[`rubrica.md`](rubrica.md)** — cómo te evalúa el jurado.
4. Prepara tu presentación con **[`pitch/plantilla_pitch.html`](pitch/plantilla_pitch.html)**.
5. Guía general del día: **[`guia_participante.md`](guia_participante.md)**.

## Importante

- **Tu equipo arma el Clean Room.** No hay guía paso a paso: **descubran cómo crearlo** e
  invitar a Deuna y Banco para cruzar los datos — es parte del reto.
- La **llave de cruce** entre empresas es siempre **`id_cliente_hash`**.
- Tus datos ya estarán **cargados en tu workspace** el día del evento.
- Ve rápido con **Genie Code** (el asistente de IA de Databricks): descríbele en español lo que
  quieres y te escribe el SQL, los notebooks y los modelos.

¡Éxitos! 🚀
