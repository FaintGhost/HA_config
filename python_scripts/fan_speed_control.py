speed = data.get('fan_speed')
status_speed = hass.states.get('input_text.status_fan_speed')

if speed is not None:
    speed = int(speed)
    last_speed = int(status_speed.state) if status_speed.state else 1
    if 1 <= speed <= 3:
        if speed > last_speed:
            loop = speed - last_speed
        else:
            loop = (3 - last_speed) + speed

        service_data = {'entity_id': 'remote.harmony',
                        'device': '69866819', 'command': 'speed'}
        for i in range(loop):
            hass.services.call('remote', 'send_command', service_data, False)
            time.sleep(0.5)
#         else:
#             logger.warning(
#                 '<fan_speed_control> Received fan speed is invalid ({})'.format(fan_speed))
# else:
#     logger.warning('<fan_speed_control> Received fan speed is invalid (None)')
