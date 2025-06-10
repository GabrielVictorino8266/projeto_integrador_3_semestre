import type { IDriverContextProps } from "@interfaces/driver.interface";
import type { IDriverRegisterData } from "@schemas/driverRegisterSchema";
import { createContext } from "react";

const DriverContext = createContext<IDriverContextProps>({
  handleCreateDriver: function (
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    newDriverData: IDriverRegisterData
  ): Promise<void> {
    throw new Error("Function not implemented.");
  },
  getDriverList: function (): void {
    throw new Error("Function not implemented.");
  },
  driverList: [],
  driverQuantity: 0,
  driverActive: 0,
  driverInactive: 0,
});

export { DriverContext };
