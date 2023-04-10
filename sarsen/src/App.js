import React, {useState} from "react";
import { Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Home from "./pages/Home";
import Signin from "./pages/Signin";
import Signup from "./pages/Signup";
import Error from "./pages/Error";
import Cabinet from "./pages/Cabinet";
import Tournaments from "./pages/Tournaments";
import EditUser from "./pages/EditUser";
import UpdatePass from "./pages/UpdatePass";
import DeleteAccount from "./pages/DeleteAccount";

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'))
    return (
    <div className="App">
      <Header />
      <Routes>
        {!token?(
          <>
            <Route path="/signin" element={<Signin />}/>
            <Route path="/signup" element={<Signup />}/>
          </>
        ):
          <>
            <Route path="/cabinet" element={<Cabinet />}/>
            <Route path="/edituser" element={<EditUser/>}/>
            <Route path="/updatepass" element={<UpdatePass/>}/>
            <Route path="/deleteaccount" element={<DeleteAccount/>}/>
            <Route path="/tournaments" element={<Tournaments />}/>
          </>
        }
        <Route path="/" element={<Home />}/>
        <Route path="*" element={<Error />}/>
      </Routes>
    </div>
  );
}

export default App;
