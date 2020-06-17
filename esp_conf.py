from typing import Any, Union

import click


def esp_con():
    no_esp = click.prompt("no of esps", type=int, default=1)
    no_passes = click.prompt("no of passes per esp", type=int, default=1)
    no_ducts = click.prompt("no ducts per pass", type=int, default=20)
    duct_width = click.prompt(" duct width", type=float, default=.3)
    no_series_sections = click.prompt("series sections", type=int, default=5)
    length = click.prompt("length of section", type=float, default=3.6)
    height = click.prompt("height of section", type=float, default=15)

    area_per_section = no_ducts * 2 * length * height
    total_coll_area = area_per_section * no_series_sections * no_passes * no_esp
    cross_section = height * no_ducts * duct_width
    total_cross_section = cross_section * no_passes * no_esp
    flow = click.prompt("total flow, actual m3/s", type=float, default=100.)
    sca: Union[float, Any] = total_coll_area / flow
    velocity = flow / total_cross_section
    print("TCA=", total_coll_area, "velocity =", velocity, "SCA= ", sca)
    return sca


# print(esp_con())
