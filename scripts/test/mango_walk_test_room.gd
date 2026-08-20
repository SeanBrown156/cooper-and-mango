extends Node2D

func _ready() -> void:
	queue_redraw()

func _draw() -> void:
	var viewport_size := get_viewport_rect().size
	draw_rect(Rect2(Vector2.ZERO, viewport_size), Color("#16212b"))
	var tile_size := 24.0
	for x in range(0, int(viewport_size.x / tile_size) + 1):
		var x_pos := x * tile_size
		draw_line(Vector2(x_pos, 0), Vector2(x_pos, viewport_size.y), Color("#20303a"), 1.0)
	for y in range(0, int(viewport_size.y / tile_size) + 1):
		var y_pos := y * tile_size
		draw_line(Vector2(0, y_pos), Vector2(viewport_size.x, y_pos), Color("#20303a"), 1.0)
	draw_rect(Rect2(16, 16, viewport_size.x - 32, viewport_size.y - 32), Color("#8cc6a1", 0.12), false, 2.0)

