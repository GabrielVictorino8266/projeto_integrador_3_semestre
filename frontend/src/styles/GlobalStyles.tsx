import { Global, css } from "@emotion/react";
import "react-toastify/dist/ReactToastify.css";
export const GlobalStyles = () => (
  <Global
    styles={css`
      :root {
        --color-brand-1: #071425;
        --color-brand-2: #006fdd;

        --color-background-dashboard: #dde8f0;

        --color-white: #ffffff;

        --color-success: #15670a;
        --color-attention: #ff6f00;
        --color-error: #ef4444;
        --color-error-2: #d0aaaa;

        --colorStatus-ok: #15670a;
        --colorStatus-maintenance: #0073e6;
        --colorStatus-unavailable: #b31010;

        --color-grey-0: #f8f9fa;
        --color-grey-1: #868e96;
        --color-grey-2: #343b41;
        --color-grey-3: #212529;
        --color-grey-4: #121214;

        --border-radius-8: 8px;
        --border-radius-16: 16px;
        --border-radius-20: 20px;

        --font-weight-400: 400;
        --font-weight-500: 500;
        --font-weight-600: 600;
        --font-weight-700: 700;
        --font-weight-800: 800;

        --font-size-10: 0.25rem; // 10px
        --font-size-12: 0.75rem; // 12px
        --font-size-14: 0.875rem; // 14px
        --font-size-16: 1rem; // 16px
        --font-size-18: 1.125rem; // 18px
        --font-size-20: 1.25rem; // 20px
        --font-size-24: 1.5rem; // 24px
        --font-size-28: 1.75rem; //28px
        --font-size-36: 2.25rem; //36px
        --font-size-40: 2.5rem; //40px

        --font-inter: "Inter", sans-serif;
      }

      body {
        font-family: var(--font-inter);
      }

      button {
        cursor: pointer;
        font-family: var(--font-inter);
      }

      input,
      select,
      option {
        border: none;
        box-sizing: border-box;
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

      .driverActive {
        color: var(--colorStatus-maintenance);
      }
      .driverInactive {
        color: var(--colorStatus-unavailable);
      }

      .iconButtonsEditDelete {
        width: 32px;
        height: 32px;
      }
    `}
  />
);
