extends Node2D

## The source art is 16px and the TileMapLayer is scaled 2×, giving the
## project its locked 32px environment grid without resampling the textures.
const GRID_COLS := 15
const GRID_ROWS := 9
const WALL_TILES := [Vector2i(1, 1), Vector2i(2, 1), Vector2i(3, 1), Vector2i(4, 1)]
const TRIM_TILES := [Vector2i(1, 3), Vector2i(2, 3), Vector2i(3, 3), Vector2i(4, 3)]
const FLOOR_TILES := [Vector2i(1, 5), Vector2i(2, 5), Vector2i(3, 5), Vector2i(4, 5)]

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
			if y < 2:
				atlas_coords = WALL_TILES[x % WALL_TILES.size()]
			elif y == 2:
				atlas_coords = TRIM_TILES[x % TRIM_TILES.size()]
			else:
				atlas_coords = FLOOR_TILES[(x + y) % FLOOR_TILES.size()]
			_tiles.set_cell(Vector2i(x, y), 0, atlas_coords)

func _on_spider_plant_awakening_triggered() -> void:
	print("[TutorialRoom] The awakening begins. The door creaks open.")
	_room_exit.set_locked(false)
	_show_status("The leaves whisper. The door creaks open.")

func _on_room_exit_requested() -> void:
	_show_status("The hallway is clear — Mango can leave the room.")
	print("[TutorialRoom] Exit reached; hallway scene is the next content handoff.")

func _show_status(message: String) -> void:
	_status.text = message
	_status.show()
