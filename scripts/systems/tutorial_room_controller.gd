extends Node2D

@onready var _room_exit: RoomExit = $RoomExit
@onready var _spider_plant: SpiderPlant = $SpiderPlant

func _ready() -> void:
	_room_exit.set_locked(true)
	_spider_plant.awakening_triggered.connect(_on_spider_plant_awakening_triggered)

func _on_spider_plant_awakening_triggered() -> void:
	print("[TutorialRoom] The awakening begins. The door creaks open.")
	_room_exit.set_locked(false)
