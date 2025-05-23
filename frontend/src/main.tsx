import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import { GlobalStyles } from "./styles/globalStyles.tsx";
import App from "./App.tsx";
import { ResetCSS } from "./styles/ResetCSS.tsx";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <BrowserRouter>
      <ResetCSS />
      <GlobalStyles />
      <App />
    </BrowserRouter>
  </StrictMode>
);
