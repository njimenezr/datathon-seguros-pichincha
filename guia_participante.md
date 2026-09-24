# Guía del participante — SEGUROS DEL PICHINCHA

Tu equipo pertenece a **Seguros del Pichincha**. Esta guía **no** te dice cómo resolver el reto ni
cómo crear el Clean Room (eso lo descubren ustedes). Solo te da lo mínimo para arrancar y, sobre
todo, **qué tener en cuenta antes de compartir datos** con otra empresa.

## 1. Carga tus datos

1. Sube este repo como **Git folder** en tu workspace (Workspace → Create → Git folder → URL).
2. Corre **[`cargar_datos.py`](cargar_datos.py)** → crea tus 3 tablas en `seguros.clean_room`
   (`clientes_seguros`, `dim_documento`, `fact_produccion_individual`).
3. Consulta **[`diccionario.md`](diccionario.md)** para entender cada campo.

## 2. Es un reto colaborativo

El valor está en **combinar datos entre empresas** del grupo. Nadie les va a decir qué cruzar:
**hablen con los equipos de Banco y Deuna**, acuerden qué información intercambiar y **descubran
juntos cómo montar el Clean Room** e invitarse. La llave para unir personas es `id_cliente_hash`.

## 3. Antes de compartir datos, piénsalo (esto es parte del reto y de la nota)

Manejas datos sensibles de asegurados. Compartirlos entre compañías **no es "publicar la tabla y
ya"**. Antes de exponer tus datos a otra empresa en el Clean Room, tu equipo debería **decidir y
justificar** cómo los protege. No es una receta — son las cosas a tener en cuenta:

- **Minimización** — comparte solo las columnas y filas necesarias para el caso de uso; nada más.
- **Anonimización / seudonimización** — no expongas identificadores directos. La llave de cruce
  ya es un **hash** (`id_cliente_hash`), no la cédula. ¿Hay otros campos que permitan reidentificar?
- **Enmascaramiento (masking)** — ofusca o transforma columnas sensibles (primas, coberturas)
  antes de compartir.
- **Seguridad por fila (RLS) / vistas** — limita qué filas o qué agregados ve la otra empresa.
  Ojo: el `fact_produccion_individual` es muy granular — ¿conviene compartir el detalle o un
  resumen por cliente?
- **Propósito, consentimiento y retención** — ¿para qué se comparte?, ¿por cuánto tiempo?, ¿está
  dentro del propósito para el que se recogió el dato?
- **Agregación** — a veces compartir métricas agregadas basta y expone mucho menos que el detalle.

> El jurado valora explícitamente el **cruce seguro** (ver [`rubrica.md`](rubrica.md)): tomar y
> explicar estas decisiones **suma puntos**.

## 4. Marco legal (Ecuador)

Tenlo en cuenta: la **Ley Orgánica de Protección de Datos Personales (LOPDP)** de Ecuador y su
**Reglamento General** regulan cómo se tratan y comparten datos personales. Léelo como referencia:
**[`referencias/reglamento-lopdp-ecuador.pdf`](referencias/reglamento-lopdp-ecuador.pdf)**.

## 5. Prepara tu pitch

Usa **[`pitch/plantilla_pitch.html`](pitch/plantilla_pitch.html)** para contar el valor de negocio,
la demo y **cómo cuidaste los datos**.

---
*Datos 100% sintéticos. Contenido educativo para el Datathon Grupo Pichincha.*
