import { ModalProvider } from "./ModalProvider";
import type { IDefaultChildrenProp } from "../interfaces";

const MainProvider = ({ children }: IDefaultChildrenProp) => {
  return <ModalProvider>{children}</ModalProvider>;
};

export default MainProvider;
