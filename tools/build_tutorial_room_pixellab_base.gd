extends SceneTree

const TILE_SIZE := 16
const ROOM_CELLS := Vector2i(32, 24)
const SOURCE_DIR := "res://assets/environments/tutorial_room_mango/wip/pixellab/tileset"
const SOURCE_STEM := "soft_off-white_plaster_walls_with_a_restrained_dar_"
const ATLAS_PATH := SOURCE_DIR + "/tutorial_room_base_atlas.png"
const TILESET_PATH := "res://assets/environments/tutorial_room_mango/composite/tutorial_room_base_tileset.tres"
const SCENE_PATH := "res://scenes/rooms/tutorial_room_base.tscn"

const FLOOR_TILES := [Vector2i(0, 0), Vector2i(1, 0)]
const WALL_CAP_TILES := [Vector2i(0, 1), Vector2i(1, 1), Vector2i(2, 1), Vector2i(3, 1)]
const WALL_FACE_TILES := [Vector2i(0, 2), Vector2i(1, 2), Vector2i(2, 2), Vector2i(3, 2)]

const PROP_ANCHORS := {
	"WindowCurtainCity": {"position": Vector2(128, 0), "note": "Top-left; 288x80; north-wall fixture"},
	"BedFutonBlue": {"position": Vector2(200, 208), "note": "Bottom-centre; 144x128; head north"},
	"RugGeometric": {"position": Vector2(224, 128), "note": "Top-left; 160x112; flat floor overlay"},
	"DiningWorkTable": {"position": Vector2(424, 176), "note": "Bottom-centre; 80x64; grain east-west"},
	"ChairNorthWest": {"position": Vector2(400, 104), "note": "Bottom-centre; 32x32; faces south"},
	"ChairNorthEast": {"position": Vector2(448, 104), "note": "Bottom-centre; 32x32; faces south"},
	"ChairSouthWest": {"position": Vector2(400, 192), "note": "Bottom-centre; 32x32; faces north"},
	"ChairSouthEast": {"position": Vector2(448, 192), "note": "Bottom-centre; 32x32; faces north"},
	"PaperPendant": {"position": Vector2(424, 144), "note": "Centre pivot; overhead layer"},
	"CatTreeGreen": {"position": Vector2(480, 112), "note": "Bottom-centre; 64x96; north-east wall"},
	"FilipinoFlagBanner": {"position": Vector2(0, 112), "note": "Top-left; 64x96; west-wall fixture"},
	"ClothesRackFull": {"position": Vector2(64, 288), "note": "Bottom-centre; 96x64; west wall"},
	"CarvedStorageChest": {"position": Vector2(232, 384), "note": "Bottom-centre; 80x48; south edge"},
	"ExitDoor": {"position": Vector2(496, 320), "note": "Bottom-centre; 48x64; east wall"},
	"PurpleHoodieFloor": {"position": Vector2(360, 320), "note": "Bottom-centre; 48x32; floor overlay"},
	"MangoSleeping": {"position": Vector2(216, 144), "note": "Bottom-centre; 48x32; bed overlay"},
	"SpiderPlant": {"position": Vector2(352, 240), "note": "Gameplay interaction; keep central route clear"},
}


func _initialize() -> void:
	var atlas := _create_atlas()
	if atlas == null:
		quit(1)
		return
	var atlas_error := atlas.save_png(ProjectSettings.globalize_path(ATLAS_PATH))
	if atlas_error != OK:
		push_error("Could not save Tutorial Room atlas: %s" % error_string(atlas_error))
		quit(1)
		return
	var texture := load(ATLAS_PATH) as Texture2D
	if texture == null:
		texture = ImageTexture.create_from_image(atlas)

	var tile_set := _build_tileset(texture)
	var save_error := ResourceSaver.save(tile_set, TILESET_PATH)
	if save_error != OK:
		push_error("Could not save Tutorial Room TileSet: %s" % error_string(save_error))
		quit(1)
		return

	# Reload so the packed scene stores the TileSet as an external resource.
	tile_set = load(TILESET_PATH) as TileSet
	var room := _build_room_scene(tile_set)
	var packed := PackedScene.new()
	var pack_error := packed.pack(room)
	if pack_error != OK:
		push_error("Could not pack Tutorial Room base: %s" % error_string(pack_error))
		quit(1)
		return
	var scene_error := ResourceSaver.save(packed, SCENE_PATH)
	if scene_error != OK:
		push_error("Could not save Tutorial Room base: %s" % error_string(scene_error))
		quit(1)
		return

	print("Built Gemini-aligned Tutorial Room base: %s" % SCENE_PATH)
	room.free()
	quit(0)


func _create_atlas() -> Image:
	var atlas := Image.create(64, 48, false, Image.FORMAT_RGBA8)
	atlas.fill(Color.TRANSPARENT)

	var floor_a := _load_source(0)
	var floor_b := _load_source(44)
	if floor_a == null or floor_b == null:
		return null
	atlas.blit_rect(floor_a, Rect2i(4, 20, 16, 16), Vector2i(0, 0))
	atlas.blit_rect(floor_b, Rect2i(4, 20, 16, 16), Vector2i(16, 0))

	var wall_sources := [1, 49, 51, 53]
	for column in range(wall_sources.size()):
		var wall := _load_source(wall_sources[column])
		if wall == null:
			return null
		atlas.blit_rect(wall, Rect2i(4, 4, 16, 16), Vector2i(column * 16, 16))
		atlas.blit_rect(wall, Rect2i(4, 12, 16, 16), Vector2i(column * 16, 32))

	return atlas


func _load_source(index: int) -> Image:
	var image := Image.new()
	var path := "%s/%s%d.png" % [SOURCE_DIR, SOURCE_STEM, index]
	var error := image.load(ProjectSettings.globalize_path(path))
	if error != OK:
		push_error("Could not load PixelLab building-kit piece: %s" % path)
		return null
	return image


func _build_tileset(texture: Texture2D) -> TileSet:
	var tile_set := TileSet.new()
	tile_set.tile_size = Vector2i(TILE_SIZE, TILE_SIZE)
	tile_set.add_custom_data_layer()
	tile_set.set_custom_data_layer_name(0, "role")
	tile_set.set_custom_data_layer_type(0, TYPE_STRING)

	var source := TileSetAtlasSource.new()
	source.texture = texture
	source.texture_region_size = Vector2i(TILE_SIZE, TILE_SIZE)
	tile_set.add_source(source, 0)
	for y in range(3):
		for x in range(4):
			if y == 0 and x > 1:
				continue
			var coords := Vector2i(x, y)
			source.create_tile(coords)
			var data := source.get_tile_data(coords, 0)
			data.set_custom_data("role", "floor" if y == 0 else "wall")
	return tile_set


func _build_room_scene(tile_set: TileSet) -> Node2D:
	var root := Node2D.new()
	root.name = "TutorialRoomBase"
	root.editor_description = "512x384 / 32x24 cells. Gemini-aligned shell. Place props at the named Marker2D anchors."

	var floor := TileMapLayer.new()
	floor.name = "Floor"
	floor.tile_set = tile_set
	floor.z_index = -20
	_add_owned(root, floor)
	for y in range(ROOM_CELLS.y):
		for x in range(ROOM_CELLS.x):
			var variant: Vector2i = FLOOR_TILES[(x * 3 + y * 5) % FLOOR_TILES.size()]
			floor.set_cell(Vector2i(x, y), 0, variant)

	var walls := TileMapLayer.new()
	walls.name = "Walls"
	walls.tile_set = tile_set
	walls.z_index = -10
	_add_owned(root, walls)
	for x in range(ROOM_CELLS.x):
		walls.set_cell(Vector2i(x, 0), 0, WALL_CAP_TILES[x % WALL_CAP_TILES.size()])
		walls.set_cell(Vector2i(x, 1), 0, WALL_FACE_TILES[x % WALL_FACE_TILES.size()])
	for y in range(2, ROOM_CELLS.y):
		walls.set_cell(Vector2i(0, y), 0, WALL_CAP_TILES[0])
		if not y in range(16, 20):
			walls.set_cell(Vector2i(ROOM_CELLS.x - 1, y), 0, WALL_CAP_TILES[0])
	for x in range(1, ROOM_CELLS.x - 1):
		walls.set_cell(Vector2i(x, ROOM_CELLS.y - 1), 0, WALL_CAP_TILES[0])

	_add_north_window(root)

	var bounds := StaticBody2D.new()
	bounds.name = "RoomBounds"
	_add_owned(root, bounds)
	_add_bound(root, bounds, "NorthWall", Vector2(256, 16), Vector2(512, 32))
	_add_bound(root, bounds, "SouthWall", Vector2(256, 376), Vector2(512, 16))
	_add_bound(root, bounds, "WestWall", Vector2(8, 208), Vector2(16, 352))
	_add_bound(root, bounds, "EastWallNorth", Vector2(504, 144), Vector2(16, 224))
	_add_bound(root, bounds, "EastWallSouth", Vector2(504, 352), Vector2(16, 64))

	var anchors := Node2D.new()
	anchors.name = "PropAnchors"
	anchors.editor_description = "Editor-only placement guides. Add prop scenes as siblings, then copy the matching marker position."
	_add_owned(root, anchors)
	for anchor_name in PROP_ANCHORS:
		var marker := Marker2D.new()
		marker.name = anchor_name
		marker.position = PROP_ANCHORS[anchor_name]["position"]
		marker.gizmo_extents = 8.0
		marker.editor_description = PROP_ANCHORS[anchor_name]["note"]
		anchors.add_child(marker)
		marker.owner = root

	return root


func _add_north_window(root: Node2D) -> void:
	# The broad city window is the visual anchor of the Gemini room. Keep it
	# architectural and pixel-aligned so props can remain independently editable.
	var daylight := Node2D.new()
	daylight.name = "WindowDaylight"
	daylight.z_index = -19
	_add_owned(root, daylight)
	_add_polygon(root, daylight, "LightFall", PackedVector2Array([
		Vector2(148, 28), Vector2(364, 28), Vector2(416, 208), Vector2(100, 208)
	]), Color(0.78, 0.91, 0.88, 0.16))

	var window := Node2D.new()
	window.name = "NorthWindow"
	window.z_index = -9
	window.editor_description = "Broad north-wall city window; room-defining Gemini composition anchor."
	_add_owned(root, window)
	_add_rect(root, window, "OuterFrame", Rect2(132, 0, 248, 48), Color("493e3a"))
	_add_rect(root, window, "Sky", Rect2(140, 4, 232, 36), Color("9ed2d7"))
	_add_rect(root, window, "CityFar", Rect2(140, 26, 232, 14), Color("71939e"))
	_add_rect(root, window, "CityNear", Rect2(140, 32, 232, 8), Color("526f78"))
	for x in [148, 172, 202, 228, 268, 294, 326, 354]:
		var height := 4 + ((x / 2) as int) % 10
		_add_rect(root, window, "Tower%d" % x, Rect2(x, 40 - height, 10, height), Color("405c66"))
	for x in [196, 256, 316]:
		_add_rect(root, window, "Mullion%d" % x, Rect2(x, 4, 6, 40), Color("493e3a"))
	_add_rect(root, window, "Sill", Rect2(128, 42, 256, 8), Color("705345"))
	_add_rect(root, window, "CurtainLeft", Rect2(140, 6, 20, 34), Color("e6ddc5"))
	_add_rect(root, window, "CurtainRight", Rect2(352, 6, 20, 34), Color("e6ddc5"))


func _add_owned(root: Node, child: Node) -> void:
	root.add_child(child)
	child.owner = root


func _add_rect(root: Node, parent: Node, node_name: String, rect: Rect2, color: Color) -> void:
	_add_polygon(root, parent, node_name, PackedVector2Array([
		rect.position,
		rect.position + Vector2(rect.size.x, 0),
		rect.position + rect.size,
		rect.position + Vector2(0, rect.size.y),
	]), color)


func _add_polygon(root: Node, parent: Node, node_name: String, points: PackedVector2Array, color: Color) -> void:
	var polygon := Polygon2D.new()
	polygon.name = node_name
	polygon.polygon = points
	polygon.color = color
	parent.add_child(polygon)
	polygon.owner = root


func _add_bound(root: Node, parent: StaticBody2D, node_name: String, position: Vector2, size: Vector2) -> void:
	var shape := RectangleShape2D.new()
	shape.size = size
	var collision := CollisionShape2D.new()
	collision.name = node_name
	collision.position = position
	collision.shape = shape
	parent.add_child(collision)
	collision.owner = root
