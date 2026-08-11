extends Interactable
class_name RoomExit

signal exit_requested

@export var locked: bool = true

@onready var _door: Sprite2D = $Door

func set_locked(value: bool) -> void:
	locked = value
	if is_node_ready():
		_update_door_visual()

func _ready() -> void:
	super._ready()
	_update_door_visual()

func _update_door_visual() -> void:
	_door.region_rect = Rect2(112, 16, 32, 48) if locked else Rect2(144, 16, 48, 48)
	_door.position.x = 0.0 if locked else 8.0

func interact() -> void:
	if locked:
		print("[RoomExit] The door won't budge yet.")
		return
	super.interact()
	print("[RoomExit] Mango slips out to meet Cooper...")
	exit_requested.emit()
