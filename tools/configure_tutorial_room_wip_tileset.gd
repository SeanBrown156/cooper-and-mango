extends SceneTree

const TILESET_PATH := "res://assets/environments/tutorial_room/composite/tutorial_room_wip_tileset.tres"
const TILE_SIZE := 16.0
const WALL_SOURCE := 4
const FLOOR_SOURCE := 1

func _initialize() -> void:
	var tile_set := load(TILESET_PATH) as TileSet
	if tile_set == null:
		push_error("Could not load WIP TileSet")
		quit(1)
		return

	if tile_set.get_physics_layers_count() == 0:
		tile_set.add_physics_layer()
	tile_set.set_physics_layer_collision_layer(0, 1)
	tile_set.set_physics_layer_collision_mask(0, 1)

	if not tile_set.has_custom_data_layer_by_name("role"):
		var role_layer := tile_set.get_custom_data_layers_count()
		tile_set.add_custom_data_layer()
		tile_set.set_custom_data_layer_name(role_layer, "role")
		tile_set.set_custom_data_layer_type(role_layer, TYPE_STRING)
	if not tile_set.has_custom_data_layer_by_name("solid"):
		var solid_layer := tile_set.get_custom_data_layers_count()
		tile_set.add_custom_data_layer()
		tile_set.set_custom_data_layer_name(solid_layer, "solid")
		tile_set.set_custom_data_layer_type(solid_layer, TYPE_BOOL)

	if tile_set.get_terrain_sets_count() == 0:
		tile_set.add_terrain_set()
		tile_set.add_terrain(0)
		tile_set.set_terrain_name(0, 0, "Domestic Floor")
		tile_set.add_terrain(0)
		tile_set.set_terrain_name(0, 1, "Domestic Wall")

	for source_id in range(tile_set.get_source_count()):
		var source := tile_set.get_source(source_id) as TileSetAtlasSource
		if source == null:
			continue
		var texture := source.texture
		var columns := int(texture.get_width() / TILE_SIZE)
		var rows := int(texture.get_height() / TILE_SIZE)
		for y in range(rows):
			for x in range(columns):
				var coords := Vector2i(x, y)
				if not source.has_tile(coords):
					continue
				var data := source.get_tile_data(coords, 0)
				var is_wall := source_id == WALL_SOURCE and y < 6
				data.set_custom_data("role", "wall" if is_wall else "floor")
				data.set_custom_data("solid", is_wall)
				if source_id == WALL_SOURCE:
					data.set_terrain_set(0)
					data.set_terrain(1 if is_wall else 0)
				if is_wall:
					data.set_collision_polygons_count(0, 1)
					data.set_collision_polygon_points(0, 0, PackedVector2Array([
						Vector2(0, 0), Vector2(TILE_SIZE, 0),
						Vector2(TILE_SIZE, TILE_SIZE), Vector2(0, TILE_SIZE),
					]))

	var error := ResourceSaver.save(tile_set, TILESET_PATH)
	if error != OK:
		push_error("Could not save configured WIP TileSet: " + str(error))
		quit(1)
		return
	print("Configured WIP TileSet metadata, collision, and domestic floor/wall terrains")
	quit(0)
