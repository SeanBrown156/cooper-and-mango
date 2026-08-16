extends SceneTree

const TILE_SIZE := Vector2i(16, 16)
const OUTPUT := "res://assets/environments/tutorial_room/composite/tutorial_room_wip_tileset.tres"
const SHEETS := [
	"res://assets/environments/tutorial_room/wip/recoloured/atlas_16x_cm.png",
	"res://assets/environments/tutorial_room/wip/recoloured/tiles/Floors_only_16x16_cm.png",
	"res://assets/environments/tutorial_room/wip/recoloured/tiles/Room_Builder_Floors_16x16_cm.png",
	"res://assets/environments/tutorial_room/wip/recoloured/tiles/Tileset_16x16_3_cm.png",
	"res://assets/environments/tutorial_room/wip/recoloured/tiles/floorswalls_LRK_cm.png",
]

func _initialize() -> void:
	var tile_set := TileSet.new()
	tile_set.tile_size = TILE_SIZE

	var source_index := 0
	for sheet_path in SHEETS:
		var texture := load(sheet_path) as Texture2D
		if texture == null:
			push_error("Could not load WIP tile sheet: " + sheet_path)
			quit(1)
			return

		var source := TileSetAtlasSource.new()
		source.texture = texture
		source.texture_region_size = TILE_SIZE
		var columns := texture.get_width() / TILE_SIZE.x
		var rows := texture.get_height() / TILE_SIZE.y
		for y in range(rows):
			for x in range(columns):
				source.create_tile(Vector2i(x, y))
		tile_set.add_source(source, source_index)
		source_index += 1

	var error := ResourceSaver.save(tile_set, OUTPUT)
	if error != OK:
		push_error("Could not save WIP TileSet: " + str(error))
		quit(1)
		return

	print("Created WIP TileSet with %d intact atlas sources: %s" % [SHEETS.size(), OUTPUT])
	quit(0)
