import io
import json
from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

from .. import D3DWorld
from ..id import local_id
from ..items import all_items
from ..levels import all_episodes, all_levels

BASE_DIR = Path(__file__).parent.parent


DEPENDENCIES = [
    BASE_DIR / "resources" / "ap_config.json",
    BASE_DIR / "resources" / "ARCHIPELAGO.CON",
    BASE_DIR / "resources" / "DUKE3DAP.CON",
    BASE_DIR / "resources" / "Tiles020.ART",
]

ID_MAP = BASE_DIR / "resources" / "id_map.json"


def update_ids():
    sprite_id_idx = 1
    sector_id_idx = 1800
    exit_id_idx = 1700

    all_ids = {"locations": {}, "items": {}}
    for level in all_levels:
        for location in level.locations.values():
            loc_id = -1
            if location.type == "sprite":
                loc_id = sprite_id_idx
                sprite_id_idx += 1
            elif location.type == "sector":
                loc_id = sector_id_idx
                sector_id_idx += 1
            elif location.type == "exit":
                loc_id = exit_id_idx
                exit_id_idx += 1
            if loc_id > 0:
                all_ids["locations"][location.name] = loc_id
    for item in all_items.values():
        all_ids["items"][item.name] = local_id(item.ap_id)

    checksum = sha256()
    checksum.update(json.dumps(all_ids, indent=None).encode("utf-8"))
    all_ids["checksum"] = checksum.hexdigest()

    with io.open(ID_MAP, "w") as out_file:
        out_file.write(json.dumps(all_ids, indent=2))


def generate_ap_config():
    ap_config = {
        "game": D3DWorld.game_full_name,
        "game_id": D3DWorld.build_game_id,
        "episodes": {},
        "locations": {},
        "items": {},
    }

    # level metadata
    for episode in all_episodes:
        episode_data = {
            "name": episode.name,
            "volumenum": episode.volumenum,
            "levels": {},
        }
        for level in episode.levels:
            episode_data["levels"][level.prefix] = {
                "name": level.name,
                "levelnum": level.levelnum,
                "unlock": local_id(all_items[level.unlock].ap_id),
            }
            level_locations = {"sprites": {}, "sectors": {}, "exits": {}}
            for location in sorted(level.locations.values(), key=lambda x: x.game_id):
                short_name = location.name[len(level.prefix) + 1 :]
                category = location.type + "s"
                level_locations[category][str(location.game_id)] = {
                    "id": local_id(D3DWorld.location_name_to_id[location.name]),
                    "name": short_name,
                }
                if location.sprite_type:
                    level_locations[category][str(location.game_id)][
                        "type"
                    ] = location.sprite_type
            ap_config["locations"][level.prefix] = level_locations

        ap_config["episodes"][f"E{episode.volumenum + 1}"] = episode_data

    # items
    for item in sorted(all_items.values(), key=lambda x: x.ap_id):
        item_data = {
            "name": item.name,
            "type": item.type,
        }
        if item.persistent:
            item_data["persistent"] = True
        if item.unique:
            item_data["unique"] = True
        if item.silent:
            item_data["silent"] = True
        item_data.update(**item.props)

        ap_config["items"][str(local_id(item.ap_id))] = item_data

    with io.open(BASE_DIR / "resources" / "ap_config.json", "w") as out_file:
        out_file.write(json.dumps(ap_config, indent=2))


def bundle_grp(target: Path):
    # update ids for consistency
    update_ids()
    generate_ap_config()
    out = ZipFile(target, "w")
    for dep in DEPENDENCIES:
        out.write(dep, dep.name)


if __name__ == "__main__":
    bundle_grp(BASE_DIR / "resources" / "DUKE3DAP.zip")
