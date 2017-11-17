import config
import datetime
import time
import cayenne.client as Cayenne
from pycirculate.anova import AnovaController

# Define channels used
CHAN_R_CURR_TEMP=0
CHAN_R_SET_TEMP=1
CHAN_R_POWER=2
CHAN_W_SET_TEMP=3
CHAN_W_POWER=4

def on_message(message):
  print("message: " + str(message))

  if message.channel == CHAN_W_SET_TEMP:
    print("Set temperature cmd received to: " + message.value)
    ctrl.set_temp(message.value)
  if message.channel == CHAN_W_POWER:
    if (message.value == '1'):
      print("Anova started!")
      ctrl.start_anova()
    else:
      print("Anova stopped")
      ctrl.stop_anova()

# Cayenne Intialize
client = Cayenne.CayenneMQTTClient()
client.on_message = on_message
client.begin(config.MQTT_USER, config.MQTT_PASS, config.MQTT_CLIENT)

ctrl = AnovaController(config.ANOVA_MAC)

def main():
  print datetime.datetime.now()
  print ctrl.set_unit('f')

  timestamp = 0
  status = 0

  while True:
    client.loop()
    if (time.time() > timestamp + 10):
      # Send current temp reading
      client.virtualWrite(CHAN_R_CURR_TEMP, ctrl.read_temp(), Cayenne.TYPE_TEMPERATURE, Cayenne.UNIT_FAHRENHEIT)

      # Send the set temp reading
      client.virtualWrite(CHAN_R_SET_TEMP, ctrl.send_command_async("read set temp"), Cayenne.TYPE_TEMPERATURE, Cayenne.UNIT_FAHRENHEIT)

      # Send the run status
      status = 0 if (ctrl.anova_status() == 'stopped') else 1
      client.virtualWrite(CHAN_R_POWER, status)

      timestamp = time.time()

if __name__ == "__main__":
  main()
