extends Node2D

## Tutorial Room build using the approved LimeZu-derived kit in
## assets/environments/rooms/tutorial_room/ (palette-remapped into the
## Cooper & Mango master palette, cropped from the licensed
## limezu_modern_interiors_full pack — see docs/ASSET_LICENSES.md).
##
## Source art is native 16px; the TileMapLayer is scaled 2x to match the
## project's locked 32px environment grid.
const GRID_COLS := 15
const GRID_ROWS := 9

## tutorial_room_tileset.png layout (16px tiles):
## row 0-1 = wall face (2 tiles tall, wallpaper pattern, 3 column variants
## from the Room Builder catalog sheet), row 2 = floor — a smooth swatch
## from the pack's dedicated Floors_only sheet rather than Room Builder's
## catalog tiles, which carry a baked-in border that reads as a grid seam
## when repeated. Single floor tile, no column variance — deliberately
## uniform rather than checkerboarded between shading variants.
const WALL_UPPER_TILES := [Vector2i(0, 0), Vector2i(1, 0), Vector2i(2, 0)]
const WALL_LOWER_TILES := [Vector2i(0, 1), Vector2i(1, 1), Vector2i(2, 1)]
const FLOOR_TILE := Vector2i(0, 2)

@onready var _tiles: TileMapLayer = $Tiles
@onready var _room_exit: RoomExit = $RoomExit
@onready var _spider_plant: SpiderPlant = $SpiderPlant
@onready var _status: Label = $Status

func _ready() -> void:
	_paint_room()
	_room_exit.set_locked(true)
	_spider_plant.awakening_triggered.connect(_on_spider_plant_awakening_triggered)
	_room_exit.exit_requested.connect(_on_room_exit_requested)

func _paint_room() -> void:
	for x in range(GRID_COLS):
		for y in range(GRID_ROWS):
			var atlas_coords: Vector2i
			if y == 0:
				atlas_coords = WALL_UPPER_TILES[x % WALL_UPPER_TILES.size()]
			elif y == 1:
				atlas_coords = WALL_LOWER_TILES[x % WALL_LOWER_TILES.size()]
			else:
				atlas_coords = FLOOR_TILE
			_tiles.set_cell(Vector2i(x, y), 0, atlas_coords)

func _on_spider_plant_awakening_triggered() -> void:
	print("[TutorialRoomLimezuVariant] The awakening begins. The door creaks open.")
	_room_exit.set_locked(false)
	_show_status("The leaves whisper. The door creaks open.")

func _on_room_exit_requested() -> void:
	_show_status("The hallway is clear — Mango can leave the room.")
	print("[TutorialRoomLimezuVariant] Exit reached; hallway scene is the next content handoff.")

func _show_status(message: String) -> void:
	_status.text = message
	_status.show()
