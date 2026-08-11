extends Interactable
class_name SpiderPlant

## The Tutorial Room's inciting trigger — see docs/GAME_BIBLE.md "Story Spine".
signal awakening_triggered

var _triggered: bool = false

func interact() -> void:
	super.interact()
	if _triggered:
		return
	_triggered = true
	print("[SpiderPlant] Mango noses into the spider plant... the world tilts sideways.")
	awakening_triggered.emit()
