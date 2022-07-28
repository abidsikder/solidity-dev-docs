
## PRBMath__MulDivFixedPointOverflow

```solidity
error PRBMath__MulDivFixedPointOverflow(uint256 prod1)
```

Emitted when the result overflows uint256.

## PRBMath__MulDivOverflow

```solidity
error PRBMath__MulDivOverflow(uint256 prod1, uint256 denominator)
```

Emitted when the result overflows uint256.

## PRBMath__MulDivSignedInputTooSmall

```solidity
error PRBMath__MulDivSignedInputTooSmall()
```

Emitted when one of the inputs is type(int256).min.

## PRBMath__MulDivSignedOverflow

```solidity
error PRBMath__MulDivSignedOverflow(uint256 rAbs)
```

Emitted when the intermediary absolute result overflows int256.

## PRBMathSD59x18__AbsInputTooSmall

```solidity
error PRBMathSD59x18__AbsInputTooSmall()
```

Emitted when the input is MIN_SD59x18.

## PRBMathSD59x18__CeilOverflow

```solidity
error PRBMathSD59x18__CeilOverflow(int256 x)
```

Emitted when ceiling a number overflows SD59x18.

## PRBMathSD59x18__DivInputTooSmall

```solidity
error PRBMathSD59x18__DivInputTooSmall()
```

Emitted when one of the inputs is MIN_SD59x18.

## PRBMathSD59x18__DivOverflow

```solidity
error PRBMathSD59x18__DivOverflow(uint256 rAbs)
```

Emitted when one of the intermediary unsigned results overflows SD59x18.

## PRBMathSD59x18__ExpInputTooBig

```solidity
error PRBMathSD59x18__ExpInputTooBig(int256 x)
```

Emitted when the input is greater than 133.084258667509499441.

## PRBMathSD59x18__Exp2InputTooBig

```solidity
error PRBMathSD59x18__Exp2InputTooBig(int256 x)
```

Emitted when the input is greater than 192.

## PRBMathSD59x18__FloorUnderflow

```solidity
error PRBMathSD59x18__FloorUnderflow(int256 x)
```

Emitted when flooring a number underflows SD59x18.

## PRBMathSD59x18__FromIntOverflow

```solidity
error PRBMathSD59x18__FromIntOverflow(int256 x)
```

Emitted when converting a basic integer to the fixed-point format overflows SD59x18.

## PRBMathSD59x18__FromIntUnderflow

```solidity
error PRBMathSD59x18__FromIntUnderflow(int256 x)
```

Emitted when converting a basic integer to the fixed-point format underflows SD59x18.

## PRBMathSD59x18__GmNegativeProduct

```solidity
error PRBMathSD59x18__GmNegativeProduct(int256 x, int256 y)
```

Emitted when the product of the inputs is negative.

## PRBMathSD59x18__GmOverflow

```solidity
error PRBMathSD59x18__GmOverflow(int256 x, int256 y)
```

Emitted when multiplying the inputs overflows SD59x18.

## PRBMathSD59x18__LogInputTooSmall

```solidity
error PRBMathSD59x18__LogInputTooSmall(int256 x)
```

Emitted when the input is less than or equal to zero.

## PRBMathSD59x18__MulInputTooSmall

```solidity
error PRBMathSD59x18__MulInputTooSmall()
```

Emitted when one of the inputs is MIN_SD59x18.

## PRBMathSD59x18__MulOverflow

```solidity
error PRBMathSD59x18__MulOverflow(uint256 rAbs)
```

Emitted when the intermediary absolute result overflows SD59x18.

## PRBMathSD59x18__PowuOverflow

```solidity
error PRBMathSD59x18__PowuOverflow(uint256 rAbs)
```

Emitted when the intermediary absolute result overflows SD59x18.

## PRBMathSD59x18__SqrtNegativeInput

```solidity
error PRBMathSD59x18__SqrtNegativeInput(int256 x)
```

Emitted when the input is negative.

## PRBMathSD59x18__SqrtOverflow

```solidity
error PRBMathSD59x18__SqrtOverflow(int256 x)
```

Emitted when the calculating the square root overflows SD59x18.

## PRBMathUD60x18__AddOverflow

```solidity
error PRBMathUD60x18__AddOverflow(uint256 x, uint256 y)
```

Emitted when addition overflows UD60x18.

## PRBMathUD60x18__CeilOverflow

```solidity
error PRBMathUD60x18__CeilOverflow(uint256 x)
```

Emitted when ceiling a number overflows UD60x18.

## PRBMathUD60x18__ExpInputTooBig

```solidity
error PRBMathUD60x18__ExpInputTooBig(uint256 x)
```

Emitted when the input is greater than 133.084258667509499441.

## PRBMathUD60x18__Exp2InputTooBig

```solidity
error PRBMathUD60x18__Exp2InputTooBig(uint256 x)
```

Emitted when the input is greater than 192.

## PRBMathUD60x18__FromUintOverflow

```solidity
error PRBMathUD60x18__FromUintOverflow(uint256 x)
```

Emitted when converting a basic integer to the fixed-point format format overflows UD60x18.

## PRBMathUD60x18__GmOverflow

```solidity
error PRBMathUD60x18__GmOverflow(uint256 x, uint256 y)
```

Emitted when multiplying the inputs overflows UD60x18.

## PRBMathUD60x18__LogInputTooSmall

```solidity
error PRBMathUD60x18__LogInputTooSmall(uint256 x)
```

Emitted when the input is less than 1.

## PRBMathUD60x18__SqrtOverflow

```solidity
error PRBMathUD60x18__SqrtOverflow(uint256 x)
```

Emitted when the calculating the square root overflows UD60x18.

## PRBMathUD60x18__SubUnderflow

```solidity
error PRBMathUD60x18__SubUnderflow(uint256 x, uint256 y)
```

Emitted when subtraction underflows UD60x18.

## PRBMath

_Common mathematical functions used in both PRBMathSD59x18 and PRBMathUD60x18. Note that this shared library
does not always assume the signed 59.18-decimal fixed-point or the unsigned 60.18-decimal fixed-point
representation. When it does not, it is explicitly mentioned in the NatSpec documentation._

### SD59x18

```solidity
struct SD59x18 {
  int256 value;
}
```

### UD60x18

```solidity
struct UD60x18 {
  uint256 value;
}
```

### SCALE

```solidity
uint256 SCALE
```

_How many trailing decimals can be represented._

### SCALE_LPOTD

```solidity
uint256 SCALE_LPOTD
```

_Largest power of two divisor of SCALE._

### SCALE_INVERSE

```solidity
uint256 SCALE_INVERSE
```

_SCALE inverted mod 2^256._

### exp2

```solidity
function exp2(uint256 x) internal pure returns (uint256 result)
```

Calculates the binary exponent of x using the binary fraction method.

_Has to use 192.64-bit fixed-point numbers.
See https://ethereum.stackexchange.com/a/96594/24693._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The exponent as an unsigned 192.64-bit fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | uint256 | The result as an unsigned 60.18-decimal fixed-point number. |

### mostSignificantBit

```solidity
function mostSignificantBit(uint256 x) internal pure returns (uint256 msb)
```

Finds the zero-based index of the first one in the binary representation of x.

_See the note on msb in the "Find First Set" Wikipedia article https://en.wikipedia.org/wiki/Find_first_set_

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The uint256 number for which to find the index of the most significant bit. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| msb | uint256 | The index of the most significant bit as an uint256. |

### mulDiv

```solidity
function mulDiv(uint256 x, uint256 y, uint256 denominator) internal pure returns (uint256 result)
```

Calculates floor(x*y÷denominator) with full precision.

_Credit to Remco Bloemen under MIT license https://xn--2-umb.com/21/muldiv.

Requirements:
- The denominator cannot be zero.
- The result must fit within uint256.

Caveats:
- This function does not work with fixed-point numbers._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The multiplicand as an uint256. |
| y | uint256 | The multiplier as an uint256. |
| denominator | uint256 | The divisor as an uint256. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | uint256 | The result as an uint256. |

### mulDivFixedPoint

```solidity
function mulDivFixedPoint(uint256 x, uint256 y) internal pure returns (uint256 result)
```

Calculates floor(x*y÷1e18) with full precision.

_Variant of "mulDiv" with constant folding, i.e. in which the denominator is always 1e18. Before returning the
final result, we add 1 if (x * y) % SCALE >= HALF_SCALE. Without this, 6.6e-19 would be truncated to 0 instead of
being rounded to 1e-18.  See "Listing 6" and text above it at https://accu.org/index.php/journals/1717.

Requirements:
- The result must fit within uint256.

Caveats:
- The body is purposely left uncommented; see the NatSpec comments in "PRBMath.mulDiv" to understand how this works.
- It is assumed that the result can never be type(uint256).max when x and y solve the following two equations:
    1. x * y = type(uint256).max * SCALE
    2. (x * y) % SCALE >= SCALE / 2_

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The multiplicand as an unsigned 60.18-decimal fixed-point number. |
| y | uint256 | The multiplier as an unsigned 60.18-decimal fixed-point number. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | uint256 | The result as an unsigned 60.18-decimal fixed-point number. |

### mulDivSigned

```solidity
function mulDivSigned(int256 x, int256 y, int256 denominator) internal pure returns (int256 result)
```

Calculates floor(x*y÷denominator) with full precision.

_An extension of "mulDiv" for signed numbers. Works by computing the signs and the absolute values separately.

Requirements:
- None of the inputs can be type(int256).min.
- The result must fit within int256._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | int256 | The multiplicand as an int256. |
| y | int256 | The multiplier as an int256. |
| denominator | int256 | The divisor as an int256. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | int256 | The result as an int256. |

### sqrt

```solidity
function sqrt(uint256 x) internal pure returns (uint256 result)
```

Calculates the square root of x, rounding down.

_Uses the Babylonian method https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method.

Caveats:
- This function does not work with fixed-point numbers._

| Name | Type | Description |
| ---- | ---- | ----------- |
| x | uint256 | The uint256 number for which to calculate the square root. |

| Name | Type | Description |
| ---- | ---- | ----------- |
| result | uint256 | The result as an uint256. |

