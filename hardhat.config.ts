import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "solidity-docgen";

const config: HardhatUserConfig = {
  solidity: {
    compilers: [
      {
        // prb-math, spatial-sol
        version: "0.8.9",
      },
      {
        // solidity-trigonometry
        version: "0.8.13",
      }
    ],
  },
  docgen: {
    outputDir: "docs",
    pages: "files",
    exclude: ["test"],
  },
};

export default config;
