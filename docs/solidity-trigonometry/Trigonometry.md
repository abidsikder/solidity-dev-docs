
## Trigonometry

Solidity library offering basic trigonometry functions where inputs and outputs are
integers. Inputs are specified in radians scaled by 1e18, and similarly outputs are scaled by 1e18.

This implementation is based off the Solidity trigonometry library written by Lefteris Karapetsas
which can be found here: https://github.com/Sikorkaio/sikorka/blob/e75c91925c914beaedf4841c0336a806f2b5f66d/contracts/trigonometry.sol

Compared to Lefteris' implementation, this version makes the following changes:
  - Uses a 32 bits instead of 16 bits for improved accuracy
  - Updated for Solidity 0.8.x
  - Various gas optimizations
  - Change inputs/outputs to standard trig format (scaled by 1e18) instead of requiring the
    integer format used by the algorithm

Lefertis' implementation is based off Dave Dribin's trigint C library
    http://www.dribin.org/dave/trigint/

Which in turn is based from a now deleted article which can be found in the Wayback Machine:
    http://web.archive.org/web/20120301144605/http://www.dattalo.com/technical/software/pic/picsine.html

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
uint32 ANGLES_IN_CYCLE
```

### QUADRANT_HIGH_MASK

```solidity
uint32 QUADRANT_HIGH_MASK
```

### QUADRANT_LOW_MASK

```solidity
uint32 QUADRANT_LOW_MASK
```

### SINE_TABLE_SIZE

```solidity
uint256 SINE_TABLE_SIZE
```

### PI

```solidity
uint256 PI
```

### TWO_PI

```solidity
uint256 TWO_PI
```

### PI_OVER_TWO

```solidity
uint256 PI_OVER_TWO
```

### entry_bytes

```solidity
uint8 entry_bytes
```

### entry_mask

```solidity
uint256 entry_mask
```

### sin_table

```solidity
bytes sin_table
```

### sin

```solidity
function sin(uint256 _angle) internal pure returns (int256)
```

Return the sine of a value, specified in radians scaled by 1e18

_This algorithm for converting sine only uses integer values, and it works by dividing the
circle into 30 bit angles, i.e. there are 1,073,741,824 (2^30) angle units, instead of the
standard 360 degrees (2pi radians). From there, we get an output in range -2,147,483,647 to
2,147,483,647, (which is the max value of an int32) which is then converted back to the standard
range of -1 to 1, again scaled by 1e18_

| Name | Type | Description |
| ---- | ---- | ----------- |
| _angle | uint256 | Angle to convert |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | int256 | Result scaled by 1e18 |

### cos

```solidity
function cos(uint256 _angle) internal pure returns (int256)
```

Return the cosine of a value, specified in radians scaled by 1e18

_This is identical to the sin() method, and just computes the value by delegating to the
sin() method using the identity cos(x) = sin(x + pi/2)
Overflow when `angle + PI_OVER_TWO > type(uint256).max` is ok, results are still accurate_

| Name | Type | Description |
| ---- | ---- | ----------- |
| _angle | uint256 | Angle to convert |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | int256 | Result scaled by 1e18 |

