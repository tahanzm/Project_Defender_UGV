# 🛡️ Defender UGV - Autonomous Surveillance & Reconnaissance Vehicle
**Version:** 1.0 | **Status:** In Design Phase | **Stack:** ROS 2 Humble & Gazebo

## 🎯 Proje Tanımı
Defender UGV, tehlikeli bölgelerde keşif ve gözetleme yapmak amacıyla tasarlanmış, **Raspberry Pi 5** (High-Level) ve **Pixhawk** (Low-Level) mimarisi üzerine kurulu otonom bir İnsansız Kara Aracı (İKA) projesidir. Proje, Savunma Sanayi standartlarına uygun olarak **V-Model SDLC** prensipleriyle geliştirilmektedir.

## 🚀 Temel Özellikler (Requirements)

### 1. Seyrüsefer (Navigation)
* **REQ-NAV-01 (Waypoint Mission):** GPS tabanlı otonom nokta takibi.
* **REQ-NAV-02 (Obstacle Avoidance):** Statik ve dinamik engellerden kaçınma.
* **REQ-NAV-03 (RTL):** Görev bitiminde kalkış noktasına güvenli dönüş.
* **REQ-NAV-04 (Patrol Mode):** Belirlenen hat üzerinde sürekli devriye.

### 2. Algılama ve Yapay Zeka (Perception)
* **REQ-VIS-01 (YOLOv8):** "İnsan" ve "Tehdit" unsurlarının gerçek zamanlı tespiti.
* **REQ-VIS-02 (Visual Tracking):** Tespit edilen hedefin görüntü merkezinde tutulması (Visual Servoing).
* **REQ-VIS-03 (Mode Selection):** "Gözlem" ve "Önleme/Takip" modları arası geçiş.

### 3. Sistem Mimarisi
* **Yazılım:** Ubuntu 22.04 LTS, ROS 2 Humble, Python, C++.
* **Donanım:** Raspberry Pi 5 (AI & Decision Making) + Pixhawk 4 (Motor Control).
* **Simülasyon:** Gazebo Classic (Digital Twin Verification).
* **Haberleşme:** MAVLink & DDS (Micro-ROS).

---
*Developed by Taha N. | Computer Engineering Student*
