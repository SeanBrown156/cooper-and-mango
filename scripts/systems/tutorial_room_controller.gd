extends Node2D

## Grid painted at native 16px tile size; the Tiles node is scaled 2x
## in the scene to hit the locked 32px effective sprite/tile spec.
const GRID_COLS := 15
const GRID_ROWS := 9
const FLOOR_ATLAS_COORDS := Vector2i(1, 1)
const WALL_ATLAS_COORDS := Vector2i(5, 0)

@onready var _tiles: TileMapLayer = $Tiles
@onready var _room_exit: RoomExit = $RoomExit
@onready var _spider_plant: SpiderPlant = $SpiderPlant

func _ready() -> void:
	_paint_room()
	_room_exit.set_locked(true)
	_spider_plant.awakening_triggered.connect(_on_spider_plant_awakening_triggered)

func _paint_room() -> void:
	for x in range(GRID_COLS):
		for y in range(GRID_ROWS):
			var is_border := x == 0 or x == GRID_COLS - 1 or y == 0 or y == GRID_ROWS - 1
			var atlas_coords := WALL_ATLAS_COORDS if is_border else FLOOR_ATLAS_COORDS
			_tiles.set_cell(Vector2i(x, y), 0, atlas_coords)

func _on_spider_plant_awakening_triggered() -> void:
	print("[TutorialRoom] The awakening begins. The door creaks open.")
	_room_exit.set_locked(false)
