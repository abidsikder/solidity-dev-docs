
## Jurisdiction

### owner

```solidity
address owner
```

### boundaries

```solidity
int256[] boundaries
```

### numBoundaryPoints

```solidity
uint256 numBoundaryPoints
```

### name

```solidity
string name
```

### tax

```solidity
uint256 tax
```

### constructor

```solidity
constructor() public
```

### owned

```solidity
modifier owned(address _account)
```

### getBalance

```solidity
function getBalance() public view returns (uint256 balance_)
```

### updateBoundaries

```solidity
function updateBoundaries(int256[] _boundaries) public
```

### updateTaxRate

```solidity
function updateTaxRate(uint256 _newTaxRate) public
```

### updateJurisdictionName

```solidity
function updateJurisdictionName(string _newName) public
```

### transferOwnership

```solidity
function transferOwnership(address _newOwner) public
```

