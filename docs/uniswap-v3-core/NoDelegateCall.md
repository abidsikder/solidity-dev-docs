
## NoDelegateCall

Base contract that provides a modifier for preventing delegatecall to methods in a child contract

### original

```solidity
address original
```

_The original address of this contract_

### constructor

```solidity
constructor() internal
```

### checkNotDelegateCall

```solidity
function checkNotDelegateCall() private view
```

_Private method is used instead of inlining into modifier because modifiers are copied into each method,
    and the use of immutable means the address bytes are copied in every place the modifier is used._

### noDelegateCall

```solidity
modifier noDelegateCall()
```

Prevents delegatecall into the modified method

