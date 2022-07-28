
## LocationAware

### owner

```solidity
address owner
```

### subscribedToJurisdiction

```solidity
mapping(address => bool) subscribedToJurisdiction
```

### jurisdictions

```solidity
address[] jurisdictions
```

### constructor

```solidity
constructor() public
```

### owned

```solidity
modifier owned(address _address)
```

### fund

```solidity
function fund() external payable
```

### getBalance

```solidity
function getBalance() public view returns (uint256 balance_)
```

### subscribeToJurisdiction

```solidity
function subscribeToJurisdiction(address _jurisdiction) public
```

### unsubscribeFromJurisdiction

```solidity
function unsubscribeFromJurisdiction(address _jurisdiction) public
```

### sendWithLocationChecks

```solidity
function sendWithLocationChecks(address payable _to, int256[2] _locationOfOwner, uint256 _value) public returns (uint256)
```

### withinJurisdictionBoundaries

```solidity
function withinJurisdictionBoundaries(int256[2] _point, int256[] _jurisdictionBoundaries) public pure returns (bool)
```

