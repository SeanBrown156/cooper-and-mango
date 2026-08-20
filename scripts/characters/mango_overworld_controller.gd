extends CharacterBody2D
class_name MangoOverworldController

@export var speed: float = 120.0

@onready var sprite: AnimatedSprite2D = $AnimatedSprite2D

var _facing := "south"

func _ready() -> void:
	_set_facing(_facing)
	sprite.pause()
	sprite.frame = 0

func _physics_process(_delta: float) -> void:
	var input_vector := Input.get_vector("move_left", "move_right", "move_up", "move_down")
	velocity = input_vector * speed
	move_and_slide()

	if input_vector.length_squared() > 0.0:
		_update_facing(input_vector)
		sprite.play("walk_" + _facing)
	else:
		sprite.pause()
		sprite.frame = 0

func _update_facing(input_vector: Vector2) -> void:
	if absf(input_vector.x) > absf(input_vector.y):
		_set_facing("east" if input_vector.x > 0.0 else "west")
	else:
		_set_facing("south" if input_vector.y > 0.0 else "north")

func _set_facing(direction: String) -> void:
	if direction == _facing and sprite.animation == "walk_" + direction:
		return
	_facing = direction
	sprite.animation = "walk_" + direction
	# Side views are 16px tall; lift them 2px so their feet share the
	# same world-space anchor as the 20px north/south views.
	sprite.position.y = 2.0 if direction == "east" or direction == "west" else 0.0
