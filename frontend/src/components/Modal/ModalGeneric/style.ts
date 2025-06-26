import styled from "@emotion/styled";

/* ------------------------------------ - ----------------------------------- */
//  TODOS OS DEMAIS ESTILOS CSS SÃO FEITOS DENTRO DO STYLES.TS DO MODALBODY, NÃO AQUI.
/* ------------------------------------ - ----------------------------------- */

const ModalStyledContainer = styled.section`
  min-width: 100%;
  min-height: 100%;
  top: 0;
  left: 0;
  margin: 0 auto;
  position: fixed;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100; // don´t change

  display: flex;
  align-items: center;
  justify-content: center;
`;

export { ModalStyledContainer };
