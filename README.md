# OTGLayers
A Python script to generate a repeating cycle of `ReplacedBlocks` directives for OpenTerrainGenerator.

The script is bit rough and ready. There is no error handling or built-in usage help.


## Usage
The script is used as follows:

    ./layers.py <y-min> <y-max> <replaced> <depth1> <replacement1> <depth2> <replacement2> ...

The arguments are:

 * `<y-min>` the minimum Y coordinate, inclusive, of replaced blocks.
 * `<y-max>` the maximum Y coordinate, *exclusive*, of replaced blocks.
 * `<replaced>` the block type to be replaced with layers.
 * `<depthN>` the depth of the layer of blocks of type `<replacementN>`
 * `<replacementN>` the material that will replace the replaced block.
 
After the third argument, the script takes a series of pairs of arguments,
`<depthN>` and `<replacementN>` specifying the depth and material of the layer
to generate. Layers are generated in a repeating cycle from `<y-min>` inclusive
to `<y-max>` exclusive, with layers generating in the order specified in the
arguments.


## Example
The following command:

    ./layers.py 42 90 ENDER_STONE 2 SNOW_BLOCK 2 CONCRETE_POWDER:6 2 CONCRETE_POWDER:10 2 SNOW_BLOCK 2 CONCRETE_POWDER:0 2 CONCRETE_POWDER:6 2 CONCRETE_POWDER:2 2 CONCRETE_POWDER:10 2 CONCRETE_POWDER:14
    
Generates this output:
```
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:6
2 x CONCRETE_POWDER:10
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:0
2 x CONCRETE_POWDER:6
2 x CONCRETE_POWDER:2
2 x CONCRETE_POWDER:10
2 x CONCRETE_POWDER:14
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:6
2 x CONCRETE_POWDER:10
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:0
2 x CONCRETE_POWDER:6
2 x CONCRETE_POWDER:2
2 x CONCRETE_POWDER:10
2 x CONCRETE_POWDER:14
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:6
2 x CONCRETE_POWDER:10
2 x SNOW_BLOCK
2 x CONCRETE_POWDER:0
2 x CONCRETE_POWDER:6
------------------------------------------------------------------------------
ReplacedBlocks: (ENDER_STONE,SNOW_BLOCK,42,43),(ENDER_STONE,CONCRETE_POWDER:6,44,45),(ENDER_STONE,CONCRETE_POWDER:10,46,47),(ENDER_STONE,SNOW_BLOCK,48,49),(ENDER_STONE,CONCRETE_POWDER:0,50,51),(ENDER_STONE,CONCRETE_POWDER:6,52,53),(ENDER_STONE,CONCRETE_POWDER:2,54,55),(ENDER_STONE,CONCRETE_POWDER:10,56,57),(ENDER_STONE,CONCRETE_POWDER:14,58,59),(ENDER_STONE,SNOW_BLOCK,60,61),(ENDER_STONE,CONCRETE_POWDER:6,62,63),(ENDER_STONE,CONCRETE_POWDER:10,64,65),(ENDER_STONE,SNOW_BLOCK,66,67),(ENDER_STONE,CONCRETE_POWDER:0,68,69),(ENDER_STONE,CONCRETE_POWDER:6,70,71),(ENDER_STONE,CONCRETE_POWDER:2,72,73),(ENDER_STONE,CONCRETE_POWDER:10,74,75),(ENDER_STONE,CONCRETE_POWDER:14,76,77),(ENDER_STONE,SNOW_BLOCK,78,79),(ENDER_STONE,CONCRETE_POWDER:6,80,81),(ENDER_STONE,CONCRETE_POWDER:10,82,83),(ENDER_STONE,SNOW_BLOCK,84,85),(ENDER_STONE,CONCRETE_POWDER:0,86,87),(ENDER_STONE,CONCRETE_POWDER:6,88,89)
```

