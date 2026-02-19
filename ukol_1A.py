# importuje knihovny
import time


# vykona ukon 50x
for _ in range(50):
	
	# Presune efektor na home pozici
	dType.SetPTPCmd(api, 2, 217, -161, 10, 0, 1)
	time.sleep(0.5)
	
	# Presune efektor nad pozici kresleni
	dType.SetPTPCmd(api, 2, 280, 15, 10, 0, 1)
	time.sleep(0.5)
	
	# Nakresli tecku 
	dType.SetPTPCmd(api, 2, 280, 15, -64, 0, 1)
	time.sleep(0.5)
	dType.SetPTPCmd(api, 2, 280, 15, 10, 0, 1)




