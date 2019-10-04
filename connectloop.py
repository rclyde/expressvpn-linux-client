#!/usr/bin/python3

import subprocess, os

dns_src = ["/etc/resolv.conf.localhost", "/etc/resolv.conf.nordvpn"]
dns_tgt = "/etc/resolv.conf"
cnt     = ["jpto3", "frpa1", "hk4", "defr", "usla5", "frpa2", "hk5", "denu", "ussf2", "ukwe", "jpto1", "usnj1", "jpto2", "itmi", "frst"]
LOG_FILE= "out.file"

for country in cnt:

	# empty log file
	open(LOG_FILE, 'w').close()

	# connect
	subprocess.call(["/usr/bin/expressvpn disconnect"],         shell=True)
	subprocess.call(["sudo cp " + dns_src[1] + " " + dns_tgt],  shell=True)
	subprocess.call("/usr/bin/expressvpn connect " + country + " | tee " + LOG_FILE, shell=True)

	# read log
	f_out = open(LOG_FILE, "r")
	out   = f_out.read()
	f_out.close()

	# loop or stop
	print("FUNCTION OUTPUT: " + out)
	if "Connected to" in out:
		print("CONNECTED! breaking...")
		break
	else:
		print("FAIL TO CONNECT. looping...")
