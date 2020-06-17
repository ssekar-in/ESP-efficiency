from esp_eff import efficiency
from esp_conf import esp_con
import click

sca1 = esp_con()
wk = click.prompt("wk=", type=float, default=.18)

print("sca=", sca1, "efficiency = ", efficiency(wk, sca1))

