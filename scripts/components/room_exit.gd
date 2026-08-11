extends Interactable
class_name RoomExit

@export var locked: bool = true

func set_locked(value: bool) -> void:
	locked = value

func interact() -> void:
	if locked:
		print("[RoomExit] The door won't budge yet.")
		return
	super.interact()
	print("[RoomExit] Mango slips out to meet Cooper...")
	# TODO (Stage 2): change_scene_to_file() once the House scene exists.
