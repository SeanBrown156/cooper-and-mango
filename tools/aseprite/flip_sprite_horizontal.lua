-- Mirror every cel in the opened sprite horizontally and save to the path
-- supplied as the first script argument.
local sprite = app.activeSprite
assert(sprite, "No sprite is open")
local output = app.params["output"]
assert(output and output ~= "", "Missing output path")

for _, layer in ipairs(sprite.layers) do
  for _, cel in ipairs(layer.cels) do
    cel.image:flip(FlipType.HORIZONTAL)
  end
end

sprite:saveAs(output)
