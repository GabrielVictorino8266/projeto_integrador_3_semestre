import { FaCircle } from "react-icons/fa";
import { IconContainer } from "./styles";

type colorOption = "red" | "green" | "blue" | "orange";
interface IOptionProp {
  option: colorOption;
}

const StatusIcon = ({ option }: IOptionProp) => {
  return (
    <IconContainer>
      <FaCircle className={`${option} iconSize`} />
    </IconContainer>
  );
};

export { StatusIcon };
