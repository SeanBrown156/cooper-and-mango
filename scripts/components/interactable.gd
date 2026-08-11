extends Area2D
class_name Interactable

signal interacted(source: Interactable)

@export_multiline var interaction_text: String = ""

func _ready() -> void:
	add_to_group("interactable")

func interact() -> void:
	interacted.emit(self)
	if interaction_text != "":
		print("[Interact] %s: %s" % [name, interaction_text])
