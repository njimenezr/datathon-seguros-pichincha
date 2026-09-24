# Guía del Participante — Datathon Grupo Pichincha · equipo **Seguros del Pichincha**

> **Bienvenido.** Hoy vas a generar valor de negocio combinando datos de **Deuna, Banco
> Pichincha y Seguros del Pichincha** — sin que ninguna empresa vea la información sensible
> de la otra. Todo con **datos 100% sintéticos** y colaboración segura vía **Clean Rooms**.

---

## 🥇 La regla de oro

1. **Todos los datos son sintéticos.** No hay PII real. Puedes explorar con libertad.
2. **El valor está en el cruce seguro.** Tu empresa sola ve poco; combinada con las otras, ve
   mucho. El Clean Room te deja cruzar **sin exponer** los datos crudos del otro.
3. **La llave de cruce es `id_cliente_hash`** (un SHA-256 de la cédula). Nunca verás la cédula
   real: solo el hash, que permite unir a la misma persona entre empresas.

---

## 1. Entra al trial de tu empresa

- Tu equipo pertenece a **Seguros del Pichincha**.
- Usa el **login compartido** que te dio el organizador para el workspace (trial) de Seguros.
- **Carga tus datos:** sube este repo como **Git folder** y corre **`cargar_datos.py`** (crea tu
  catálogo y las 3 tablas desde los Parquet de `datos/`). Tus tablas quedan en:

| Empresa | Tus tablas |
|---|---|
| Seguros | `seguros.clean_room.clientes_seguros` (+ `fact_produccion_individual`, `dim_documento`) |

> **¿Qué significa cada columna y cada término?** Ten a mano el **diccionario de datos +
> glosario de negocio**: [`diccionario.md`](diccionario.md).

## 2. ¿Qué es un Clean Room? (en 3 frases)

- Es una **sala neutral y segura** donde dos o más empresas aportan tablas y ejecutan análisis
  **sin que nadie vea los datos crudos del otro** — solo salen los resultados aprobados.
- Cada empresa se identifica por su **Sharing ID** (el identificador de su metastore).
- En este datathon **tu equipo debe descubrir cómo crear el Clean Room** e invitar a las otras
  empresas (Deuna y Banco) para poder cruzar los datos — **es parte del reto**.

## 3. El día (resumen)

| Hora | Qué pasa |
|---|---|
| 8:30 | Kickoff: tu reto, reglas, rúbrica |
| 9:00 | Setup + crear el Clean Room |
| 10:00 | Hacking con Genie Code |
| 12:30 | Almuerzo |
| 14:00 | Hacking + preparar pitch (congelar 16:00) |
| 16:10 | Pitches (10 min por equipo) |
| 17:35 | Premiación |

## 4. Ve rápido con **Genie Code**

Genie Code (el asistente de IA de Databricks) escribe el SQL, los notebooks y hasta modelos
por ti. Descríbele lo que quieres en español. Ejemplos:
- *"Cruza mi tabla con la del banco por id_cliente_hash y muéstrame los clientes sin seguro."*
- *"Agrega el fact de prima a nivel cliente y detecta quiénes están cancelando."*

## 5. Entrega por niveles (value stack)

Sube tan alto como puedas — cada nivel suma puntos:

| Nivel | Entregable |
|---|---|
| 1 · Insight *(mínimo)* | Cruce en Clean Room + **dashboard AI/BI** que responde tu pregunta |
| 2 · Predicción | Modelo (propensión / churn / riesgo) |
| 3 · Enriquecimiento | AI Functions (`ai_classify`, `ai_gen` para ofertas, `ai_summarize`) |
| 4 · Conversacional | **Genie Space** sobre los datos combinados |
| 5 · Producto *(bonus)* | Un **agente** o **Databricks App** de next-best-action |

## 6. Consejos para el pitch (10 min)

- Cuenta una **historia de negocio**: problema → qué cruzaste → qué descubriste → **impacto** ($, % retención, # clientes).
- Muestra que el cruce fue **seguro** (Clean Room, no exportaste datos crudos).
- Si tienes Genie/agente, **deja que el jurado le pregunte en vivo** — es el mejor cierre.
- Menos slides, más demo.

**¡Éxitos! 🚀**
