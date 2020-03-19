# Kenney 3d assets converter

This little script for [Blender](https://www.blender.org/) (tested with Blender 2.82) converts [3d assets from Kenney](https://kenney.nl/assets?q=3d) to GLTF binary format, and fixes their origin point such that they are centered.

Use case for this is to automatically convert a bunch of 3d assets such that they work well in the [Godot engine](https://godotengine.org/), specifically with Godot's gridmaps.

## Usage

1. Clone this repository
2. Place all of your Kenney 3d assets (`.obj` and `.mtl`) in the `input` folder
3. Open Blender, with a new scene
4. Load the `convert.py` script in the Blender Scripting tab
5. Run the script to batch convert all models!

