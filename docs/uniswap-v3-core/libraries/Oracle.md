
## Oracle

Provides price and liquidity data useful for a wide variety of system designs

_Instances of stored oracle data, "observations", are collected in the oracle array
Every pool is initialized with an oracle array length of 1. Anyone can pay the SSTOREs to increase the
maximum length of the oracle array. New slots will be added when the array is fully populated.
Observations are overwritten when the full length of the oracle array is populated.
The most recent observation is available, independent of the length of the oracle array, by passing 0 to observe()_

### Observation

```solidity
struct Observation {
  uint32 blockTimestamp;
  int56 tickCumulative;
  uint160 secondsPerLiquidityCumulativeX128;
  bool initialized;
}
```

### transform

```solidity
function transform(struct Oracle.Observation last, uint32 blockTimestamp, int24 tick, uint128 liquidity) private pure returns (struct Oracle.Observation)
```

Transforms a previous observation into a new observation, given the passage of time and the current tick and liquidity values

_blockTimestamp _must_ be chronologically equal to or greater than last.blockTimestamp, safe for 0 or 1 overflows_

| Name | Type | Description |
| ---- | ---- | ----------- |
| last | struct Oracle.Observation | The specified observation to be transformed |
| blockTimestamp | uint32 | The timestamp of the new observation |
| tick | int24 | The active tick at the time of the new observation |
| liquidity | uint128 | The total in-range liquidity at the time of the new observation |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | struct Oracle.Observation | Observation The newly populated observation |

### initialize

```solidity
function initialize(struct Oracle.Observation[65535] self, uint32 time) internal returns (uint16 cardinality, uint16 cardinalityNext)
```

Initialize the oracle array by writing the first slot. Called once for the lifecycle of the observations array

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| time | uint32 | The time of the oracle initialization, via block.timestamp truncated to uint32 |

| Name | Type | Description |
| ---- | ---- | ----------- |
| cardinality | uint16 | The number of populated elements in the oracle array |
| cardinalityNext | uint16 | The new length of the oracle array, independent of population |

### write

```solidity
function write(struct Oracle.Observation[65535] self, uint16 index, uint32 blockTimestamp, int24 tick, uint128 liquidity, uint16 cardinality, uint16 cardinalityNext) internal returns (uint16 indexUpdated, uint16 cardinalityUpdated)
```

Writes an oracle observation to the array

_Writable at most once per block. Index represents the most recently written element. cardinality and index must be tracked externally.
If the index is at the end of the allowable array length (according to cardinality), and the next cardinality
is greater than the current one, cardinality may be increased. This restriction is created to preserve ordering._

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| index | uint16 | The index of the observation that was most recently written to the observations array |
| blockTimestamp | uint32 | The timestamp of the new observation |
| tick | int24 | The active tick at the time of the new observation |
| liquidity | uint128 | The total in-range liquidity at the time of the new observation |
| cardinality | uint16 | The number of populated elements in the oracle array |
| cardinalityNext | uint16 | The new length of the oracle array, independent of population |

| Name | Type | Description |
| ---- | ---- | ----------- |
| indexUpdated | uint16 | The new index of the most recently written element in the oracle array |
| cardinalityUpdated | uint16 | The new cardinality of the oracle array |

### grow

```solidity
function grow(struct Oracle.Observation[65535] self, uint16 current, uint16 next) internal returns (uint16)
```

Prepares the oracle array to store up to `next` observations

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| current | uint16 | The current next cardinality of the oracle array |
| next | uint16 | The proposed next cardinality which will be populated in the oracle array |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | uint16 | next The next cardinality which will be populated in the oracle array |

### lte

```solidity
function lte(uint32 time, uint32 a, uint32 b) private pure returns (bool)
```

comparator for 32-bit timestamps

_safe for 0 or 1 overflows, a and b _must_ be chronologically before or equal to time_

| Name | Type | Description |
| ---- | ---- | ----------- |
| time | uint32 | A timestamp truncated to 32 bits |
| a | uint32 | A comparison timestamp from which to determine the relative position of `time` |
| b | uint32 | From which to determine the relative position of `time` |

| Name | Type | Description |
| ---- | ---- | ----------- |
| [0] | bool | bool Whether `a` is chronologically <= `b` |

### binarySearch

```solidity
function binarySearch(struct Oracle.Observation[65535] self, uint32 time, uint32 target, uint16 index, uint16 cardinality) private view returns (struct Oracle.Observation beforeOrAt, struct Oracle.Observation atOrAfter)
```

Fetches the observations beforeOrAt and atOrAfter a target, i.e. where [beforeOrAt, atOrAfter] is satisfied.
The result may be the same observation, or adjacent observations.

_The answer must be contained in the array, used when the target is located within the stored observation
boundaries: older than the most recent observation and younger, or the same age as, the oldest observation_

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| time | uint32 | The current block.timestamp |
| target | uint32 | The timestamp at which the reserved observation should be for |
| index | uint16 | The index of the observation that was most recently written to the observations array |
| cardinality | uint16 | The number of populated elements in the oracle array |

| Name | Type | Description |
| ---- | ---- | ----------- |
| beforeOrAt | struct Oracle.Observation | The observation recorded before, or at, the target |
| atOrAfter | struct Oracle.Observation | The observation recorded at, or after, the target |

### getSurroundingObservations

```solidity
function getSurroundingObservations(struct Oracle.Observation[65535] self, uint32 time, uint32 target, int24 tick, uint16 index, uint128 liquidity, uint16 cardinality) private view returns (struct Oracle.Observation beforeOrAt, struct Oracle.Observation atOrAfter)
```

Fetches the observations beforeOrAt and atOrAfter a given target, i.e. where [beforeOrAt, atOrAfter] is satisfied

_Assumes there is at least 1 initialized observation.
Used by observeSingle() to compute the counterfactual accumulator values as of a given block timestamp._

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| time | uint32 | The current block.timestamp |
| target | uint32 | The timestamp at which the reserved observation should be for |
| tick | int24 | The active tick at the time of the returned or simulated observation |
| index | uint16 | The index of the observation that was most recently written to the observations array |
| liquidity | uint128 | The total pool liquidity at the time of the call |
| cardinality | uint16 | The number of populated elements in the oracle array |

| Name | Type | Description |
| ---- | ---- | ----------- |
| beforeOrAt | struct Oracle.Observation | The observation which occurred at, or before, the given timestamp |
| atOrAfter | struct Oracle.Observation | The observation which occurred at, or after, the given timestamp |

### observeSingle

```solidity
function observeSingle(struct Oracle.Observation[65535] self, uint32 time, uint32 secondsAgo, int24 tick, uint16 index, uint128 liquidity, uint16 cardinality) internal view returns (int56 tickCumulative, uint160 secondsPerLiquidityCumulativeX128)
```

_Reverts if an observation at or before the desired observation timestamp does not exist.
0 may be passed as `secondsAgo' to return the current cumulative values.
If called with a timestamp falling between two observations, returns the counterfactual accumulator values
at exactly the timestamp between the two observations._

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| time | uint32 | The current block timestamp |
| secondsAgo | uint32 | The amount of time to look back, in seconds, at which point to return an observation |
| tick | int24 | The current tick |
| index | uint16 | The index of the observation that was most recently written to the observations array |
| liquidity | uint128 | The current in-range pool liquidity |
| cardinality | uint16 | The number of populated elements in the oracle array |

| Name | Type | Description |
| ---- | ---- | ----------- |
| tickCumulative | int56 | The tick * time elapsed since the pool was first initialized, as of `secondsAgo` |
| secondsPerLiquidityCumulativeX128 | uint160 | The time elapsed / max(1, liquidity) since the pool was first initialized, as of `secondsAgo` |

### observe

```solidity
function observe(struct Oracle.Observation[65535] self, uint32 time, uint32[] secondsAgos, int24 tick, uint16 index, uint128 liquidity, uint16 cardinality) internal view returns (int56[] tickCumulatives, uint160[] secondsPerLiquidityCumulativeX128s)
```

Returns the accumulator values as of each time seconds ago from the given time in the array of `secondsAgos`

_Reverts if `secondsAgos` > oldest observation_

| Name | Type | Description |
| ---- | ---- | ----------- |
| self | struct Oracle.Observation[65535] | The stored oracle array |
| time | uint32 | The current block.timestamp |
| secondsAgos | uint32[] | Each amount of time to look back, in seconds, at which point to return an observation |
| tick | int24 | The current tick |
| index | uint16 | The index of the observation that was most recently written to the observations array |
| liquidity | uint128 | The current in-range pool liquidity |
| cardinality | uint16 | The number of populated elements in the oracle array |

| Name | Type | Description |
| ---- | ---- | ----------- |
| tickCumulatives | int56[] | The tick * time elapsed since the pool was first initialized, as of each `secondsAgo` |
| secondsPerLiquidityCumulativeX128s | uint160[] | The cumulative seconds / max(1, liquidity) since the pool was first initialized, as of each `secondsAgo` |

