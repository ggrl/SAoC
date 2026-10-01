import src.targeting as targeting
import time
import importlib
import configs.UI_config as UI_config

UI_config.current = importlib.import_module(f"configs.UI_config_{1920}")

print(targeting.get_px_hh(2))
print(targeting.get_px('healthbar', 'red'))
list1 = targeting.get_px_hh(2)
print('erster wert: ', list1[0])
time.sleep(2)