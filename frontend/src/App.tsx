import { ToastContainer } from "react-toastify";
import RoutesMain from "./routes";
import { MainProvider } from "./providers/MainProvider";

const App = () => {
  return (
    <MainProvider>
      <ToastContainer
        position="top-right"
        autoClose={3000}
        hideProgressBar={false}
        newestOnTop={false}
        closeOnClick
        rtl={false}
        pauseOnFocusLoss
        draggable
        pauseOnHover
        theme="light"
      />
      <RoutesMain />
    </MainProvider>
  );
};

export default App;
