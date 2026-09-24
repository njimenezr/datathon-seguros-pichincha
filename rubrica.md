# Rúbrica de evaluación — Datathon Grupo Pichincha

El jurado califica cada equipo en **4 criterios** con la escala 1-5, y aplica el peso de cada
uno. El puntaje final es la suma ponderada (máximo 5.0).

| Criterio | Peso |
|---|---|
| 1. Valor de negocio | **35%** |
| 2. Cruce seguro / uso del Clean Room | **30%** |
| 3. Calidad técnica (+ bonus por productos Databricks) | **20%** |
| 4. Pitch / storytelling | **15%** |

---

## 1. Valor de negocio — 35%

*¿El resultado sirve y es accionable? ¿Cuantifica el impacto?*

| Nivel | Descriptor |
|---|---|
| 1 | Insight genérico, sin acción ni impacto claro. |
| 2 | Insight relevante pero vago; no se aterriza en una acción. |
| 3 | Insight accionable para el negocio. |
| 4 | Accionable + estimación de impacto ($, # clientes, % retención/loss ratio). |
| 5 | Accionable, cuantificado y priorizado; se ve el ROI y el siguiente paso. |

## 2. Cruce seguro / uso del Clean Room — 30%

*¿Colaboraron de forma segura, sin exponer PII, usando bien el Clean Room?*

| Nivel | Descriptor |
|---|---|
| 1 | No lograron el cruce cross-company. |
| 2 | Cruce logrado pero fuera del Clean Room / expusieron datos. |
| 3 | Clean Room creado y cruce por `id_cliente_hash` correcto. |
| 4 | Clean Room bien gobernado (solo salen agregados/resultados aprobados). |
| 5 | Uso ejemplar: colaboración multi-empresa, gobierno claro, cero PII expuesta. |

## 3. Calidad técnica — 20%

*¿La solución funciona y está bien construida? Bonus por usar más productos Databricks.*

| Nivel | Descriptor |
|---|---|
| 1 | No corre / resultados poco confiables. |
| 2 | Funciona parcialmente. |
| 3 | Solución que corre y es correcta (nivel 1-2 del value stack). |
| 4 | Sólida + sube el value stack (modelo con MLflow, AI Functions o Genie). |
| 5 | Robusta y **muestra varios productos** (Clean Rooms + ML + AI Functions + Genie/Agente/App). |

> **Bonus (hasta +0.3):** cada producto Databricks adicional bien usado suma. Nivel 5 del value stack (agente/app) es el techo.

## 4. Pitch / storytelling — 15%

*¿Comunican claro el problema, la solución y el impacto en 10 min?*

| Nivel | Descriptor |
|---|---|
| 1 | Confuso, sin hilo. |
| 2 | Se entiende pero le falta impacto/estructura. |
| 3 | Claro: problema → solución → impacto. |
| 4 | Claro y convincente, con datos que respaldan. |
| 5 | Excelente + **demo en vivo** (el jurado le pregunta al Genie/agente del equipo). |

---

## Hoja de punteo por equipo

| Equipo: __________________ | Empresa: __________ | Jurado: __________ |
|---|---|---|

| Criterio | Peso | Puntaje (1-5) | Ponderado (peso × puntaje / 5) |
|---|---|---|---|
| 1. Valor de negocio | 0.35 | ____ | ____ |
| 2. Cruce seguro / Clean Room | 0.30 | ____ | ____ |
| 3. Calidad técnica (+bonus) | 0.20 | ____ | ____ |
| 4. Pitch / storytelling | 0.15 | ____ | ____ |
| **TOTAL** | | | **____ / 5.0** |

Comentarios del jurado:
_____________________________________________________________________
_____________________________________________________________________
