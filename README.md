# GrowCube Home Assistant Integration

![License](https://img.shields.io/badge/License-MIT-green.svg)  
![HACS Supported](https://img.shields.io/badge/HACS-yes-blue.svg)  
![Home Assistant](https://img.shields.io/badge/HA-%3E%3D2025.4.0-orange.svg)

A custom Home Assistant integration for the GrowCube smart planter. Monitor soil moisture and watering events, trigger automations, and visualize plant health right from your Home Assistant dashboard.

---

## Features

- **Soil Moisture Sensor**: Real-time percentage reading of soil moisture.
- **Watering Events**: Track last watered timestamp.
- **Binary Alert Sensor**: “Needs watering” flag when moisture drops below a threshold.
- **Config Flow**: GUI-based setup in Settings → Devices & Services.
- **HACS-Ready**: One-click install and automatic updates via HACS.
- **Translatable**: English (default) with easy JSON translation file.

---

## Requirements

- Home Assistant **2025.4.0** or newer
- GrowCube device on the same LAN
- API key for your GrowCube (see device docs)

---

## Installation

### 1. Add via HACS

1. In Home Assistant, go to **Settings → Integrations → HACS**.
2. Click **“+” → Custom repository**.
3. Paste this repository’s URL:  
   ```
   https://github.com/DanStasiak/growcube-hass-integration
   ```
4. Select **Integration**, click **Add**.
5. After installation, restart Home Assistant.

### 2. Manual Install

1. Clone or download this repo.
2. Copy the `custom_components/growcube/` folder into your HA `config/` directory.
3. Ensure the structure is:
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
4. Restart Home Assistant.

---

## Configuration

1. In Home Assistant, navigate to **Settings → Devices & Services**.
2. Click **“Add Integration”** and search for **GrowCube**.
3. Enter:
   - **Host**: IP or hostname of your GrowCube.
   - **API Key**: Your device’s API key.
4. Click **Submit**. The integration will create one or more sensors.

---

## Entities

| Entity ID                          | Type          | Description                               |
| ---------------------------------- | ------------- | ----------------------------------------- |
| `sensor.growcube_moisture`         | Sensor        | Current soil moisture (%).               |
| `sensor.growcube_last_watered`     | Sensor        | Timestamp of last watering event.        |
| `binary_sensor.growcube_needs_water` | Binary Sensor | `on` if moisture < threshold.            |

> **Tip:** Adjust the “needs watering” threshold in your automations or via an options flow (coming soon).

---

## Example Lovelace Card

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

---

## Troubleshooting

- **Integration not found**  
  - Confirm you installed into `custom_components/growcube/`
  - Check Home Assistant logs (`Settings → Logs`) for errors.

- **Invalid host or API key**  
  - Verify network connectivity and correct credentials.
  - Test with `curl http://<host>/api/status?api_key=<key>`.

- **Sensor remains unavailable**  
  - Ensure your GrowCube firmware is up to date.
  - Restart Home Assistant after any config changes.

---

## Contributing

1. Fork the repo and create your branch:  
   ```bash
   git checkout -b feature/my-feature
   ```
2. Make your changes and add tests where appropriate.
3. Submit a pull request describing your improvements.

Please follow semantic versioning and update `manifest.json` accordingly.

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


