
## PRBMathUD60x18Typed

Smart contract library for advanced fixed-point math that works with uint256 numbers considered to have 18
trailing decimals. We call this number representation unsigned 60.18-decimal fixed-point, since there can be up to 60
digits in the integer part and up to 18 decimals in the fractional part. The numbers are bound by the minimum and the
maximum values permitted by the Solidity type uint256.

_This is the same as PRBMathUD59x18, except that it works with structs instead of raw uint256s._

### HALF_SCALE

```solidity
uint256 HALF_SCALE
```

_Half the SCALE number._

### LOG2_E

```solidity
uint256 LOG2_E
```

_log2(e) as an unsigned 60.18-decimal fixed-point number._

### MAX_UD60x18

```solidity
uint256 MAX_UD60x18
```

_The maximum value an unsigned 60.18-decimal fixed-point number can have._

### MAX_WHOLE_UD60x18

```solidity
uint256 MAX_WHOLE_UD60x18
```

_The maximum whole value an unsigned 60.18-decimal fixed-point number can have._

### SCALE

```solidity
uint256 SCALE
```

_How many trailing decimals can be represented._

### add

```solidity
function add(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Adds two unsigned 60.18-decimal fixed-point numbers together, returning a new unsigned 60.18-decimal
fixed-point number.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The first summand as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The second summand as an unsigned 60.18-decimal fixed-point number. |

### avg

```solidity
function avg(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the arithmetic average of x and y, rounding down.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The first operand as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The second operand as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The arithmetic average as an unsigned 60.18-decimal fixed-point number. |

### ceil

```solidity
function ceil(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Yields the least unsigned 60.18 decimal fixed-point number greater than or equal to x.

_Optimized for fractional value inputs, because for every whole value there are (1e18 - 1) fractional counterparts.
See https://en.wikipedia.org/wiki/Floor_and_ceiling_functions.

Requirements:
- x must be less than or equal to MAX_WHOLE_UD60x18._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number to ceil. |

### div

```solidity
function div(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Divides two unsigned 60.18-decimal fixed-point numbers, returning a new unsigned 60.18-decimal fixed-point number.

_Uses mulDiv to enable overflow-safe multiplication and division.

Requirements:
- The denominator cannot be zero._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The numerator as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The denominator as an unsigned 60.18-decimal fixed-point number. |

### e

```solidity
function e() internal pure returns (struct PRBMath.UD60x18 result)
```

Returns Euler's number as an unsigned 60.18-decimal fixed-point number.

_See https://en.wikipedia.org/wiki/E_(mathematical_constant)._

### exp

```solidity
function exp(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the natural exponent of x.

_Based on the insight that e^x = 2^(x * log2(e)).

Requirements:
- All from "log2".
- x must be less than 88.722839111672999628._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The exponent as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The result as an unsigned 60.18-decimal fixed-point number. |

### exp2

```solidity
function exp2(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the binary exponent of x using the binary fraction method.

_See https://ethereum.stackexchange.com/q/79903/24693.

Requirements:
- x must be 192 or less.
- The result must fit within MAX_UD60x18._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The exponent as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The result as an unsigned 60.18-decimal fixed-point number. |

### floor

```solidity
function floor(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Yields the greatest unsigned 60.18 decimal fixed-point number less than or equal to x.

_Optimized for fractional value inputs, because for every whole value there are (1e18 - 1) fractional counterparts.
See https://en.wikipedia.org/wiki/Floor_and_ceiling_functions._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number to floor. |

### frac

```solidity
function frac(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Yields the excess beyond the floor of x.

_Based on the odd function definition https://en.wikipedia.org/wiki/Fractional_part._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number to get the fractional part of. |

### fromUint

```solidity
function fromUint(uint256 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Converts a number from basic integer form to unsigned 60.18-decimal fixed-point representation.

_Requirements:
- x must be less than or equal to MAX_UD60x18 divided by SCALE._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The basic integer to convert. |

### gm

```solidity
function gm(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates geometric mean of x and y, i.e. sqrt(x * y), rounding down.

_Requirements:
- x * y must fit within MAX_UD60x18, lest it overflows._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The first operand as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The second operand as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The result as an unsigned 60.18-decimal fixed-point number. |

### inv

```solidity
function inv(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates 1 / x, rounding toward zero.

_Requirements:
- x cannot be zero._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number for which to calculate the inverse. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The inverse as an unsigned 60.18-decimal fixed-point number. |

### ln

```solidity
function ln(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the natural logarithm of x.

_Based on the insight that ln(x) = log2(x) / log2(e).

Requirements:
- All from "log2".

Caveats:
- All from "log2".
- This doesn't return exactly 1 for 2.718281828459045235, for that we would need more fine-grained precision._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number for which to calculate the natural logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The natural logarithm as an unsigned 60.18-decimal fixed-point number. |

### log10

```solidity
function log10(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the common logarithm of x.

_First checks if x is an exact power of ten and it stops if yes. If it's not, calculates the common
logarithm based on the insight that log10(x) = log2(x) / log2(10).

Requirements:
- All from "log2".

Caveats:
- All from "log2"._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number for which to calculate the common logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The common logarithm as an unsigned 60.18-decimal fixed-point number. |

### log2

```solidity
function log2(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the binary logarithm of x.

_Based on the iterative approximation algorithm.
https://en.wikipedia.org/wiki/Binary_logarithm#Iterative_approximation

Requirements:
- x must be greater than or equal to SCALE, otherwise the result would be negative.

Caveats:
- The results are nor perfectly accurate to the last decimal, due to the lossy precision of the iterative approximation._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number for which to calculate the binary logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The binary logarithm as an unsigned 60.18-decimal fixed-point number. |

### mul

```solidity
function mul(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Multiplies two unsigned 60.18-decimal fixed-point numbers together, returning a new unsigned 60.18-decimal
fixed-point number.

_See the documentation for the "PRBMath.mulDivFixedPoint" function._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The multiplicand as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The multiplier as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The product as an unsigned 60.18-decimal fixed-point number. |

### pi

```solidity
function pi() internal pure returns (struct PRBMath.UD60x18 result)
```

Returns PI as an unsigned 60.18-decimal fixed-point number.

### pow

```solidity
function pow(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Raises x to the power of y.

_Based on the insight that x^y = 2^(log2(x) * y).

Requirements:
- All from "exp2", "log2" and "mul".

Caveats:
- All from "exp2", "log2" and "mul".
- Assumes 0^0 is 1._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | Number to raise to given power y, as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | Exponent to raise x to, as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | x raised to power y, as an unsigned 60.18-decimal fixed-point number. |

### powu

```solidity
function powu(struct PRBMath.UD60x18 x, uint256 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Raises x (unsigned 60.18-decimal fixed-point number) to the power of y (basic unsigned integer) using the
famous algorithm "exponentiation by squaring".

_See https://en.wikipedia.org/wiki/Exponentiation_by_squaring

Requirements:
- The result must fit within MAX_UD60x18.

Caveats:
- All from "mul".
- Assumes 0^0 is 1._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The base as an unsigned 60.18-decimal fixed-point number. |
| y | uint256 | The exponent as an uint256. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The result as an unsigned 60.18-decimal fixed-point number. |

### scale

```solidity
function scale() internal pure returns (struct PRBMath.UD60x18 result)
```

Returns 1 as an unsigned 60.18-decimal fixed-point number.

### sqrt

```solidity
function sqrt(struct PRBMath.UD60x18 x) internal pure returns (struct PRBMath.UD60x18 result)
```

Calculates the square root of x, rounding down.

_Uses the Babylonian method https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method.

Requirements:
- x must be less than MAX_UD60x18 / SCALE._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number for which to calculate the square root. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | struct PRBMath.UD60x18 | The result as an unsigned 60.18-decimal fixed-point . |

### sub

```solidity
function sub(struct PRBMath.UD60x18 x, struct PRBMath.UD60x18 y) internal pure returns (struct PRBMath.UD60x18 result)
```

Subtracts one unsigned 60.18-decimal fixed-point number from another one, returning a new unsigned 60.18-decimal
fixed-point number.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The minuend as an unsigned 60.18-decimal fixed-point number. |
| y | struct PRBMath.UD60x18 | The subtrahend as an unsigned 60.18-decimal fixed-point number. |

### toUint

```solidity
function toUint(struct PRBMath.UD60x18 x) internal pure returns (uint256 result)
```

Converts a unsigned 60.18-decimal fixed-point number to basic integer form, rounding down in the process.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | struct PRBMath.UD60x18 | The unsigned 60.18-decimal fixed-point number to convert. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | uint256 | The same number in basic integer form. |

