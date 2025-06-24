import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import { DriverProvider } from "./DriverProvider";
import { ModalProvider } from "./ModalProvider";
import { TripProvider } from "./TripProvider";

const MainProvider = ({ children }: IDefaultChildrenProp) => {
  return (
    <ModalProvider>
      <DriverProvider>
        <TripProvider>{children}</TripProvider>
      </DriverProvider>
    </ModalProvider>
  );
};

export { MainProvider };
