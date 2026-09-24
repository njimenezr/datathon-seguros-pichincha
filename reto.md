# Reto SEGUROS DEL PICHINCHA — Cross-sell al gap y pricing por riesgo real

## Contexto de negocio

Eres el equipo de datos de **Seguros del Pichincha**. Sabes todo de tus asegurados, pero
tu mayor oportunidad está en la gente que **aún no tiene póliza** — y esa gente son clientes
del **Banco** y dueños de comercios de **Deuna**. Además, para tarifar bien necesitas señales
de riesgo que tú no ves y ellos sí. Un **Clean Room** te permite llegar a ese universo y
mejorar el pricing sin exponer datos sensibles de las otras compañías.

## Pregunta central

> **¿A quién del grupo (banco/Deuna) sin póliza deberíamos ofrecerle qué seguro, y cómo
> segmentar el riesgo para tarifar mejor usando su perfil financiero y transaccional?**

## Tus datos — modelo real de Seguros (3 tablas en `seguros.clean_room`)

Trabajas con el **modelo de producción**: un fact de movimientos de prima, su puente de
documentos, y un resumen por cliente que es tu llave hacia el resto del grupo.

| Tabla | Grano | Úsala para |
|---|---|---|
| `fact_produccion_individual` (~1.68M) | 1 movimiento de prima | Retención (TERMINACION / `considerar_cancelacion`), upsell/downsell, tendencia de prima |
| `dim_documento` (~141k) | 1 documento/póliza | **Puente** `documento_id → id_cliente_hash` (para agregar el fact a nivel cliente) |
| `clientes_seguros` (~60k) | 1 asegurado | **Cruce cross-company** por `id_cliente_hash` + rollups listos |

**`clientes_seguros` trae 27 columnas de rollups listos:** `id_cliente_hash` (llave),
`prima_total_anual`, `prima_neta_anual`, `prima_promedio_mov`, `ticket_prima_promedio`,
`num_polizas`, `num_ramos`, `ramo_principal`, `producto_principal`, `meses_relacion`,
`num_upselling`, `num_downselling`, `num_reactivaciones`, `num_primer_pago`,
`num_cancelaciones_12m`, `num_terminaciones`, `tasa_cancelacion`, `pct_movimientos_negativa`,
`segmento_valor`, `segmento_riesgo`, `estado_cliente` (VIGENTE/EN_RIESGO/RETIRADO), `edad`,
`ciudad`, `canal_preferente`. (`dim_documento` suma `num_movimientos_doc` y `prima_acumulada_doc`.)

**En el fact:** `tipo_prima` (POSITIVA/NEGATIVA), `prima_individual` (signo = tipo_prima),
`tipo_movimiento_uds` (UPSELLING/DOWNSELLING/TERMINACION/…), `considerar_cancelacion`,
`numero_cuota`, `producto_id`, `fecha_registro`. Regla de oro: si `tipo_prima='POSITIVA'` →
prima ≥ 0 y `considerar_cancelacion=0`.

> Para llevar el fact a nivel cliente: `fact JOIN dim_documento USING(documento_id)` y agrega
> por `id_cliente_hash`. Los rollups más útiles ya están en `clientes_seguros`.

## Datos que obtienes vía Clean Room

- **Banco** (`clientes_banco`): `sub_segmento`, `saldo_cuentas`, `score_buro`, `flag_mora_30d`, `maximo_cupo_tc`… → capacidad de pago y riesgo del prospecto.
- **Deuna** (`comercios_deuna`): `monto`, `num_transacciones`, `segmento`… → actividad económica del dueño-comercio.

**Llave de cruce:** `id_cliente_hash`. El **gap** clave: ~40k clientes de banco y ~70k dueños de Deuna **sin póliza**.

## Pistas (señal real en los datos)

- El **`score_buro` / mora** del banco correlaciona con tus **cancelaciones y terminaciones**
  (`score_buro ↔ num_terminaciones ≈ −0.27`, `flag_mora_30d ↔ num_cancelaciones ≈ +0.14`) →
  úsalo para pricing, suscripción y **modelo de retención**.
- La **afluencia** (saldos del banco) se asocia a **mayor prima total** (`saldo_cuentas ↔
  prima_total_anual ≈ +0.19`) → dimensiona la prima potencial del gap.
- El **churn de Deuna** correlaciona con tus cancelaciones (`prob_desercion ↔ num_cancelaciones
  ≈ +0.19`) → señal temprana de fuga multi-empresa.
- Los prospectos de **bajo riesgo y alta afluencia** son los más rentables para cross-sell.

## Entregables por nivel (sube tan alto como puedas)

1. **Insight** *(obligatorio)*: cruce en Clean Room + dashboard AI/BI del gap de cross-sell y del riesgo por segmento.
2. **Predicción** *(obligatorio)*: modelo de propensión a contratar póliza **o** un modelo de **retención/cancelación** (predecir `num_cancelaciones`/TERMINACION) para pricing y salvamento, con features del banco/Deuna. MLflow.
3. **Enriquecimiento**: `ai_classify` (segmento de prospecto), `ai_gen` (propuesta de póliza personalizada).
4. **Conversacional**: Genie Space que responda "¿cuántos clientes AFLUENTE del banco sin seguro tienen bajo riesgo?".
5. **Agente / App** *(bonus)*: agente que recomiende el ramo + prima estimada por prospecto, o app para bancaseguros.

## Ideas de insight

- Dimensionar el **$ de prima potencial** del gap no asegurado (banco + Deuna).
- Micro-segmentar el gap por afluencia × riesgo para priorizar campañas.
- Recargo/descuento de prima según señales de riesgo del banco (mora, score).

## Criterios de éxito

- Cruce **dentro del Clean Room**, sin exponer PII.
- Resultado **accionable** con **impacto cuantificado** (prima potencial, # prospectos, mejora de loss ratio).
- Pitch con demo en vivo (Genie/agente).
