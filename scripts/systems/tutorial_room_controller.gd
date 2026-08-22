extends Node2D

@onready var _room_exit: RoomExit = $YSort/RoomExit
@onready var _spider_plant: SpiderPlant = $YSort/SpiderPlant
@onready var _status: Label = $UI/Status

func _ready() -> void:
	_room_exit.set_locked(true)
	_spider_plant.awakening_triggered.connect(_on_spider_plant_awakening_triggered)
	_room_exit.exit_requested.connect(_on_room_exit_requested)

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
