import json

def loadGcode(path):
  with open(path) as f:
    lines = f.read()
  return lines

def loadJson(path):
  with open(path) as f:
    lines = f.read()
  return json.loads(lines)

def updateJson(obj, path):
  with open(path, "w") as f:
    f.write(json.dumps(obj, indent=4))

creator_pro_path = 'resources/definitions/creator_pro.def.json'
creatorpro_extruder_1_path = 'resources/extruders/creatorpro_extruder_1.def.json'
creatorpro_extruder_2_path = 'resources/extruders/creatorpro_extruder_2.def.json'

creator_pro = loadJson(creator_pro_path)
creator_pro['settings']['single_gcode']['default_value'] = loadGcode("src/start_gcode.gcode")
creator_pro['settings']['dual_gcode']['default_value'] = loadGcode("src/dual_start_gcode.gcode")
creator_pro['overrides']['machine_end_gcode']['default_value'] = loadGcode("src/stop_gcode.gcode")

creatorpro_extruder_1 = loadJson(creatorpro_extruder_1_path)
creatorpro_extruder_1['overrides']['initial_pos_gcode']['default_value'] = loadGcode("src/init_right.gcode")
creatorpro_extruder_1['overrides']['nozzle_wipe_gcode']['default_value'] = loadGcode("src/wipe_right.gcode")

creatorpro_extruder_2 = loadJson(creatorpro_extruder_2_path)
creatorpro_extruder_2['overrides']['initial_pos_gcode']['default_value'] = loadGcode("src/init_left.gcode")
creatorpro_extruder_2['overrides']['nozzle_wipe_gcode']['default_value'] = loadGcode("src/wipe_left.gcode")

updateJson(creator_pro, creator_pro_path)
updateJson(creatorpro_extruder_1, creatorpro_extruder_1_path)
updateJson(creatorpro_extruder_2, creatorpro_extruder_2_path)
