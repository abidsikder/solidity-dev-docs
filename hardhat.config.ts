import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "solidity-docgen";

const uniswap_v3_core_settings = {
  version: "0.7.6",
  settings: {
    optimizer: {
      enabled: true,
      runs: 800,
    },
    metadata: {
      // do not include the metadata hash, since this is machine dependent
      // and we want all generated code to be deterministic
      // https://docs.soliditylang.org/en/v0.7.6/metadata.html
      bytecodeHash: 'none',
    },
  },
}

const config: HardhatUserConfig = {
  solidity: {
    compilers: [
      {
        // prb-math, spatial-sol
        version: "0.8.9",
      },
      uniswap_v3_core_settings,
    ],
    overrides: {
      "contracts/uniswap-v3-core/libraries/TickBitmap.sol" : uniswap_v3_core_settings
    }
  },
  docgen: {
    outputDir: "docs",
    pages: "files",
    exclude: ["test"],
  },
};

export default config;
