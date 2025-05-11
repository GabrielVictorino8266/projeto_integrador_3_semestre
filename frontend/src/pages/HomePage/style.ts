import styled from "@emotion/styled";

interface ButtonProps {
  primary?: boolean;
}

export const TestComponent = styled.div<ButtonProps>`
  font-size: 48;
  background-color: ${(props) => (props.primary ? '#0070f3' : '#ccc' )};
  border: 1px solid;
`;

export const CustomText = styled.p`
  color: blue;
`;

