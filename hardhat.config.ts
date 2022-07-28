import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "solidity-docgen";

const config: HardhatUserConfig = {
  solidity: "0.8.9",
  docgen: {
    outputDir: "docs",
    pages: "files",
    exclude: ["test"],
  },
};

export default config;