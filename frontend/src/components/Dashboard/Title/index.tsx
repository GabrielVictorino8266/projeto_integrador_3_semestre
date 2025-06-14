import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import { StyledDashboardHeader } from "./styles";

const DashboardHeader = ({ children }: IDefaultChildrenProp) => {
  return <StyledDashboardHeader>{children}</StyledDashboardHeader>;
};

export { DashboardHeader };
