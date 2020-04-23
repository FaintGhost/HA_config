# 个人hassio配置

```
config/
│  automations.yaml
│  configuration.yaml
│  home-assistant.log
│  home-assistant_v2.db
│  README.md
│  secrets.yaml
│  ui-lovelace.yaml
│
├─customize
│      binary_sensors.yaml
│      lights.yaml
│      sensors.yaml
│      switches.yaml
│
├─deps
├─integrations
│  │  discovery.yaml
│  │  history.yaml
│  │  homekit.yaml
│  │  logbook.yaml
│  │  logger.yaml
│  │  mqtt.yaml
│  │  scripts.yaml
│  │  weather.yaml
│  │  zone.yaml
│  │
│  ├─light
│  │      ceiling_light.yaml
│  │      doorway_light.yaml
│  │      kitchen_light.yaml
│  │
│  ├─sensor
│  │      load_power_temp.yaml
│  │      networkmap.yaml
│  │      pi_cpu_temp.yaml
│  │      power_consumed_temp.yaml
│  │
│  ├─switch
│  │      shelly_switch.yaml
│  │      wol.yaml
│  │
│  ├─xiaomi_aqara
│  │      gateway.yaml.DISABLED
│  │
│  └─yeelight
│          light_strip.yaml.DISABLED
│          night_light.yaml
│          toilet_light.yaml
│
├─themes
│      dark_green.yaml
│      google_light_theme.yaml
│      green_dark_mode.yaml
│      light_blue.yaml
│      palms.yaml
│
└─www
    └─zigbee2mqtt-networkmap
            zigbee2mqtt-networkmap.js
            zigbee2mqtt-networkmap.js.gz
```