import { ModalProvider } from "../contexts/modal.context";
import type { IDefaultProviderProps } from "../interfaces";

const MainProvider = ({ children }: IDefaultProviderProps) => {
  return <ModalProvider>{children}</ModalProvider>;
};

export default MainProvider;
