# Diccionario de datos y glosario — Seguros del Pichincha

Guía de referencia para el equipo de **Seguros**: qué datos tienes, qué significa cada columna
y qué quiere decir cada término de negocio.

> **Todo es sintético.** Cédulas, montos, pólizas y clientes son ficticios (cero PII). Las
> estructuras imitan las reales de Seguros del Pichincha.
>
> **Llave de cruce:** `id_cliente_hash` (SHA-256 de la cédula). Es el único campo con el que
> unirás a la misma persona con **Banco** y **Deuna** dentro del Clean Room.

---

## 1. Tus tablas (mapa rápido)

| Tabla | 1 fila = | Filas aprox. | Columnas |
|---|---|---|---|
| `seguros.clean_room.clientes_seguros` | un asegurado (resumen) | ~60 000 | 27 |
| `seguros.clean_room.dim_documento` | una póliza/documento (puente) | ~141 000 | 9 |
| `seguros.clean_room.fact_produccion_individual` | un **movimiento de prima** | ~1 680 000 | 14 |

> Cruzarás con **Banco** y **Deuna** por `id_cliente_hash`. **Descubrirás el esquema de las
> otras empresas dentro del Clean Room** — no está en este diccionario.

---

## 2. Glosario cross-company (aplica a todos)

- **`id_cliente_hash`** — huella SHA-256 de la cédula. Igual en las 3 empresas para la misma
  persona → permite cruzar sin exponer la cédula real.
- **Clean Room** — sala limpia de datos: cada empresa comparte tablas para analizarlas en
  conjunto **sin ver la fila cruda de la otra**. Ahí se hace el join gobernado.
- **Overlap / cruce** — personas que aparecen en más de una empresa (misma `id_cliente_hash`).
- **Gap de cross-sell** — clientes de otra empresa que **no** son asegurados tuyos: la
  oportunidad de vender pólizas.
- **Cross-sell** — venderle a un cliente actual del grupo un producto de otra línea/empresa.
- **Churn / retención** — abandono del cliente (churn) vs. acciones para conservarlo (retención).
- **Next-Best-Action (NBA)** — la siguiente mejor oferta o acción recomendada por cliente.
- **PII** — datos personales identificables. Aquí no hay: todo es sintético y hasheado.

---

## 3. Diccionario de datos

Convención: **tipo** · **dominio/rango** · descripción de negocio.

### 3.1 `clientes_seguros` (tabla de cruce, nivel cliente)

Resumen por asegurado. Sus métricas son **rollups calculados del fact** (ver 3.3) vía
`dim_documento`. Es la tabla que unes a Banco/Deuna.

| Columna | Tipo | Dominio / rango | Descripción |
|---|---|---|---|
| `id_cliente_hash` | string | SHA-256 | **Llave de cruce** (hash de la cédula). |
| `edad` | int | 18–77 | Edad del asegurado. |
| `genero` | string | F / M | Género. |
| `ciudad` | string | — | Ciudad. |
| `canal_preferente` | string | AGENCIA · BROKER · DIGITAL · BANCASEGUROS | Canal principal de contratación. |
| `antiguedad_anios` | int | 1–20 | Años como asegurado. |
| `num_polizas` | int | ≥ 1 | Documentos/pólizas del cliente. |
| `num_ramos` | int | 1–5 | Ramos distintos contratados. |
| `ramo_principal` | string | VIDA · AUTO · SALUD · HOGAR · ASIST_MEDICA | Ramo más frecuente del cliente. |
| `producto_principal` | string | id de producto | `producto_id` más frecuente del cliente. |
| `meses_relacion` | int | ≥ 0 | Meses desde la póliza más antigua. |
| `prima_total_anual` | double | ≥ 0 (USD) | **Σ de prima positiva** del cliente. Valor del cliente. |
| `prima_neta_anual` | double | (USD) | Σ de prima (positiva + negativa). |
| `prima_promedio_mov` | double | (USD) | Prima promedio por movimiento. |
| `ticket_prima_promedio` | double | ≥ 0 (USD) | `prima_total_anual / num_movimientos_12m`. |
| `num_movimientos_12m` | int | ≥ 0 | Movimientos de prima del cliente. |
| `num_upselling` | int | ≥ 0 | Movimientos de UPSELLING (expansión). |
| `num_downselling` | int | ≥ 0 | Movimientos de DOWNSELLING (reducción). |
| `num_reactivaciones` | int | ≥ 0 | Movimientos de REACTIVACION. |
| `num_primer_pago` | int | ≥ 0 | Movimientos de PRIMER_PAGO. |
| `num_cancelaciones_12m` | int | ≥ 0 | Movimientos con `considerar_cancelacion=1`. Señal de fuga. |
| `num_terminaciones` | int | ≥ 0 | Movimientos de TERMINACION (fuga). |
| `tasa_cancelacion` | double | [0, 1] | `num_cancelaciones_12m / num_movimientos_12m`. |
| `pct_movimientos_negativa` | double | [0, 1] | Proporción de movimientos NEGATIVA. |
| `segmento_valor` | string | ALTO · MEDIO · BAJO | Por `prima_total_anual`. |
| `segmento_riesgo` | string | ALTO · MEDIO · BAJO | Por `num_cancelaciones_12m`. |
| `estado_cliente` | string | VIGENTE · EN_RIESGO · RETIRADO | Estado según cancelaciones/terminaciones. |

### 3.2 `dim_documento` (puente)

Permite llevar el fact a nivel cliente. Una fila = un documento/póliza.

| Columna | Tipo | Dominio / rango | Descripción |
|---|---|---|---|
| `documento_id` | string | jerárquico | PK del documento (`agencia-ramo-secuencia`). |
| `id_cliente_hash` | string | SHA-256 | **Llave de cruce** hacia el asegurado. |
| `agencia` | int | 1–40 | Agencia comercial. |
| `ramo` | string | VIDA · AUTO · SALUD · HOGAR · ASIST_MEDICA | Ramo del seguro. |
| `tipo_poliza` | string | = `ramo` | Alias de ramo. |
| `fecha_alta_poliza` | date | — | Fecha de alta de la póliza. |
| `estado_poliza` | string | VIGENTE · POR_RENOVAR · EN_MORA | Estado de la póliza. |
| `num_movimientos_doc` | int | ≥ 0 | Movimientos de prima del documento (rollup del fact). |
| `prima_acumulada_doc` | double | ≥ 0 (USD) | Σ de prima positiva del documento. |

### 3.3 `fact_produccion_individual` (detalle transaccional)

Una fila = **un movimiento de prima**. Replica el modelo real de producción de Seguros. Sigue
un árbol de dependencias: `tipo_prima → tipo_movimiento_uds → {considerar_cancelacion,
clasificacion_produccion_id, prima_individual, numero_cuota} → fechas`.

| Columna | Tipo | Dominio / rango | Descripción |
|---|---|---|---|
| `fact_id` | bigint | único | PK del movimiento. |
| `documento_id` | string | FK → `dim_documento` | Documento/póliza al que pertenece el movimiento. |
| `producto_id` | string | 289 valores (heavy-tail) | Producto comercial (un producto concentra ~64%). |
| `numero_factura` | string | alta cardinalidad | Identificador de factura (no sensible). |
| `cotizacion_codigo` | string | alta cardinalidad | Código de cotización (no sensible). |
| `numero_cuota` | bigint | 1–18 (NULL ~1.08%) | Nº de cuota de la prima. Muy concentrada en 1. |
| `fecha_registro` | date | 2025-01-01 → 2026-09-13 | Fecha del movimiento. |
| `origen_registro` | string | SISTEMA TRANSACCIONAL (99.97%) · AJUSTES MANUALES | Origen del registro. |
| `prima_individual` | decimal | ± (USD); 3.67% ceros | Valor de la prima. **Signo = `tipo_prima`.** |
| `fecha_emision` | date | ≤ `fecha_registro` | Emisión del documento. |
| `tipo_prima` | string | **POSITIVA** (95.25%) · **NEGATIVA** (4.75%) | **Raíz.** Define el signo de la prima. |
| `considerar_cancelacion` | int | 0/1 | Bandera de cancelación. **=0 si POSITIVA**; en NEGATIVA sube con TERMINACION. |
| `tipo_movimiento_uds` | string | DOWNSELLING · UPSELLING · SIN_CAMBIO · PRIMER_PAGO · TERMINACION · REACTIVACION · (NULL) | Tipo de movimiento comercial. |
| `clasificacion_produccion_id` | bigint | 1–33 | Clasificación de producción (condicionada a tipo_prima × movimiento). |

> **Para llevar el fact a nivel cliente:** `fact_produccion_individual JOIN dim_documento
> USING (documento_id)` y agrega por `id_cliente_hash`. Los rollups más útiles ya están
> pre-calculados en `clientes_seguros`.

---

## 4. Glosario de negocio — Seguros

- **Póliza / documento** — contrato de seguro. Aquí, un `documento_id` en `dim_documento`.
- **Ramo** — línea de seguro (VIDA, AUTO, SALUD, HOGAR, ASIST_MEDICA).
- **Prima** — lo que paga el asegurado por la cobertura. **`prima_total_anual`** = suma de las
  primas positivas del cliente.
- **`tipo_prima`** — **POSITIVA** (ingreso de prima: venta/renovación) o **NEGATIVA**
  (devolución/ajuste a la baja). Define el **signo** de `prima_individual`.
- **`prima_individual`** — valor de un movimiento de prima (positivo o negativo según tipo_prima).
- **`tipo_movimiento_uds`** — tipo de movimiento comercial de la venta:
  - **UPSELLING** — el cliente sube de cobertura/valor (expansión).
  - **DOWNSELLING** — baja de cobertura/valor (reducción).
  - **SIN_CAMBIO** — movimiento sin variación de venta.
  - **PRIMER_PAGO** — primer pago de una póliza nueva.
  - **TERMINACION** — fin de la póliza (fuga / cancelación total).
  - **REACTIVACION** — la póliza se reactiva.
- **`considerar_cancelacion`** — bandera (0/1) de si el movimiento cuenta como cancelación.
  Solo aplica a NEGATIVA; se concentra en TERMINACION. Señal fuerte de fuga.
- **`clasificacion_produccion_id`** — clasificación interna del movimiento (Venta Nueva /
  Renovación / Cancelación / Anulación), condicionada a tipo_prima × movimiento.
- **`numero_cuota`** — número de cuota de la prima (1–18); casi siempre 1.
- **Certificado** — nivel intermedio del modelo (documento → certificado → póliza → ramo → agencia).
- **Bancaseguros** — venta de seguros a través del canal bancario.
- **`segmento_valor` / `segmento_riesgo` / `estado_cliente`** — resúmenes derivados: valor (por
  prima), riesgo (por cancelaciones) y estado (VIGENTE / EN_RIESGO / RETIRADO).
- **Prima neta (`prima_neta_anual`)** — suma de prima positiva **y** negativa (producción neta,
  descontando devoluciones/cancelaciones). La `prima_total_anual` cuenta solo la positiva.
- **Prima promedio (`prima_promedio_mov`) / ticket de prima (`ticket_prima_promedio`)** — prima
  media por movimiento y prima total sobre nº de movimientos.
- **Tasa de cancelación (`tasa_cancelacion`)** — cancelaciones / movimientos; % de fuga del cliente.
- **Ramo principal (`ramo_principal`) / nº de ramos (`num_ramos`)** — línea dominante y variedad
  de coberturas contratadas.
- **Meses de relación (`meses_relacion`)** — antigüedad desde la póliza más antigua.

---

## 5. ¿Qué puedes responder?

- ¿Quién genera más prima? ¿quién está cancelando (TERMINACION) o en riesgo de fuga?
- ¿Qué ramos concentran upselling / downselling?
- ¿Qué **gap de protección** existe entre los clientes de Banco y los dueños de comercios de Deuna
  que **aún no tienen póliza**?
- Cruzando en el Clean Room: ¿los que cancelan seguro tienen peor perfil financiero? ¿cuánta
  prima potencial vale el gap no asegurado? ¿el churn de Deuna anticipa la cancelación de seguros?

---

## 6. Cómo cruzar (recordatorio)

La única llave es **`id_cliente_hash`**. Primero, agrega tu fact a nivel cliente:

```sql
-- Prima y cancelaciones por cliente (rollup del fact)
SELECT d.id_cliente_hash,
       SUM(CASE WHEN f.prima_individual > 0 THEN f.prima_individual END) AS prima_total,
       SUM(f.considerar_cancelacion)                                     AS cancelaciones
FROM fact_produccion_individual f
JOIN dim_documento d USING (documento_id)
GROUP BY d.id_cliente_hash;
```

Luego, dentro del **Clean Room**, une `clientes_seguros` (o tu rollup) con las tablas que
compartan Banco y Deuna **por `id_cliente_hash`**. El esquema de esas tablas lo verás cuando
ellas se agreguen al Clean Room — descúbrelo ahí.
