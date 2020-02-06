# 个人hassio配置

```
config/
│  automations.yaml
│  configuration.yaml
│  ui-lovelace.yaml
│
├─customize
│      binary_sensors.yaml
│      groups.yaml
│      lights.yaml
│      sensors.yaml
│      switches.yaml
│
├─integrations
│  │  discovery.yaml
│  │  groups.yaml
│  │  history.yaml
│  │  homekit.yaml
│  │  logbook.yaml
│  │  media_player.yaml
│  │  pihole.yaml
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
│  │      pi_cpu_temp.yaml
│  │
│  ├─switch
│  │      shelly_switch.yaml
│  │      template_switch.yaml
│  │
│  ├─xiaomi_aqara
│  │      gateway.yaml
│  │
│  └─yeelight
│          light_strip.yaml
│          night_light.yaml
│          toilet_light.yaml
│
├─node-red
│     flows.json
│     settings.js
│
└─themes
        dark_green.yaml
        light_blue.yaml
        palms.yaml
```