import { Global, css } from '@emotion/react';
import 'react-toastify/dist/ReactToastify.css';
export const GlobalStyles = () => (
  <Global
    styles={css`
      body {
          margin: 0px;
          padding: 0px;
          box-sizing: border-box;
          outline: none;
          font-family: 'Inter', sans-serif;
      }

      button {
          cursor: pointer;
      }

      a{
          text-decoration: none;
      }

      input{
          border: none;
      }
      input:focus {
          outline: none;
          box-shadow: none;
      }

      input[type="number"]::-webkit-inner-spin-button,
      input[type="number"]::-webkit-outer-spin-button {
        -webkit-appearance: none;
        margin: 0;
      }

    `}
  />
);

