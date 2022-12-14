import React from "react";
import Home from "./home";
import Profile from "./profile";
import { useAuth0 } from "@auth0/auth0-react";
import {
  BrowserRouter as Router,
  Link,
  Redirect,
  Layout,
  Routes,
  Route,
} from "react-router-dom";

export default function App() {
  const { user, isAuthenticated, isLoading } = useAuth0();

  return (
    <>
      <Router>
        <Routes>
          <Route exact path="/" element={<Home />} />
        </Routes>
        <Routes>
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </Router>
    </>
  );
}
