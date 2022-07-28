
## Trigonometry

### INDEX_WIDTH

```solidity
uint256 INDEX_WIDTH
```

### INTERP_WIDTH

```solidity
uint256 INTERP_WIDTH
```

### INDEX_OFFSET

```solidity
uint256 INDEX_OFFSET
```

### INTERP_OFFSET

```solidity
uint256 INTERP_OFFSET
```

### ANGLES_IN_CYCLE

```solidity
uint16 ANGLES_IN_CYCLE
```

### QUADRANT_HIGH_MASK

```solidity
uint16 QUADRANT_HIGH_MASK
```

### QUADRANT_LOW_MASK

```solidity
uint16 QUADRANT_LOW_MASK
```

### SINE_TABLE_SIZE

```solidity
uint256 SINE_TABLE_SIZE
```

### entry_bytes

```solidity
uint8 entry_bytes
```

### sin_table

```solidity
bytes sin_table
```

### bits

```solidity
function bits(uint256 _value, uint256 _width, uint256 _offset) internal pure returns (uint256)
```

Convenience function to apply a mask on an integer to extract a certain
number of bits. Using exponents since solidity still does not support
shifting.

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | uint256 | The integer whose bits we want to get |
| _width | uint256 | The width of the bits (in bits) we want to extract |
| _offset | uint256 | The offset of the bits (in bits) we want to extract |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | uint256 | An integer containing _width bits of _value starting at the         _offset bit |

### sin_table_lookup

```solidity
function sin_table_lookup(uint256 index) internal pure returns (uint16)
```

### sin

```solidity
function sin(uint16 _angle) public pure returns (int256)
```

Return the sine of an integer approximated angle as a signed 16-bit
integer.

| Name | Type | Description |
| ---- | ---- | ----------- |
| _angle | uint16 | A 16-bit angle. This divides the circle into 16384               angle units, instead of the standard 360 degrees. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | int256 | The sine result as a number in the range -32767 to 32767. |

### cos

```solidity
function cos(uint16 _angle) public pure returns (int256)
```

Return the cos of an integer approximated angle.
It functions just like the sin() method but uses the trigonometric
identity sin(x + pi/2) = cos(x) to quickly calculate the cos.

