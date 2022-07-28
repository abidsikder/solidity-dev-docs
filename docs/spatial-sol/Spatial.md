
## Spatial

### earthRadius

```solidity
uint256 earthRadius
```

### piScaled

```solidity
uint256 piScaled
```

### sinDegrees

```solidity
function sinDegrees(uint256 _degrees) public pure returns (int256)
```

### sinNanodegrees

```solidity
function sinNanodegrees(uint256 _nanodegrees) public pure returns (int256)
```

### cosDegrees

```solidity
function cosDegrees(uint256 _degrees) public pure returns (int256)
```

### cosNanodegrees

```solidity
function cosNanodegrees(uint256 _nanodegrees) public pure returns (int256)
```

### isPolygon

```solidity
function isPolygon(int256[2][] _coordinates) public pure returns (bool)
```

### isLine

```solidity
function isLine(int256[2][] _coordinates) public pure returns (bool)
```

### sqrt

```solidity
function sqrt(int256 _x) public pure returns (uint256 y_)
```

### degreesToNanoradians

```solidity
function degreesToNanoradians(uint256 _degrees) public pure returns (uint256 radians_)
```

### nanodegreesToNanoradians

```solidity
function nanodegreesToNanoradians(uint256 _nanodegrees) public pure returns (uint256 radians_)
```

### nanoradiansToDegrees

```solidity
function nanoradiansToDegrees(uint256 _nanoradians) public pure returns (uint256 degrees_)
```

### earthNanoradiansToNanometers

```solidity
function earthNanoradiansToNanometers(uint256 _nanoradians) public pure returns (uint256 nanometers_)
```

### earthNanodegreesToNanometers

```solidity
function earthNanodegreesToNanometers(uint256 _nanodegrees) public pure returns (uint256 nanometers_)
```

### distance

```solidity
function distance(int256[2] ptA, int256[2] ptB) public view returns (uint256 distanceNanometers_)
```

### area

```solidity
function area(int256[2][] _coordinates) public pure returns (uint256 area_)
```

### centroid

```solidity
function centroid(int256[2][] _coordinates) public pure returns (int256[2])
```

### boundingBox

```solidity
function boundingBox(int256[2][] _coordinates) public pure returns (int256[2][2])
```

### length

```solidity
function length(int256[2][] _coordinates) public view returns (uint256 length_)
```

### perimeter

```solidity
function perimeter(int256[2][] _coordinates) public view returns (uint256 perimeter_)
```

### distanceBetweenAzimuthalEquidistantProjectedPoints

```solidity
function distanceBetweenAzimuthalEquidistantProjectedPoints(uint256[2] ptA, uint256[2] ptB) public view returns (uint256)
```

### bearingFromAzimuthalEquidistantProjectedPoints

```solidity
function bearingFromAzimuthalEquidistantProjectedPoints(uint256[2] ptA, uint256[2] ptB) public view returns (uint256)
```

### boundingBoxBuffer

```solidity
function boundingBoxBuffer(int256[2] _point, int256 _buffer) public pure returns (int256[2][2])
```

### pointInBbox

```solidity
function pointInBbox(int256[2] _point, int256[2][2] _bbox) public pure returns (bool ptInsideBbox_)
```

### pointInPolygon

```solidity
function pointInPolygon(int256[2] _point, int256[] _polygon) public pure returns (bool)
```

