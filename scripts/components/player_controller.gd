extends CharacterBody2D
class_name PlayerController

@export var speed: float = 120.0

var _nearby_interactables: Array[Interactable] = []

func _physics_process(_delta: float) -> void:
	var input_vector := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	velocity = input_vector * speed
	move_and_slide()

func _unhandled_input(event: InputEvent) -> void:
	if event.is_action_pressed("interact") and not _nearby_interactables.is_empty():
		_nearby_interactables[0].interact()

func _on_interaction_range_area_entered(area: Area2D) -> void:
	if area is Interactable:
		_nearby_interactables.append(area)

func _on_interaction_range_area_exited(area: Area2D) -> void:
	if area is Interactable:
		_nearby_interactables.erase(area)
