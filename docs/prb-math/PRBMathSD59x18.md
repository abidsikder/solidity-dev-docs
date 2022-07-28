
## PRBMathSD59x18

Smart contract library for advanced fixed-point math that works with int256 numbers considered to have 18
trailing decimals. We call this number representation signed 59.18-decimal fixed-point, since the numbers can have
a sign and there can be up to 59 digits in the integer part and up to 18 decimals in the fractional part. The numbers
are bound by the minimum and the maximum values permitted by the Solidity type int256.

### LOG2_E

```solidity
int256 LOG2_E
```

_log2(e) as a signed 59.18-decimal fixed-point number._

### HALF_SCALE

```solidity
int256 HALF_SCALE
```

_Half the SCALE number._

### MAX_SD59x18

```solidity
int256 MAX_SD59x18
```

_The maximum value a signed 59.18-decimal fixed-point number can have._

### MAX_WHOLE_SD59x18

```solidity
int256 MAX_WHOLE_SD59x18
```

_The maximum whole value a signed 59.18-decimal fixed-point number can have._

### MIN_SD59x18

```solidity
int256 MIN_SD59x18
```

_The minimum value a signed 59.18-decimal fixed-point number can have._

### MIN_WHOLE_SD59x18

```solidity
int256 MIN_WHOLE_SD59x18
```

_The minimum whole value a signed 59.18-decimal fixed-point number can have._

### SCALE

```solidity
int256 SCALE
```

_How many trailing decimals can be represented._

### abs

```solidity
function abs(int256 x) internal pure returns (int256 result)
```

Calculate the absolute value of x.

_Requirements:
- x must be greater than MIN_SD59x18._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The number to calculate the absolute value for. |

### avg

```solidity
function avg(int256 x, int256 y) internal pure returns (int256 result)
```

Calculates the arithmetic average of x and y, rounding down.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The first operand as a signed 59.18-decimal fixed-point number. |
| y | int256 | The second operand as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The arithmetic average as a signed 59.18-decimal fixed-point number. |

### ceil

```solidity
function ceil(int256 x) internal pure returns (int256 result)
```

Yields the least greatest signed 59.18 decimal fixed-point number greater than or equal to x.

_Optimized for fractional value inputs, because for every whole value there are (1e18 - 1) fractional counterparts.
See https://en.wikipedia.org/wiki/Floor_and_ceiling_functions.

Requirements:
- x must be less than or equal to MAX_WHOLE_SD59x18._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number to ceil. |

### div

```solidity
function div(int256 x, int256 y) internal pure returns (int256 result)
```

Divides two signed 59.18-decimal fixed-point numbers, returning a new signed 59.18-decimal fixed-point number.

_Variant of "mulDiv" that works with signed numbers. Works by computing the signs and the absolute values separately.

Requirements:
- All from "PRBMath.mulDiv".
- None of the inputs can be MIN_SD59x18.
- The denominator cannot be zero.
- The result must fit within int256.

Caveats:
- All from "PRBMath.mulDiv"._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The numerator as a signed 59.18-decimal fixed-point number. |
| y | int256 | The denominator as a signed 59.18-decimal fixed-point number. |

### e

```solidity
function e() internal pure returns (int256 result)
```

Returns Euler's number as a signed 59.18-decimal fixed-point number.

_See https://en.wikipedia.org/wiki/E_(mathematical_constant)._

### exp

```solidity
function exp(int256 x) internal pure returns (int256 result)
```

Calculates the natural exponent of x.

_Based on the insight that e^x = 2^(x * log2(e)).

Requirements:
- All from "log2".
- x must be less than 133.084258667509499441.

Caveats:
- All from "exp2".
- For any x less than -41.446531673892822322, the result is zero._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The exponent as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as a signed 59.18-decimal fixed-point number. |

### exp2

```solidity
function exp2(int256 x) internal pure returns (int256 result)
```

Calculates the binary exponent of x using the binary fraction method.

_See https://ethereum.stackexchange.com/q/79903/24693.

Requirements:
- x must be 192 or less.
- The result must fit within MAX_SD59x18.

Caveats:
- For any x less than -59.794705707972522261, the result is zero._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The exponent as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as a signed 59.18-decimal fixed-point number. |

### floor

```solidity
function floor(int256 x) internal pure returns (int256 result)
```

Yields the greatest signed 59.18 decimal fixed-point number less than or equal to x.

_Optimized for fractional value inputs, because for every whole value there are (1e18 - 1) fractional counterparts.
See https://en.wikipedia.org/wiki/Floor_and_ceiling_functions.

Requirements:
- x must be greater than or equal to MIN_WHOLE_SD59x18._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number to floor. |

### frac

```solidity
function frac(int256 x) internal pure returns (int256 result)
```

Yields the excess beyond the floor of x for positive numbers and the part of the number to the right
of the radix point for negative numbers.

_Based on the odd function definition. https://en.wikipedia.org/wiki/Fractional_part_

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number to get the fractional part of. |

### fromInt

```solidity
function fromInt(int256 x) internal pure returns (int256 result)
```

Converts a number from basic integer form to signed 59.18-decimal fixed-point representation.

_Requirements:
- x must be greater than or equal to MIN_SD59x18 divided by SCALE.
- x must be less than or equal to MAX_SD59x18 divided by SCALE._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The basic integer to convert. |

### gm

```solidity
function gm(int256 x, int256 y) internal pure returns (int256 result)
```

Calculates geometric mean of x and y, i.e. sqrt(x * y), rounding down.

_Requirements:
- x * y must fit within MAX_SD59x18, lest it overflows.
- x * y cannot be negative._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The first operand as a signed 59.18-decimal fixed-point number. |
| y | int256 | The second operand as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as a signed 59.18-decimal fixed-point number. |

### inv

```solidity
function inv(int256 x) internal pure returns (int256 result)
```

Calculates 1 / x, rounding toward zero.

_Requirements:
- x cannot be zero._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number for which to calculate the inverse. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The inverse as a signed 59.18-decimal fixed-point number. |

### ln

```solidity
function ln(int256 x) internal pure returns (int256 result)
```

Calculates the natural logarithm of x.

_Based on the insight that ln(x) = log2(x) / log2(e).

Requirements:
- All from "log2".

Caveats:
- All from "log2".
- This doesn't return exactly 1 for 2718281828459045235, for that we would need more fine-grained precision._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number for which to calculate the natural logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The natural logarithm as a signed 59.18-decimal fixed-point number. |

### log10

```solidity
function log10(int256 x) internal pure returns (int256 result)
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
| x | int256 | The signed 59.18-decimal fixed-point number for which to calculate the common logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The common logarithm as a signed 59.18-decimal fixed-point number. |

### log2

```solidity
function log2(int256 x) internal pure returns (int256 result)
```

Calculates the binary logarithm of x.

_Based on the iterative approximation algorithm.
https://en.wikipedia.org/wiki/Binary_logarithm#Iterative_approximation

Requirements:
- x must be greater than zero.

Caveats:
- The results are not perfectly accurate to the last decimal, due to the lossy precision of the iterative approximation._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number for which to calculate the binary logarithm. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The binary logarithm as a signed 59.18-decimal fixed-point number. |

### mul

```solidity
function mul(int256 x, int256 y) internal pure returns (int256 result)
```

Multiplies two signed 59.18-decimal fixed-point numbers together, returning a new signed 59.18-decimal
fixed-point number.

_Variant of "mulDiv" that works with signed numbers and employs constant folding, i.e. the denominator is
always 1e18.

Requirements:
- All from "PRBMath.mulDivFixedPoint".
- None of the inputs can be MIN_SD59x18
- The result must fit within MAX_SD59x18.

Caveats:
- The body is purposely left uncommented; see the NatSpec comments in "PRBMath.mulDiv" to understand how this works._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The multiplicand as a signed 59.18-decimal fixed-point number. |
| y | int256 | The multiplier as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The product as a signed 59.18-decimal fixed-point number. |

### pi

```solidity
function pi() internal pure returns (int256 result)
```

Returns PI as a signed 59.18-decimal fixed-point number.

### pow

```solidity
function pow(int256 x, int256 y) internal pure returns (int256 result)
```

Raises x to the power of y.

_Based on the insight that x^y = 2^(log2(x) * y).

Requirements:
- All from "exp2", "log2" and "mul".
- z cannot be zero.

Caveats:
- All from "exp2", "log2" and "mul".
- Assumes 0^0 is 1._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | Number to raise to given power y, as a signed 59.18-decimal fixed-point number. |
| y | int256 | Exponent to raise x to, as a signed 59.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | x raised to power y, as a signed 59.18-decimal fixed-point number. |

### powu

```solidity
function powu(int256 x, uint256 y) internal pure returns (int256 result)
```

Raises x (signed 59.18-decimal fixed-point number) to the power of y (basic unsigned integer) using the
famous algorithm "exponentiation by squaring".

_See https://en.wikipedia.org/wiki/Exponentiation_by_squaring

Requirements:
- All from "abs" and "PRBMath.mulDivFixedPoint".
- The result must fit within MAX_SD59x18.

Caveats:
- All from "PRBMath.mulDivFixedPoint".
- Assumes 0^0 is 1._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The base as a signed 59.18-decimal fixed-point number. |
| y | uint256 | The exponent as an uint256. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as a signed 59.18-decimal fixed-point number. |

### scale

```solidity
function scale() internal pure returns (int256 result)
```

Returns 1 as a signed 59.18-decimal fixed-point number.

### sqrt

```solidity
function sqrt(int256 x) internal pure returns (int256 result)
```

Calculates the square root of x, rounding down.

_Uses the Babylonian method https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method.

Requirements:
- x cannot be negative.
- x must be less than MAX_SD59x18 / SCALE._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number for which to calculate the square root. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as a signed 59.18-decimal fixed-point . |

### toInt

```solidity
function toInt(int256 x) internal pure returns (int256 result)
```

Converts a signed 59.18-decimal fixed-point number to basic integer form, rounding down in the process.

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The signed 59.18-decimal fixed-point number to convert. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The same number in basic integer form. |

