import styled from '@emotion/styled';

export const Container = styled.div`
  width: 220px;
  height: 100vh;
  background-color: #071425;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  transition: all 0.3s;

  @media (max-width: 768px) {
    display: none;
  }
`;

export const TitleContainer = styled.div`
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: start;
  margin-top: 20px;
  padding: 0 10px;
  gap: 10px;

  img {
    height: 60px;
  }

  p {
    display: flex;
    flex-direction: column;
    color: white;
    font-size: 14px;
    font-weight: 300;

    span {
      font-size: 24px;
      font-weight: 700;
    }

    @media (max-width: 768px) {
      display: none;
    }
  }
`;

export const Main = styled.div`
  height: 80%;
  padding: 20px 0;
`;

export const ItemContainer = styled.div`
  ul {
    padding: 0;
    margin: 0;
  }
`;

export const MenuItem = styled.li`
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: white;
  padding: 12px 20px;
  list-style: none;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;

  &:hover {
    background-color: #024c7c;
  }

  @media (max-width: 768px) {
    justify-content: center;
    padding: 12px 10px;
  }
`;

export const IconText = styled.span`
  display: flex;
  align-items: center;
  gap: 10px;
  color: #e0e0e0;

  @media (max-width: 768px) {
    gap: 0;
    span {
      display: none;
    }
  }
`;

export const Baseboard = styled.div`
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  padding: 10px 0;
  border-top: 1px solid white;
  height: 60px;

  img {
    height: 40px;
  }

  .botao {
    height: 30px;
  }

  button {
    background: none;
    border: none;
    height: 40px;
    cursor: pointer;
  }

  @media (max-width: 768px) {
    justify-content: center;
    gap: 10px;
  }
`;

export const UserContainer = styled.div`
  color: white;
  text-align: center;

  strong {
    font-size: 15px;
  }

  small {
    font-size: 12px;
  }

  @media (max-width: 768px) {
    display: none;
  }
`;
