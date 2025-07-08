import styled from '@emotion/styled';

export const Container = styled.section`
  margin: 0 auto;
  padding: 0 24px;
  width: 100%;
`;

export const ContainerList = styled.div`
  height: 350px;
`;

export const ContainerFilter = styled.div`
  display: flex;
  width: 100%;

  gap: 20px;
  align-items: start;
  img {
    margin-top: 5px;
    cursor: pointer;
  }
`;

export const InputWrapper = styled.div`
  flex: 1 1 0;
  min-width: 0;
  align-items: center;
  width: 30%;
  justify-content: center;
`;
