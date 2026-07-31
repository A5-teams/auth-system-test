import RegisterPage from "./component/RegisterPage";
import LoginPage from "./component/LoginPage";

function App() {
  const path = window.location.pathname;

  if (path === "/login") {
    return <LoginPage />;
  }

  return <RegisterPage />;
}

export default App;