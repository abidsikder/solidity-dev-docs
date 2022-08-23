
## Arcsin

Calculates arcsine. Fuzz testing shows that relative error is always
smaller than 0.01%. Uses the polynomial approximation functions found in
https://dsp.stackexchange.com/a/25771, but chooses between them at x=0.4788
due to differences in the relative errors as can be seen here
https://www.desmos.com/calculator/wrfwjhythe

_See the desmos link for what functions f and g in the code refer to._

### g

```solidity
function g(int256 _x) internal pure returns (int256)
```

### f

```solidity
function f(int256 _x) internal pure returns (int256)
```

### arcsin

```solidity
function arcsin(int256 _x) internal pure returns (int256)
```

Arcsine function

| Name | Type | Description |
| ---- | ---- | ----------- |
| _x | int256 | A integer with 18 fixed decimal points, where the whole part is bounded inside of [-1,1] |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | int256 | The arcsine, with 18 fixed decimal points |

