# GrowCube Home Assistant Integration

![License](https://img.shields.io/badge/License-MIT-green.svg)  
![HACS Supported](https://img.shields.io/badge/HACS-yes-blue.svg)  
![Home Assistant](https://img.shields.io/badge/HA-%3E%3D2025.4.0-orange.svg)

A custom Home Assistant integration for the GrowCube smart planter. Monitor soil moisture, track watering events, get alerts when plants need water, and build automations—all from your Home Assistant dashboard.

---

## Table of Contents

1. [Features](#features)  
2. [Prerequisites](#prerequisites)  
3. [Installation](#installation)  
   - [HACS (Recommended)](#add-via-hacs)  
   - [Manual Install](#manual-install)  
4. [Configuration Reference](#configuration-reference)  
5. [Entities & Attributes](#entities--attributes)  
6. [Lovelace Examples](#lovelace-examples)  
7. [Troubleshooting](#troubleshooting)  
8. [Advanced Usage](#advanced-usage)  
9. [Contributing](#contributing)  
10. [License](#license)  

---

## Features

- **Soil Moisture Sensor**: Real‐time percentage reading of soil moisture  
- **Last Watered Sensor**: Timestamp of the most recent watering event  
- **Needs Water Binary Sensor**: Flags when moisture falls below your threshold  
- **GUI Setup**: Native Config Flow (no YAML needed)  
- **HACS-Ready**: One-click install + automatic updates  
- **Translatable**: JSON-based language files  

---

## Prerequisites

- Home Assistant **2025.4.0** or newer  
- GrowCube device accessible on your LAN  
- API key for your GrowCube (see your device’s docs)  

---

## Installation

### Add via HACS (Recommended)

1. In Home Assistant go to **Settings → Integrations → HACS**  
2. Click **“+” → Custom repository**  
3. Paste this repo’s URL:  
   ```
   https://github.com/DanStasiak/growcube-hass-integration
   ```  
4. Select **Integration**, click **Add**  
5. Restart Home Assistant  

### Manual Install

1. Clone or download this repo  
2. Copy `custom_components/growcube/` into your HA `config/` folder  
3. Confirm structure:
   ```
   config/
   └── custom_components/
       └── growcube/
           ├── __init__.py
           ├── manifest.json
           ├── config_flow.py
           ├── sensor.py
           └── translation/
               └── en.json
   ```
4. Restart Home Assistant  

---

## Configuration Reference

> **Note:** Config Flow is preferred; YAML is still supported for advanced users.

### Config Flow Options

| Option               | Type    | Required | Default | Description                                        |
| -------------------- | ------- | -------- | ------- | -------------------------------------------------- |
| **Host**             | string  | yes      | —       | IP or hostname of your GrowCube                    |
| **API Key**          | string  | yes      | —       | Your device’s API key                              |
| **Poll Interval**    | integer | no       | 300     | Seconds between updates                            |
| **Moisture Threshold** | integer | no       | 30      | % moisture below which the **Needs Water** sensor turns `on` |

### (Optional) YAML Example

```yaml
growcube:
  host: 192.168.1.50
  api_key: YOUR_API_KEY_HERE
  poll_interval: 600            # poll every 10 minutes
  moisture_threshold: 25        # alert when < 25%
```

---

## Entities & Attributes

| Entity ID                          | Type          | Description                               |
| ---------------------------------- | ------------- | ----------------------------------------- |
| `sensor.growcube_moisture`         | Sensor        | Current soil moisture (%)                 |
|   • `.state`                       | string        | Moisture reading (e.g. “42”)              |
|   • `.attributes.battery_level`    | integer       | Device battery (%) (when available)       |
| `sensor.growcube_last_watered`     | Sensor        | Timestamp of last watering event          |
|   • `.state`                       | datetime      | e.g. “2025-05-19T18:22:00+00:00”          |
| `binary_sensor.growcube_needs_water` | Binary Sensor | `on` if moisture < threshold; otherwise `off` |

---

## Lovelace Examples

### Simple Entities Card

```yaml
type: entities
title: GrowCube Status
entities:
  - entity: sensor.growcube_moisture
    name: Soil Moisture
  - entity: binary_sensor.growcube_needs_water
    name: Needs Water
  - entity: sensor.growcube_last_watered
    name: Last Watered
```

### ApexCharts Card

```yaml
type: custom:apexcharts-card
graph_span: 24h
header:
  show: true
  title: Soil Moisture (Last 24 h)
series:
  - entity: sensor.growcube_moisture
    name: Moisture %
    type: column
```

*(Requires [apexcharts-card](https://github.com/RomRider/apexcharts-card))*  

---

## Troubleshooting

- **Integration Not Found**  
  - Verify `custom_components/growcube/manifest.json` exists  
  - Check HA logs: **Settings → System → Logs**

- **Invalid Host/API Key**  
  - Ping your GrowCube from the HA host  
  - Test with `curl http://<host>/api/status?api_key=<key>`

- **Sensor Unavailable or `unknown`**  
  - Increase `poll_interval` if your device sleeps  
  - Update GrowCube firmware to latest version  

---

## Advanced Usage

- **InfluxDB + Grafana**  
  ```yaml
  influxdb:
    reports:
      - entity: sensor.growcube_moisture
      - entity: sensor.growcube_last_watered
  ```
  Import [this Grafana dashboard JSON](./extras/grafana-dashboard.json) for ready-made charts.

- **Automation Blueprint**  
  Save under `blueprints/automation/growcube/needs_water.yaml` and invoke to send notifications when your plants need watering.

---

## Contributing

1. Fork the repo & create a branch  
   ```bash
   git checkout -b feature/my-feature
   ```
2. Add tests if you add or change logic  
3. Submit a PR with a clear changelog entry  

Please follow [Semantic Versioning](https://semver.org/) and update `version` in `manifest.json`.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---

## ☕ Support This Project

If you found this useful, you can support future work here:

<a href="https://buymeacoffee.com/dstasiak" target="_blank">
  <img src="https://img.shields.io/badge/Buy%20me%20a%20coffee-%23FFDD00.svg?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me A Coffee">
</a>

---


