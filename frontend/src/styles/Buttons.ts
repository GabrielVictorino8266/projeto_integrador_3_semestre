import { css } from '@emotion/react';
import styled from '@emotion/styled';
import { Link } from 'react-router-dom';

const genericButton = css`
  width: 200px;
  height: 48px;
  border-radius: var(--border-radius-24);
  font-size: var(--font-size-20);
  font-weight: var(--font-weight-500);
  border: none;
`;

const Button = styled.button`
  ${genericButton}
`;

const DeleteButton = styled(Button)`
  background-color: var(--color-error);
  color: var(--color-white);
`;

const DarkBlueButton = styled(Button)`
  background-color: var(--color-brand-1);
  color: var(--color-white);
  transition: background-color 0.3s ease;
  width: 18rem;

  :hover {
    background-color: var(--color-brand-2);
  }
`;

const BorderedButton = styled(Button)`
  border: 2px solid var(--color-brand-1);
  background-color: transparent;
`;

const LinkStyled = styled(Link)`
  ${genericButton}
  background-color: var(--color-brand-1);
  color: var(--color-white);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;

  :hover {
    background-color: var(--color-brand-2);
  }
`;

const GoToDriverRegister = styled(LinkStyled)``;

const GoToDriverEdit = styled(Link)`
  background-color: transparent;
  border: none;
  text-decoration: none;
  color: inherit;
`;

const IconButton = styled.button`
  background-color: transparent;
  border: none;
`;

export {
  Button,
  DeleteButton,
  DarkBlueButton,
  BorderedButton,
  GoToDriverRegister,
  GoToDriverEdit,
  IconButton
};
