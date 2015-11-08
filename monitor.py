import subprocess
from time import sleep

if __name__=="__main__":
    while True:
        sleep(60)
        #every minute, check battery level and if it's below 5%, create an alert
        full = int(subprocess.check_output(["cat", "/sys/class/power_supply/BAT0/energy_full_design"]))
        now = int(subprocess.check_output(["cat", "/sys/class/power_supply/BAT0/energy_now"]))

        percent = (100 * now) / float(full)

        if percent < 10:
            subprocess.call(["notify-send", "-i", "error", "Battery at 10%"])
