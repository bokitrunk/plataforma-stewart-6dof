# ✈️ Guía de integración: Simulink (Aerospace Blockset) + FlightGear

Esta guía describe el procedimiento para conectar un modelo de simulación de dinámica de vuelo en Simulink con el motor gráfico FlightGear mediante comunicación UDP NetFDM.

---

## 🛠️ Requisitos previos
* MATLAB / Simulink con **Aerospace Blockset** e **Simulink Coder** instalados.
* **FlightGear Flight Simulator** instalado en el sistema.

---

## 🛰️ Protocolo de comunicación (NetFDM over UDP)

Simulink actúa como el motor dinámico (FDM - Flight Dynamics Model) y FlightGear actúa únicamente como el renderizador visual en tiempo real.

* **Dirección IP:** `127.0.0.1` (localhost) o IP del equipo en red local.
* **Puerto UDP:** `5502`
* **Protocolo:** `native-fdm` (NetFDM v24)
* **Frecuencia de refresco recomendada:** 60 Hz - 100 Hz.

---

## ⚙️ Argumentos de inicio para FlightGear

Al ejecutar FlightGear, se debe pausar la dinámica interna y escuchar las consignas de Simulink mediante el comando:

```bash
fgfs --fdm=null --native-fdm=socket,in,60,,5502,udp --aircraft=c172p