import styled from '@emotion/styled';
import VanFundo from '@assets/vu_login.png';

export const Container = styled.div`
  display: flex;
  height: 100vh;
  width: 100%;
  margin: 0;
  padding: 0;
`;

export const LeftContainer = styled.div`
  width: 50%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #071425;
  justify-content: center;

  @media (max-width: 768px) {
    width: 100%;
    height: auto;
    padding: 20px;
    justify-content: center;
  }
`;

export const RightContainer = styled.div`
  width: 100%;
  height: 100vh;
  background-image: url(${VanFundo});
  background-position: center;
  background-size: 100%;

  @media (max-width: 768px) {
    display: none;
  }
`;

export const TitleDiv = styled.div`
  margin-top: 0;
  display: flex;
  gap: 20px;
  align-items: center;
  justify-content: center;

  img {
    height: 150px;

    @media (max-width: 768px) {
      height: 100px;
      display: none;
    }
  }

  h1 {
    font-size: 40px;
    color: #e0e0e0;
    span {
      font-size: 80px;
    }

    @media (max-width: 768px) {
      font-size: 28px;
      flex-direction: column;
    }
  }
`;

export const Links = styled.div`
  display: flex;
  width: 100%;
  margin: 10px 0px;
  justify-content: space-between;

  a {
    color: #ff6f00;
    font-size: 14px;
  }

  @media (max-width: 768px) {
    flex-direction: column;
    gap: 8px;
    align-items: center;
  }
`;

export const BotaoEntrar = styled.button`
  background-color: #72b5f8;
  border-radius: 10px;
  width: 410px;
  height: 70px;
  font-size: 24px;
  font-weight: 700;
  color: black;
  border: none;
  transition: all 0.3s ease;
  margin-top: 5%;

  &:hover {
    background-color: rgb(88, 153, 218);
    transform: scale(1.05);
  }

  @media (max-width: 768px) {
    width: 100%;
    font-size: 20px;
    height: 60px;
  }
`;

export const ConainerLift = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 70%;

  form {
    margin-top: 3rem;
  }
`;
